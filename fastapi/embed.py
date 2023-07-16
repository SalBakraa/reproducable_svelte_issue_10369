# API Boilerplate
from fastapi import APIRouter, Form, UploadFile
from typing_extensions import Annotated
from pydantic import BaseModel

router = APIRouter()

class EmbedResult(BaseModel):
	is_success: bool

@router.post('/embed')
def create_embeddigs(api_key: Annotated[str, Form()], file: UploadFile) -> EmbedResult:
	print('recieved request', flush=True)
	print('api_key: ', api_key, flush=True)
	print('file: ', file, flush=True)
	return EmbedResult(is_success = True)
