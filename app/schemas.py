from pydantic import BaseModel
from typing import Dict

class DocumentRequest(BaseModel):
    raw_text: str

class DocumentResponse(BaseModel):
    status: str
    document_type: str
    extracted_fields: Dict[str, str]
    processing_summary: str
