from base64 import b16decode, b16encode


class BinaryHexConverter:
    regex = "(?:[0-9a-fA-F]{2})+"

    def to_python(self, value: str) -> bytes:
        return b16encode(b16decode(value, casefold=True)).decode

    def to_url(self, value: bytes) -> str:
        return value
