from sqlalchemy.orm import Session
from backend.app.user.model import User
from backend.app.apikey.model import Apikey
from backend.app.core.security import generate_secret, generate_hash, compare_hash, encode_apikey
from backend.app.apikey.schema import ApikeyCreateResponse


def create_api_key_service(name: str, description: str, current_user: User, db: Session) -> ApikeyCreateResponse:
    prefix = generate_secret(16)
    secret = generate_secret(32)
    hash_secret = generate_hash(secret)

    apikey = Apikey(name=name, description=description, prefix=prefix, secret=hash_secret, user=current_user)

    db.add(apikey)
    db.commit()
    db.refresh(apikey)

    return ApikeyCreateResponse(key=encode_apikey(prefix=apikey.prefix, secret=secret))