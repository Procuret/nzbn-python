"""
New Zealand Business Number
Command Line Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
import sys
from typing import Optional, Dict, List, TypeVar, Type
from typing import Any

T = TypeVar('T', bound='CommandLine')


class CommandLine:

    def __init__(
        self,
        arguments: List[str]
    ) -> None:

        data: Dict[str, Optional[str]] = dict()
        index = 0
        while index < len(arguments):
            value: Optional[str] = None
            argument = arguments[index]
            if argument[0] == '-':
                n = index + 1
                if (n) < len(arguments) and arguments[n][0] != '-':
                    value = arguments[n]
                    index += 1
                else:
                    value = None
            data[argument] = value
            index += 1
            continue

        self._data = data
        return

    def contains_flag(self, flag: str) -> bool:
        if flag in self._data.keys():
            return True
        return False

    def get(
        self,
        key: str,
        of_type: Optional[Type] = None,
        type_name: Optional[str] = None
    ) -> Optional[Any]:

        if key not in self._data.keys():
            return None

        value = self._data[key]

        if of_type is not None and not isinstance(value, of_type):
            try:
                value = of_type(value)
            except Exception:
                raise ValueError('Value for parameter {k} must be a string tha\
t may be cast to {t}'.format(k=key, t=(type_name or str(of_type))))

        return value

    def require(
        self,
        key: str,
        of_type: Optional[Type] = None,
        type_name: Optional[str] = None
    ) -> Any:

        value = self.get(key, of_type, type_name=type_name)
        if value is None:
            raise RuntimeError('Missing command line parmeter "{p}"'.format(
                p=key
            ))

        return value

    @classmethod
    def load(cls: Type[T]) -> T:
        return cls(sys.argv[1:])
