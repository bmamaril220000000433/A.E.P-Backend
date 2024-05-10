# model/visitor.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db
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
        "visitorid": visitor[0], 
        "visitor_fname": visitor[1], 
        "visitor_lname": visitor[2], 
        "purpose": visitor[3], 
        "date_of_visit": visitor[4], 
        "time_of_visit": visitor[5]
        }      
        for visitor in cursor.fetchall()
        ]
    return visitor_data

@Visitor_Router.post("/Visitors/", response_model=dict)
async def createVisitorTransaction(
    visitor_First_name: str = Form(...), 
    visitor_Last_name: str = Form(...),
    purpose: str = Form(...),
    date_of_visit: str = Form(...),
    time_of_visit: str = Form(...),
    db=Depends(get_db)
):
    try:
        cursor = db.cursor()
        query = "INSERT INTO visitor (visitor_fname, visitor_lname, purpose, date_of_visit, time_of_visit) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (visitor_First_name, visitor_Last_name, purpose, date_of_visit, time_of_visit))

        # Retrieve the last inserted ID using LAST_INSERT_ID()
        cursor.execute("SELECT LAST_INSERT_ID()")
        new_visitor_id = cursor.fetchone()
        db.commit()

        return {"id": new_visitor_id, "visitor_First_name": visitor_First_name, "visitor_Last_name": visitor_Last_name, 
        "purpose": purpose, "date_of_visit": date_of_visit, "time_of_visit": time_of_visit}
    finally:
        if cursor:
            cursor.close()  # Close cursor in the finally block

@Visitor_Router.delete("/VisitorInfo/{visitor_id}", response_model=dict)
async def deleteVisitorInfo(
    visitor_id: int,
    db=Depends(get_db)
):
    try:
        cursor = db.cursor()
        # Check if the visitor info exists
        query_check_visitor_info = "SELECT visitor_id FROM visitor WHERE visitor_id = %s"
        cursor.execute(query_check_visitor_info, (visitor_id,))
        existing_visitor = cursor.fetchone()

        if not existing_visitor:
            raise HTTPException(status_code=404, detail="visitor info not found")

        # Delete the visitor info
        query_delete_visitor_info = "DELETE FROM visitor WHERE visitor_id = %s"
        cursor.execute(query_delete_visitor_info, (visitor_id,))
        db.commit()

        return {"message": "visitor info deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        if cursor:
            cursor.close()
