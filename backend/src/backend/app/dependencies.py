from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from backend.app.user.model import User, Identity
from backend.app.db.database import SessionLocal
from backend.app.core.auth import verify_token

security = HTTPBearer()

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)) -> dict:
    try:
        creds: dict = verify_token(credentials.credentials)
        iss = creds.get("iss")
        if iss == None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token: missing issuer"
            )
        sub = creds.get("sub")
        if sub == None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token: missing subject"
            )
        user = db.query(User).join(User.identity).filter(Identity.sub == sub, Identity.iss == iss).first()
        
        if user:
            return user

        identity = Identity(sub=sub, iss=iss)
        user = User(identity=identity)
        
        db.add(user)
        db.commit()
        db.refresh(user)
        
        return user

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        ) from e