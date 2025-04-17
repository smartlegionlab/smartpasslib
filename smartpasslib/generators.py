import hashlib
import os
import random
import secrets
import string
from typing import Union


class HashGenerator:
    """SHA3-512 hash generator."""

    @classmethod
    def generate(cls, text: str) -> str:
        """
        Generates a SHA3-512 hash for the given text.

        Args:
            text (str): Input string to hash.

        Returns:
            str: Hexadecimal representation of the hash.
        """
        text = str(text)
        sha = hashlib.sha3_512(text.encode('utf-8'))
        return sha.hexdigest()


class UrandomGenerator:
    """Cryptographically secure random bytes generator using `os.urandom`."""

    @classmethod
    def generate(cls, size: int = 32) -> bytes:
        """
        Generates random bytes of the specified size.

        Args:
            size (int): Number of bytes to generate (default: 32).

        Returns:
            bytes: Random byte string.
        """
        return os.urandom(size)


class SmartKeyGenerator:
    """Key generator based on iterative hashing."""

    @classmethod
    def _create_key(cls, login: str = '', secret: str = '', public_step: int = 15) -> str:
        """
        Internal method for key generation.

        Args:
            login (str): User login.
            secret (str): Secret string.
            public_step (int): Number of hashing iterations.

        Returns:
            str: Generated key.
        """
        login_hash = cls.get_hash(text=login)
        secret_hash = cls.get_hash(text=secret)
        all_hash = cls.get_hash(text=login_hash + secret_hash)
        for _ in range(public_step):
            temp_hash = cls.get_hash(all_hash)
            all_hash = cls.get_hash(all_hash + temp_hash + secret_hash)
        return cls.get_hash(all_hash)

    @classmethod
    def generate_public_key(cls, login: str = '', secret: str = '') -> str:
        """
        Generates a public key.

        Args:
            login (str): User login.
            secret (str): Secret string.

        Returns:
            str: Public key.
        """
        return cls._create_key(login, secret, 60)

    @classmethod
    def generate_private_key(cls, login: str = '', secret: str = '') -> str:
        """
        Generates a private key.

        Args:
            login (str): User login.
            secret (str): Secret string.

        Returns:
            str: Private key.
        """
        return cls._create_key(login, secret, 30)

    @classmethod
    def check_key(cls, login: str = '', secret: str = '', key: str = '') -> bool:
        """
        Verifies if a key matches the given login and secret.

        Args:
            login (str): User login.
            secret (str): Secret string.
            key (str): Key to verify.

        Returns:
            bool: True if the key is valid, False otherwise.
        """
        return cls.generate_public_key(login=login, secret=secret) == key

    @classmethod
    def get_hash(cls, text: str = '') -> str:
        """
        Generates a hash for the given text.

        Args:
            text (str): Input string.

        Returns:
            str: Hash of the input string.
        """
        text = str(text)
        return HashGenerator.generate(str(text.encode('utf-8')))


class BasePasswordGenerator:
    """Basic password generator with letters, digits, and symbols."""

    letters = string.ascii_letters
    digits = string.digits
    symbols = '!@#$%&^_'

    @classmethod
    def generate(cls, length: int = 10) -> str:
        """
        Generates a password of the specified length.

        Args:
            length (int): Password length (default: 10).

        Returns:
            str: Generated password.
        """
        symbols_string = cls.letters + cls.digits + cls.symbols
        return ''.join((random.choice(symbols_string) for _ in range(length)))


class StrongPasswordGenerator:
    """Strong password generator ensuring at least one character from each category."""

    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    digits = string.digits
    symbols = '!@#$%&^_'

    @classmethod
    def generate(cls, length: int = 10) -> str:
        """
        Generates a strong password with guaranteed character diversity.

        Args:
            length (int): Password length (default: 10).

        Returns:
            str: Generated password.

        Raises:
            ValueError: If length is less than 4.
        """
        if length < 4:
            raise ValueError("The length cannot be less than 4.")

        result = [
            secrets.choice(cls.upper_letters),
            secrets.choice(cls.lower_letters),
            secrets.choice(cls.digits),
            secrets.choice(cls.symbols),
        ]
        result += [
            secrets.choice(cls.upper_letters + cls.lower_letters + cls.digits + cls.symbols)
            for _ in range(length - 4)
        ]
        secrets.SystemRandom().shuffle(result)
        return ''.join(result)


class SmartPasswordGenerator:
    """Seed-based reproducible password generator."""

    @classmethod
    def generate(cls, seed: Union[str, bytes] = '', length: int = 15, size: int = 32) -> str:
        """
        Generates a password based on a seed.

        Args:
            seed (str | bytes): Seed for reproducibility (if empty, generates a random one).
            length (int): Password length (default: 15).
            size (int): Seed size in bytes (default: 32).

        Returns:
            str: Generated password.
        """
        if not seed:
            seed = cls.get_seed(size)
        cls._set_seed(seed)
        password = BasePasswordGenerator.generate(length)
        seed = str(cls.get_seed())
        cls._set_seed(seed)
        return password

    @classmethod
    def _set_seed(cls, seed: Union[str, bytes]) -> str:
        """
        Sets the random seed for reproducibility.

        Args:
            seed (str | bytes): Seed value.

        Returns:
            str: Seed as a string.
        """
        seed = str(seed)
        random.seed(seed)
        return seed

    @classmethod
    def get_seed(cls, size: int = 32) -> bytes:
        """
        Generates a cryptographically secure random seed.

        Args:
            size (int): Seed size in bytes (default: 32).

        Returns:
            bytes: Random seed.
        """
        return UrandomGenerator.generate(size=size)


class SmartPasswordMaster:
    """Main class for password and key generation management."""

    @staticmethod
    def generate_base_password(length: int = 10) -> str:
        """
        Generates a basic password.

        Args:
            length (int): Password length (default: 10).

        Returns:
            str: Generated password.
        """
        return BasePasswordGenerator.generate(length)

    @staticmethod
    def generate_strong_password(length: int = 10) -> str:
        """
        Generates a strong password.

        Args:
            length (int): Password length (default: 10).

        Returns:
            str: Generated password.
        """
        return StrongPasswordGenerator.generate(length)

    @classmethod
    def generate_default_smart_password(cls, secret: str = '', length: int = 10) -> str:
        """
        Generates a smart password using a default method.

        Args:
            secret (str): Secret string.
            length (int): Password length (default: 10).

        Returns:
            str: Generated password.
        """
        return cls.generate_smart_password(secret=secret, length=length)

    @classmethod
    def generate_smart_password(cls, login: str = '', secret: str = '', length: int = 10) -> str:
        """
        Generates a reproducible password based on login and secret.

        Args:
            login (str): User login.
            secret (str): Secret string.
            length (int): Password length (default: 10).

        Returns:
            str: Generated password.
        """
        seed = SmartKeyGenerator.generate_private_key(login, secret)
        return SmartPasswordGenerator.generate(seed, length=length)

    @classmethod
    def generate_public_key(cls, login: str = '', secret: str = '') -> str:
        """
        Generates a public key.

        Args:
            login (str): User login.
            secret (str): Secret string.

        Returns:
            str: Public key.
        """
        return SmartKeyGenerator.generate_public_key(login, secret)

    @classmethod
    def generate_private_key(cls, login: str = '', secret: str = '') -> str:
        """
        Generates a private key.

        Args:
            login (str): User login.
            secret (str): Secret string.

        Returns:
            str: Private key.
        """
        return SmartKeyGenerator.generate_public_key(login, secret)

    @classmethod
    def check_public_key(cls, login: str, secret: str, public_key: str) -> bool:
        """
        Validates a public key against login and secret.

        Args:
            login (str): User login.
            secret (str): Secret string.
            public_key (str): Public key to verify.

        Returns:
            bool: True if the key is valid, False otherwise.
        """
        return SmartKeyGenerator.check_key(login, secret, public_key)
