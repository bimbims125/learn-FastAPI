from fastapi import APIRouter
from app.api.postingan.buat_postingan import BuatPostinganResponseModel, buat_postingan
from app.api.postingan.get_postingan import GetPostinganResponseModel, get_postingan


route = APIRouter(prefix='/api')

route.add_api_route(
    '/v1/postingan',
    buat_postingan,
    methods=['POST'],
    tags=['Postingan'],
    response_model=BuatPostinganResponseModel
)

route.add_api_route(
    '/v1/postingan/{postingan_id}', 
    get_postingan, methods=['GET'], 
    tags=['Postingan'], 
    response_model=GetPostinganResponseModel
    )