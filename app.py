import streamlit as st
import requests
from fpdf import FPDF
from docx import Document
from io import BytesIO

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide"
)
with st.sidebar:
    st.header("⚖️ LegalEase")
    st.write("AI-Powered Legal Document Generator")
    st.divider()
    st.write("📄 Generate legal documents")
    st.write("✏️ Edit your document")
    st.write("📥 Download as PDF, Word or TXT")

st.divider()
st.subheader("ℹ️ About LegalEase")
st.write(
    "LegalEase is an AI-powered application "
    "for generating customizable legal documents."
)

st.title("⚖️ LegalEase")
st.markdown("### AI-Powered Legal Document Generator")
st.write(
    "Create professional legal documents quickly using AI. "
    "Generate, edit, preview, and download your documents."
)

st.markdown("## 📋 Document Details")

document_type = st.selectbox(
    "Document Type",
    ["NDA", "Employment Contract", "Lease Agreement"]
)

parties = st.text_area(
    "Parties",
    placeholder="Example: Bharath (Disclosing Party), ABC Company (Receiving Party)"
)

terms = st.text_area(
    "Terms and Conditions",
    placeholder="Example: Confidentiality must be maintained; Information must not be shared"
)

dates = st.text_input(
    "Effective Date",
    placeholder="Example: 22 September 2026"
)

if st.button("⚡ Generate Legal Document", use_container_width=True):

    if not parties or not terms or not dates:
        st.warning("Please fill all the required fields.")

    else:
        response = requests.post(
            "http://127.0.0.1:8000/generate",
            json={
                "document_type": document_type,
                "parties": parties,
                "terms": terms,
                "dates": dates
            }
        )

        if response.status_code == 200:

            document = response.json()["document"]

            st.success("Document generated successfully!")

            st.markdown("## 📄 Document Preview")

            st.text_area(
                "Generated Document",
                document,
                height=500
            )

            st.markdown("## ✏️ Edit Document")

            edited_document = st.text_area(
                "Edit your document below",
                document,
                height=500
            )

            st.success("You can edit the document above before downloading.")

            st.markdown("## 📥 Download Document")

            # PDF Download
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            for line in edited_document.split("\n"):
                safe_line = line.replace("₹", "Rs.")
                pdf.multi_cell(0, 8, safe_line)

            pdf_data = pdf.output()

            st.download_button(
                label="📄 Download as PDF",
                data=pdf_data,
                file_name="LegalEase_Document.pdf",
                mime="application/pdf"
            )

            # DOCX Download
            docx_file = BytesIO()

            word_document = Document()

            for line in edited_document.split("\n"):
                word_document.add_paragraph(line)

            word_document.save(docx_file)
            docx_file.seek(0)

            st.download_button(
                label="📝 Download as Word",
                data=docx_file,
                file_name="LegalEase_Document.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

            st.download_button(
                label="📃 Download as TXT",
                data=edited_document,
                file_name="LegalEase_Document.txt",
                mime="text/plain"
            )

        else:
            st.error("Document generation failed.")