from fastapi import APIRouter

router = APIRouter()

@router.post("/catch")
def catch_pokemon_endpoint():
    return {"message": "caught pikachu" }
