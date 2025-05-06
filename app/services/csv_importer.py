# app/services/csv_importer.py
from ..models import Transaction
from ..database import SessionLocal

def parse_csv(df):
    db = SessionLocal()
    for _, row in df.iterrows():
        transaction = Transaction(
            date=row.get("Date") or row.get("date"),
            description=row.get("Description") or row.get("description"),
            amount=row.get("Amount") or row.get("amount"),
            category="Uncategorized"
        )
        db.add(transaction)
    db.commit()
    db.close()
