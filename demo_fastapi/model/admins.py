# model/guard.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db
from .accounts import hash_password
import mysql.connector.errors

Admin_Router = APIRouter(tags=["Admin"])

@Admin_Router.get("/AllAdmins/", response_model=list)
async def get_all_admins(db=Depends(get_db)):
    query = "SELECT * FROM admin"
    db.execute(query)
    admin_data = [
        {
        "admin_name": admin[0], 
        "admin_password": admin[1]
        }      
        for admin in db.fetchall()]
    return admin_data

@Admin_Router.post("/CreateAdmin/", response_model=dict)
async def create_admin(
    username: str = Form(...), 
    password: str = Form(...), 
    db=Depends(get_db)
):
    cursor = None
    try:     
        cursor = db.cursor()   
        hashed_password = hash_password(password)
        # Check if the account exists
        query_check_existing = "SELECT username FROM user_accounts WHERE username = %s"
        cursor.execute(query_check_existing, (username,))
        existing_account = cursor.fetchone()

        
        query = "INSERT INTO admin (admin_name, admin_password) VALUES (%s, %s)"
        cursor.execute(query, (username, hashed_password))
        db.commit()
        cursor.close()
        
        return {"Message": "Admin account created successfully!"}
    
    except mysql.connector.errors.IntegrityError as e:
        if e.errno == 1062:  # Duplicate entry error
            raise HTTPException(status_code=400, detail="Admin already exists")
        else:
            raise HTTPException(status_code=500, detail="Database error occurred")

    finally:
        if cursor:
            cursor.close()  # Close cursor in the finally block

@Admin_Router.put("/admin/{admin_info}", response_model=dict)
async def admin_change_password(
    admin_user: str = Form(...),
    admin_password: str = Form(...),
    db=Depends(get_db)
):
    try:    
        cursor = db.cursor()
        # Hash the password using bcrypt
        hashed_password = hash_password(admin_password)

        # Update user information in the database 
        query = "UPDATE admin SET admin_password = %s WHERE admin_name = %s"
        cursor.execute(query, (hashed_password, admin_user))

        # Check if the update was successful
        if cursor.rowcount > 0:
            db.commit()
            return {"message": "Admin password successfully"}
        
        # If no rows were affected, user not found
        raise HTTPException(status_code=404, detail="Admin not found")

    finally:
        if cursor:
            cursor.close()  

@Admin_Router.delete("/Deleteadmin/{admin_name}", response_model=dict)
async def delete_admin_account(
    admin_name: int,
    db=Depends(get_db)
):
    try:
        cursor = db.cursor()
        # Check if the account exists
        query_check_account = "SELECT admin_name FROM admin WHERE admin_name = %s"
        cursor.execute(query_check_account, (admin_name,))
        existing_account = cursor.fetchone()[0]

        if not existing_account:
            raise HTTPException(status_code=404, detail="account not found")

        # Delete the account
        query_delete_account = "DELETE FROM admin_name WHERE admin_name = %s"
        cursor.execute(query_delete_account, (admin_name,))
        db.commit()
        cursor.close()

        return {"Message": "Admin account deleted successfully!"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        if cursor:
            cursor.close()