# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------


class TestSmartPassword:
    def test_login(self, smart_password, context):
        assert smart_password.login == context.login

    def test_key(self, smart_password, context):
        assert smart_password.key == context.pub_key

    def test_length(self, smart_password, context):
        assert smart_password.length == context.length


class TestSmartPassMan:
    def test_file(self, pass_man, context):
        assert pass_man.file == context.file

    def test_passwords(self, pass_man):
        assert isinstance(pass_man.passwords, dict)
        assert pass_man.passwords == {}

    def test_add(self, pass_man, smart_password):
        pass_man.add(smart_password)
        assert smart_password.login in pass_man.passwords

    def test_count(self, pass_man, smart_password):
        pass_man.add(smart_password)
        assert pass_man.count == 1

    def test_add_smart_pass(self, pass_man, context):
        password = pass_man.add_smart_pass(login=context.login, secret=context.secret, length=context.length)
        assert password.login in pass_man.passwords

    def test_add_passwords(self, pass_man, smart_password, smart_password2):
        password_list = [smart_password, smart_password2]
        pass_man.add_passwords(password_list)
        assert all([password.login in pass_man.passwords for password in password_list])

    def test_get_password(self, pass_man, smart_password):
        pass_man.add(smart_password)
        assert pass_man.get_password(smart_password.login) == smart_password

    def test_remove(self, pass_man, smart_password):
        pass_man.add(smart_password)
        assert smart_password in pass_man.passwords.values()
        pass_man.remove(smart_password.login)
        assert smart_password not in pass_man.passwords.values()

    def test_load_file(self, pass_man, file):
        pass_man.file = file
        pass_man.load_file()
        assert pass_man.count == 1

    def test_load_bad_file(self, pass_man, bad_file):
        pass_man.file = bad_file
        assert pass_man.load_file() == {}

    def test_load_not_file(self, pass_man):
        pass_man.file = ''
        assert pass_man.load_file() == {}

    def test_save_file(self, pass_man, smart_password, context):
        pass_man.add(smart_password)
        pass_man.file = context.file
        pass_man.save_file()
        file = open(context.file)
        lines = file.read()
        file.close()
        assert smart_password.login in lines

    def test_clear(self, pass_man, smart_password):
        pass_man.add(smart_password)
        assert pass_man.count == 1
        pass_man.clear()
        assert pass_man.count == 0

    def test__save_file(self, pass_man, smart_password, context):
        pass_man.add(smart_password)
        pass_man.file = context.file
        pass_man.save_file()
        file = open(context.file)
        lines = file.read()
        file.close()
        assert smart_password.login in lines
