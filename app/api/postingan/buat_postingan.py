from fastapi import Header
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime

from app.api_models import BaseResponseModel
from app.utils.db import db_engine
from app.models.postingan import Postingan

class BuatPostinganResponseModel(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'id':1,
                    'author':'admin',
                    'post':'ini adalah postingan',
                    'created_at':'2020-01-01 00:00:00',
                    'url':'/api/v1/postingan/1',
                },
                'meta':{},
                'success':True,
                'code':200,
                'message':'Success',
            },
        }

async def buat_postingan(author: str, post: str, created_at: Optional[datetime] = None):
    with Session(db_engine) as session:
        postingan = Postingan(
            author=author,
            post=post,
            created_at=created_at,
        )
        session.add(postingan)
        session.commit()
        
        return BuatPostinganResponseModel(
            data = {
                'id':postingan.id,
                'author':postingan.author,
                'post':postingan.post,
                'created-at':postingan.created_at,
            }
        )