from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Replace this with your actual frontend URL
frontend_origin = os.environ.get("FRONT_END_URL")


print(frontend_origin)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_origin],  # Only allow your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI with Poetry!"}