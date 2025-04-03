import random
from app.data.fake_data import FAKE_USERS_POKEMON, FAKE_POKEMON_LIST

def get_user_pokemon(user_id: str):
    return FAKE_USERS_POKEMON.get(user_id, [])

def catch_random_pokemon(user_id: str):
    new_pokemon = random.choice(FAKE_POKEMON_LIST)
    
    if user_id not in FAKE_USERS_POKEMON:
        FAKE_USERS_POKEMON[user_id] = []
    
    FAKE_USERS_POKEMON[user_id].append(new_pokemon)
    return new_pokemon
