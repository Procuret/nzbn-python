"""
New Zealand Business Number
QueryParameter Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from typing import Any, TypeVar, Type, List
from urllib.parse import quote

Self = TypeVar('Self', bound='QueryParameter')


class QueryParameter:
    """A single URL parameter, e.g. beep=boop"""
    def __init__(
        self,
        key: str,
        value: Any
    ) -> None:

        assert isinstance(key, str)
        str(value)  # provoke error early
        self._key = key
        self._value = value

        self._url_representation = self._represent(value)

        return

    key = property(lambda s: s._key)

    def __str__(self) -> str:
        return self._key + '=' + self._url_representation

    @classmethod
    def remove_targets_with(
        cls: Type[Self],
        key: str,
        targets: List[Self]
    ) -> List[Self]:

        retained_targets: List[QueryParameter] = list()
        for target in targets:
            if target._key == key:
                continue
            retained_targets.append(target)
            continue

        return targets

    @staticmethod
    def _represent(value: Any) -> str:

        if isinstance(value, str):
            return quote(value)

        if isinstance(value, bool):
            if value is True:
                return 'true'
            return 'false'

        return quote(str(value))
