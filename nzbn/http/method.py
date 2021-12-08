"""
New Zealand Business Number
HTTP Method Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from enum import Enum


class HTTPMethod(Enum):
    GET = 'GET'
    POST = 'POST'
    DELETE = 'DELETE'
    PUT = 'PUT'
    PATCH = 'PATCH'
