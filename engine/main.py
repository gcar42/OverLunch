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

# event endpoints

@app.post("/event/new")
def create_event(venue_id: String, today: bool, start: String, end: String, user: String, confirmed: bool, meeting_name: String, token: String):
    return {"success": False, "error": "Venue not open in requested time range", "token": ""}
 
@app.get("/event/friends")
def list_friend_events(user: String, token: String)
    return []
 
@app.post("/event/cancel")
def cancel_event(evetn_id: String, user: String, token: String):
    return {"success": False, "error": "No such event", "token": ""}
 
@app.post("/event/invite")
def invite_to_event(event_id: String, email: String, message: String, token: String):
    return {"success": False, "error": "Invalid email domain", "token": ""}
 
@app.post("/event/confirm")
def confirm_event(event_id: String, user: String, start: String, end: String, token: String):
    return {"success": False, "error": "No such event", "token": ""}

# friend/block endpoints

@app.post("/friend/request")
def request_friend(user: String, friend: String, token: String):
    return {"success": False, "error": "No such user available to request", "token": ""}

@app.post("/friend/block")
def block_user(user: String, block: String, token: String):
    return {"success": False, "error": "No such user available to block", "token": ""}

@app.post("/friend/unblock")
def unblock_user(user: String, blocked: String, token: String):
    return {"success": False, "error": "No such user available to unblock", "token": ""}
