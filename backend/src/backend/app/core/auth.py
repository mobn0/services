from jwt import PyJWKClient, decode
from backend.app.core.config import BACKEND_DOMAIN, LOGTO_PUBLIC_DOMAIN

LOGTO_ISSUER = f"{LOGTO_PUBLIC_DOMAIN}/oidc"

jwks_client = PyJWKClient(f"{LOGTO_ISSUER}/jwks")

def verify_token(token: str) -> dict:
    signing_key = jwks_client.get_signing_key_from_jwt(token)

    return decode(
    token, signing_key.key, algorithms=["RS256"], audience=BACKEND_DOMAIN, issuer=LOGTO_ISSUER
    )