# LegalEase: AI-Powered Legal Document Generator

LegalEase is an AI-powered web application that helps users generate customizable legal documents using Google Gemini AI.

## Features

- Generate legal documents using AI
- Supports NDA, Employment Contract, and Lease Agreement
- Enter parties, terms, and effective date
- Preview generated documents
- Edit generated documents before downloading
- Download documents as PDF
- Download documents as Word (DOCX)
- FastAPI backend
- Streamlit frontend
- Google Gemini AI integration

## Technologies Used

- Python
- Streamlit
- FastAPI
- Google Gemini AI
- python-docx
- FPDF
- ReportLab
- Requests
- Pillow

## Project Structure

```text
LegalEase/
│
├── ai_core/
│   └── gemini_generator.py
│
├── app.py
├── main.py
├── routes.py
├── requirements.txt
└── README.md
