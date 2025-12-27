from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()

 
@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello, FastAPI!"}


@app.get("/hello/{first_name}/{last_name}")
async def welcome_user(first_name: str, last_name: str) -> dict:
    return {"user": f"Hello {first_name} {last_name}"}


@app.get("/order/{order_id}")
async def order(order_id: int) -> dict:
    return {"id": order_id}


@app.get("/user/profile")
async def profile() -> dict:
    return {"profile": "View profile user"}


@app.get("/employee/{name}/company/{company}")
async def get_employee(name: str, department: str, company: str) -> dict:
    return {"Employee": name, "Department": department, "Company": company}


@app.get("/user/{username}")
async def login(
    username: Annotated[
        str,
        Path(
            min_length=3,
            max_length=15,
            description="Enter your username",
            example="permin0ff",
        ),
    ],
    first_name: Annotated[str | None, Query(max_length=10, pattern="^J|s$")] = None,
) -> dict:
    return {"user": username, "Name": first_name}


@app.get("/user")
async def search(
    people: Annotated[
        list[str],
        Query(
            min_length=1,
            max_length=5,
            description="List of user names",
            example=["Tom", "Sam"],
        ),
    ],
) -> dict:
    return {"user": people}
