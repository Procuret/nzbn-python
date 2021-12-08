"""
New Zealand Business Number
Order Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from enum import Enum


class OrderBy(Enum):
    NZBN = 'NZBN'
    ENTITY_NAME = 'ENTITY_NAME'
    ENTITY_STATUS = 'ENTITY_STATUS'
    ENTITY_TYPE = 'ENTITY_TYPE_CODE'


class Order(Enum):
    ASCENDING = 'ASC'
    DESCENDING = 'DESC'
