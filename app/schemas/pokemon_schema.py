from pydantic import BaseModel
from typing import List

class UserListPokemonResponse(BaseModel):
    user_id: str
    pokemon: List[str]

class CatchPokemonResponse(BaseModel):
    user_id: str
    pokemon: str

class UserListPokemonRequest(BaseModel):
    user_id: str

class CatchPokemonRequest(BaseModel):
    user_id: str