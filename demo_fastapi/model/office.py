# model/guard.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db
import bcrypt

Office_Router = APIRouter(tags=["Offices"])

@Office_Router.get("/AllOffice/", response_model=list)
async def get_all_office(db=Depends(get_db)):
    query = "SELECT * FROM office"
    db.execute(query)
    office_data = [
        {
        "office_name": office[0], 
        "date_of_shift": office[1]
        }      
        for office in db.fetchall()]
    return office_data
