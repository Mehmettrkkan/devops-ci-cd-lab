from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mesaj": "CI/CD Pipeline basariyla calisiyor!"}

@app.get("/topla/{a}/{b}")
def topla(a: int, b: int):
    return {"sonuc": a + b}
