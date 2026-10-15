from fastapi import FastAPI

app = FastAPI(title='Entreprise knowledge AI')

@app.get("/health")
def health_check():
    return {"status": "healthy"}

