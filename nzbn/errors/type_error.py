"""
New Zealand Business Number
Error Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from typing import Any
from nzbn.errors.error import NzbnError


class NzbnTypeError(NzbnError):

    def __init__(
        self,
        value_name: str,
        provided_value: Any,
        expected_type_name: str
    ) -> None:
    
        description = 'Expected type `{t}` for value `{v}`, got `{p}`'.format(
            t=expected_type_name,
            p=str(type(provided_value)),
            v=value_name
        )

        return super().__init__(description)
