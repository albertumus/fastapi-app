from typing import List, Optional
from bson import ObjectId

from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.param_functions import Depends

from starlette.responses import JSONResponse

import main

from models.catalog import Film
from depends.db_depends import verify_key, verify_user_key


router = APIRouter(
    dependencies=[ Depends( verify_key ), Depends( verify_user_key ) ],
    prefix="/catalog",
)

@router.middleware( verify_user_key )
@router.get('/films')
async def list_films():
    """ Vista GET LIST para las películas"""
    list_films = []
    films =  await main.server.db["film"].find().to_list(1000)
    for film in films:
        list_films.append(Film.helper(film))
    print(user)
    return list_films

@router.get('/films/{id}')
async def detail_films( id: str ):
    """ Vista GET DETAIL para las películas"""
    film =  await main.server.db["film"].find_one({"_id": ObjectId(id) })
    if film is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return Film.helper(film)

@router.post('/films', status_code=201 )
async def create_films( film: Film ):
    """ Vista CREATE para las peliculas"""
    new_film    = await main.server.db["film"].insert_one(jsonable_encoder(film))
    new_film    = await main.server.db["film"].find_one({"_id": new_film.inserted_id})

    return Film.helper(new_film)

@router.put('/films/{ id }', status_code=200 )
async def update_films( id:str, film: Film ):
    """ Vista UPDATE para las peliculas"""
    old_film            = await main.server.db["film"].find_one({"_id": ObjectId(id)})
    if old_film is None:
        raise HTTPException(status_code=404, detail="Item not found")

    updated_film    = await main.server.db["film"].update_one({"_id": ObjectId(id)}, { "$set": jsonable_encoder(film) }, upsert=True )  

    return film

@router.delete('/films/{id}', status_code=204 )
async def delete_films( id: str ):
    """ Vista DELETE para borrar peliculas """
    film =  await main.server.db["film"].delete_one({"_id": ObjectId(id) })
    if film is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return JSONResponse("No content", 204)



