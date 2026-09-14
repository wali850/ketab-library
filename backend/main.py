from fastapi import FastAPI
from database.database import init_db
from backend.routes import router

app = FastAPI(
    title="Ketab Library API",
    description="Modern multilingual digital library API",
    version="1.0.0",
)

app.include_router(router, prefix="/api")


@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def root():
    return {
        "name": "Ketab Library",
        "status": "online",
        "message": "Welcome to Ketab Library API 📚",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
