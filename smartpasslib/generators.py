# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import hashlib
import os
import random
import string


class UrandomGen:
    @classmethod
    def generate(cls, size=32):
        return os.urandom(size)


class BasePassGen:
    """Password generator"""
    # The set of symbols used in the generation.
    symbols = string.ascii_letters + string.digits + '`!@#$%^&()_[]{}"|<>?'
    _urandom = UrandomGen()

    @classmethod
    def generate(cls, seed='', length=15, size=32) -> str:
        """
        Generates a regular password
        :param seed: A string for configuring the randomness.
        :param length: Password length.
        :param size: The size of the data for generating random data if no seed is specified.
        :return: - <str> - A string with a password of the specified length.
        """

        if not seed:
            seed = cls.get_seed(size)

        cls._set_seed(seed)

        password = ''.join([random.choice(cls.symbols) for _ in range(length)])
        seed = str(cls.get_seed())

        cls._set_seed(seed)
        return password

    @classmethod
    def _set_seed(cls, seed):
        """
        Configuring the randomness
        :param seed: A string for configuring the randomness.
        :return: <str> - A string for configuring the randomness.
        """
        seed = str(seed)
        random.seed(seed)
        return seed

    @classmethod
    def get_seed(cls, size=32) -> bytes:
        """
        Generation of random data
        :param size: The size of the data for generating random
        data if no seed is specified.
        :return: <bytes> - Bytes of random data of the specified size.
        """
        return cls._urandom.generate(size=size)


class HashGen:
    _method = hashlib.sha3_512

    @classmethod
    def generate(cls, text=''):
        sha = cls._method(text.encode('utf-8'))
        return sha.hexdigest()


class KeyGen:
    _hash_gen = HashGen()
    _pass_gen = BasePassGen()

    @classmethod
    def make(cls, login, secret, step=15):
        login_hash = cls._hash_gen.generate(text=login)
        secret_hash = cls._hash_gen.generate(text=secret)
        all_hash = cls._hash_gen.generate(login_hash + secret_hash)

        for _ in range(step):
            temp_hash = cls._hash_gen.generate(all_hash)
            all_hash = cls._hash_gen.generate(all_hash + temp_hash + secret_hash)

        public_key = cls._hash_gen.generate(all_hash)
        return public_key

    @classmethod
    def check(cls, login, secret, key):
        return cls.make(login=login, secret=secret) == key


class SmartPassGen:
    step = 2
    _generator = BasePassGen()
    _key_gen = KeyGen()

    @classmethod
    def generate(cls, login='', secret='', length=15):
        seed = cls._key_gen.make(login=login, secret=secret, step=cls.step)
        return cls._generator.generate(seed=seed, length=length)


class NormalPassGen:
    step = 2
    _key_gen = KeyGen()
    _pass_gen = BasePassGen()

    @classmethod
    def generate(cls, secret, length):
        seed = cls._key_gen.make(login=secret, secret=secret, step=cls.step)
        return cls._pass_gen.generate(seed=seed, length=length)


class PassGen:
    smart = SmartPassGen()
    normal = NormalPassGen()
    base = BasePassGen()


class Tools:
    pass_gen = PassGen()
    urandom_gen = UrandomGen()
    hash_gen = HashGen()
    key_gen = KeyGen()
