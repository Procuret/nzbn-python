"""
New Zealand Business Number
Disposition Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""


class Disposition:

    def __init__(
        self,
        sequence: int,
        offset: int,
        count: int,
        limit: int
    ) -> None:

        self._sequence = sequence
        self._offset = offset
        self._count = count
        self._limit = limit

        return
