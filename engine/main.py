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

@app.get("/venues")
def read_venues():
    return [{"id": "PDC", "name": "Pathfinder Dining Center", "hours": {"today": {"Start": "T11:30", "End": "T15"}, "tomorrow": {"Start": "T10", "End": "T14"}}}]