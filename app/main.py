from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# In-memory "database"
items = []


# Pydantic model for Item
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


# Create an item
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    if any(existing_item.id == item.id for existing_item in items):
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items.append(item)
    return item


# Read all items
@app.get("/items/", response_model=List[Item])
def read_items():
    return items


# Read a single item by ID
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = next((item for item in items if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# Update an item by ID
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    item_index = next((index for index, item in enumerate(items) if item.id == item_id), None)
    if item_index is None:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_index] = updated_item
    return updated_item


# Delete an item by ID
@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    item_index = next((index for index, item in enumerate(items) if item.id == item_id), None)
    if item_index is None:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items.pop(item_index)
    return deleted_item
