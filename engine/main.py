# copied from FastAPI home page as the example
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# venue endpoints

@app.get("/venues")
def read_venues():
    return [{"id": "PDC", "name": "Pathfinder Dining Center", "hours": {"today": {"Start": "T11:30", "End": "T15"}, "tomorrow": {"Start": "T10", "End": "T14"}}}]

# account endpoints

@app.post("/account/new")
def create_account(email: String, name: String, password: String):
    return {"success": False, "error": "No database known.", "token": ""}

@app.post("/account/confirm")
def confirm_account(email: String, code: String):
    return {"success": False, "error": "No database known", "token": ""}

@app.post("/account/login")
def login_account(email: String, password: String):
    return {"success": False, "error": "No database known", "token": ""}

@app.get("/account/profile")
def read_profile(user: String, token: String):
    return {"display_name": "Name not found", "events": []}

@app.get("/account/verify")
def verify_account(token: String):
    return {"success": False, "error": "Invalid token", "token": ""}

@app.get("/account/friends")
def list_friends(user: String, token: String):
    return {"confirmed": [], "pending" []}

@app.post("/account/rename")
def change_display_name(user: String, name: String, token: String):
    return {"success": False, "error": "No such user", "token": ""}
