from fastapi import FastAPI

from api.hardware import router as hardware_router
from api.diagnostics import router as diag_router
from api.plugins import router as plugin_router

app = FastAPI()

app.include_router(hardware_router)
app.include_router(diag_router)
app.include_router(plugin_router)
