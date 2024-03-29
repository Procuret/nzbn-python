"""
New Zealand Business Number
Time Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from datetime import datetime, tzinfo, timedelta
from typing import Optional, TypeVar, Type

Self = TypeVar('Self', bound='NzbnTime')


class TimeZoneUTC(tzinfo):
    """
    UTC timezone.
    """
    def utcoffset(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return 'UTC'

    def dst(self, dt):
        return timedelta(0)


UTC = TimeZoneUTC()


class NzbnTime(datetime):

    _FORMAT = '%Y-%m-%dT%H:%M:%S.%f%z'

    @classmethod
    def decode(Self: Type[Self], data: str) -> Self:

        time = datetime.strptime(data, Self._FORMAT)
        time = time - time.tzinfo.utcoffset(time)

        return NzbnTime(
            year=time.year,
            month=time.month,
            day=time.day,
            hour=time.hour,
            minute=time.minute,
            second=time.second,
            microsecond=time.microsecond,
            tzinfo=UTC
        )

    @classmethod
    def optionally_decode(
        Self: Type[Self],
        data: Optional[str]
    ) -> Optional[Self]:

        if data is None:
            return None
        
        return Self.decode(data)

    @classmethod
    def utcnow(Self: Type[Self]) -> Self:
        time = datetime.utcnow()
        return Self._from_datetime(time)

    @classmethod
    def _from_datetime(Self: Type[Self], time: datetime) -> Self:
        return Self(
            year=time.year,
            month=time.month,
            day=time.day,
            hour=time.hour,
            minute=time.minute,
            second=time.second,
            microsecond=time.microsecond,
            tzinfo=UTC
        )
