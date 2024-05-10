# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model.visitor import Visitor_Router
from model.accounts import Accounts_Router
from model.guards import Guards_Router
from model.office import Office_Router

app = FastAPI()

# Include CRUD routes from users module
app.include_router(Visitor_Router, prefix="/api")
app.include_router(Accounts_Router, prefix="/api")
app.include_router(Guards_Router, prefix="/api")
app.include_router(Office_Router, prefix="/api")

origins = [
    "http://localhost:",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["GET", "POST", "PUT", "DELETE"],
    allow_headers = ["*"],
)
