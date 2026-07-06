from fastapi import FastAPI

app = FastAPI(
    title="Game Telemetry API",
    description="Staj Projesi - Oyun Telemetri Servisi",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Merhaba Game Telemetry API!"}


@app.get("/health")
def health():
    return {"status": "ok"}