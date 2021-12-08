"""
New Zealand Business Number
Entity Type Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from enum import Enum


class EntityType(Enum):

    NZ_COMPANY = 'NZCompany'
    OVERSEAS_COMPANY = 'OverseasCompany'
    SOLE_TRADER = 'SoleTrader'
    PARTNERSHIP = 'Partnership'
    TRUST = 'Trust'
    BUILDING_SOCIETY = 'BuildingSociety'
    CHARITABLE_TRUST = 'CharitableTrust'
    CREDIT_UNION = 'CreditUnion'
    FRIENDLY_SOCIETY = 'FriendlySociety'
    INCORPORATED_SOCIETY = 'IncorporatedSociety'
    INDUSTRIAL_PROVIDENT_SOCIETY = 'IndustrialAndProvidentSociety'
    LIMITED_PARTNERSHIP_NZ = 'LimitedPartnershipNz'
    LIMITED_PARTNERSHIP_OVERSEAS = 'LimitedPartnershipOverseas'
    SPECIAL_BODIES = 'SpecialBodies'
    SPECIAL_BODY = 'SpecialBody'
    TRADING_TRUST = 'Trading_Trust'
    SOLE_TRADER_ALTERNATE = 'Sole_Trader'
    B = 'B'
    I = 'I'
    D = 'D'
    F = 'F'
    N = 'N'
    S = 'S'
    T = 'T'
    Y = 'Y'
    Z = 'Z'
    GOVT_CENTRAL = 'GovtCentral'
    GOVT_EDU = 'GovtEdu'
    GOVT_LOCAL = 'GovtLocal'
    GOVT_OTHER = 'GovtOther'
    G = 'G'
    LTD = 'LTD'
    ULTD = 'ULTD'
    COOP = 'COOP'
    ASIC = 'ASIC'
    NON_ASIC = 'NON_ASIC'
