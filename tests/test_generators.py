# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------


class TestUrandomGen:
    def test_generate(self, urandom):
        assert urandom.generate() != urandom.generate()


class TestDefaultPassGen:
    def test_generate(self, default):
        assert default.generate() != default.generate()


class TestHashGen:
    def test_generate(self, hash_gen):
        assert hash_gen.generate('test') == hash_gen.generate('test')


class TestKeyGen:
    def test_make(self, key_gen, context):
        assert key_gen.make(login=context.login, secret=context.secret) == context.pub_key

    def test_check(self, key_gen, context):
        assert key_gen.check(login=context.login, secret=context.secret, key=context.pub_key)


class TestSmartPassGen:
    def test_generate(self, smart, context):
        assert smart.generate(login=context.login, secret=context.secret, length=context.length) == context.smart_pass


class TestNormalPassGen:
    def test_generate(self, normal, context):
        assert normal.generate(secret=context.secret, length=context.length) == context.normal_pass
