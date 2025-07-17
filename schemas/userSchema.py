from pydantic import BaseModel


class LoginSchema(BaseModel):
    username : str
    password : str


class RegisterSchema(BaseModel):
    username : str
    email : str = ''
    phone : str = ''
    password : str
    height : str = ''
    weight : str = ''


class UpdateUserSchema(BaseModel):
    email : str = ''
    phone : str = ''
    height : str = ''
    weight : str = ''


class PunchInSchema(BaseModel):
    user_id : str


class AttendanceSchema(BaseModel):
    start_date : str = ''
    end_date : str = ''
    user_id : str = ''
    