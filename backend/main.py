from fastapi import FastAPI
from database.database import init_db

app = FastAPI(
    title="Ketab Library API",
    description="Modern multilingual digital library API",
    version="1.0.0",
)


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
