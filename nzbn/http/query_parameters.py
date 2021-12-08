"""
New Zealand Business Number
Query Parameters Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from nzbn.http.query_parameter import QueryParameter
from typing import List


class QueryParameters:
    """A collection of URL Query path parameters"""

    def __init__(self, targets: List[QueryParameter]) -> None:

        assert isinstance(targets, list)
        assert False not in [isinstance(t, QueryParameter) for t in targets]

        self._targets = targets
        return

    query_string = property(lambda s: s._form_query_string())

    def _form_query_string(self) -> str:
        if len(self._targets) < 1:
            return ''

        query = '?' + str(self._targets[0])

        for target in self._targets[1:]:
            query += '&' + str(target)

        return query

    def add_to(self, url: str) -> str:
        """Return a URL with parameters bolted on"""
        if len(self._targets) < 1:
            return url

        return url + self.query_string
