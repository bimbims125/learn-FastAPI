from sqlalchemy.orm import Session
from fastapi import Header
from fastapi.exceptions import HTTPException
from typing import Optional
from datetime import datetime

from app.api_models import BaseResponseModel
from app.models.postingan import Postingan
from app.api_models.get_postingan_models import PostinganModel
from app.utils.db import db_engine


class GetPostinganResponseModel(BaseResponseModel):
    class Config:
        schema_extra = {
            'example':{
                'data':{
                    'id':1,
                    'nama':'Firman',
                    'created_at':'2020-01-01 00:00:00'
                },
                'meta':{},
                'success':True,
                'code':200,
                'message':'Success'
            }
        }

async def get_postingan(id: int ):
    if id == 0:
        raise HTTPException(status_code=404, detail="Postingan not found, enter the correct id!")
    
    with Session(db_engine) as session:
        postingan = session.query(
            Postingan
            ).filter(
                Postingan.id == id
            ).first()
        
        if not postingan:
            raise HTTPException(status_code=404, detail="Postingan not found")
        
        return GetPostinganResponseModel(
            data= PostinganModel(
                id=postingan.id,
                author=postingan.author,
                post=postingan.post,
                created_at=postingan.created_at
            )                                        
        )