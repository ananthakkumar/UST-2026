from fastapi import FastAPI

app = FastAPI(title="Order Service")  # <-- Must be named 'app'

orders = [
    {"id": 1, "item": "Laptop"},
    {"id": 2, "item": "Phone"}
]

@app.get("/orders")
def get_orders():
    return orders