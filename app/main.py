# mint_mvp_backend/app/main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
from .database import engine, SessionLocal
from . import models, schemas
from .services.csv_importer import parse_csv
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS for frontend dev later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
def upload_csv(file: UploadFile = File(...)):
    # Input validation
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")

    # Parse csv
    df = pd.read_csv(file.file)
    parse_csv(df)
    return {"message": "CSV uploaded and parsed."}

@app.get("/transactions")
def get_transactions():
    db = SessionLocal()
    transactions = db.query(models.Transaction).all()
    db.close()
    return transactions
