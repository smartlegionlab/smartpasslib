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


class PassGen:
    """Password generator"""
    # The set of symbols used in the generation.
    symbols = string.ascii_letters + string.digits + '`!@#$%^&()_[]{}"|<>?'

    def generate(self, seed='', length=15, size=32) -> str:
        """
        Generates a regular password

        :param seed: A string for configuring the randomness.
        :param length: Password length.
        :param size: The size of the data for generating random data if no seed is specified.
        :return: - <str> - A string with a password of the specified length.

        """

        if not seed:
            seed = self.get_seed(size)

        self._set_seed(seed)

        password = ''.join([random.choice(self.symbols) for _ in range(length)])
        seed = str(self.get_seed())

        self._set_seed(seed)
        return password

    @staticmethod
    def _set_seed(seed):
        """
        Configuring the randomness

        :param seed: A string for configuring the randomness.
        :return: <str> - A string for configuring the randomness.

        """
        seed = str(seed)
        random.seed(seed)
        return seed

    @staticmethod
    def get_seed(size=32) -> bytes:
        """
        Generation of random data

        :param size: The size of the data for generating random
        data if no seed is specified.
        :return: <bytes> - Bytes of random data of the specified size.

        """
        return os.urandom(size)

    def __call__(self, seed='', length=15, size=32):
        return self.generate(seed=seed, length=length, size=size)


class HashGen:
    """Hash generator"""

    # Hash method
    hash_gen = hashlib.sha3_512

    def get_hash(self, text=''):
        """
        Hashes a string

        :param text: Hashes a string.
        :return: <str> - The string to be hashed.

        """
        sha = self.hash_gen(text.encode('utf-8'))
        return sha.hexdigest()

    def __call__(self, text=''):
        return self.get_hash(text=text)


class KeyGen:
    """
    Key generator.

    Allows you to generate public keys,
    for open storage,
    with which you can make
    checking for the correctness of the entered data.

    """

    def __init__(self):
        # Hash generator
        self._hash_gen = HashGen()
        # Password generator
        self._pass_gen = PassGen()

    def get_key(self, login, secret, step=15):
        """
        Generates a public key.

        Allows you to generate public keys,
        for open storage,
        with which you can make
        checking for the correctness of the entered data.

        :param login: Login.
        :param secret: Secret phrase.
        :param step: The number of hashes to make it harder to crack.
        :return: <str> - Public key linked to login and secret phrase.

        """
        login_hash = self._make_hash(login)
        secret_hash = self._make_hash(secret)
        all_hash = self._make_hash(login_hash + secret_hash)

        for _ in range(step):
            temp_hash = self._make_hash(all_hash)
            all_hash = self._make_hash(all_hash + temp_hash)

        return self._hash_gen(all_hash)

    def _make_hash(self, text):
        """
        Generates a hash of the string.

        :param text: String.
        :return: <str> - The hash of the string.

        """
        return self._hash_gen(text)

    def check_key(self, login, secret, user_key):
        """
        Checking for the correspondence of the
        login and the secret phrase.

        Generates a new public key from the username
        and password, then compares it to the passed key.

        :param login: Login.
        :param secret: Secret phrase.
        :param user_key: User public key.
        :return: <bool> - True/False logical check status.

        """
        return self.get_key(login=login, secret=secret) == user_key

    def __call__(self, login, secret, step=15):
        return self.get_key(login=login, secret=secret, step=step)


class SmartPassGen:
    """
    Smart password generator.

    Generator of smart passwords "on the fly", linked to the login
    and the secret phrase and the possibility of recovery.

    """
    # The hash generation step at which the generated hash is
    # will be used to generate the password.
    step = 2

    def __init__(self):
        # Password generator
        self._generator = PassGen()
        # Key generator
        self._key_gen = KeyGen()
        # Hash generator
        self._hash_gen = HashGen()

    def generate(self, login, secret, length):
        """
        Generates a smart password.

        Password linked to the login and secret phrase,
        with the ability to generate "on the fly" and the ability to recover.

        :param login: login.
        :param secret: secret phrase.
        :param length: password length.
        :return: smart password.

        """
        seed = self._key_gen(login=login, secret=secret, step=self.step)
        return self._generator(seed=seed, length=length)

    def __call__(self, login, secret, length):
        return self.generate(login=login, secret=secret, length=length)


class NormalPassGen:
    """
    Generator of recoverable passwords.

    The password is tied only to the secret phrase.

    """
    # The hash generation step at which the generated hash is
    # will be used to generate the password.
    step = 2

    def __init__(self):
        # Key Generator
        self._key_gen = KeyGen()
        # Password generator
        self._pass_gen = PassGen()

    def generate(self, secret, length):
        """
        Generates a password.

        In this case, the secret phrase is used and
        as a login and as a secret phrase.

        This effect can be obtained using a smart password generator,
        while entering the same phrase or word instead
        of the login and the secret phrase.

        :param secret: Secret phrase.
        :param length: Password length.
        :return: <str> - Password linked to a secret phrase.

        """
        seed = self._key_gen(login=secret, secret=secret, step=self.step)
        return self._pass_gen(seed=seed, length=length)

    def __call__(self, secret, length):
        return self.generate(secret=secret, length=length)


class GeneratorsFactory:
    """Generators factory."""

    @classmethod
    def get_hash_gen(cls):
        """Get hash generator."""
        return HashGen()

    @classmethod
    def get_key_gen(cls):
        """Get key generator."""
        return KeyGen()

    @classmethod
    def get_pass_gen(cls):
        """Get default password generator."""
        return PassGen()

    @classmethod
    def get_norm_pass_gen(cls):
        """Get normal password generator."""
        return NormalPassGen()

    @classmethod
    def get_smart_pass_gen(cls):
        """Get smart password generator."""
        return SmartPassGen()


class PasswordsGenerator:
    """Generator of common, standard and smart passwords."""
    def __init__(self):
        self._pass_gen = GeneratorsFactory.get_pass_gen()
        self._norm_pass_gen = GeneratorsFactory.get_norm_pass_gen()
        self._smart_pass_gen = GeneratorsFactory.get_smart_pass_gen()

    def get_def_pass(self, seed: str = '', length: int = 15, size: int = 32):
        """
        Generates a regular password.

        :param seed: A string for configuring the randomness.
        :param length: Password length.
        :param size: The size of the data for generating random data if no seed is specified.
        :return: <str> - A string with a password of the specified length.

        """
        return self._pass_gen(seed=seed, length=length, size=size)

    def get_norm_pass(self, secret='', length=15):
        """
        Generates a password.

        In this case, the secret phrase is used and
        as a login and as a secret phrase.

        This effect can be obtained using a smart password generator,
        while entering the same phrase or word instead
        of the login and the secret phrase.

        :param secret: Secret phrase.
        :param length: Password length.
        :return: <str> - Password linked to a secret phrase.

        """
        return self._norm_pass_gen(secret=secret, length=length)

    def get_smart_pass(self, login='', secret='', length=15):
        """
        Generates a smart password.

        Password linked to the login and secret phrase,
        with the ability to generate "on the fly" and the ability to recover.

        :param login: login.
        :param secret: secret phrase.
        :param length: password length.
        :return: <str> - smart password.
        """
        return self._smart_pass_gen(login=login, secret=secret, length=length)


def norm_pass_gen(secret='', length=15):
    """
    Generates a password associated with a secret phrase.

    By using the same passphrase, you will always
    receive the same password.

    :param secret: Secret phrase.
    :param length: Password length.
    :return: <str> - Generated password string.

    """
    pass_gen = PasswordsGenerator()
    return pass_gen.get_norm_pass(secret=secret, length=length)


def smart_pass_gen(login='', secret='', length=15):
    """
    Generates a smart password.

    Generates a password linked to a login and a secret phrase.
    The password can be recovered or generated at any time
    using the login and secret phrase specified
    during the first generation.

    :param login: Login.
    :param secret: Secret phrase.
    :param length: Password length.
    :return: <str> - Generated password string.

    """
    pass_gen = PasswordsGenerator()
    return pass_gen.get_smart_pass(
        login=login,
        secret=secret,
        length=length
    )


def get_random_data(size=32):
    """
    Generation of random data.

    :param size: The size of the data for generating random
    data if no seed is specified.
    :return: <bytes> - Bytes of random data of the specified size.

    """
    return os.urandom(size)


def def_pass_gen(length=15):
    """
    Generates a regular password.

    When called, it will return different
    passwords each time.

    :param length: Password length.
    :return: <str> - Generated password string.

    """
    pass_gen = PasswordsGenerator()
    return pass_gen.get_def_pass(length=length)


def get_hash(text=''):
    """
    Hashes a string.

    :param text: string.
    :return: <str> - The hash of the string.

    """
    hash_gen = GeneratorsFactory.get_hash_gen()
    return hash_gen(text)


def get_key(login='', secret=''):
    """
    Generates a public key.

    :param login: Login.
    :param secret: Secret phrase.
    :return: <str> - Public key.

    """
    key_gen = GeneratorsFactory.get_key_gen()
    return key_gen(login=login, secret=secret)


def check_key(login='', secret='', user_key=''):
    """
    Checking for the correspondence of the
    login and the secret phrase.

    Generates a new public key from the username
    and password, then compares it to the passed key.

    :param login: Login.
    :param secret: Secret phrase.
    :param user_key: User public key.
    :return: <bool> - True/False logical check status.

    """
    key_gen = GeneratorsFactory.get_key_gen()
    return key_gen.check_key(
        login=login,
        secret=secret,
        user_key=user_key
    )
