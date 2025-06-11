import hashlib


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
