"""
New Zealand Business Number
Search Entities By Name Test Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from nzbn.abbreviated_entity import AbbreviatedEntity
from nzbn.tests.test import Test
from nzbn.tests.test_result import Success, TestResult


class SearchByName(Test):

    NAME = 'Search Entities by name'

    def execute(self) -> TestResult:

        entities = AbbreviatedEntity.retrieve_many(
            access_token=self.access_token,
            search_text='COMPANY REBUILDERS HOLDINGS',
            sandbox=True
        )

        assert isinstance(entities, list)
        assert len(entities) > 0

        assert False not in [
            isinstance(e, AbbreviatedEntity) for e in entities
        ]

        return Success()
