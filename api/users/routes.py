from fastapi import APIRouter, Depends, Body, HTTPException, Query

from middleware.verify_jwt import verify_jwt

router = APIRouter()


@router.get("/hello-world", dependencies=[Depends(verify_jwt)])
async def hello_world():
    return {"message": "Hello World"}
