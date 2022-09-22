from fastapi import APIRouter, Query
from rectangle import Rectangle

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


# path parameter

@router.get("/hello/{name}")
async def say_hello(name: str):
    """function to say hello, using name in the path"""
    return {"message": f"Hello {name}!"}


# query parameter

@router.get("/users")
async def read_body(users_lst: list[str] = Query(None), q: int | None = None):
    """function to say hello to q first people in the list users_lst (in the one sentence),
     if q is None, says hello to all"""
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
    """function calculates rectangle square if calculate_area = true. Checks if rectangle's parameters are positive"""
    rect_dict = rect.dict()
    if rect.calculate_area:
        area = rect.width * rect.height
        rect_dict.update({"area": area})
    return rect_dict
