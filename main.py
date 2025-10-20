from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime
from app import database, models, schemas, crud, nlp_parser

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="String Analyzer API", docs_url="/docs", redoc_url="/redoc")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

