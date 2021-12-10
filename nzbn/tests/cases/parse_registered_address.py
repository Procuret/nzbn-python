"""
New Zealand Business Number
Parse Registered Address Test Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from nzbn.address import AddressType
from nzbn.entity import Entity, Address
from nzbn.tests.test import Test
from nzbn.tests.test_result import Success, TestResult


class ParseRegisteredAddress(Test):

    NAME = 'Parse an Entity\'s registered address'

    def execute(self) -> TestResult:

        entity = Entity.retrieve(
            access_token=self.access_token,
            nzbn='9429032530384',
            sandbox=True
        )

        address = entity.registered_address

        assert isinstance(address, Address)

        assert address.line1 == '151 Dominion Road'
        assert address.address_type == AddressType.REGISTERED

        return Success()
