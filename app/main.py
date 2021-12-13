import os

from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware

import motor.motor_asyncio

from routers import catalog
from routers import basics


class App: 

    app = None
    con = None
    db  = None

    def __init__(self):
        # Se levanta la aplicacion
        self.app = FastAPI(
            title           = "Mi primera aplicacion de FastAPI",
            description     = "Prueba de la pimera aplicacion de API con FastAPI para simular un catalogo de peliculas",
            version         = "0.1"
            )

        # Añadimos los middlewares
        self.add_middlewares()
        # Añadismo las bases de datos
        self.add_databases()

    def add_middlewares(self):
        """ Funcion para añadir middleware a la app """

        # Middleware para los hosts
        self.app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"] )

    def add_databases(self):
        """ Funcion para añadir bases de datos a la app """

        # Añadimos la base de datos de mongo
        self.con = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://%s:%s@cluster0.0d4rh.mongodb.net" % ( os.environ['MONGO_USER'], os.environ['MONGO_PASSWORD'] ) )
        # Añadimos la ddbb
        self.db = self.con.fastApiApp

# Levantamos y devolvemos la app final instanciada
server  = App()
app     = server.app

# Eventos para cuando se lanza el servidor
@app.on_event("startup")
def startup():
    print("Inicio el servidor")

# Eventos para cuando se apaga el servidor
@app.on_event("shutdown")
def shutdown():
    print("Apagado el servidor")

# Añadismos las rutas
app.include_router(basics.router)
app.include_router(catalog.router)





