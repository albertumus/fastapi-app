from fastapi import APIRouter

router = APIRouter(
    prefix="",
    #dependencies=dependencies=[Depends(get_token_header)]
)

@router.get('/')
async def index():
    return { "msg": "¡Bienvenido a la API hecha con FastAPI!"}


@router.get('/about')
async def about():
    return "API Rest de prueba para FastAPI donde se simula una lista de peliculas y donde podemos añadirlas a los deseos"

