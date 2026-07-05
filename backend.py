from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Enable CORS so your frontend can communicate with your backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/check-pnr/{pnr}")
def get_pnr(pnr: str):
    url = f"https://irctc-indian-railway-pnr-status.p.rapidapi.com/getPNRStatus/{pnr}"
    headers = {
        "x-rapidapi-key": "a3b903492cmsh1493f2f55cacbffp1e4d67jsn3f8cca494f9a", # Keep this hidden later!
        "x-rapidapi-host": "irctc-indian-railway-pnr-status.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch PNR data")