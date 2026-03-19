from sqlalchemy import Column, Integer, String, Text
from .db import Base

class ProcessedDocument(Base):
    __tablename__ = "processed_documents"

    id = Column(Integer, primary_key=True, index=True)
    document_type = Column(String, nullable=False)
    raw_text = Column(Text, nullable=False)
    extracted_data = Column(Text, nullable=False)
    processing_summary = Column(Text, nullable=False)
