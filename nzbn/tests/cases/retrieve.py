"""
New Zealand Business Number
Retrieve Entity Test Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from nzbn.tests.test import Test
from nzbn.tests.test_result import Success, TestResult, Failure
from nzbn.entity import Entity


class RetrieveEntity(Test):

    NAME = 'Retrieve an Entity'

    def execute(self) -> TestResult:

        rocketwerkz = Entity.retrieve(
            api_key=self.api_key,
            nzbn='9429032530384',
            sandbox=True
        )

        if rocketwerkz is None:
            return Failure('Expected Entity absent')

        assert isinstance(rocketwerkz, Entity)

        return Success()
