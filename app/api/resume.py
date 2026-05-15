from fastapi import APIRouter
from app.models.resume_models import ResumeInput, ResumeSkills
from app.services.resume_extractor import extract_skills
from app.services.skill_inference import infer_skill_levels

router = APIRouter()

@router.post("/extract", response_model=ResumeSkills)
def extract_resume_skills(data: ResumeInput):
    raw_skills = extract_skills(data.text)
    inferred = infer_skill_levels(raw_skills, data.text)
    return ResumeSkills(skills=inferred)
