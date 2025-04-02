from fastapi import APIRouter

router = APIRouter()

@router.get("/{user_id}/pokemon")
def list_caught_pokemon(user_id: str):
    return {"user_id": "1", "caught_pokemon": ["pikachu"]}
