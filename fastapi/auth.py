from passlib.context import CryptContext
from sqlalchemy.orm import Session
from crud import get_user_by_username

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, username: str, password: str):
    print("authenticate_user was called")
    user = get_user_by_username(db, username)
    if not user:
        print("User not found")
        return False
    if not verify_password(password, user.hashed_password):
        print("Invalid password")
        return False
    print("User authenticated successfully")
    return user