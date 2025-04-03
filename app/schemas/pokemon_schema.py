from pydantic import BaseModel
from typing import List

class UserPokemonResponse(BaseModel):
    user_id: str
    pokemon: List[str]

class CatchPokemonResponse(BaseModel):
    user_id: str
    pokemon: str
