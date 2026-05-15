def match_resume_to_job(resume_skills, job_requirements):
    required = job_requirements["required_skills"]
    nice = job_requirements["nice_to_have"]

    strong = [s for s in required if s in resume_skills]
    medium = [s for s in nice if s in resume_skills]
    missing = [s for s in required if s not in resume_skills]

    score = len(strong) * 20 + len(medium) * 10 - len(missing) * 15
    score = max(0, min(100, score))

    explanation = (
        f"Strong fit: {strong}. "
        f"Medium fit: {medium}. "
        f"Missing: {missing}. "
        f"Overall score: {score}."
    )

    return {
        "score": score,
        "strong_fit": strong,
        "medium_fit": medium,
        "missing": missing,
        "explanation": explanation
    }
