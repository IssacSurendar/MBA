from fastapi import APIRouter, Depends
from schemas.userSchema import LoginSchema, RegisterSchema, UpdateUserSchema
from fastapi.responses import JSONResponse
from core import response as RES
from core.db import SyncMongoDep
from core.oauth2 import get_password_hash
import copy, uuid
from motor.motor_asyncio import AsyncIOMotorDatabase
from pymongo.database import Database
from datetime import datetime
from fastapi.encoders import jsonable_encoder


router = APIRouter(prefix='/api/v1', tags=['User'])


@router.post('/auth/login')
async def login(request:LoginSchema):
    response = copy.deepcopy(RES.LOGIN_FAILED)
    status_code = 401
    if request.username == 'admin' and request.password == 'upload':
        response = copy.deepcopy(RES.LOGIN_SUCCESS)
        status_code = 200
    return JSONResponse(status_code=status_code, content=response)


@router.post('/auth/register')
async def get_users(request: RegisterSchema, db: Database = SyncMongoDep):
    response = copy.deepcopy(RES.FAILED)
    status_code = 422
    try:
        user = db['Users'].find_one({'username': request.username}, {'_id':0})
        if user is None:
            request = request.dict()
            request['id'] = str(uuid.uuid4())
            request['password'] = get_password_hash(request['password'])
            request['created_at'] = datetime.now()
            insert = db['Users'].insert_one(request)
            if insert:
                response = copy.deepcopy(RES.SUCCESS)
                status_code = 200
        else:
            response = copy.deepcopy(RES.USER_ALREADY_EXIST)
    except Exception as Err:
        response['message'] = str(Err)
    return JSONResponse(status_code=status_code, content=response)


@router.get('/users')
async def get_users(db: Database = SyncMongoDep):
    response = copy.deepcopy(RES.NO_DATA_FOUND)
    status_code = 422
    try:
        user = db['Users'].find({}, {'_id':0, 'password':0})
        if user:
            response = copy.deepcopy(RES.SUCCESS)
            response['result'] = list(user)
            status_code = 200
    except Exception as Err:
        response['message'] = str(Err)
    return JSONResponse(status_code=status_code, content=jsonable_encoder(response))

    
@router.get('/user/{id}')
async def update_users(id: str, db: Database = SyncMongoDep):
    response = copy.deepcopy(RES.NO_DATA_FOUND)
    status_code = 422
    try:
        user = db['Users'].find_one({'id': id}, {'_id':0, 'password': 0})
        if user:
            response = copy.deepcopy(RES.SUCCESS)
            response['result'] = user
            status_code = 200
    except Exception as Err:
        response['message'] = str(Err)
    return JSONResponse(status_code=status_code, content=jsonable_encoder(response))


@router.put('/user/{id}')
async def update_users(id: str, request: UpdateUserSchema, db: Database = SyncMongoDep):
    response = copy.deepcopy(RES.NO_DATA_FOUND)
    status_code = 422
    try:
        request = request.dict()
        request['updated_at'] = datetime.now()
        user = db['Users'].update_one({'id': id}, {'$set': request})
        if user:
            response = copy.deepcopy(RES.SUCCESS)
            status_code = 200
    except Exception as Err:
        response['message'] = str(Err)
    return JSONResponse(status_code=status_code, content=jsonable_encoder(response))


@router.delete('/user/{id}')
async def delete_users(id: str, db: Database = SyncMongoDep):
    response = copy.deepcopy(RES.NO_DATA_FOUND)
    status_code = 422
    try:
        user = db['Users'].delete_one({'id': id})
        if user:
            response = copy.deepcopy(RES.SUCCESS)
            status_code = 200
    except Exception as Err:
        response['message'] = str(Err)
    return JSONResponse(status_code=status_code, content=jsonable_encoder(response))

