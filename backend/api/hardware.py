from fastapi import APIRouter
from hardware.scan import full_scan

router = APIRouter()

@router.get("/hardware")

def hardware():

    return full_scan()
