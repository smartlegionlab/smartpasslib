# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
from smartpasslib import generators


class GeneratorsFactory:
    """Generators factory."""

    @classmethod
    def get_urandom_gen(cls):
        """Get urandom generator."""
        return generators.UrandomGen()

    @classmethod
    def get_base_pass_gen(cls):
        """Get default password generator."""
        return generators.BasePassGen()

    @classmethod
    def get_hash_gen(cls):
        """Get hash generator."""
        return generators.HashGen()

    @classmethod
    def get_key_gen(cls):
        """Get key generator."""
        return generators.KeyGen()

    @classmethod
    def get_smart_pass_gen(cls):
        """Get smart password generator."""
        return generators.SmartPassGen()

    @classmethod
    def get_norm_pass_gen(cls):
        """Get normal password generator."""
        return generators.NormalPassGen()

    @classmethod
    def get_pass_gen(cls):
        """Get password generators"""
        return generators.PassGen()
