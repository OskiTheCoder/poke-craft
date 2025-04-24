from fastapi import APIRouter
from app.services.pokemon_service import get_user_pokemon, catch_random_pokemon
from app.schemas.pokemon_schema import UserListPokemonResponse, CatchPokemonResponse, UserListPokemonRequest, CatchPokemonRequest

router = APIRouter()

@router.get("/list", response_model=UserListPokemonResponse)
async def get_pokemon(data: UserListPokemonRequest):
    """Fetch all Pokémon a user has caught."""
    user_id = data.user_id
    return {"user_id": user_id, "pokemon": get_user_pokemon(user_id)}

@router.post("/catch", response_model=CatchPokemonResponse)
async def catch_pokemon(data: CatchPokemonRequest):
    """Catch a random Pokémon."""
    user_id = data.user_id
    new_pokemon = catch_random_pokemon(user_id)
    return {"user_id": user_id, "pokemon": new_pokemon}
