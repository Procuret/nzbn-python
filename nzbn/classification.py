"""
New Zealand Business Number
Classification Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from typing import List, Dict, TypeVar, Type, Optional

Self = TypeVar('Self', bound='Classification')


class Classification:

    def __init__(
        self,
        unique_identifier: Optional[str],
        classification_code: str,
        classification_description: str
    ) -> None:

        self._unique_identifier = unique_identifier
        self._classification_code = classification_code
        self._classification_description = classification_description

        return

    unique_identifier: Optional[str] = property(
        lambda s: s._unique_identifier
    )
    classification_code = property(lambda s: s._classification_code)
    classification_description = property(
        lambda s: s._classification_description
    )

    @classmethod
    def decode(
        Self: Type[Self],
        data: Dict[str, str]
    ) -> Self:

        return Classification(
            unique_identifier=(
                data['unique_identifier'] if 'unique_identifier' in data
                else None
            ),
            classification_code=data['classification_code'],
            classification_description=data['classification_description']
        )

    @classmethod
    def decode_many(
        Self: Type[Self],
        data: List[Dict[str, str]]
    ) -> List[Self]:

        return [Self.decode(c) for c in data]
