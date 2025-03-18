from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to the CRUD App!"}

@app.post("/items/{item_id}")
def create_item(item_id: int, name: str):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = {"id": item_id, "name": name}
    return items[item_id]

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id]["name"] = name
    return items[item_id]

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"detail": "Item deleted successfully"}
