from fastapi import FastAPI
from app.api.v1 import pokemon, users

app = FastAPI(title="PokeCraft API", version="1.0")

app.include_router(pokemon.router, prefix="/pokemon", tags=["Pokemon"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Welcome to the PokeCraft API!"}
