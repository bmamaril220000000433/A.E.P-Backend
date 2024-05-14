# model/visitor.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db
from pydantic import BaseModel
import bcrypt

Visitor_Router = APIRouter(tags=["Visitor"])

# CRUD operations

@Visitor_Router.get("/Visitors/", response_model=list)
async def getAllVisitorsBooking(db=Depends(get_db)):
    cursor = db.cursor()
    query = "SELECT * FROM visitor"
    cursor.execute(query)
    visitor_data = [
        {
        "transaction_id": visitor[0],
        "email": visitor[1],
        "date_of_visit": visitor[2], 
        "time_of_visit": visitor[3], 
        "office_name": visitor[4],
        "purpose": visitor[5]
        }      
        for visitor in cursor.fetchall()
        ]
    return visitor_data

@Visitor_Router.get("/VisitorInfo/{visitor_email}", response_model=list)
async def getSpecificVisitorInfo(
    email: str,
    db=Depends(get_db)
):
    try:
        cursor = db.cursor()
        query = "SELECT transaction_id, email, date_of_visit, time_of_visit, office_name, purpose FROM visitor WHERE email = %s"
        cursor.execute(query, (email,))
        visitor_data = []

        for visitor in cursor.fetchall():
            visitor_info = {
                "transaction_id": visitor[0],
                "email": visitor[1],
                "date_of_visit": visitor[2], 
                "time_of_visit": visitor[3], 
                "office_name": visitor[4],
                "purpose": visitor[5]
            }
            visitor_data.append(visitor_info)

        if not visitor_data:
            raise HTTPException(status_code=404, detail="Visitor not found")

        return visitor_data
    finally:
        if cursor:
            cursor.close()  

class book(BaseModel):
    email: str
    date_of_visit: str
    time_of_visit: str
    office_name: str
    purpose: str 

@Visitor_Router.post("/Visitors/", response_model=dict)
async def createVisitorTransaction(
    book: book,
    db=Depends(get_db)
):
    try:
        cursor = db.cursor()
        query = "INSERT INTO visitor (email, date_of_visit, time_of_visit, office_name, purpose) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (book.email, book.date_of_visit, book.time_of_visit, book.office_name, book.purpose))

        db.commit()

        return {"message": "Booked successful"}
    finally:
        if cursor:
            cursor.close()  # Close cursor in the finally block

@Visitor_Router.delete("/VisitorInfo/{visitor_id}", response_model=dict)
async def deleteVisitorInfo(
    email: str,
    transaction_id: int,
    db=Depends(get_db)
):
    try:
        cursor = db.cursor()
        # Check if the visitor info exists
        query_check_visitor_info = "SELECT email, transaction_id FROM visitor WHERE email = %s AND transaction_id = %s"
        cursor.execute(query_check_visitor_info, (email, transaction_id,))
        existing_visitor = cursor.fetchone()

        if not existing_visitor:
            raise HTTPException(status_code=404, detail="visitor info not found")

        # Delete the visitor info
        query_delete_visitor_info = "DELETE FROM visitor WHERE email = %s AND transaction_id = %s"
        cursor.execute(query_delete_visitor_info, (email, transaction_id))
        db.commit()

        return {"message": "visitor info deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        if cursor:
            cursor.close()