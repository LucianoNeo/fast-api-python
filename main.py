from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional


class SaleModel(BaseModel):
    id: Optional[int]
    name: str
    price: float = Field(
        gt=0, description="The price must be greater than zero")
    quantity: int = Field(
        gt=0, description="The quantity must be greater than zero")


app = FastAPI()

sales = [
    {"id": 1, "name": "notebook", "price": 500, "quantity": 3},
    {"id": 2, "name": "iphone", "price": 700, "quantity": 1},
    {"id": 3, "name": "monitor", "price": 200, "quantity": 3},
    {"id": 4, "name": "keyboard", "price": 10, "quantity": 6},
    {"id": 5, "name": "mouse", "price": 10, "quantity": 5},
    {"id": 6, "name": "webcam", "price": 20, "quantity": 2}
]


@app.get('/')
def home():
    return {"message": "Welcome to Neo's Python FASTAPI!"}


@app.get('/sales')
def all_sales():
    return sales


@app.get('/sales/{id}')
def sale_by_id(id: int):
    for sale in sales:
        if sale.get('id') == id:
            return sale
    else:
        return {"Error": "ID not found"}


@app.get('/sales_qty')
def sales_qty():
    return {"Sales Quantity": len(sales)}


@app.post('/sales')
async def create_sale(item: SaleModel):
    for sale in sales:
        if sale.get('id') == item.id:
            return {"error": "Id Already Exists"}
    else:
        sales.append(item)
        return sales
