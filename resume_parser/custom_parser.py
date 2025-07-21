# Central skill list (expand as needed)
MASTER_SKILLS = [
    'Python', 'Java', 'C++', 'Machine Learning', 'Deep Learning',
    'SQL', 'TensorFlow', 'Keras', 'Pandas', 'Numpy', 'Scikit-learn',
    'React', 'Django', 'Flask', 'Git', 'Linux', 'Data Analysis',
    'Cloud', 'Docker', 'Kubernetes', 'Azure', 'AWS', 'Statistics'
]

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from pdfminer.high_level import extract_text
import re
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    return extract_text(file_path)

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else None

def extract_phone(text):
    # More global regex pattern
    pattern = r'(?:(?:\+|00)?\d{1,3}[\s\-\.]?)?(?:\(?\d{2,4}\)?[\s\-\.]?)?\d{3,4}[\s\-\.]?\d{4}'
    matches = re.findall(pattern, text)

    for match in matches:
        cleaned = match.strip()
        # Ignore if it looks like a year range (e.g., "2021 - 2023")
        if not re.search(r'\b(19|20)\d{2}\b.*\b(19|20)\d{2}\b', cleaned):
            return cleaned

    return "Not found"


def extract_name(text):
    # Look for 2–3 capitalized words in a row
    lines = text.split("\n")
    for line in lines:
        words = line.strip().split()
        if 1 < len(words) <= 4 and all(w[0].isupper() for w in words if w.isalpha()):
            return line.strip()
    return "Not found"


def extract_skills(text, skills_list):
    found_skills = []
    text_lower = text.lower()
    for skill in skills_list:
        if skill.lower() in text_lower:
            found_skills.append(skill)
    return list(set(found_skills))

def extract_skills_from_text(text, skill_list):
    found_skills = []
    text_lower = text.lower()
    for skill in skill_list:
        if skill.lower() in text_lower:
            found_skills.append(skill)
    return list(set(found_skills))

if __name__ == "__main__":
    file_path = "resumes/ML-Resume.pdf"
    text = extract_text_from_pdf(file_path)

    # Define a simple skill list (expand later)
    skills_list = [
        'Python', 'Java', 'C++', 'Machine Learning', 'Deep Learning',
        'SQL', 'TensorFlow', 'Pandas', 'Numpy', 'Django', 'React',
        'Git', 'Flask', 'Linux', 'Data Analysis'
    ]

    print("✅ Name:", extract_name(text))
    print("📧 Email:", extract_email(text))
    print("📞 Phone:", extract_phone(text))
    print("🛠️ Skills:", extract_skills(text, skills_list))
