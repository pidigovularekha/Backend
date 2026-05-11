from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register")
def register(data: dict):
    return {
        "message": "Registration Successful",
        "user": data
    }

@app.post("/login")
def login(data: dict):
    return {
        "message": "Login Successful",
        "user": data
    }

@app.get("/events")
def get_events():
    return [
        {
            "id": 1,
            "title": "Tech Fest",
            "venue": "Auditorium"
        },
        {
            "id": 2,
            "title": "Coding Contest",
            "venue": "Lab 1"
        }
    ]