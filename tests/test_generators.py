# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import random


class TestPassGen:
    def test_generate(self, pass_gen):
        assert pass_gen.generate() != pass_gen.generate()

    def test__set_seed(self, pass_gen):
        pass_gen._set_seed('login')
        num = random.randint(1, 10)
        num2 = random.randint(1, 10)
        assert num == 1 and num2 == 3

    def test_get_seed(self, pass_gen):
        assert pass_gen.get_seed() != pass_gen.get_seed()
        assert len(pass_gen.get_seed()) == 32

    def test__call__(self, pass_gen):
        assert pass_gen() != pass_gen()


class TestHashGen:
    def test_get_hash(self, hash_gen, info, hash_login):
        assert hash_gen.get_hash(info.login) == hash_login

    def test__call__(self, hash_gen, info, hash_login):
        assert hash_gen(info.login) == hash_login


class TestKeyGen:
    def test_get_key(self, key_gen, info):
        assert key_gen.get_key(login=info.login, secret=info.secret) == info.pub_key

    def test__make_hash(self, key_gen, info, hash_login):
        assert key_gen._make_hash(text=info.login) == hash_login

    def test_check_key(self, key_gen, info):
        assert key_gen.check_key(login=info.login, secret=info.secret, user_key=info.pub_key)

    def test__call__(self, key_gen, info):
        assert key_gen(login=info.login, secret=info.secret) == info.pub_key


class TestSmartPassGen:
    def test_generate(self, smart_pass_generator, info):
        kwargs = dict(login=info.login, secret=info.secret, length=info.length)
        assert smart_pass_generator.generate(**kwargs) == info.smart_pass

    def test__call__(self, smart_pass_generator, info):
        kwargs = dict(login=info.login, secret=info.secret, length=info.length)
        assert smart_pass_generator(**kwargs) == info.smart_pass


class TestNormalPassGen:
    def test_generate(self, normal_pass_gen, info):
        assert normal_pass_gen.generate(secret=info.secret, length=info.length) == info.normal_pass

    def test__call__(self, normal_pass_gen, info):
        kwargs = dict(secret=info.secret, length=info.length)
        assert normal_pass_gen(**kwargs) == info.normal_pass


class TestGeneratorsFactory:
    def test_get_hash_gen(self, gen_factory, hash_gen):
        assert isinstance(gen_factory.get_hash_gen(), type(hash_gen))

    def test_get_key_gen(self, gen_factory, key_gen):
        assert isinstance(gen_factory.get_key_gen(), type(key_gen))

    def test_get_pass_gen(self, gen_factory, pass_gen):
        assert isinstance(gen_factory.get_pass_gen(), type(pass_gen))

    def test_get_norm_pass_gen(self, gen_factory, normal_pass_gen):
        assert isinstance(gen_factory.get_norm_pass_gen(), type(normal_pass_gen))

    def test_get_smart_pass_gen(self, gen_factory, smart_pass_generator):
        assert isinstance(gen_factory.get_smart_pass_gen(), type(smart_pass_generator))


class TestPasswordsGenerator:
    def test_get_def_pass(self, passwords_generator, info):
        assert passwords_generator.get_def_pass() != passwords_generator.get_def_pass()

    def test_get_norm_pass(self, passwords_generator, info):
        pass1 = passwords_generator.get_norm_pass(secret=info.secret, length=info.length)
        pass2 = passwords_generator.get_norm_pass(secret=info.secret, length=info.length)
        assert pass1 == pass2

    def test_get_smart_password(self, passwords_generator, info):
        kwargs = dict(login=info.login, secret=info.secret, length=info.length)
        pass1 = passwords_generator.get_smart_pass(**kwargs)
        pass2 = passwords_generator.get_smart_pass(**kwargs)
        assert pass1 == pass2


def test_norm_pass_gen(func_norm_pass_gen, info):
    assert func_norm_pass_gen(secret=info.secret, length=info.length) == info.normal_pass


def test_smart_pass_gen(func_smart_pass_gen, info):
    assert func_smart_pass_gen(login=info.login, secret=info.secret, length=info.length)


def test_get_random_data(func_get_random_data):
    assert func_get_random_data(size=30) != func_get_random_data(size=30)


def test_def_pass_gen(func_def_pass_gen, info):
    assert func_def_pass_gen(length=info.length) != func_def_pass_gen(length=info.length)


def test_get_hash(func_get_hash, info, hash_login):
    assert func_get_hash(info.login) == hash_login


def test_get_key(func_get_key, info):
    assert func_get_key(login=info.login, secret=info.secret) == info.pub_key


def test_check_key(func_check_key, info):
    assert func_check_key(login=info.login, secret=info.secret, user_key=info.pub_key)
