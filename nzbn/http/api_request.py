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

SANDBOX_ENDPOINT = 'https://api.business.govt.nz/sandbox/nzbn/v5'
API_ENDPOINT = 'https://api.business.govt.nz/gateway/nzbn/v5/'
USER_AGENT = 'NZBN Python ' + AGENT_VERSION


class ApiRequest:

    @staticmethod
    def make(
        path: str,
        method: HTTPMethod,
        api_key: Optional[str] = None,
        data: Optional[Union[Dict, List[Dict]]] = None,
        query_parameters: Optional[QueryParameters] = None,
        api_endpoint: Optional[str] = None,
        throw_on_404: bool = False,
        sandbox: bool = False,
        timeout: int = 10
    ) -> Optional[Union[Dict, List[Dict]]]:
        """Return the decoded json body of a response from the Procuret API"""

        api_endpoint = api_endpoint or (
            SANDBOX_ENDPOINT if sandbox is True
            else API_ENDPOINT
        )

        url = api_endpoint + path
        if query_parameters is not None:
            url = query_parameters.add_to(url)

        headers = {
            'User-Agent': USER_AGENT,
            'Ocp-Apim-Subscription-Key': api_key
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
            response = urlopen(request, timeout=timeout).read()
        except HTTPError as error:
            if error.code == 404 and throw_on_404 is False:
                return None
            body: Optional[str] = None
            try:
                body = error.read()
                try:
                    jsonbody = json.loads(body)
                    if 'errorDescription' in jsonbody and (
                        'Object Not Found' in jsonbody['errorDescription']
                    ) and throw_on_404 is False:
                        return None
                except Exception:
                    pass
            except Exception:
                pass
            raise NzbnApiError(error.code, body=body)

        return json.loads(response)
