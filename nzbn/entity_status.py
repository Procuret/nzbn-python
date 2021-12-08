"""
New Zealand Business Number
Entity Status Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from enum import Enum


class EntityStatus(Enum):

    REGISTER = 'Registered'
    VOLUNTARY_ADMINISTRATION = 'VoluntaryAdministration'
    IN_LIQUIDATION = 'InLiquidation'
    IN_STATUTORY_ADMINISTRATION = 'InStatutoryAdministration'
    IN_RECEIVERSHIP = 'InReceivership'
    INACTIVE = 'Inactive'
    REMOVED_CLOSED = 'RemovedClosed'
