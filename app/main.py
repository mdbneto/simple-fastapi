from enum import Enum

from fastapi import FastAPI



fake_items_db = [
        {"item_name": "Foo"},
        {"item_name": "Bar"},
        {"item_name": "Baz"},
        ]


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


my_app = FastAPI()


@my_app.get("/")
async def root():
    return {"message": "Hello World!"}


##my_app.get("/items/{item_id}")
##async def read_item(item_id: int):
##    return {"item_id": item_id}


#Multiple path and query parameters
@my_app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: str | None = None, short: bool = False 
        ):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
                {"description": "This is an amazing item that has a long description"}
                )
    return item


@my_app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@my_app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@my_app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet": 
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


#Let's say you have a path operation with a path /files/{file_path}.
#But you need file_path itself to contain a path, like home/johndoe/myfile.txt.
@my_app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


#Query Parameters
@my_app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


#Requerid query paramenter
@my_app.get("/items/{item_id}")
async def get_item_query(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


#Optional Parameters and
@my_app.get("/items2/{item_id}")
async def read_item2(item_id: str, q: str | None = None): 
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


#Query parameter typr conversion
@my_app.get("/items3/{item_id}")
async def read_item3(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is a very nice item description"})
    return item

