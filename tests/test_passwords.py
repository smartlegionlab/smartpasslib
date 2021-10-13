# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------


class TestSmartPassword:
    def test_login(self, smart_password, info):
        assert smart_password.login == info.login

    def test_key(self, smart_password, info):
        assert smart_password.key == info.pub_key

    def test_length(self, smart_password, info):
        assert smart_password.length == info.length
