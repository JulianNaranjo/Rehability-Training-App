from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import attention, users

app = FastAPI() 

#En esta variable se colocan las direcciones habilitadas para el acceso a los servicios
origins = [
    "http://localhost",
    "http://localhost:8000", #acceso local a los servicios usar otro puerto
    "http://localhost:3000",
    "http://localhost:4200",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Routers
app.include_router(attention.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {"Hello World"}