from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/roles/')
async def post_roles(raw_data: schemas.PostRoles, headers: Request, db: Session = Depends(get_db)):
    try:
        return await service.post_roles(db, raw_data, headers)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/login')
async def post_login(raw_data: schemas.PostLogin, db: Session = Depends(get_db)):
    try:
        return await service.post_login(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test')
async def get_test(db: Session = Depends(get_db)):
    try:
        return await service.get_test(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/roles/')
async def get_roles(db: Session = Depends(get_db)):
    try:
        return await service.get_roles(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/roles/role_id')
async def get_roles_role_id(role_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_roles_role_id(db, role_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/roles/role_id/')
async def put_roles_role_id(raw_data: schemas.PutRolesRoleId, db: Session = Depends(get_db)):
    try:
        return await service.put_roles_role_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/roles/role_id')
async def delete_roles_role_id(role_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_roles_role_id(db, role_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/user_id')
async def get_users_user_id(user_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_user_id(db, user_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/user_id/')
async def put_users_user_id(raw_data: schemas.PutUsersUserId, db: Session = Depends(get_db)):
    try:
        return await service.put_users_user_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/user_id')
async def delete_users_user_id(user_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_user_id(db, user_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/join')
async def get_join(db: Session = Depends(get_db)):
    try:
        return await service.get_join(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/document/upload')
async def post_document_upload(file_upload: UploadFile, db: Session = Depends(get_db)):
    try:
        return await service.post_document_upload(db, file_upload)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/document')
async def post_document(document_url: UploadFile, db: Session = Depends(get_db)):
    try:
        return await service.post_document(db, document_url)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

