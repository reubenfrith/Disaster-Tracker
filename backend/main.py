from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mcp_schema import DisasterEvent
from data_fetcher import fetch_earthquake_data

app = FastAPI()

# Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (change this to your frontend URL in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/disasters", response_model=list[DisasterEvent])
def get_disasters():
    return fetch_earthquake_data()