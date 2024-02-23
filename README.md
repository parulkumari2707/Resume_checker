Resume Checker
===
This is a simple web application built with Streamlit to analyze the content of a resume uploaded by the user. The application checks for the presence of specific skills in the resume and determines if the resume is ATS-friendly (Applicant Tracking System friendly).

Features
===
+ Upload Resume: Users can upload their resumes in PDF or DOCX format.
+ Skill Analysis: The application analyzes the uploaded resume to suggest skills that the user may consider adding.
+ ATS-Friendliness Check: It checks if the uploaded resume contains certain keywords typically expected by Applicant Tracking Systems.

Technologies Used
====
+ Python
+ Streamlit
+ PyPDF4
+ docx2txt
+ NLTK (Natural Language Toolkit)

Setup
===
1. Clone the repository:
```bash
git clone https://github.com/parulkumari2707/Resume_checker.git
cd resume-checker
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```
4. Open your web browser and navigate to http://localhost:8501 to access the application.

Usage
====
Upload your resume by clicking on the "Upload your resume" button.
The application will analyze the uploaded resume and provide suggestions for skills to add.
It will also indicate if the resume is ATS-friendly.

Contributing
===
Contributions are welcome! If you have any ideas, enhancements, or bug fixes, feel free to open an issue or submit a pull request.

License
===
This project is licensed under the [MIT License].
