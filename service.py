from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def post_roles(db: Session, raw_data: schemas.PostRoles, request: Request):
    role_id: int = raw_data.role_id
    user_email: str = raw_data.user_email
    role_name: str = raw_data.role_name

    header_authorization: str = request.headers.get("header-authorization")

    record_to_be_added = {
        "role_id": role_id,
        "role_name": role_name,
        "user_email": user_email,
    }
    new_roles = models.Roles(**record_to_be_added)
    db.add(new_roles)
    db.commit()
    db.refresh(new_roles)
    roles_inserted_record = new_roles.to_dict()

    try:
        thislist = ["apple", "banana", "cherry"]
        print(thislist)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

    role_1: str = user_email

    # Get element at index 1 from the list 'thislist'
    roles_inserted_record = thislist[1]

    try:
        decode_jwt = jwt.decode(
            header_authorization,
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
            algorithms=["HS256"],
        )
    except jwt.ExpiredSignatureError:
        decode_jwt = "Token has expired."
    except jwt.InvalidTokenError:
        decode_jwt = "Invalid token."

    res = {
        "roles_inserted_record": roles_inserted_record,
        "dghj": thislist,
        "hgj": role_1,
        "decode_jwt": decode_jwt,
    }
    return res


async def post_login(db: Session, raw_data: schemas.PostLogin):
    email: str = raw_data.email
    password: str = raw_data.password

    query = db.query(models.Users)
    query = query.filter(
        and_(models.Users.email == email, models.Users.password == password)
    )

    login_user = query.first()

    login_user = (
        (login_user.to_dict() if hasattr(login_user, "to_dict") else vars(login_user))
        if login_user
        else login_user
    )

    try:
        is_exist_login = bool(login_user)
        is_true = True
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

    is_As: bool = is_true

    if is_true == is_exist_login:

        bs_jwt_payload = {
            "exp": int(
                (
                    datetime.datetime.utcnow() + datetime.timedelta(seconds=100000)
                ).timestamp()
            ),
            "data": login_user,
        }

        jwt_secret_keys_login = jwt.encode(
            bs_jwt_payload,
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
            algorithm="HS256",
        )

    else:

        raise HTTPException(status_code=401, detail="user not exist")
    res = {
        "login_user": login_user,
        "jwt_secret_keys_login": jwt_secret_keys_login,
    }
    return res


async def get_test(db: Session):

    c = aliased(models.Class)
    query = db.query(models.Class, c)

    query = query.join(c, and_(models.Class.id == c.id))

    ukghjjhgj = query.first()

    if ukghjjhgj:
        s1, s2 = ukghjjhgj
        ukghjjhgj = {
            "ukghjjhgj_1": s1.to_dict() if hasattr(s1, "to_dict") else vars(s1),
            "ukghjjhgj_2": s2.to_dict() if hasattr(s2, "to_dict") else vars(s2),
        }

    res = {
        "hkjghkgul": ukghjjhgj,
    }
    return res


async def get_roles(db: Session):

    query = db.query(models.Roles)

    roles_all = query.all()
    roles_all = (
        [new_data.to_dict() for new_data in roles_all] if roles_all else roles_all
    )
    res = {
        "roles_all": roles_all,
    }
    return res


async def get_roles_role_id(db: Session, role_id: int):

    query = db.query(models.Roles)
    query = query.filter(and_(models.Roles.role_id == role_id))

    roles_one = query.first()

    roles_one = (
        (roles_one.to_dict() if hasattr(roles_one, "to_dict") else vars(roles_one))
        if roles_one
        else roles_one
    )

    res = {
        "roles_one": roles_one,
    }
    return res


async def put_roles_role_id(db: Session, raw_data: schemas.PutRolesRoleId):
    role_id: int = raw_data.role_id
    user_email: str = raw_data.user_email
    role_name: str = raw_data.role_name

    query = db.query(models.Roles)
    query = query.filter(and_(models.Roles.role_id == role_id))
    roles_edited_record = query.first()

    if roles_edited_record:
        for key, value in {
            "role_id": role_id,
            "role_name": role_name,
            "user_email": user_email,
        }.items():
            setattr(roles_edited_record, key, value)

        db.commit()
        db.refresh(roles_edited_record)

        roles_edited_record = (
            roles_edited_record.to_dict()
            if hasattr(roles_edited_record, "to_dict")
            else vars(roles_edited_record)
        )
    res = {
        "roles_edited_record": roles_edited_record,
    }
    return res


async def delete_roles_role_id(db: Session, role_id: int):

    query = db.query(models.Roles)
    query = query.filter(and_(models.Roles.role_id == role_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        roles_deleted = record_to_delete.to_dict()
    else:
        roles_deleted = record_to_delete
    res = {
        "roles_deleted": roles_deleted,
    }
    return res


async def get_users(db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )
    res = {
        "users_all": users_all,
    }
    return res


async def get_users_user_id(db: Session, user_id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.user_id == user_id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "users_one": users_one,
    }
    return res


async def post_users(db: Session, raw_data: schemas.PostUsers):
    user_id: int = raw_data.user_id
    full_name: str = raw_data.full_name
    email: str = raw_data.email
    password: str = raw_data.password

    record_to_be_added = {
        "email": email,
        "user_id": user_id,
        "password": password,
        "full_name": full_name,
    }
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        "users_inserted_record": users_inserted_record,
    }
    return res


async def put_users_user_id(db: Session, raw_data: schemas.PutUsersUserId):
    user_id: int = raw_data.user_id
    full_name: str = raw_data.full_name
    email: str = raw_data.email
    password: str = raw_data.password

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.user_id == user_id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "email": email,
            "user_id": user_id,
            "password": password,
            "full_name": full_name,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()
        db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )
    res = {
        "users_edited_record": users_edited_record,
    }
    return res


async def delete_users_user_id(db: Session, user_id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.user_id == user_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete
    res = {
        "users_deleted": users_deleted,
    }
    return res


async def get_join(db: Session):

    r = aliased(models.Roles)
    query = db.query(models.Users, r)

    query = query.join(
        r, and_(models.Users.user_id == r.role_id, models.Users.email == r.user_email)
    )

    join1 = query.first()

    if join1:
        s1, s2 = join1
        join1 = {
            "join1_1": s1.to_dict() if hasattr(s1, "to_dict") else vars(s1),
            "join1_2": s2.to_dict() if hasattr(s2, "to_dict") else vars(s2),
        }

    res = {
        "join1": join1,
    }
    return res


async def post_document_upload(db: Session, file_upload: UploadFile):

    bucket_name = "backstract-testing"
    region_name = "ap-south-1"
    file_path = "resources"

    s3_client = boto3.client(
        "s3",
        aws_access_key_id="AKIATET5D5CPSTHVVX25",
        aws_secret_access_key="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",
        aws_session_token=None,  # Optional, can be removed if not used
        region_name="ap-south-1",
    )

    # Read file content
    file_content = await file_upload.read()

    name = file_upload.filename
    file_path = file_path + "/" + name

    import mimetypes

    file_upload.file.seek(0)

    content_type = mimetypes.guess_type(name)[0] or "application/octet-stream"
    s3_client.upload_fileobj(
        file_upload.file, bucket_name, name, ExtraArgs={"ContentType": content_type}
    )

    file_type = Path(file_upload.filename).suffix
    file_size = 200

    file_url = f"https://{bucket_name}.s3.amazonaws.com/{name}"

    document_url = file_url
    res = {
        "document_url": document_url,
    }
    return res


async def post_document(db: Session, document_url: UploadFile):

    bucket_name = "backstract-testing"
    region_name = "ap-south-1"
    file_path = "resources"

    s3_client = boto3.client(
        "s3",
        aws_access_key_id="AKIATET5D5CPSTHVVX25",
        aws_secret_access_key="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",
        aws_session_token=None,  # Optional, can be removed if not used
        region_name="ap-south-1",
    )

    # Read file content
    file_content = await document_url.read()

    name = document_url.filename
    file_path = file_path + "/" + name

    import mimetypes

    document_url.file.seek(0)

    content_type = mimetypes.guess_type(name)[0] or "application/octet-stream"
    s3_client.upload_fileobj(
        document_url.file, bucket_name, name, ExtraArgs={"ContentType": content_type}
    )

    file_type = Path(document_url.filename).suffix
    file_size = 200

    file_url = f"https://{bucket_name}.s3.amazonaws.com/{name}"

    document_url1 = file_url
    res = {
        "document_url1": document_url1,
    }
    return res
