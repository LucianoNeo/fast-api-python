from fastapi import FastAPI, HTTPException, File, UploadFile, Form
from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4 as uuid


class SaleModel(BaseModel):
    id: Optional[str]
    name: str
    price: float = Field(
        gt=0, description="The price must be greater than zero")
    quantity: int = Field(
        gt=0, description="The quantity must be greater than zero")


app = FastAPI()

sales = [
    {
        "id": "1bd48a77-9653-435c-ac73-af67bd4acb2e",
        "name": "notebook",
        "price": 500,
        "quantity": 3
    },
    {
        "id": "1bd48a77-9653-435c-ac73-af67bd4acb2f",
        "name": "iphone",
        "price": 700,
        "quantity": 1
    },
    {
        "id": "1bd48a77-9653-435c-ac73-af67bd4acb2g",
        "name": "monitor",
        "price": 200,
        "quantity": 3
    },
    {
        "id": "1bd48a77-9653-435c-ac73-af67bd4acb2h",
        "name": "keyboard",
        "price": 10,
        "quantity": 6
    },
    {
        "id": "1bd48a77-9653-435c-ac73-af67bd4acb2i",
        "name": "mouse",
        "price": 10,
        "quantity": 5
    },
    {
        "id": "1bd48a77-9653-435c-ac73-af67bd4acb2j",
        "name": "webcam",
        "price": 20,
        "quantity": 2
    }
]


@app.get('/')
def home():
    return {"message": "Welcome to Neo's Python FASTAPI!"}


@app.get('/sales')
def get_all_sales():
    return sales


@app.get('/sales/{id}')
def get_sale_by_id(id: str):
    for sale in sales:
        if sale["id"] == id:
            return sale
    raise HTTPException(status_code=404, detail='Sale not found')


@app.get('/sales_qty')
def get_sales_qty():
    return {"Sales Quantity": len(sales)}


@app.post('/sales')
async def create_sale(item: SaleModel):
    item.id = str(uuid())
    sales.append(item)
    return sales

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    with open(file.filename, "wb") as f:
        f.write(file.file)
    return {"file_saved": True}

@app.put("/sales/{id}")
def update_sale(id: str, updatedSale: SaleModel):
    for index, sale in enumerate(sales):
        if sale['id'] == id:
            sales[index]["name"] = updatedSale.name
            sales[index]["price"] = updatedSale.price
            sales[index]["quantity"] = updatedSale.quantity
            return (sales[index])
    raise HTTPException(status_code=404, detail='Sale ID not found')


@app.delete("/sales/{id}")
def delete_sale(id: str):
    for index, sale in enumerate(sales):
        if sale['id'] == id:
            sales.pop(index)
            return {"message": "Sale deleted successfully"}
    raise HTTPException(status_code=404, detail='Sale ID not found')
