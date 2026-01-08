import streamlit as st
import PyPDF2
import re
import io
from datetime import datetime

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="Skill Gap Analyzer", layout="wide")

# --------------------------------------------------
# CSS DESIGN
# --------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #f4f6fb;
    font-family: Arial, sans-serif;
}

.header {
    background: linear-gradient(90deg, #0f2027, #203a43, #2c5364);
    color: white;
    padding: 36px;
    border-radius: 14px;
    text-align: center;
    margin-bottom: 30px;
}

.card {
    background-color: white;
    padding: 22px;
    border-radius: 14px;
    margin-bottom: 20px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.08);
}

/* JD Input */
.jd-main {
    background: #ffffff;
    border-left: 6px solid #4e54c8;
    padding: 22px;
    border-radius: 12px;
    margin-bottom: 10px;
}

.jd-title {
    font-size: 20px;
    font-weight: bold;
    color: #2c3e50;
}

.jd-subtitle {
    font-size: 14px;
    color: #6c757d;
    margin-bottom: 12px;
}

textarea {
    background-color: #f0f3ff !important;
    border: 1px solid #d0d7ff !important;
    color: #2c3e50 !important;
    border-radius: 10px !important;
    padding: 14px !important;
}

/* Buttons */
div.stButton > button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 45px;
    font-size: 16px;
    font-weight: bold;
}
div.stButton > button:last-child {
    background-color: #f44336;
}

.footer {
    text-align: center;
    color: gray;
    font-size: 14px;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("""
<div class="header">
    <h1>Skill Gap Detection & Employment Readiness</h1>
    <p>Analyze job descriptions and evaluate job readiness</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# DATA
# --------------------------------------------------
skills = [
    "python", "java", "sql", "html", "css", "javascript",
    "react", "flask", "django",
    "machine learning", "data analysis",
    "git", "aws"
]

learning_platform_link = "https://www.w3schools.com/"

# --------------------------------------------------
# FUNCTIONS
# --------------------------------------------------
def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text.lower()

def detect_experience(jd):
    if re.search(r"fresher|entry level|0-1 year", jd):
        return "Fresher / Entry Level"
    elif re.search(r"1-2 year|1\\+ year|2 year", jd):
        return "1–2 Years"
    return "Not Specified"

def detect_job_type(jd):
    if "internship" in jd:
        return "Internship"
    if "remote" in jd:
        return "Remote"
    if "full time" in jd:
        return "Full-time"
    return "Not Specified"

def detect_location(jd):
    cities = ["bangalore","chennai","hyderabad","mumbai","pune","delhi"]
    for city in cities:
        if city in jd:
            return city.title()
    return "Not Specified"

# --------------------------------------------------
# PDF REPORT
# --------------------------------------------------
def generate_pdf_report(data):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>Skill Gap Analysis Report</b>", styles["Title"]))
    story.append(Spacer(1, 12))

    for key, value in data.items():
        story.append(Paragraph(f"<b>{key}</b>: {value}", styles["Normal"]))
        story.append(Spacer(1, 8))

    story.append(Spacer(1, 12))
    story.append(Paragraph(
        f"Generated on: {datetime.now().strftime('%d %b %Y, %I:%M %p')}",
        styles["Italic"]
    ))

    doc.build(story)
    buffer.seek(0)
    return buffer

# --------------------------------------------------
# JD INPUT
# --------------------------------------------------
st.markdown("""
<div class="jd-main">
    <div class="jd-title">📄 Job Description</div>
    <div class="jd-subtitle">Paste the job description you want to analyze</div>
</div>
""", unsafe_allow_html=True)

jd = st.text_area("", height=230)

# --------------------------------------------------
# RESUME INPUT
# --------------------------------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📂 Resume Upload")
resume_file = st.file_uploader("Choose a file", type=["pdf"])
st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# BUTTONS
# --------------------------------------------------
col1, col2 = st.columns(2)
analyze = col1.button("🔍 Analyze", use_container_width=True)
reset = col2.button("🔄 Reset", use_container_width=True)

if reset:
    st.session_state.clear()
    st.rerun()

# --------------------------------------------------
# ANALYSIS
# --------------------------------------------------
if analyze and jd and resume_file:

    jd_lower = jd.lower()
    resume_text = read_pdf(resume_file)

    jd_skills = [s for s in skills if s in jd_lower]
    resume_skills = [s for s in skills if s in resume_text]

    matched = list(set(jd_skills) & set(resume_skills))
    missing = list(set(jd_skills) - set(resume_skills))

    score = round((len(matched) / len(jd_skills)) * 100, 2) if jd_skills else 0

    job_type = detect_job_type(jd_lower)
    location = detect_location(jd_lower)
    experience = detect_experience(jd_lower)

    # Job Overview
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📊 Job Overview")
    st.write("🧑‍💼 Job Type:", job_type)
    st.write("📍 Location:", location)
    st.write("🧠 Experience Required:", experience)
    st.markdown("</div>", unsafe_allow_html=True)

    # Required Skills
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📌 Required Skills")
    for s in jd_skills:
        st.write("✔️", s.title())
    st.markdown("</div>", unsafe_allow_html=True)

    # Skill Match
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🛠 Skill Match Analysis")
    st.success("Matched Skills: " + ", ".join(matched))
    st.error("Missing Skills: " + ", ".join(missing))
    st.markdown("</div>", unsafe_allow_html=True)

    # Score
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📈 Job Readiness Score")
    st.progress(int(score))
    st.write(f"{score}% Job Ready")
    st.markdown("</div>", unsafe_allow_html=True)

    # PDF Download
    pdf_data = {
        "Job Type": job_type,
        "Location": location,
        "Experience Required": experience,
        "Required Skills": ", ".join(jd_skills),
        "Matched Skills": ", ".join(matched),
        "Missing Skills": ", ".join(missing),
        "Job Readiness Score": f"{score}%"
    }

    pdf_file = generate_pdf_report(pdf_data)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📥 Download Report")
    st.download_button(
        "⬇️ Download Skill Gap Analysis Report (PDF)",
        pdf_file,
        file_name="Skill_Gap_Analysis_Report.pdf",
        mime="application/pdf"
    )
    st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("""
<div class="footer">
Skill Gap Detection & Employment Readiness • College Hackathon Project
</div>
""", unsafe_allow_html=True)
