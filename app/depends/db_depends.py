import os
import main
from fastapi import Header, HTTPException

token = os.environ['SECRECT_KEY']

async def verify_key(x_token: str = Header(...)):
    """ Depends para verificar el token en la llamada """
    if x_token is None:
        raise HTTPException(status_code=400, detail="X-Token must be in headers")
    if x_token != token:
        raise HTTPException(status_code=403, detail="X-Token invalid")
    return x_token

async def verify_user_key(x_key: str = Header(...)):
    """ Dependen para verificar al usuario y poder añadirlo al request """
    if x_key is None:
        raise HTTPException(status_code=400, detail="X-Key must be in headers")

    user = await main.server.db["users"].find_one({ "key":x_key })

    if user is None:
        raise HTTPException(status_code=403, detail="X-Key invalid")

    return user