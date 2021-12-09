"""
New Zealand Business Number
Test Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from nzbn.tests.test_result import TestResult, Failure
from nzbn.ancillary.command_line import CommandLine
from datetime import datetime
from typing import Optional
import traceback


class Test:
    """A test of a single unit of Procuret Python functionality"""
    NAME = NotImplemented

    _REPORT = '[{result}] {name} ({elapsed})'
    _FAILURE_ADDENDUM = '\n       {reason}'

    def __init__(self) -> None:

        name = self.NAME
        if not isinstance(name, str):
            raise TypeError('Supply name as .NAME property')

        self._name = name
        self._failure_reason: Optional[str] = None
        self._did_pass_store: Optional[bool] = None
        self._test_start: Optional[datetime] = None
        self._test_end: Optional[datetime] = None

        arguments = CommandLine.load()

        self._access_token = arguments.require(
            key='--access-token',
            of_type=str,
            type_name='string'
        )

        return

    name = property(lambda s: s._name)
    did_pass = property(lambda s: s._did_pass())
    did_fail = property(lambda s: s._did_fail())
    is_complete = property(lambda s: s._is_complete())
    time_elapsed = property(lambda s: s._time_elapsed())

    access_token = property(lambda s: s._access_token)

    def run(self) -> None:
        """Run the test"""
        self._test_start = datetime.utcnow()
        try:
            result = self.execute()
        except Exception as error:
            self.fail_test(error=error)
            self._test_end = datetime.utcnow()
            return
        self._test_end = datetime.utcnow()
        assert isinstance(result, TestResult)
        if result.DID_PASS:
            self.pass_test()
        else:
            assert isinstance(result, Failure)
            self.fail_test(
                reason=result.description,
                error=result.exception
            )
        return

    def execute(self) -> TestResult:
        """Perform the test procedure"""
        raise NotImplementedError

    def _did_pass(self) -> bool:
        """Return True if this test did pass"""
        if self._did_pass_store is None:
            return False
        assert isinstance(self._did_pass_store, bool)
        return self._did_pass_store

    def _did_fail(self) -> bool:
        """Return True if this test did fail"""
        if self._did_pass_store is None:
            return False
        assert isinstance(self._did_pass_store, bool)
        return not self._did_pass_store

    def _is_complete(self) -> bool:
        """Return True if this test is complete"""
        if self._did_pass_store is None:
            return False
        assert isinstance(self._did_pass_store, bool)
        return True

    def _time_elapsed(self) -> int:
        """Return the test run time in milliseconds"""
        if not self.is_complete:
            raise RuntimeError('Cannot measure runtime of an unfinished test')
        assert isinstance(self._test_start, datetime)
        assert isinstance(self._test_end, datetime)
        delta = self._test_end - self._test_start
        elapsed = int(delta.microseconds / 1000) + int(delta.seconds * 1000)
        return elapsed

    def pass_test(self) -> None:
        """Mark this test as having passed"""
        if self._did_pass_store is not None:
            raise RuntimeError('Test already passed or failed')
        self._did_pass_store = True
        return

    def fail_test(
        self,
        reason: Optional[str] = None,
        error: Optional[Exception] = None
    ) -> None:
        """Mark this test has having failed"""
        if self._did_pass_store is not None:
            raise RuntimeError('Test already passed or failed')
        self._did_pass_store = False
        if reason is not None and not isinstance(reason, str):
            raise TypeError(
                'Reason must be str or None, not ' + str(type(reason))
            )
        self._failure_reason = reason
        if error is not None and not isinstance(error, Exception):
            raise TypeError(
                'error must be None or Exception, not ' + str(type(error))
            )
        self._failure_error = error
        return

    def report(self) -> str:
        """Return a string describing the outcome of this Test"""
        if not self.is_complete:
            raise RuntimeError('Cannot report on an unfinished test')
        result = 'PASS'
        if self.did_fail:
            result = 'FAIL'
        report = self._REPORT.format(
            result=result,
            name=self.name,
            elapsed=self._format_elapsed()
        )
        if self.did_fail and self._failure_reason is not None:
            report += self._FAILURE_ADDENDUM.format(
                reason=self._failure_reason
            )
        if self.did_fail and self._failure_error is not None:
            report += '\n       ' + '       '.join(traceback.format_exception(
                None,
                self._failure_error,
                self._failure_error.__traceback__
            ))
        return report

    def _format_elapsed(self) -> str:
        elapsed = self.time_elapsed
        if elapsed < 1000:
            return '{:,}'.format(elapsed) + 'ms'
        return '{:,}'.format(round(elapsed / 1000, 2)) + 's'
