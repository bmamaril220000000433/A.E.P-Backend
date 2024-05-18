# model/accounts.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db
from pydantic import BaseModel
import bcrypt
import mysql.connector.errors

Accounts_Router = APIRouter(tags=["UserAccounts"])

# CRUD operations

# Password hashing function using bcrypt
def hash_password(password: str):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  # Decode bytes to string for storage

def verify_password(input_password: str, hashed_password: str) -> bool:
    # Verify the input password against the stored hashed password
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))

def verify_passwordUnencrypted(input_password: str, stored_password: str) -> bool:
    # Simple comparison of input_password with stored_password
    return input_password == stored_password

@Accounts_Router.get("/AllUsers/", response_model=list)
async def getAllUsers(db=Depends(get_db)):
    query = "SELECT * FROM users"
    cursor = db.cursor()
    cursor.execute(query)
    user_data = [
        {
        "email": user[0], 
        "password": user[1], 
        "firstname": user[2], 
        "lastname": user[3],
        "role": user[4]
        }      
        for user in cursor.fetchall()]
    return user_data

@Accounts_Router.get("/userEmail/{email}", response_model=dict)
async def readUser(
    email: str, 
    db=Depends(get_db)
):
    try:
        cursor = db.cursor()
        query = "SELECT email, firstname, lastname FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        if user is not None:
            return {"email": user[0], "firstname": user[1], "lastname": user[2]}
        raise HTTPException(status_code=404, detail="User not found")
    finally:
        if cursor:
            cursor.close()  

class LoginRequest(BaseModel):
    email: str
    password: str

@Accounts_Router.post("/Login/", response_model=dict)
async def Login(login: LoginRequest,db=Depends(get_db)):

    cursor = db.cursor()

    query = "SELECT email, password FROM users WHERE email = %s"
    cursor.execute(query, (login.email,))
    user = cursor.fetchone()

    if not user or user[1] != login.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    cursor.close()
    return {"message": "Login successful"}

class UserRegistration(BaseModel):
    email: str
    firstname: str
    lastname: str
    password: str
    role: str = "visitor" 

@Accounts_Router.post("/CreateAccount/", response_model=dict)
async def createUser(register: UserRegistration, db=Depends(get_db)
):
    cursor = None
    try:        
        cursor = db.cursor()
        hashed_password = hash_password(register.password)
        
        # Check if the account exists
        query_check_existing = "SELECT email FROM users WHERE email = %s"
        cursor.execute(query_check_existing, (register.email,))
        existing_account = cursor.fetchone()
        
        query = "INSERT INTO users (email, password, firstname, lastname, role) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (register.email, register.password, register.firstname, register.lastname, register.role)) # Temporarily not hashed
        existing_account = cursor.fetchone()

        db.commit()
        cursor.close()
        
        return {"Message": "Account created successfully!"}
    
    except mysql.connector.errors.IntegrityError as e:
        if e.errno == 1062:  # Duplicate entry error
            raise HTTPException(status_code=400, detail="email already exists")
        else:
            raise HTTPException(status_code=500, detail="Database error occurred")
        
    finally:
        if cursor:
            cursor.close()  

class ChangePass(BaseModel):
    old_password: str
    new_password: str

@Accounts_Router.put("/users/{email}", response_model=dict)
async def Change_Pass(
    email: str,
    change_password: ChangePass,
    db=Depends(get_db)
):
    try:
        cursor = db.cursor()

        # Retrieve password from the database for the user
        query = "SELECT password FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        user_data = cursor.fetchone()

        if not user_data:
            raise HTTPException(status_code=404, detail="User not found")

        # new_password = user_data[0]

        # Verify the old password -- this is a comment
        # if not verify_password(old_password, hashed_password):
        #    raise HTTPException(status_code=400, detail="Old password is incorrect")

        # Hash the new password -- this is a comment
        # new_hashed_password = hash_password(new_password)

        stored_password = user_data[0]

        # Verify the old password (using basic comparison)
        if not verify_passwordUnencrypted(change_password.old_password, stored_password):
            raise HTTPException(status_code=400, detail="Old password is incorrect")

        # Update the password in the database
        update_query = "UPDATE `users` SET `password` = %s WHERE `users`.`email` = %s;"
        cursor.execute(update_query, (change_password.new_password, email))

        if cursor.rowcount > 0:
            db.commit()
            return {"message": "User password updated successfully"}

        raise HTTPException(status_code=400, detail="Failed to update password")

    finally:
        if cursor:
            cursor.close()

@Accounts_Router.delete("/DeleteAccount/{email}", response_model=dict)
async def deleteAccount(
    email: str,
    db=Depends(get_db)
):
    try:
        cursor = db.cursor()

        # Check if the account exists
        query_check_account = "SELECT email FROM users WHERE email = %s"
        cursor.execute(query_check_account, (email,))
        existing_account = cursor.fetchone()

        if not existing_account:
            raise HTTPException(status_code=404, detail="Account not found")

        # Delete the account
        query_delete_account = "DELETE FROM users WHERE email = %s"
        cursor.execute(query_delete_account, (email,))
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