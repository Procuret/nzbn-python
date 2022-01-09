"""
New Zealand Business Number
Trading Name Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from typing import Type,  TypeVar, Dict, List, Optional
from nzbn.time import NzbnTime

Self = TypeVar('Self', bound='TradingName')


class TradingName:

    def __init__(
        self,
        unique_identifier: str,
        name: str,
        start_date: Optional[NzbnTime],
        end_date: Optional[NzbnTime]
    ) -> None:

        self._unique_identifier = unique_identifier
        self._name = name
        self._start_date = start_date
        self._end_date = end_date

        return
    
    @classmethod
    def decode(Self: Type[Self], data: Dict[str, str]) -> Self:
        return Self(
            unique_identifier=data['uniqueIdentifier'],
            name=data['name'],
            start_date=NzbnTime.optionally_decode(data['startDate']),
            end_date=NzbnTime.optionally_decode(data['endDate'])
        )

    @classmethod
    def decode_many(
        Self: Type[Self],
        data: List[Dict[str, str]]
    ) -> List[Self]:

        return [Self.decode(t) for t in data]
