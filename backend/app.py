from fastapi import FastAPI
from backend.router.benchmark_router import router as benchmark_router


app = FastAPI(title="AlgoForge Backend", version="1.0.0" )

app.include_router(benchmark_router, prefix="/api")

@app.get("/")
def root():
    return {"status": "OK", "message": "AlgoForge backend running!"}