
"""
Simple Cloud Run Job to Fetch Pokemon and its Metadata
"""

import requests

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title = "Pokemon Fetcher"
)

class PokemonRequest(BaseModel):
    """
    Schema for the incoming Pokemon request payload.
    """
    pokemon: str

@app.get("/")
async def root_health_check():
    """
    Simple GET route for browser testing.
    """
    return {
        "status": "online", 
        "message": "Pokemon API is running. Go to /docs to use it."
    }

@app.post("/")
async def get_pokemon_metadata(request_data: PokemonRequest):
    """
    Fetch and return metadata for a specified Pokemon from PokeAPI.
    """
    pokemon_name = request_data.pokemon.lower().strip()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        pokemon_stats = {
            "name": data.get("name"),
            "abilities": [
                ability["ability"]["name"]
                for ability in data.get("abilities", [])
            ],
            "moves": [
                move["move"]["name"] for move in data.get("moves", [])
            ],
        }

        return pokemon_stats

    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code if e.response is not None else 500

        if status_code == 404:
            raise HTTPException(
                status_code = 404,
                detail = f"Pokemon '{pokemon_name}' not found."
            )
        raise HTTPException(
            status_code = status_code,
            detail = f"PokeAPI Error: {str(e)}"
        )

    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code = 503,
            detail = f"Failed to connect to PokeAPI: {str(e)}"
        )

    except KeyError as e:
        raise HTTPException(
            status_code = 500,
            detail = f"Unexpected data format from PokeAPI. Missing key: {str(e)}"
        )

    except Exception as e:
        raise HTTPException(
            status_code = 500,
            detail = f"An internal server error occurred: {str(e)}"
        )
