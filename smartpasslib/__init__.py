# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Smart Password Library - Cross-platform library for generating smart passwords."""
from .generators import (
    SmartPasswordMaster,
    HashGenerator,
    UrandomGenerator,
    SmartKeyGenerator,
    BasePasswordGenerator,
    StrongPasswordGenerator,
    SmartPasswordGenerator,
)
from .managers import SmartPassword, SmartPasswordManager, SmartPasswordFactory
__version__ = '0.7.1'
__author__ = 'A.A. Suvorov'
__all__ = [
    "SmartPasswordMaster",
    "HashGenerator",
    "UrandomGenerator",
    "SmartKeyGenerator",
    "BasePasswordGenerator",
    "StrongPasswordGenerator",
    "SmartPasswordGenerator",
    "SmartPasswordFactory",
    "SmartPasswordManager",
    "SmartPassword"
]
