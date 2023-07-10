from typing import Annotated

from fastapi import FastAPI, Query
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None



app = FastAPI()


#@app.post("/items")
#async def create_item(item: Item):
#    item_dict = item.model_dump()
#    if item.tax:
#        price_with_tax = item.price + item.tax
#        item_dict.update({"price_with_tax": price_with_tax})
#    return item_dict


#Request body + path parameters
# @app.post("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.model_dump()}


#Request body + path + query parameters
# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item, q: str | None = None):
#     result = {"item_it": item_id, **item.model_dump()}
#     if q:
#         result.update({"q": q})
#     return result


#Query parameters and string validation - inside query you can use pattern for regex validation
# @app.get("/items")
# async def read_items(q: Annotated[str | None, Query(min_length=2, max_length=50, pattern="^fixedquery$")] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     req[turn results


# #Query parameter list / multiple values - example: http://localhost:8000/items/?q=foo&q=bar
# @app.get("/items/")
# async def read_items(q: Annotated[list[str] | None, Query()] = None):
#     query_items = {"q": q}
#     return query_items


#Declare more metadata
@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, 
        Query(
            title="Query string", 
            description="Query string for the items to search in the database that have a good match",
            alias="item_query",
            min_length=3,
            deprecated=True, #use this for deprecated parameters but clients still using
            )
        ] = None
    ):
          results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
          if q:
            results.update({"q": q})
          return results

