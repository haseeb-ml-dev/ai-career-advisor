# streamlit_app.py

import streamlit as st
import os
from resume_parser.custom_parser import (
    extract_text_from_pdf,
    extract_skills,
    extract_skills_from_text,
    MASTER_SKILLS
)
from job_matcher.matcher import match_resume_to_jobs
from course_recommender.recommender import recommend_courses

# Set up page
st.set_page_config(page_title="AI Career Advisor", layout="centered")

# Stylish header
st.markdown("<h1 style='text-align: center; color: #00c8ff;'>🤖 AI Career Advisor</h1>", unsafe_allow_html=True)
st.markdown("###### Upload your resume and get job matches, skill gaps, and learning recommendations.", unsafe_allow_html=True)
st.markdown("---")

# Resume upload
uploaded_file = st.file_uploader("📄 Upload your resume (PDF only)", type=["pdf"])

if uploaded_file is not None:
    # Save file temporarily
    os.makedirs("resumes", exist_ok=True)
    resume_path = f"resumes/temp_resume.pdf"

    with open(resume_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ Resume uploaded successfully!")

    # Extract resume text
    with st.spinner("🔍 Extracting text from resume..."):
        resume_text = extract_text_from_pdf(resume_path)

    # Match to job descriptions (already embedded)
    with st.spinner("🧠 Matching your resume with job roles..."):
        matches = match_resume_to_jobs(resume_text)

    # Show matching jobs
    st.subheader("🎯 Top Matching Jobs")
    for title, desc, score in matches:
        with st.expander(f"🧩 {title} — Match Score: {score:.2f}"):
            st.markdown(desc[:500] + "...")
    st.markdown("---")

    # Extract skills from resume
    resume_skills = extract_skills(resume_text, MASTER_SKILLS)

    # Extract required skills from job descriptions
    required_skills = set()
    for _, desc, _ in matches:
        job_skills = extract_skills_from_text(desc, MASTER_SKILLS)
        required_skills.update(job_skills)

    missing_skills = sorted(list(set(required_skills) - set(resume_skills)))

    # Recommend courses
    recommendations = recommend_courses(missing_skills)

    st.subheader("📚 Recommended Courses to Fill Skill Gaps")
    if not recommendations:
        st.success("🎉 No major skill gaps found! You're well-matched!")
    else:
        for skill, courses in recommendations:
            st.markdown(f"### 🛠️ {skill}")
            for title, url in courses:
                st.markdown(f"- [{title}]({url})")

    # Footer
    st.markdown("---")
    st.markdown("<p style='text-align: center;'>Made with ❤️ by Haseeb Bukhari</p>", unsafe_allow_html=True)
