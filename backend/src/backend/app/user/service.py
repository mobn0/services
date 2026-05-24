from backend.app.user.model import User
from backend.app.user.schemas import Me


def me_service(current_user: User) -> Me:
    return Me(user={
        "id": current_user.id,
        "iss": current_user.identity.iss,
        "sub": current_user.identity.sub
    })
