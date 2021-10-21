# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
from smartpasslib.generators import (
    UrandomGen,
    BasePassGen,
    HashGen,
    KeyGen,
    SmartPassGen,
    NormalPassGen, PassGen
)


class TestGeneratorsFactory:
    def test_get_urandom_gen(self, gen_factory):
        assert isinstance(gen_factory.get_urandom_gen(), UrandomGen)

    def test_get_base_pass_gen(self, gen_factory):
        assert isinstance(gen_factory.get_base_pass_gen(), BasePassGen)

    def test_get_hash_gen(self, gen_factory):
        assert isinstance(gen_factory.get_hash_gen(), HashGen)

    def test_get_key_gen(self, gen_factory):
        assert isinstance(gen_factory.get_key_gen(), KeyGen)

    def test_get_smart_pass_gen(self, gen_factory):
        assert isinstance(gen_factory.get_smart_pass_gen(), SmartPassGen)

    def test_get_norm_pass_gen(self, gen_factory):
        assert isinstance(gen_factory.get_norm_pass_gen(), NormalPassGen)

    def test_get_pass_gen(self, gen_factory):
        assert isinstance(gen_factory.get_pass_gen(), PassGen)
