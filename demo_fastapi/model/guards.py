# model/guard.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db
import bcrypt

Guards_Router = APIRouter(tags=["Guards"])

@Guards_Router.get("/AllGuards/", response_model=list)
async def getAllGuards(db=Depends(get_db)):
    cursor = db.cursor()
    query = "SELECT * FROM guard"
    cursor.execute(query)
    guard_data = [
        {
        "guard_name": guard[0], 
        "date_of_shift": guard[1]
        }      
        for guard in cursor.fetchall()]
    return guard_data
