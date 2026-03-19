# Document Processing Automation Demo

A lightweight backend service that simulates how businesses can automate document handling by classifying incoming documents, extracting structured fields, and preparing the output for downstream workflows.

This project demonstrates a practical document-processing workflow often used in accounting, legal, administrative, healthcare, and operations-heavy environments.

---

## Overview

Many businesses still process incoming documents manually.

A staff member receives a document, reads it, identifies what type of document it is, extracts important fields, and then enters that information into another system such as a spreadsheet, CRM, accounting platform, or internal database.

This demo shows how part of that workflow can be automated.

The system:

1. Accepts document text
2. Detects document type
3. Extracts structured fields
4. Generates a processing summary
5. Stores the result for further automation

---

## Example Business Use Cases

This workflow can support many industries:

**Accounting / Bookkeeping**
- invoice extraction
- receipt parsing
- expense processing

**Law Firms**
- agreement review intake
- lease document metadata extraction
- client-submitted document processing

**Medical / Dental Clinics**
- intake form digitization
- patient document classification
- administrative form automation

**Property Management**
- lease-related document parsing
- maintenance form intake
- vendor invoice processing

---

## Workflow Comparison

### Manual Process

    Staff receives document
    ↓
    Staff reads document manually
    ↓
    Staff identifies document type
    ↓
    Staff extracts key fields
    ↓
    Staff copies data into another system
    ↓
    Staff follows up or routes the document

### Automated Workflow

    Document is submitted to the processing service
    ↓
    System detects document type
    ↓
    Relevant fields are extracted automatically
    ↓
    Structured output is generated
    ↓
    Record is saved to database
    ↓
    Data is ready for downstream automation

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

FastAPI provides a lightweight API with interactive Swagger documentation.

---

## Project Structure

    document-processing-automation/
    │
    ├── app/
    │   ├── main.py
    │   ├── db.py
    │   ├── models.py
    │   ├── schemas.py
    │   ├── services.py
    │   └── utils.py
    │
    ├── data/
    │   └── documents.db
    │
    ├── requirements.txt
    ├── .env.example
    └── README.md

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mikailzaheri/document-processing-automation.git
cd document-processing-automation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API server:

```bash
uvicorn app.main:app --reload
```

Server will start at:

```bash
http://127.0.0.1:8000
```

