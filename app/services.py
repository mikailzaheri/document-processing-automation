import re
import json

def detect_document_type(raw_text: str) -> str:
    text = raw_text.lower()

    if "invoice" in text:
        return "invoice"
    if "receipt" in text:
        return "receipt"
    if "intake form" in text or "patient" in text:
        return "intake_form"
    if "lease" in text or "agreement" in text:
        return "legal_document"
    return "general_document"

def extract_invoice_fields(raw_text: str) -> dict:
    fields = {}

    patterns = {
        "invoice_number": r"Invoice\s*#?\s*[:\-]?\s*([A-Z0-9\-]+)",
        "date": r"Date\s*[:\-]?\s*([0-9]{4}-[0-9]{2}-[0-9]{2})",
        "vendor": r"Vendor\s*[:\-]?\s*(.+)",
        "total": r"Total\s*[:\-]?\s*(\$?[0-9,]+\.[0-9]{2})",
        "due_date": r"Due Date\s*[:\-]?\s*([0-9]{4}-[0-9]{2}-[0-9]{2})",
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, raw_text, re.IGNORECASE)
        if match:
            fields[key] = match.group(1).strip()

    return fields

def extract_receipt_fields(raw_text: str) -> dict:
    fields = {}

    patterns = {
        "merchant": r"Merchant\s*[:\-]?\s*(.+)",
        "date": r"Date\s*[:\-]?\s*([0-9]{4}-[0-9]{2}-[0-9]{2})",
        "total": r"Total\s*[:\-]?\s*(\$?[0-9,]+\.[0-9]{2})",
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, raw_text, re.IGNORECASE)
        if match:
            fields[key] = match.group(1).strip()

    return fields

def extract_general_fields(raw_text: str) -> dict:
    return {
        "preview": raw_text[:200].strip()
    }

def extract_fields(document_type: str, raw_text: str) -> dict:
    if document_type == "invoice":
        return extract_invoice_fields(raw_text)
    if document_type == "receipt":
        return extract_receipt_fields(raw_text)
    return extract_general_fields(raw_text)

def build_processing_summary(document_type: str, extracted_fields: dict) -> str:
    if not extracted_fields:
        return f"Processed as {document_type}, but no structured fields were extracted."

    field_list = ", ".join(extracted_fields.keys())
    return f"Processed document as {document_type}. Extracted fields: {field_list}."

def serialize_extracted_data(extracted_fields: dict) -> str:
    return json.dumps(extracted_fields)
