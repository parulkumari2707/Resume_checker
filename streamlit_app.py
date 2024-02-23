# -*- coding: utf-8 -*-
"""resume_checker_ui.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mZ0HegtAuuFqwcFiUBLllqK43Cn4bMYn
"""

# Install necessary libraries for Google Colab environment

# Import necessary libraries
import streamlit as st
import PyPDF4
from PyPDF4.pdf import PdfFileReader
import docx2txt
import nltk
from nltk.corpus import stopwords
from collections import Counter
from string import punctuation
import ipywidgets as widgets
from IPython.display import display
import traitlets
from io import BytesIO

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Function to extract text from PDF
def extract_text_from_pdf(pdf_bytes):
    with BytesIO(pdf_bytes) as f:
        reader = PyPDF4.PdfFileReader(f)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extractText()
    return text

# Function to extract text from Word document
def extract_text_from_docx(docx_bytes):
    return docx2txt.process(docx_bytes)

# Function to preprocess text
def preprocess_text(text):
    # Tokenization
    tokens = nltk.word_tokenize(text.lower())

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and word not in punctuation]

    # Lemmatization or stemming (optional)
    lemmatizer = nltk.WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens

#Function to analyze skills in the resume
def analyze_skills(tokens):
    # Example predefined list of skills
    predefined_skills = ['python', 'machine learning', 'data analysis', 'communication', 'problem solving']

    # Count occurrences of predefined skills in the resume
    skill_counter = Counter(tokens)
    skill_recommendations = [skill for skill in predefined_skills if skill_counter[skill] == 0]

    return skill_recommendations

# Function to check ATS-friendliness
def check_ats_friendly(tokens):
    # Example check: presence of specific keywords
    ats_friendly_keywords = ['experience', 'skills', 'education', 'summary']
    for keyword in ats_friendly_keywords:
        if keyword not in tokens:
            return False
    return True

# Main function
def main(resume_content, filename):
    file_extension = filename.split('.')[-1]

    if file_extension == 'pdf':
        resume_text = extract_text_from_pdf(resume_content)
    elif file_extension == 'docx':
        resume_text = extract_text_from_docx(resume_content)
    else:
        print("Unsupported file format")
        return

    # Preprocess text
    tokens = preprocess_text(resume_text)
    
    # Analyze skills
    skill_recommendations = analyze_skills(tokens)
    
    # Check ATS-friendliness
    ats_friendly = check_ats_friendly(tokens)
    
    # Display results
    st.write("Skills you may consider adding to your resume:")
    for skill in skill_recommendations:
        st.write("- " + skill)
    
    if ats_friendly:
        st.write("Your resume is ATS-friendly.")
    else:
        st.write("Your resume may not be ATS-friendly. Consider adding sections such as 'Experience', 'Skills', 'Education', and 'Summary'.")


# Streamlit UI
def streamlit_ui():
    st.title("Resume Checker")
    upload = st.file_uploader("Upload your resume", type=['pdf', 'docx'])
    if upload is not None:
        resume_content = upload.read()
        filename = upload.name
        main(resume_content, filename)

streamlit_ui()

#!streamlit run /usr/local/lib/python3.10/dist-packages/colab_kernel_launcher.py

''' # UI for uploading resume file
upload = widgets.FileUpload(accept='.pdf,.docx', multiple=False)
display(upload)

# Event handler for file upload
def on_upload_change(change):
    if upload.value:
        resume_content = next(iter(upload.value.values()))['content']  # Accessing content as bytes
        filename = next(iter(upload.value.values()))['metadata']['name']  # Get filename
        main(resume_content, filename)

upload.observe(on_upload_change, names='_counter')
'''

