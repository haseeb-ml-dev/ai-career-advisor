# run_matcher.py
from course_recommender.recommender import recommend_courses
from resume_parser.custom_parser import extract_text_from_pdf
from job_matcher.matcher import load_jobs, match_resume_to_jobs

def main():
    # Path to your resume PDF and job dataset
    resume_path = "resumes/ML-Resume.pdf"
    job_csv_path = "data/job_descriptions.csv"

    # Step 1: Extract resume text
    print("[INFO] Extracting resume text...")
    resume_text = extract_text_from_pdf(resume_path)

    # Step 2: Load job descriptions
    print("[INFO] Loading job descriptions...")
    job_titles, job_descriptions = load_jobs(job_csv_path)

    # Step 3: Match resume to jobs
    print("[INFO] Matching resume to job roles...")
    matches = match_resume_to_jobs(resume_text, job_titles, job_descriptions)

    from resume_parser.custom_parser import extract_skills_from_text, MASTER_SKILLS, extract_skills

    # Step 4: Extract resume skills
    resume_skills = extract_skills(resume_text, MASTER_SKILLS)

    # Step 5: Extract required skills from top job descriptions
    required_skills = set()
    for _, desc, _ in matches:
        job_skills = extract_skills_from_text(desc, MASTER_SKILLS)
        required_skills.update(job_skills)

    # Step 6: Find missing skills
    missing_skills = sorted(list(set(required_skills) - set(resume_skills)))


    print("\n🎯 Top Matching Jobs:\n")
    for title, desc, score in matches:
        print(f"{title} (Match Score: {score:.2f})")
        print("Description:", desc[:200], "...\n")
    

    print("🔧 Your Skills:", resume_skills)
    print("📌 Skills Required by Jobs:", sorted(list(required_skills)))
    print("❌ Missing Skills:", missing_skills)

    print("\n📚 Recommended Courses to Learn Missing Skills:\n")

    recommendations = recommend_courses(missing_skills)

    for skill, courses in recommendations:
        print(f"📌 {skill}")
        for title, url in courses:
            print(f"   🔗 {title}: {url}")
        print()


if __name__ == "__main__":
    main()
