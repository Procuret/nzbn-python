"""
New Zealand Business Number
Test Result Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from typing import Optional


class TestResult:
    """Abstract class defining an interface for test result classes"""
    DID_PASS: bool = NotImplemented


class Success(TestResult):
    DID_PASS = True


class Failure(TestResult):
    DID_PASS = False

    def __init__(
        self,
        description: str,
        exception: Optional[Exception] = None
    ) -> None:

        self._description = description
        self._exception = exception

        return

    description = property(lambda s: s._description)
    exception = property(lambda s: s._exception)
