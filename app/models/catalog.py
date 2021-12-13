from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    """ Modelo padre para la creacion de Items """
    name            : str
    genre           : str
    rating          : float
    description     : Optional[str]

class Film(Item):
    """ Modelo para las peliculas """
    duration        : Optional[int]

    def helper( film ):
        return {
            "id"            : str(film.get('_id')),
            "name"          : film.get("name", ""),
            "genre"         : film.get("genre", ""),
            "rating"        : film.get("rating", 0),
            "description"   : film.get("description", ""),
            "duracion"      : film.get("duracion", 0)
        }

class Serie(Item):
    """ Modelo para las series"""
    seasons         : Optional[int]
    chapters        : Optional[int]

    def helper( film ):
        return {
            "id"            : str(film.get('_id')),
            "name"          : film.get("name", ""),
            "genre"         : film.get("genre", ""),
            "rating"        : film.get("rating", ""),
            "description"   : film.get("description", ""),
            "seasons"       : film.get("seasons", 0),
            "chapters"      : film.get("chapters", 0)
        }

