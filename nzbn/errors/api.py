"""
New Zealand Business Number
API Error Class
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from nzbn.errors.error import NzbnError
from typing import Optional


class NzbnApiError(NzbnError):

    def __init__(
        self,
        code: int,
        body: Optional[str]
    ) -> None:

        self._code = code
        self._body = body

        super().__init__('NZBN API emitted error with HTTP code {c}. {b}\
'.format(
            c=str(code),
            b=(
                'Examine .body property for more information.' if (
                    self._body is not None
                ) else 'No further information provided by NZBN API.'
            )
        ))

        return
    