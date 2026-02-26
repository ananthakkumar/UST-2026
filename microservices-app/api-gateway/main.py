from fastapi import FastAPI
import requests
from fastapi.responses import JSONResponse

app = FastAPI(title="API Gateway")   # <-- this is the "app" Uvicorn looks for

USER_SERVICE_URL = "http://localhost:8080"
ORDER_SERVICE_URL = "http://localhost:8081"

@app.get("/users")
def get_users():
    resp = requests.get(f"{USER_SERVICE_URL}/users")
    return JSONResponse(content=resp.json())

@app.get("/orders")
def get_orders():
    resp = requests.get(f"{ORDER_SERVICE_URL}/orders")
    return JSONResponse(content=resp.json())