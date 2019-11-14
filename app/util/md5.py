import hashlib


def encode_md5(password: str) -> str:
    return hashlib.md5(bytes(password, encoding='utf-8')).hexdigest()

