from course_recommender.course_map import COURSE_MAP

def recommend_courses(missing_skills):
    recommendations = []

    for skill in missing_skills:
        if skill in COURSE_MAP:
            recommendations.append((skill, COURSE_MAP[skill]))

    return recommendations
