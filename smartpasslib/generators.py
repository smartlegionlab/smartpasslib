# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
"""Smart Random Generators"""
import random

from smartrandom.random_master import RandomStringMaster, HashMaster, UrandomGen


class SmartKeyGen:
    _hash_master = HashMaster()

    @classmethod
    def __make_key(cls, login='', secret='', public_step=15):
        login_hash = cls._get_hash(text=login)
        secret_hash = cls._get_hash(text=secret)
        all_hash = cls._get_hash(text=login_hash + secret_hash)
        for _ in range(public_step):
            temp_hash = cls._get_hash(all_hash)
            all_hash = cls._get_hash(all_hash + temp_hash + secret_hash)
        return cls._get_hash(all_hash)

    @classmethod
    def get_public_key(cls, login='', secret=''):
        return cls.__make_key(login, secret, 15)

    @classmethod
    def get_private_key(cls, login='', secret=''):
        return cls.__make_key(login, secret, 30)

    @classmethod
    def check_data(cls, login='', secret='', key=''):
        return cls.get_public_key(login=login, secret=secret) == key

    @classmethod
    def _get_hash(cls, text=''):
        text = str(text)
        return cls._hash_master.create(str(text.encode('utf-8')))


class BaseSmartPassGen:
    random_master = RandomStringMaster()
    urandom = UrandomGen()

    @classmethod
    def generate(cls, seed='', length=15, size=32) -> str:
        if not seed:
            seed = cls.get_seed(size)
        cls._set_seed(seed)
        password = cls.random_master.create_string(length)
        seed = str(cls.get_seed())
        cls._set_seed(seed)
        return password

    @classmethod
    def _set_seed(cls, seed):
        seed = str(seed)
        random.seed(seed)
        return seed

    @classmethod
    def get_seed(cls, size=32) -> bytes:
        return cls.urandom.generate(size=size)


class SmartPasswordMaster:
    random_master = RandomStringMaster()
    key_gen = SmartKeyGen()
    smart_pass_gen = BaseSmartPassGen()

    @classmethod
    def get_password(cls, length=10):
        return cls.random_master.create_string(length)

    @classmethod
    def get_default_password(cls, secret='', length=10):
        return cls.get_smart_password(secret=secret, length=length)

    @classmethod
    def get_smart_password(cls, login='', secret='', length=10):
        seed = cls.key_gen.get_private_key(login, secret)
        return cls.smart_pass_gen.generate(seed, length=length)

    @classmethod
    def get_public_key(cls, login='', secret=''):
        return cls.key_gen.get_public_key(login, secret)

    @classmethod
    def check_data(cls, login, secret, public_key):
        return cls.key_gen.check_data(login, secret, public_key)
