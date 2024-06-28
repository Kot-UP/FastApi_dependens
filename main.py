from fastapi import FastAPI, Depends, Query, HTTPException
from pydantic import BaseModel
from starlette.requests import Request
from starlette import status


log_user = []


def log_client(request: Request):
    log_user.append(request.headers)


app = FastAPI(dependencies=[Depends(log_client)])


@app.get("/log_user")
async def print_log_user():
    return {"user": log_user}


# app = FastAPI()
#
#
# def Post(BaseModel):
#     id: int
#     text: str
#
#
# db = []
#
#
class Paginator:
    def __init__(self, limit: int = 10, page: int = 1):
        self.limit = limit
        self.page = page

    def __call__(self, limit: int):
        if limit < self.limit:
            return [{"limit": self.limit, "page": self.page}]
        else:
            return [{"limit": limit, "page": self.page}]


my_paginator = Paginator()
#
#
# async def sub_dependency(request: Request) -> str:
#     return request.method
#
#
# async def main_dependency(sub_dependency_value: str = Depends(sub_dependency)) -> str:
#     return sub_dependency_value
#
#
# @app.get("/test/")
# def test_endpoint(test: str = Depends(main_dependency)):
#     return test
#
#
@app.get("/users")
async def all_users(pagination: Paginator = Depends(my_paginator)):
    return {"user": pagination}
#
#
# async def get_post_or_404(id: int):
#     try:
#         return db[id]
#     except IndexError:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#
#
# async def pagination_path_func(page: int):
#     if page < 0:
#         raise HTTPException(status_code=404, detail="Page does not exist")
#     if page == 0:
#         raise HTTPException(status_code=500, detail="Invalid page value")
#
#
# async def pagination_func(limit: int = Query(10, ge=0), page: int = 1):
#     return [{"limit": limit, "page": page}]
#
#
# @app.get("/messages/dependencies=[Depends(pagination_path_func)]")
# async def all_message(pagination: dict = Depends(pagination_func)):
#     return {"messages": pagination}
#
#
# @app.post("/message", status_code=status.HTTP_201_CREATED)
# async def create_massage(post: Post) -> str:
#     post.id = len(db)
#     db.append(post)
#     return "Message created!"
#
#
# @app.get("/comments")
# async def all_comments(pagination: dict = Depends(pagination_func)):
#     return {"message": pagination}
#
#
# @app.put("/message/{id}")
# async def update_message(post: Post = Depends(get_post_or_404)):
#     pass
#
#
# @app.delete("/message/{id}")
# async def delete_message(post: Post = Depends(get_post_or_404)):
#     pass
