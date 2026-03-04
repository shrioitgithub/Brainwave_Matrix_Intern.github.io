import string
STOPWORDS = {
    "the", "and", "with", "in", "of"
}

def clean_text(resume_text):
    if not resume_text:
        return []

    text = resume_text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word for word in words if word not in STOPWORDS]

    return words

exact_word = {
    "python", "django", "rest", "api", "mysql",
    "docker",  "experience"
}


def score_logic(job, resume):
    job_keywords = set(clean_text(job))
    resume_words = set(clean_text(resume))

    score = 0
    matched_skills = job_keywords.intersection(resume_words)
    for skill in matched_skills:
        if skill in exact_word:
            score += 2

    resume_text = resume.lower()

    if "3 year" in resume_text:
        score += 3
    elif "2 year" in resume_text:
        score += 2
    elif "1 year" in resume_text:
        score += 1

    return score