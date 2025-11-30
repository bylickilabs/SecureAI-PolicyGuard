from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List, Tuple

from classifier import analyze_content
from policy_engine import get_policy_for_decision

Entity = Tuple[str, str]


class TextRequest(BaseModel):
    text: str


class AnalysisResult(BaseModel):
    classification: str
    risk_score: int
    entities: List[Entity]
    explanation: str
    policy: dict


app = FastAPI(
    title="SecureAI PolicyGuard API",
    description="HTTP-API für AI-gestützte Klassifizierung und Policy-Empfehlungen.",
    version="1.1.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze-text", response_model=AnalysisResult)
def analyze_text(req: TextRequest):
    decision = analyze_content(req.text)
    policy = get_policy_for_decision(
        decision["classification"],
        decision["risk_score"],
        decision["entities"],
    )
    return AnalysisResult(
        classification=decision["classification"],
        risk_score=decision["risk_score"],
        entities=decision["entities"],
        explanation=decision["explanation"],
        policy=policy,
    )


@app.post("/analyze-file", response_model=AnalysisResult)
async def analyze_file(file: UploadFile = File(...)):
    try:
        raw = await file.read()
        text = raw.decode("utf-8", errors="ignore")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not read file: {e}")

    decision = analyze_content(text)
    policy = get_policy_for_decision(
        decision["classification"],
        decision["risk_score"],
        decision["entities"],
    )
    return AnalysisResult(
        classification=decision["classification"],
        risk_score=decision["risk_score"],
        entities=decision["entities"],
        explanation=decision["explanation"],
        policy=policy,
    )
