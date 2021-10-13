# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
class SmartPassword:
    """
    Smart password.

    Smart password with the ability to recover and
    linking to a login and a secret phrase.

    The password itself is not stored either in the open or
    in encrypted form, but is generated on the fly.

    """

    def __init__(self, login='', key='', length=12):
        """
        When creating an object, it should be passed:

        :param login: login.
        :param key: a public key that needs to be generated before creating a
        password using a username and a secret phrase.
        :param length: password length.
        """
        self._login = login
        self._length = length
        self._key = key

    @property
    def login(self):
        """Get login"""
        return self._login

    @property
    def key(self):
        """get public key"""
        return self._key

    @property
    def length(self):
        """Get password length"""
        return self._length
