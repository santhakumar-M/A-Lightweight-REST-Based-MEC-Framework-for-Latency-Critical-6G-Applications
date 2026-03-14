
from fastapi import FastAPI
from app.api import router as api_router
import uvicorn

app = FastAPI(title="MEC Prototype")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "MEC Prototype Active", "version": "0.1"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
