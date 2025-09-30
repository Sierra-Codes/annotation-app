from fastapi import FastAPI

app = FastAPI(title="Annotation App")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Annotation App!"}
