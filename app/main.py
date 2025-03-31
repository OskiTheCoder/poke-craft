from fastapi import FastAPI

app = FastAPI(title="TBD")

@app.get("/")
def root():
    return {"message": "Hello, World!"}
