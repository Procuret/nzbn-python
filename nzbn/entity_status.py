"""
New Zealand Business Number
Entity Status Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from enum import Enum


class EntityStatus(Enum):

    REGISTERED = '50'
    VOLUNTARY_ADMINISTRATION = '55'
    VOLUNTARY_ADMINISTRATION_AND_RECEIVERSHIP = '56'
    RECEIVERSHIP_AND_VOLUNTARY_ADMINISTRATION = '57'
    IN_LIQUIDATION = '60'
    IN_RECEIVERSHIP_AND_LIQUIDATION = '61'
    REMOVED_AND_IN_LIQUIDATION = '62'
    IN_RECEIVERSHIP_LIQUIDIATION_AND_VOLUNTARY_ADMINISTRATION = '63'
    IN_LIQUIDATION_AND_RECEIVERSHIP_AND_VOLUNTARY_ADMINISTRATION = '64'
    VOLUNTARY_ADMINISTRATION_AND_LIQUIDATION = '65'
    IN_LIQUIDATION_AND_VOLUNTARY_ADMINISTRATION_AND_RECEIVERSHIP = '66'
    IN_RECEIVERSHIP = '70'
    IN_RECEIVERSHIP_AND_LIQUIDATION_DUPLICATE = '71'
    IN_STATUTORY_ADMINISTRATION = '72'
    REMOVED = '80'
    INACTIVE = '90'
    REMOVED_CLOSED = '91'
