from fastapi import FastAPI

app = FastAPI(title="User Service")  # <-- must be named 'app'

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.get("/users")
def get_users():
    return users