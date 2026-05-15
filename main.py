from fastapi import FastAPI
from app.api import resume, jobs, match

app = FastAPI(
    title="Resume Job Agent",
    description="AI-powered resume skill extraction and job matching engine",
    version="1.0.0"
)

app.include_router(resume.router, prefix="/resume", tags=["Resume"])
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
app.include_router(match.router, prefix="/match", tags=["Matching"])

@app.get("/")
def root():
    return {"message": "Resume Job Agent API is running"}
