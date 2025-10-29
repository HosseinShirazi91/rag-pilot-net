from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import api_router
from app.core.config import settings

app = FastAPI(
    title="RAG Assistant Pilot API",
    version="1.0.0",
    docs_usr="/docs" if settings.env != "production" else None,
    redoc_url = None,
)

# CORS - only proxy host
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://app.localhost", "https://backend.localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status" : "ok"}


app.include_router(api_router)
