from fastapi import APIRouter
from app.services.pokemon_service import get_user_pokemon, catch_random_pokemon
from app.schemas.pokemon_schema import UserPokemonResponse, CatchPokemonResponse

router = APIRouter()

@router.get("/", response_model=UserPokemonResponse)
def get_pokemon(user_id: str):
    """Fetch all Pokémon a user has caught."""
    return {"user_id": user_id, "pokemon": get_user_pokemon(user_id)}

@router.post("/catch", response_model=CatchPokemonResponse)
def catch_pokemon(user_id: str):
    """Catch a random Pokémon."""
    new_pokemon = catch_random_pokemon(user_id)
    return {"user_id": user_id, "pokemon": new_pokemon}
