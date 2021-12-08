"""
New Zealand Business Number
Api Request Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
import json
from nzbn.http.method import HTTPMethod
from typing import Optional, Dict, Union, List
from nzbn.http.query_parameters import QueryParameters
from nzbn.errors.api import NzbnApiError
from urllib.request import HTTPError
from urllib.request import Request
from urllib.request import urlopen
from nzbn.version import VERSION as AGENT_VERSION

API_ENDPOINT = 'https://sandbox.api.business.govt.nz'
USER_AGENT = 'NZBN Python ' + AGENT_VERSION


class ApiRequest:

    @staticmethod
    def make(
        path: str,
        method: HTTPMethod,
        access_token: Optional[str] = None,
        data: Optional[Union[Dict, List[Dict]]] = None,
        query_parameters: Optional[QueryParameters] = None,
        api_endpoint: str = API_ENDPOINT,
        throw_on_404: bool = False
    ) -> Optional[Union[Dict, List[Dict]]]:
        """Return the decoded json body of a response from the Procuret API"""

        url = api_endpoint + path
        if query_parameters is not None:
            url = query_parameters.add_to(url)

        headers = {
            'User-Agent': USER_AGENT,
            'Authorization': 'Bearer ' + access_token
        }

        encoded_data: Optional[bytes] = None
        if data is not None:
            encoded_data = json.dumps(data).encode('utf-8')
            headers['Content-Type'] = 'application/json'

        request = Request(
            url=url,
            method=method.value,
            data=encoded_data,
            headers=headers
        )

        try:
            response = urlopen(request).read()
        except HTTPError as error:
            if error.code == 404 and throw_on_404 is False:
                return None
            body: Optional[str] = None
            try:
                body = error.read()
            except Exception:
                pass
            raise NzbnApiError(error.code, body=body)

        return json.loads(response)
