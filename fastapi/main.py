# API Boilerplate
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# API routes
import embed

app = FastAPI(docs_url=None)
app.add_middleware(
	CORSMiddleware,
	allow_origin_regex='.*',
	allow_credentials=True,
	allow_methods=['*'],
	allow_headers=['*'],
)

app.include_router(embed.router)

if __name__ == '__main__':
	import uvicorn
	uvicorn.run('main:app')
