from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/events")
def create_event():
    return {"message": "Event alındı."}
