# from typing import Annotated
# import datetime
# from fastapi import APIRouter, Depends, HTTPException, Path, Query
# from fastapi.encoders import jsonable_encoder
# from rest_framework import status
# from sqlalchemy.ext.asyncio import AsyncSession
# from fastapi.security import OAuth2PasswordRequestForm
#
# from schemas import UserInDB, UserCreate, TokenInfo, AuthUser, RefreshToken
# from models import User
#
#
# router = APIRouter()
#
# @router.post('/client/create', response_model=UserInDB, status_code=status.HTTP_201_CREATED)
# async def create_use