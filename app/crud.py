from sqlalchemy.orm import Session
from app import models, utils

def create_string(db: Session, value: str):
    props = utils.analyze_string(value)
    existing = db.query(models.StringRecord).filter(models.StringRecord.id == props["sha256_hash"]).first()
    if existing:
        return None  # conflict

    record = models.StringRecord(
        id=props["sha256_hash"],
        value=value,
        length=props["length"],
        is_palindrome=int(props["is_palindrome"]),
        unique_characters=props["unique_characters"],
        word_count=props["word_count"],
        character_frequency_map=props["character_frequency_map"]
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def get_string(db: Session, value: str):
    return db.query(models.StringRecord).filter(models.StringRecord.value == value).first()


def delete_string(db: Session, value: str):
    record = get_string(db, value)
    if not record:
        return False
    db.delete(record)
    db.commit()
    return True


def get_all_strings(db: Session, filters: dict):
    query = db.query(models.StringRecord)
    if filters.get("is_palindrome") is not None:
        query = query.filter(models.StringRecord.is_palindrome == int(filters["is_palindrome"]))
    if filters.get("min_length") is not None:
        query = query.filter(models.StringRecord.length >= filters["min_length"])
    if filters.get("max_length") is not None:
        query = query.filter(models.StringRecord.length <= filters["max_length"])
    if filters.get("word_count") is not None:
        query = query.filter(models.StringRecord.word_count == filters["word_count"])
    if filters.get("contains_character"):
        char = filters["contains_character"]
        query = query.filter(models.StringRecord.value.contains(char))
    return query.all()
