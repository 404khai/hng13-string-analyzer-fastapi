from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database, crud, nlp_parser
from app.database import get_db

router = APIRouter(prefix="/strings", tags=["Strings"])

# Create / Analyze String
@router.post("", status_code=201, response_model=schemas.StringResponse)
def create_string(data: schemas.StringCreate, db: Session = Depends(get_db)):
    if not isinstance(data.value, str):
        raise HTTPException(status_code=422, detail="Invalid data type for value")
    record = crud.create_string(db, data.value)
    if not record:
        raise HTTPException(status_code=409, detail="String already exists")
    props = crud.utils.analyze_string(data.value)
    return {
        "id": props["sha256_hash"],
        "value": data.value,
        "properties": props,
        "created_at": record.created_at
    }

# Get Specific String
@router.get("/{string_value}", response_model=schemas.StringResponse)
def get_string(string_value: str, db: Session = Depends(get_db)):
    record = crud.get_string(db, string_value)
    if not record:
        raise HTTPException(status_code=404, detail="String not found")
    props = crud.utils.analyze_string(record.value)
    return {
        "id": record.id,
        "value": record.value,
        "properties": props,
        "created_at": record.created_at
    }

# Get All Strings with Filtering
@router.get("")
def list_strings(
    is_palindrome: bool | None = None,
    min_length: int | None = None,
    max_length: int | None = None,
    word_count: int | None = None,
    contains_character: str | None = None,
    db: Session = Depends(get_db)
):
    filters = {
        "is_palindrome": is_palindrome,
        "min_length": min_length,
        "max_length": max_length,
        "word_count": word_count,
        "contains_character": contains_character
    }
    records = crud.get_all_strings(db, filters)
    data = []
    for r in records:
        props = crud.utils.analyze_string(r.value)
        data.append({
            "id": r.id,
            "value": r.value,
            "properties": props,
            "created_at": r.created_at
        })
    return {
        "data": data,
        "count": len(data),
        "filters_applied": {k: v for k, v in filters.items() if v is not None}
    }


# Natural Language Filtering
@router.get("/filter-by-natural-language")
def natural_filter(query: str, db: Session = Depends(get_db)):
    try:
        filters = nlp_parser.parse_query(query)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    records = crud.get_all_strings(db, filters)
    data = []
    for r in records:
        props = crud.utils.analyze_string(r.value)
        data.append({
            "id": r.id,
            "value": r.value,
            "properties": props,
            "created_at": r.created_at
        })
    return {
        "data": data,
        "count": len(data),
        "interpreted_query": {
            "original": query,
            "parsed_filters": filters
        }
    }

# Delete Specific String
@router.delete("/{string_value}", status_code=204)
def delete_string(string_value: str, db: Session = Depends(get_db)):
    success = crud.delete_string(db, string_value)
    if not success:
        raise HTTPException(status_code=404, detail="String not found")
