from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Roles(BaseModel):
    user_email: Optional[str]=None
    role_name: Optional[str]=None


class ReadRoles(BaseModel):
    user_email: Optional[str]=None
    role_name: Optional[str]=None
    class Config:
        from_attributes = True


class Users(BaseModel):
    full_name: Optional[str]=None
    email: Optional[str]=None
    password: Optional[str]=None


class ReadUsers(BaseModel):
    full_name: Optional[str]=None
    email: Optional[str]=None
    password: Optional[str]=None
    class Config:
        from_attributes = True


class Student(BaseModel):
    student_id: Optional[str]=None
    student_name: Optional[str]=None
    address: Optional[str]=None


class ReadStudent(BaseModel):
    student_id: Optional[str]=None
    student_name: Optional[str]=None
    address: Optional[str]=None
    class Config:
        from_attributes = True


class Class(BaseModel):
    class_name: Optional[str]=None
    class_teacher: Optional[str]=None


class ReadClass(BaseModel):
    class_name: Optional[str]=None
    class_teacher: Optional[str]=None
    class Config:
        from_attributes = True




class PostRoles(BaseModel):
    role_id: Optional[int]=None
    user_email: Optional[str]=None
    role_name: Optional[str]=None

    class Config:
        from_attributes = True



class PostLogin(BaseModel):
    email: Optional[str]=None

    @field_validator('email')
    def validate_email(cls, value: Optional[str]):
        if value is None:
            if True:
                return value
            else:
                raise ValueError("Field 'email' cannot be None")
        # Ensure re is imported in the generated file
        pattern = r'''^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'''
        if isinstance(value, str) and not re.match(pattern, value):
            # Use repr() for the regex pattern in the error for clarity
            raise ValueError(f"Field '{schema.key}' does not match regex pattern: {repr(                  schema.regularExpression)}")
        return value
    password: Optional[str]=None

    @field_validator('password')
    def validate_password(cls, value: Optional[str]):
        if value is None:
            if True:
                return value
            else:
                raise ValueError("Field 'password' cannot be None")
        # Ensure re is imported in the generated file
        pattern = r'''^[a-zA-Z0-9!@#$%^&*()_\-+=[\]{}|;:,.<>?]{8,64}$'''
        if isinstance(value, str) and not re.match(pattern, value):
            # Use repr() for the regex pattern in the error for clarity
            raise ValueError(f"Field '{schema.key}' does not match regex pattern: {repr(                  schema.regularExpression)}")
        return value

    class Config:
        from_attributes = True



class PutRolesRoleId(BaseModel):
    role_id: Optional[int]=None
    user_email: Optional[str]=None
    role_name: Optional[str]=None

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    user_id: Optional[int]=None
    full_name: Optional[str]=None
    email: Optional[str]=None
    password: Optional[str]=None

    class Config:
        from_attributes = True



class PutUsersUserId(BaseModel):
    user_id: Optional[int]=None
    full_name: Optional[str]=None
    email: Optional[str]=None
    password: Optional[str]=None

    class Config:
        from_attributes = True

