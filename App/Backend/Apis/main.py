from fastapi import FastAPI
from routers import attention, users

app = FastAPI() 

#Routers
app.include_router(attention.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {"Hello World"}