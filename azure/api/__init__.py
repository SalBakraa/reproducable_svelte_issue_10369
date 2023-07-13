# Azure Boilerplate
import azure.functions as func

# API Boilerplate
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# API routes
from . import embed

app = FastAPI(docs_url=None)
app.add_middleware(
	CORSMiddleware,
	allow_origin_regex='.*',
	allow_credentials=True,
	allow_methods=['*'],
	allow_headers=['*'],
)

app.include_router(embed.router)

print('------------------------------- Loaded Module ---------------------------------', flush=True)

async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
	print('recieved request', flush=True)
	print('req: ', req, flush=True)
	print('con: ', context, flush=True)
	return await func.AsgiMiddleware(app).handle_async(req, context)
