import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


class GeminiDocumentGenerator:

    def generate_document(self, document_type, parties, terms, dates):

        prompt = f"""
You are a legal document drafting assistant.

Create a professional draft for the following document:

Document Type: {document_type}
Parties: {parties}
Terms and Conditions: {terms}
Effective Date: {dates}

Requirements:
- Use clear professional language.
- Organize the document with suitable headings.
- Include the provided parties, terms, and date.
- Do not invent important facts that were not provided.
- Return only the document draft.
"""

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text