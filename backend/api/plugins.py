from fastapi import APIRouter
from plugins.manager import list_plugins

router = APIRouter()

@router.get("/plugins")

def plugins():

    return {"plugins":list_plugins()}
