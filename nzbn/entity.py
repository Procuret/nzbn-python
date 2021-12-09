"""
New Zealand Business Number
Entity Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from typing import List, Optional, Dict, Any
from nzbn.address import Address
from nzbn.disposition import Disposition
from nzbn.entity_type import EntityType
from nzbn.entity_status import EntityStatus
from nzbn.errors.error import NzbnError
from nzbn.errors.type_error import NzbnTypeError
from nzbn.http.api_request import ApiRequest
from nzbn.http.method import HTTPMethod
from nzbn.http.query_parameter import QueryParameter
from nzbn.http.query_parameters import QueryParameters
from nzbn.time import NzbnTime
from nzbn.trading_name import TradingName
from nzbn.classification import Classification
from typing import TypeVar, Type
from nzbn.address import Address

Self = TypeVar('Self', bound='Entity')


class Entity:

    path = '/entities'

    def __init__(
        self,
        entity_name: str,
        status: EntityStatus,
        nzbn: str,
        entity_type: EntityType,
        trading_names: List[TradingName],
        classifications: List[Classification],
        registration_date: NzbnTime,
        disposition: Disposition,
        addresses: List[Address]
    ) -> None:

        self._entity_name = entity_name
        self._status = status
        self._nzbn = nzbn
        self._entity_type = entity_type
        self._trading_names = trading_names
        self._classifications = classifications
        self._registration_date = registration_date
        self._disposition = disposition
        self._addresses = addresses

        return

    entity_name: str = property(lambda s: s._entity_name)
    status: EntityStatus = property(lambda s: s._status)
    nzbn: str = property(lambda s: s._nzbn)
    entity_type: EntityType = property(lambda s: s._entity_type)
    trading_names: List[str] = property(lambda s: s._trading_names)
    classifications: List[Classification] = property(
        lambda s: s._classifications
    )
    registration_date: NzbnTime = property(lambda s: s._registration_date)
    disposition: Disposition = property(
        lambda s: s._disposition
    )
    addresses: List[Address] = property(lambda s: s._addresses)

    @classmethod
    def decode(
        Self: Type[Self],
        data: Dict[str, Any],
        disposition: Optional[Disposition] = None
    ) -> Self:

        return Self(
            entity_name=data['entityName'],
            status=EntityStatus(data['entityStatusCode']),
            nzbn=data['nzbn'],
            entity_type=EntityType(data['entityTypeCode']),
            trading_names=TradingName.decode_many(data['tradingNames']),
            classifications=Classification.decode_many(
                data['classifications']
            ) if 'classifications' in data else [],
            registration_date=NzbnTime.decode(data['registrationDate']),
            disposition=disposition or Disposition(
                1,
                1,
                1,
                1
            ),
            addresses=Address.decode_many(data['addresses']['addressList'])
        )

    @classmethod
    def retrieve(
        Self: Type[Self],
        access_token: str,
        nzbn: str
    ) -> Optional[Self]:

        if not isinstance(access_token, str):
            raise NzbnTypeError('access_token', access_token, 'str')
        
        if not isinstance(nzbn, str):
            raise NzbnTypeError('nzbn', nzbn, 'str')
        
        if len(nzbn) != 13:
            raise NzbnError('nzbn must be 13 characters')
        
        for character in nzbn:
            if character not in '0123456789':
                raise NzbnError('nzbn must be only numeric characters')
            continue

        result = ApiRequest.make(
            path=Self.path + '/' + nzbn,
            method=HTTPMethod.GET,
            access_token=access_token
        )
        
        if result is None:
            return None
        
        return Self.decode(result)
