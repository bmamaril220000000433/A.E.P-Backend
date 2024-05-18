# model/guard.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db
from pydantic import BaseModel
import bcrypt

Office_Router = APIRouter(tags=["Offices"])

@Office_Router.get("/AllOffice/", response_model=list)
async def getAllOffice(db=Depends(get_db)):
    cursor = db.cursor()
    query = "SELECT * FROM office"
    cursor.execute(query)
    office_data = [
        {
        "office_name": office[0], 
        "office_in_charge": office[1]
        }      
        for office in cursor.fetchall()]
    return office_data

@Office_Router.get("/AllOfficeOnly/", response_model=list)
async def getAllOfficeOnly(db=Depends(get_db)):
    cursor = db.cursor()
    query = "SELECT office_name FROM office"
    cursor.execute(query)
    office_data = [
        {
        "office_name": office[0], 
        }      
        for office in cursor.fetchall()]
    return office_data

@Office_Router.get("/officePerson/{Person}", response_model=dict)
async def specificOffice(
    office_in_charge: str, 
    db=Depends(get_db)
):
    try:
        cursor = db.cursor()
        query = "SELECT office_in_charge, office_name FROM office WHERE office_in_charge = %s"
        cursor.execute(query, (office_in_charge,))
        user = cursor.fetchone()
        if user is not None:
            return {"office_in_charge": user[0], "office_name": user[1]}
        raise HTTPException(status_code=404, detail="User not found")
    finally:
        if cursor:
            cursor.close()  

class OfficeInfo(BaseModel):
    office_name: str
    office_in_charge: str

@Office_Router.post("/CreateOffice/", response_model=dict)
async def CreateOffice(
    createOffice: OfficeInfo,
    db=Depends(get_db)
):
    try:
        cursor = db.cursor()
        query = "INSERT INTO office (office_name, office_in_charge) VALUES (%s, %s)"
        cursor.execute(query, (createOffice.office_name, createOffice.office_in_charge,))

        db.commit()

        return {"message": "Office created"}
    finally:
        if cursor:
            cursor.close()  # Close cursor in the finally block

class OfficeRequest(BaseModel):
    office_in_charge: str
    office_name: str

@Office_Router.post("/OfficeLogin/", response_model=dict)
async def LoginOffice(loginOffice: OfficeRequest,db=Depends(get_db)):

    cursor = db.cursor()

    query = "SELECT office_in_charge, office_name FROM office WHERE office_in_charge = %s"
    cursor.execute(query, (loginOffice.office_in_charge,))
    user = cursor.fetchone()

    if not user or user[1] != loginOffice.office_name:
        raise HTTPException(status_code=401, detail="Invalid Office or password")

    cursor.close()
    return {"message": "Login successful"}

@Office_Router.delete("/DeleteOffice/{office}", response_model=dict)
async def deleteOffice(
    office_name: str,
    db=Depends(get_db)
):
    try:
        cursor = db.cursor()

        # Check if the office exists
        query_check_office = "SELECT office_name FROM office WHERE office_name = %s"
        cursor.execute(query_check_office, (office_name,))
        existing_account = cursor.fetchone()

        if not existing_account:
            raise HTTPException(status_code=404, detail="office not found")

        # Delete the office
        query_delete_office = "DELETE FROM office WHERE office_name = %s"
        cursor.execute(query_delete_office, (office_name,))
        db.commit()
        cursor.close()

        return {"Message": "Office deleted successfully!"}
    finally:
        # Close the database cursor
        if cursor:
            cursor.close()