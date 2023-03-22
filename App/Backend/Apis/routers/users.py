from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

#app = FastAPI() se cambia por routers

router = APIRouter()

# inicio servidor: uvicorn users:app --reload


#entidad user

#BaseModel, capacidad de crear una entidad.

# al tener una clase que recibe un base model, el trata los datos que se le envian como parametros, como un json.

# hay parametros que pueden ir poor el propia path y otros por la query. que significa. por query puedo meter filtros para traer elementos.

# por path cuando es casi ibligatorio el campo o parametros que van fijo, por query para los parametros que puden no ser
# necesarios para jacer la peticion

#en un APi todas las funciones son asincronas "async def"

#podriamos tener dos apis una para users y otra para user.

class User(BaseModel):
    id : int
    letter : str


#users_list = [User(id=1, letter2="B", surname="Naranjo", url="ficti.com", age= 36 ),
#                User(id=12,name="Juab", surname="Naranjo", url="ficti.com", age= 36 ),
#                User(id=3,name="Maria", surname="Naranjo", url="ficti.com", age= 36 )]

users_list = [User(id=1, letter="B"),
                User(id=2, letter="C"),
                User(id=3, letter="A")]

#@app.get("/users") cambiamos todos los app + peticion por router + peticion. ej app.get... X router.get...

@router.get("/users")
async def users_all():
    return users_list

#path
#GET: http://127.0.0.1:8000/user/1
@router.get("/user/{id}")
async def user(id: int):
    return search_users(id)

#query
#GET: http://127.0.0.1:8000/userquery/?id=12
@router.get("/user")
async def user(id: int):
    return search_users(id)


@router.post("/user/",response_model=User, status_code=201)
async def user(user: User):
    if type(search_users(user.id)) == User:
        raise HTTPException(status_code=404, detail="Usuario ya existe") #no se retorna porque ya estamso lanzanod una excepcion
        # pero si lo debemos raisear
    else:
        users_list.append(user)
        return user # buena practica una vez haga put o post en el api retornar la informacion que actualice.

@router.put("/user/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate (users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    
    if not found:
        return {"error": "No se ha encontrado el usuario"} #raise HTTPException(
    else:
        return user

@router.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate (users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True 
    
    if not found:
        return {"error": "No se ha eliminado"} #raise HTTPException(


def search_users(id: int):
    users = filter(lambda user: user.id == id, users_list) #es lo que se llama una funcion de orden superior, porque se encargfa de hacer operaciones co,plejas y devovlernos un resultado. 
    # lo podemos usar en cualquier estructura que tenga varios objetos.
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"} #raise HTTPException(



