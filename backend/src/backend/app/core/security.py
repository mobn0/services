from secrets import token_urlsafe
from passlib.hash import pbkdf2_sha256
from backend.app.apikey.schema import ApikeyDecoded

def generate_secret(length: int) -> str:
    return token_urlsafe(length)

def generate_hash(secret: str) -> str:
    return pbkdf2_sha256.hash(secret)

def compare_hash(secret: str, hash: str) -> bool:
    return pbkdf2_sha256.verify(secret, hash)

def encode_apikey(prefix: str, secret: str) -> str:
    return f"nsc_{prefix}_{secret}"

def decode_apikey(apikey: str) -> ApikeyDecoded:
    parts = apikey.split("_")
    return ApikeyDecoded(prefix=parts[1], secret=[2])
