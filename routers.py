from fastapi import APIRouter, Query
from rectangle import Rectangle

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


# path parameter

@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}!"}


# query parameter

@router.get("/users")
async def read_body(users_lst: list[str] = Query(None), q: int | None = None):
    users_lst = users_lst[:q]
    greeting = f"Hello "
    for i in range(len(users_lst)):
        greeting += users_lst[i]
        if i < len(users_lst) - 1:
            greeting += ", "
    greeting += "!"
    return greeting


# request body

@router.get("/request")
async def calculate_square(rect: Rectangle):
    rect_dict = rect.dict()
    if rect.calculate_area:
        area = rect.width * rect.height
        rect_dict.update({"area": area})
    return rect_dict
