from fastapi import APIRouter
from ai.log_ai import analyze_log

router = APIRouter()

@router.post("/diagnose")

def diagnose(data:dict):

    return analyze_log(data["log"])
