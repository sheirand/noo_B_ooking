from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/item/{item_id}", tags=["items"])
async def get_item(item_id: int):
    return {"item_id": item_id}
