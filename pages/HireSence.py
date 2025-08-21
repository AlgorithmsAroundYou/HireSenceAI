import streamlit as st
import PyPDF2
from src.generate_sence import GenerateSence

class HireSence:
    def __init__(self):
        self.page_title = "HireSence"
        self.layout = "wide"
        self.generate_sence = GenerateSence()

    def set_page_config(self):
        st.set_page_config(page_title=self.page_title, layout=self.layout)

    def display_header(self):
        st.markdown("<h1 style='text-align: center;'>HireSence</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Welcome to the HireSence platform. Please upload your files and provide additional information as needed.</p>", unsafe_allow_html=True)
        st.markdown("---")

    def display_upload_section(self):
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Resumes")
            file1 = st.file_uploader("Choose a file for Resumes", key="file1")
            pdf_text1 = ""
            if file1 is not None and file1.type == "application/pdf":
                pdf_reader = PyPDF2.PdfReader(file1)
                for page in pdf_reader.pages:
                    pdf_text1 += page.extract_text() or ""
                st.text_area("Extracted Resume Content", pdf_text1, key="pdf_text1", height=200)
            text1 = st.text_area("Optional Information for Resumes Content", key="text1", height=200)

        with col2:
            st.subheader("Job Descriptions")
            file2 = st.file_uploader("Choose a file for Job Descriptions", key="file2")
            pdf_text2 = ""
            if file2 is not None and file2.type == "application/pdf":
                pdf_reader = PyPDF2.PdfReader(file2)
                for page in pdf_reader.pages:
                    pdf_text2 += page.extract_text() or ""
                st.text_area("Extracted Resume Content", pdf_text2, key="pdf_text2", height=200)
            text2 = st.text_area("Optional Information for Job Descriptions Content", key="text2", height=200)

        return file1, text1, file2, text2, pdf_text1, pdf_text2

    def display_output(self, submitted, file1, text1, file2, text2, result):
        st.markdown("---")
        st.subheader("Output")
        if submitted:
            st.write("Generating hiring scene...")
            st.write(result)
            st.markdown("---")
            st.write("Files and information submitted successfully!")
            if file1:
                st.write(f"File 1: {file1.name}")
            if text1:
                st.write(f"Text 1: {text1}")
            if file2:
                st.write(f"File 2: {file2.name}")
            if text2:
                st.write(f"Text 2: {text2}")    
    def run(self):
        self.set_page_config()
        self.display_header()

        file1, text1, file2, text2, pdf_text1, pdf_text2 = self.display_upload_section()
        result = self.generate_sence.generate_hire_sence(resumeContent=pdf_text1 + text1, job_description=pdf_text2 + text2)

        submitted = st.button("Submit")
        self.display_output(submitted, file1, text1, file2, text2, result)  

if __name__ == "__main__":
    hire_sence = HireSence()
    hire_sence.run()