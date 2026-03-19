from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .db import Base, engine, SessionLocal
from .models import ProcessedDocument
from .schemas import DocumentRequest, DocumentResponse
from .services import (
    detect_document_type,
    extract_fields,
    build_processing_summary,
    serialize_extracted_data,
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Document Processing Automation Demo")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Document Processing Automation Demo is running"}

@app.post("/process-document", response_model=DocumentResponse)
def process_document(payload: DocumentRequest, db: Session = Depends(get_db)):
    document_type = detect_document_type(payload.raw_text)
    extracted_fields = extract_fields(document_type, payload.raw_text)
    processing_summary = build_processing_summary(document_type, extracted_fields)

    document = ProcessedDocument(
        document_type=document_type,
        raw_text=payload.raw_text,
        extracted_data=serialize_extracted_data(extracted_fields),
        processing_summary=processing_summary,
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return DocumentResponse(
        status="success",
        document_type=document_type,
        extracted_fields=extracted_fields,
        processing_summary=processing_summary,
    )
