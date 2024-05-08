# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
"""Generators"""
import hashlib
import os
import random
import string


class RandomStringMaster:
    letters = string.ascii_letters

    @classmethod
    def get(cls, length=10):
        return ''.join((random.choice(cls.letters) for _ in range(length)))


class RandomNumberMaster:
    numbers = string.digits

    @classmethod
    def get(cls, length=10):
        return ''.join((random.choice(cls.numbers) for _ in range(length)))


class RandomSymbolMaster:
    symbols = '@$!%*#?&-'

    @classmethod
    def get(cls, length=10):
        return ''.join((random.choice(cls.symbols) for _ in range(length)))


class RandomPasswordMaster:
    letters = string.ascii_letters
    numbers = string.digits
    symbols = '@$!%*#?&-'

    @classmethod
    def get(cls, length=10):
        return ''.join((random.choice(cls.letters + cls.numbers + cls.symbols) for _ in range(length)))


class RandomHashMaster:
    @classmethod
    def get(cls, text):
        text = str(text)
        sha = hashlib.sha3_512(text.encode('utf-8'))
        new_hash = sha.hexdigest()
        return new_hash


class RandomMaster:
    string = RandomStringMaster()
    number = RandomNumberMaster()
    symbol = RandomSymbolMaster()
    password = RandomPasswordMaster()
    hash = RandomHashMaster()

    @classmethod
    def get_code(cls, length=10, number_flag=False, string_flag=False, symbol_flag=False):
        data = ''
        if string_flag:
            data += cls.string.letters
        if number_flag:
            data += cls.number.numbers
        if symbol_flag:
            data += cls.symbol.symbols
        return ''.join((random.choice(data) for _ in range(length)))


class UrandomGen:
    @classmethod
    def generate(cls, size=32):
        return os.urandom(size)


class HashGen:
    _method = hashlib.sha3_512

    @classmethod
    def generate(cls, text=''):
        text = str(text)
        sha = cls._method(text.encode('utf-8'))
        return sha.hexdigest()


class SmartKeyGen:
    _hash_gen = HashGen()

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
        return cls._hash_gen.generate(str(text.encode('utf-8')))


class BaseSmartPassGen:
    master = RandomMaster()
    urandom = UrandomGen()

    @classmethod
    def generate(cls, seed='', length=15, size=32) -> str:
        if not seed:
            seed = cls.get_seed(size)
        cls._set_seed(seed)
        password = cls.master.password.get(length)
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
    random_master = RandomMaster()
    key_gen = SmartKeyGen()
    smart_pass_gen = BaseSmartPassGen()

    @classmethod
    def get_password(cls, length=10):
        return cls.random_master.password.get(length)

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
