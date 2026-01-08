Skill Gap Detection & Employment Readiness
📌 Project Overview

Skill Gap Detection & Employment Readiness is a web-based application built using Python and Streamlit.
The system analyzes a Job Description (JD) and a Resume (PDF) to identify:

Required skills from the job description

Skills present in the candidate’s resume

Skill gaps (missing skills)

Overall job readiness score

Downloadable PDF analysis report

This project is designed especially for students and freshers to understand how well their resume matches a job role and what skills they need to learn.

🎯 Key Features

📄 Job Description analysis

📂 Resume upload (PDF)

📌 Required skills extraction

✅ Matched skills detection

❌ Missing skills identification

📈 Job readiness score

📥 Downloadable analysis report (PDF)

🎨 Clean UI using custom CSS

🔄 Reset option

🛠️ Technologies Used

Frontend: Streamlit + Custom CSS

Backend: Python

PDF Processing: PyPDF2

PDF Report Generation: ReportLab

📁 Project Structure
jobproject/
│
├── app.py
├── requirements.txt
├── Backend_Developer_Junior_Resume.pdf
├── README.md

⚙️ Installation & Setup
1️⃣ Install Python

Make sure Python 3.9+ is installed.

2️⃣ Install Required Libraries

Run the following command in terminal:

pip install -r requirements.txt

3️⃣ Run the Application
streamlit run app.py


The application will open automatically in your browser.

🧪 How to Use the Application

Paste a Job Description in the input box

Click Choose a file and upload a resume (PDF)

Click Analyze

View:

Job overview

Required skills

Matched and missing skills

Job readiness score

Click Download Skill Gap Analysis Report (PDF)

📥 Sample Input Files

A sample resume PDF is included for testing:

Backend_Developer_Junior_Resume.pdf

📊 Output

On-screen analysis (skills & readiness)

Downloadable PDF report containing:

Job type

Location

Experience

Required skills

Matched skills

Missing skills

Readiness score

🚀 Future Enhancements

AI-based skill matching (NLP)

Skill proficiency level detection

Personalized learning roadmap

Multiple resume comparison

User login and progress tracking

🎓 Use Case

College students

Freshers preparing for jobs

Resume screening demonstration

Hackathons and academic projects

🏆 Hackathon Note

This project focuses on practical problem-solving, clean UI, and real-world relevance, making it ideal for college hackathons and evaluations.

👤 Author

Name: Akash
Project Type: College Hackathon Project

✅ Final Note

This project is easy to run, well-structured, and ready for submission.
