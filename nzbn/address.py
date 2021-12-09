"""
New Zealand Business Number
Address Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from datetime import datetime
from nzbn.time import NzbnTime
from enum import Enum
from typing import Optional, Type, TypeVar, Dict, List

Self = TypeVar('Self', bound='Address')


class AddressType(Enum):

    POSTAL = 'POSTAL'
    REGISTERED = 'REGISTERED'
    SERVICE = 'SERVICE'



class Address:

    def __init__(
        self,
        unique_identifier: str,
        start_date: NzbnTime,
        end_date: Optional[NzbnTime],
        care_of: Optional[str],
        address_1: str,
        address_2: Optional[str],
        address_3: Optional[str],
        address_4: Optional[str],
        post_code: Optional[str],
        country_code: Optional[str],
        address_type: Optional[AddressType],
        paf_id: Optional[str]
    ) -> None:

        self._unique_identifier = unique_identifier
        self._start_date = start_date
        self._end_date = end_date
        self._care_of = care_of
        self._address_1 = address_1
        self._address_2 = address_2
        self._address_3 = address_3
        self._address_4 = address_4
        self._post_code = post_code
        self._country_code = country_code
        self._address_type = address_type
        self._paf_id = paf_id

        return

    unique_identifier = property(lambda s: s._unqiue_identifier)
    start_date = property(lambda s: s._start_date)
    end_date = property(lambda s: s._end_date)

    line1: str = property(lambda s: s._address_1)
    line2: Optional[str] = property(lambda s: s._address_2)
    line3: Optional[str] = property(lambda s: s._address_3)
    line4: Optional[str] = property(lambda s: s._address_4)

    post_code: Optional[str] = property(lambda s: s._post_code)
    country_code: Optional[str] = property(lambda s: s._country_code)

    address_type: Optional[AddressType] = property(
        lambda s: s._address_type
    )
    paf_id: Optional[str] = property(lambda s: s._paf_id)

    expired: bool = property(
        lambda s: (
            s._end_date is not None and s._end_date <= datetime.utcnow()
        )
    )
    not_expired: bool = property(lambda s: not s.expired)

    @classmethod
    def decode(
        Self: Type[Self],
        data: Dict[str, Optional[str]]
    ) -> Self:

        return Address(
            unique_identifier=data['uniqueIdentifier'],
            start_date=NzbnTime.decode(data['startDate']),
            end_date=NzbnTime.optionally_decode(data['endDate']),
            care_of=data['careOf'],
            address_1=data['address1'],
            address_2=data['address2'],
            address_3=data['address3'],
            address_4=data['address4'],
            post_code=data['postCode'],
            country_code=data['countryCode'],
            address_type=(
                AddressType(data['addressType']) if data['addressType']
                is not None else None
            ),
            paf_id=data['pafId']
        )        

    @classmethod
    def decode_many(
        Self: Type[Self],
        data: List[Dict[str, Optional[str]]]
    ) -> List[Self]:

        return [Self.decode(a) for a in data]
