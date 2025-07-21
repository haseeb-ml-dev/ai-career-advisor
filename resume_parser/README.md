# 🤖 AI Career Advisor

An intelligent career-matching web app that analyzes your resume and recommends the most relevant job roles, detects skill gaps, and suggests personalized online courses — all in seconds.

Built using cutting-edge NLP models and deployed with Streamlit.

---

## 📌 Key Features

- 📄 **Resume Upload** — Accepts PDF resumes  
- 🧠 **Job Matching** — Matches your resume with over 2,000 job descriptions using SBERT + cosine similarity  
- 🛠️ **Skill Extraction** — Extracts your technical skills from resume text  
- ⚙️ **Gap Analysis** — Detects missing skills by comparing resume with matched jobs  
- 📚 **Learning Recommendations** — Suggests Coursera/Udemy courses for skill gaps  

---

## 📁 Project Structure

```
ai-career-advisor/
│
├── streamlit_app.py                  # Main Streamlit app
├── requirements.txt                  # Project dependencies
│
├── job_matcher/
│   └── matcher.py                    # SBERT + cosine matching logic
│
├── resume_parser/
│   └── custom_parser.py              # Resume text/skill extractor
│
├── course_recommender/
│   └── recommender.py                # Course recommendation engine
│
├── resumes/
│   └── temp_resume.pdf               # Temp storage for uploads
│
├── data/
│   ├── job_descriptions.csv          # Dataset of jobs (title + description)
│   └── job_embeddings.pkl            # Precomputed SBERT embeddings
```

---

## 🧑‍💻 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/haseeb-ml-dev/ai-career-advisor.git
cd ai-career-advisor
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Launch the Streamlit App

```bash
streamlit run streamlit_app.py
```

---

## 📦 Tech Stack

- Python 3.10+
- Streamlit
- spaCy
- Sentence Transformers (SBERT)
- scikit-learn
- pdfminer.six
- Pyresparser

---

## 🙋‍♂️ About the Developer

Made with ❤️ by **Syed Haseeb Hassan**  
Built for learning, real-world ML practice, and portfolio enhancement.

---

## 📄 License

MIT License — free to use, fork, and contribute!