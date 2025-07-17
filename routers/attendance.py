from fastapi import APIRouter
from schemas.userSchema import PunchInSchema, AttendanceSchema
from pymongo.database import Database
from core.db import SyncMongoDep
from datetime import datetime
import copy
from core.response import FAILED, SUCCESS
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


router = APIRouter(prefix='/api/v1', tags=['attendance'])


@router.post('/punchin')
async def attendance_punchin(request:PunchInSchema, db: Database = SyncMongoDep):
    response = copy.deepcopy(FAILED)
    status_code = 422
    try:
        request = request.dict()
        request['in_time'] = datetime.now()
        punchin = db['Attendance'].insert_one(request)
        if punchin:
            response = copy.deepcopy(SUCCESS)
            status_code = 200
    except Exception as Err:
        response['message'] = str(Err)
    return JSONResponse(status_code=status_code, content=response)



@router.post('/attendance')
async def attendance_punchin(request:AttendanceSchema, db: Database = SyncMongoDep):
    response = copy.deepcopy(FAILED)
    status_code = 422
    try:
        filter = {}
        if request.user_id != '':
            filter['user.id'] = request.user_id

        pipeline = [
            {
                "$lookup": {
                    "from": "Users",
                    "localField": "user_id",
                    "foreignField": "id",
                    "as": "user"
                }
            },
            {
                "$unwind": "$user"
            },
            {
                "$match": filter
            },
            {
                "$project": {
                    "_id": 0,
                    'user.username':1,
                    'user_id':1,
                    'in_time':1
                }
            }
        ]
        print(pipeline)
        punchin = list(db['Attendance'].aggregate(pipeline))

        if punchin:
            response = copy.deepcopy(SUCCESS)
            response['result'] = punchin
            status_code = 200
    except Exception as Err:
        response['message'] = str(Err)
    return JSONResponse(status_code=status_code, content=jsonable_encoder(response))
    
