from fastapi import FastAPI
import uuid

app = FastAPI()


user_data = {"1":{"username": "John", "password":"mypass"}, "2": {"username": "Peter", "password":"mypass@123"}}

# Honme page
@app.get("/")  
def home():
    return {"Hello": "World"}

#get users
@app.get("/users")  
def get_users():
    return {"data" : user_data}

#Sign Up
@app.post("/users/signup")
def signup(username:str, password:str):
    
    Id = str(uuid.uuid4())
    
    user = dict()
    user["username"] = username
    user["password"] = password

    user_data[Id] = user
    return "Registration Succesful"
    
#Login        
@app.post("/users/login") 
def login(username:str, password:str):
    for user_id, user_info in user_data.items():
        if user_info["username"] == username and user_info["password"] == password:
            return {"status": "Login Successful"}
    return {"status": "Login Failed"} 

#Get User
@app.get("/users/{user_Id}")
def get_user(user_Id:str):
    user = user_data.get(user_Id)
    if not user:
        return "User not Found"
    return user_data[user_Id]
        