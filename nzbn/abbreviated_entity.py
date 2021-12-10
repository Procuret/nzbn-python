"""
New Zealand Business Number
Abbreviated Entity Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from typing import List, Optional, Dict, Union, Any
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

Self = TypeVar('Self', bound='AbbreviatedEntity')


class AbbreviatedEntity:

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
        disposition: Disposition
    ) -> None:

        self._entity_name = entity_name
        self._status = status
        self._nzbn = nzbn
        self._entity_type = entity_type
        self._trading_names = trading_names
        self._classifications = classifications
        self._registration_date = registration_date
        self._disposition = disposition

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

    @classmethod
    def decode_encapsulated_list(
        Self: Type[Self],
        data: Dict[str, Any]
    ) -> List[Self]:

        total = data['totalItems']
        page = data['page']
        page_size = data['pageSize']

        offset = (page - 1) * page_size

        sequence = offset

        entities: List[AbbreviatedEntity] = []

        for entity_data in data['items']:
            sequence += 1
            disposition = Disposition(
                sequence=sequence,
                offset=offset,
                count=total,
                limit=page_size
            )
            entities.append(AbbreviatedEntity.decode(
                data=entity_data,
                disposition=disposition
            ))
            continue
        
        return entities

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
            )
        )

    @classmethod
    def retrieve_many(
        Self: Type[Self],
        access_token: str,
        page: int = 0,
        limit: int = 20,
        search_text: Optional[str] = None,
        entity_status: Optional[Union[
            EntityStatus,
            List[EntityStatus]
        ]] = None,
        entity_type: Optional[Union[
            EntityType,
            List[EntityType]
        ]] = None,
        sandbox: bool = False
    ) -> List[Self]:


        if not isinstance(page, int):
            raise NzbnTypeError('offset', page, 'int')

        if not isinstance(limit, int):
            raise NzbnTypeError('limit', limit, 'int')

        if page < 0:
            raise NzbnError('page must be >= 0')

        if limit < 0:
            raise NzbnError('limit must be >= 0')

        parameters: List[QueryParameter] = [
            QueryParameter(key='page', value=page),
            QueryParameter(key='page-size', value=limit)
        ]

        if search_text is not None:
            if not isinstance(search_text, str):
                raise NzbnTypeError(
                    'search_text',
                    search_text,
                    'Optional[str]'
                )
            parameters.append(QueryParameter(
                key='search-term',
                value=search_text
            ))
            pass

        if entity_status is not None:

            def raise_error() -> None:
                raise NzbnTypeError(
                    'entity_status',
                    entity_status,
                    'Optional[Union[EntityStatus, List[EntityStatus]]]'
                )

            if isinstance(entity_status, list):
                if False in [
                    isinstance(e, EntityStatus) for e in entity_status
                ]:
                    raise_error()
                pass
            else:
                if not isinstance(entity_status, EntityStatus):
                    raise_error()
    
            parameters.append(QueryParameters(
                key='entity-status',
                value=(
                    ','.join([e.value for e in entity_status] if (
                        isinstance(entity_status, list)
                    ) else entity_status.value
                )
            )))

            pass

        if entity_type is not None:

            def raise_error() -> None:
                raise NzbnTypeError(
                    'entity_type',
                    entity_status,
                    'Optional[Union[EntityType, List[EntityType]]]'
                )

            if isinstance(entity_type, list):
                if False in [
                    isinstance(e, EntityType) for e in entity_type
                ]:
                    raise_error()
                pass
            else:
                if not isinstance(entity_type, EntityType):
                    raise_error()
    
            parameters.append(QueryParameters(
                key='entity-type',
                value=(
                    ','.join([e.value for e in entity_type] if (
                        isinstance(entity_type, list)
                    ) else entity_type.value
                )
            )))

            pass

        result = ApiRequest.make(
            path=Self.path,
            method=HTTPMethod.GET,
            query_parameters=QueryParameters(parameters),
            access_token=access_token,
            sandbox=sandbox
        )

        return Self.decode_encapsulated_list(result)
