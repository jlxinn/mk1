from fastapi import FastAPI

app = FastAPI(title="Qr iin Bishkek Babe")

@app.get("/")
async def root():
    return {"message": "FastAPI is running successfully in Bishkek! 🚀"}
