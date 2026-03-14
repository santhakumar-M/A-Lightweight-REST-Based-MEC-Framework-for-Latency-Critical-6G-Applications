from fastapi import FastAPI
import subprocess
import time

app = FastAPI()

@app.post("/invoke")
def invoke():
    start = time.time()
    result = subprocess.run(
        ["python", "--version"],
        capture_output=True,
        text=True
    )
    end = time.time()

    return {
        "stdout": result.stdout,
        "execution_time": end - start
    }
