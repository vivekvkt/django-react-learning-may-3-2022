from enum import Enum

from fastapi import FastAPI


# class ModelName(int, Enum):
#     alexnet = 10
#     resnet = 20
#     lenet = 30


# app = FastAPI()


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == 10:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == 20:
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}


from pydantic import BaseModel
from typing import Union

class Items(BaseModel):
    name : str
    description: Union[str ,None] = None
    price : float
    text :  Union[float , None ] = None



app = FastAPI()

@app.post("/items/")
async def create_item(item:Items):
    return item