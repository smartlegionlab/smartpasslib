import os


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
