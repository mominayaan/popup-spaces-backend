from fastapi import HTTPException, Request
import jwt

from config import config


def verify_jwt(request: Request):
    token = request.headers.get("Authorization")
    if token is None or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authorization token is missing")

    token_data = token.split(" ")[1]
    try:
        # Decode the token using your secret key and algorithm
        payload = jwt.decode(token_data, config.JWT_SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
