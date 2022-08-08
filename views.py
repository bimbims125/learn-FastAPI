from doctest import debug_src
from multiprocessing import reduction

from asgiref.sync import sync_to_async
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from app.models import Book
from app.decorators import method

import asyncio
# Create your views here.


'''GET ALL BOOK LIST'''
# =====================
@method('GET')
async def getBook(request):
    try:
        book = list(Book.objects.values())
        await asyncio.sleep(0.9)
        return request.jsonResponse(book)
    except:
        return request.jsonResponse({'a':'hehe'})
# =======================
'''END'''


'''GET BOOK LIST BY ID'''
# =====================
@method('GET')
async def getBookById(request,id:str):
    book = Book.objects.filter(id=id).values()
    if book:
        await asyncio.sleep(0.5)
        return request.jsonResponse(list(book))
    else:
        return request.jsonResponse({
            'success':False,
            'message':"data doesn't exist",
            'error_code':1307,
        })
# =======================
'''END'''


'''ADD BOOK TO DB'''
# ======================
@method('POST')
async def postBook(request):
    #  request params title
    _title = dict(request.GET)
    title = ''.join(_title['title'])

    # request params desc
    _desc = dict(request.GET)
    desc = ''.join(_desc['desc'])

    # processing data
    await Book.objects.async_create(title=title, desc=desc)

    # returned data
    return request.jsonResponse({
        "success":True,
        "message":"Added data success",
        "success_code":203,
        "data":{
            "title":title,
            "desc":desc
        }
    })
# =======================
'''END'''


'''UPDATE DATA FROM DB'''
# =======================
@method('PUT')
async def putBook(request, id:str):
    _title = request.GET
    title = ''.join(_title['title'])
    _desc = request.GET
    desc = ''.join(_desc['desc'])
    if await Book.objects.filter(id=id).async_update(title=title, desc=desc):
        return request.jsonResponse({
            "success":True,
            "message":"Get data success",
            "success_code":203,
            "data":{
                "title":title,
                "desc":desc
            }
        })

    else:
        return request.jsonResponse({
            "success": False,
            "message": "Data doesn't exist",
            "error_code": 1308,
            "data": {}
        })
# =======================
'''END'''

'''DELETE DATA FROM DB'''
# =======================
@method('DELETE')
async def deleteBook(request, id:str):
    data = Book.objects.filter(id=id)
    if data:
        await data.async_delete()
        return request.jsonResponse({
            "success":True,
            "message":"Delete data success",
        })
    else:
        return request.jsonResponse({
            "success":False,
            "message":"Delete data failed, data doesn't exist",
            "data":{}
        })
# =======================
'''END'''