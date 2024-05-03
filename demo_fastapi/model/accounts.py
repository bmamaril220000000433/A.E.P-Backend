# model/accounts.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db
import bcrypt
import mysql.connector.errors

Accounts_Router = APIRouter(tags=["User Accounts"])

# CRUD operations

# Password hashing function using bcrypt
def hash_password(password: str):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  # Decode bytes to string for storage

@Accounts_Router.get("/AllUsers/", response_model=list)
async def get_all_users(db=Depends(get_db)):
    query = "SELECT * FROM user_accounts"
    db.execute(query)
    user_data = [
        {
        "id": user[0], 
        "username": user[1], 
        "password": user[2], 
        "email": user[3]
        }      
        for user in db.fetchall()]
    return user_data

@Accounts_Router.get("/users/{user_id}", response_model=dict)
async def read_user(
    user_id: int, 
    db=Depends(get_db)
):
    try:
        cursor = db.cursor()
        query = "SELECT id, username FROM user_accounts WHERE id = %s"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
        if user is not None:
            return {"id": user[0], "username": user[1]}
        raise HTTPException(status_code=404, detail="User not found")
    finally:
        if cursor:
            cursor.close()  

@Accounts_Router.post("/CreateAccount/", response_model=dict)
async def create_user(
    email: str = Form(...), 
    username: str = Form(...), 
    password: str = Form(...), 
    db=Depends(get_db)
):
    cursor = None
    try:        
        cursor = db.cursor()
        hashed_password = hash_password(password)
        
        # Check if the account exists
        query_check_existing = "SELECT id FROM user_accounts WHERE email = %s OR username = %s"
        cursor.execute(query_check_existing, (email, username,))
        existing_account = cursor.fetchone()
        
        query = "INSERT INTO user_accounts (email, username, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (email, username, hashed_password))
        existing_account = cursor.fetchone()

        cursor.execute("SELECT LAST_INSERT_ID()")
        new_user_id = cursor.fetchone()[0]
        db.commit()
        cursor.close()
        
        return {"Message": "Account created successfully!",
            "id": new_user_id,
            "email": email,
            "username": username}
    
    except mysql.connector.errors.IntegrityError as e:
        if e.errno == 1062:  # Duplicate entry error
            raise HTTPException(status_code=400, detail="Username or email already exists")
        else:
            raise HTTPException(status_code=500, detail="Database error occurred")
        
    finally:
        if cursor:
            cursor.close()  

@Accounts_Router.put("/users/{user_id}", response_model=dict)
async def user_change_password(
    user_id: int,
    password: str = Form(...),
    db=Depends(get_db)
):
    try:    
        cursor = db.cursor()
        # Hash the password using bcrypt
        hashed_password = hash_password(password)

        # Update user information in the database 
        query = "UPDATE user_accounts SET password = %s WHERE id = %s"
        cursor.execute(query, (hashed_password, user_id))

        # Check if the update was successful
        if cursor.rowcount > 0:
            db.commit()
            return {"message": "User password successfully"}
        
        # If no rows were affected, user not found
        raise HTTPException(status_code=404, detail="User not found")

    finally:
        if cursor:
            cursor.close()  

@Accounts_Router.delete("/DeleteAccount/{account_id}", response_model=dict)
async def delete_account(
    account_id: int,
    db=Depends(get_db)
):
    try:
        cursor = db.cursor()

        # Check if the account exists
        query_check_account = "SELECT id FROM user_accounts WHERE id = %s"
        cursor.execute(query_check_account, (account_id,))
        existing_account = cursor.fetchone()

        if not existing_account:
            raise HTTPException(status_code=404, detail="Account not found")

        # Delete the account
        query_delete_account = "DELETE FROM user_accounts WHERE id = %s"
        cursor.execute(query_delete_account, (account_id,))
        db.commit()
        cursor.close()

        return {"Message": "Account deleted successfully!"}
        '''
        except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
        '''
    finally:
        # Close the database cursor
        if cursor:
            cursor.close()