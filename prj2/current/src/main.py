import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def central_function():
    return {"Var2": "val1"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")

    