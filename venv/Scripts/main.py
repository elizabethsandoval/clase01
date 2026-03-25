from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def saludar():
    return {"mensaje":"¡Hola! Bienvenido a mi API"}
@app.get("/bienvenido/{nombre}")
def saludar_persona(nombre: str):
    return {"mensaje": f"Hola {nombre}, ¡qué bueno verte por aquí!"}