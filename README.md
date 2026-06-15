# AI FAQ Triage System

## Overview

#### An automated FAQ triage system built using Flask, Google Gemini, Make.com, Tally Forms, ngrok and Google Sheets.

#### The system receives customer questions from a Tally form, sends them to a Flask API for processing, checks the question against a predefined knowledge base using Gemini, determines whether the question can be answered automatically or requires human review, generates a professional customer support response when possible, and stores all interactions in Google Sheets.

## Screenshots

### Tally Form

![tally scr.png](assets/tally%20scr.png)

### Make.com Workflow

![make.com scr.png](assets/make.com%20scr.png)

### Google Sheets Output

![AI ANSWERED.png](assets/AI%20ANSWERED.png)

![HUMAN ANSWERED.png](assets/HUMAN%20ANSWERED.png)

## Features

* Customer question intake through Tally Forms
* Flask REST API
* Google Gemini 2.5 Flash integration
* Knowledge base powered responses
* Automatic FAQ detection
* AI-generated customer support replies
* Human review escalation for unknown questions
* Timestamp generation (IST)
* Make.com automation
* Google Sheets integration

## Tech Stack

* Python
* Flask
* Google Gemini 2.5 Flash
* Make.com
* Tally Forms
* Google Sheets
* ngrok

## Workflow

Tally Form
↓
Make.com Trigger
↓
HTTP Request
↓
Flask API
↓
Knowledge Base Lookup
↓
Google Gemini Analysis
↓
AI Answer Generation
↓
Answered by AI / Needs Human Review
↓
Google Sheets

## Sample Input

```json
{
    "name": "John Doe",
    "email": "john@gmail.com",
    "question": "Do you offer refunds?"
}
```

## Sample Output (Answered by AI)

```json
{
    "name": "John Doe",
    "email": "john@gmail.com",
    "question": "Do you offer refunds?",
    "answer": "Hello John Doe,\n\nYes, customers can request a full refund within 30 days of purchase. Refund requests submitted after 30 days are not eligible. Refunds are typically processed within 5-7 business days.\n\nBest regards,\nCustomer Support",
    "status": "Answered by AI",
    "timestamp": "2026-06-14 15:37:30"
}
```

## Sample Output (Needs Human Review)

```json
{
    "name": "John Doe",
    "email": "john@gmail.com",
    "question": "I signed a custom enterprise contract in 2024 and was promised a special refund. Can I get it?",
    "answer": "",
    "status": "Needs Human Review",
    "timestamp": "2026-06-14 15:38:58"
}
```

## Project Structure

```text
ai-faq-triage-system/
│
├── main.py
├── knowledge_base.txt
├── requirements.txt
├── README.md
├── .env
│
└── assets/
    ├── Tally scr.png
    ├── make.com scr.png
    └── GoogleSheet.png
```

