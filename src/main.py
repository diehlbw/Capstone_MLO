from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from transformers import pipeline

from log_config import get_logger

logger = get_logger("my-project-logger")
app = FastAPI()

class PredictionRequest(BaseModel):
  query_string: str

@app.get('/')
async def root():
    return RedirectResponse(url="/docs")

@app.get('/health')
async def health():
    logger.info("Health was queried")
    return {'message': "App is running"}

@app.post('/analyze')
def analyze(request: PredictionRequest):
    raise NotImplementedError


##############
# Error overrides

from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    logger.error(f"{request['path']} Invalid data!: {exc}")
    return await request_validation_exception_handler(request, exc)