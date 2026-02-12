from fastapi import FastAPI
from pathlib import Path
from pydantic import BaseModel
from persistencia import cargar_pokemons, guardar_pokemons
from typing import List
import json

app = FastAPI()


# archivo_json = Path(__file__).parent / "lista_pokemon.json" # Ruta del JSON

pokemons = cargar_pokemons()


# with open(archivo_json, "r") as archivo: # Archivo el JSON
#    pokemons = json.load(archivo)

class Movimiento(BaseModel):
    nombre: str
    tipo: str
    poder: int


class Pokemon(BaseModel):
    nombre: str
    tipo: str
    vida: int
    ataque: int
    defensa: int
    velocidad: int
    movimientos: List[Movimiento]


@app.get("/pokemon") # Lista de Pokemon _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
def lista_pokemon():
    return pokemons

@app.get("/movimientos") # Lista de movimientos _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
def pokemovimientos():
    movimientos = []

    for pokemon in pokemons:
        for movimiento in pokemon["movimientos"]:
            movimientos.append({
                "pokemon": pokemon["nombre"],
                "nombre": movimiento["nombre"],
                "tipo": movimiento["tipo"],
                "poder": movimiento["poder"]
            })

    return movimientos

@app.post("/pokemon") # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
def crear(nuevo_pokemon: Pokemon):

    pokemon_dict = nuevo_pokemon.dict()

    pokemons.append(pokemon_dict)

    guardar_pokemons(pokemons)

    return {
        "mensaje": "Pokemon creado ha creado el Pokemon, valgame dios majaris lo tuyo que fuerte ",
        "pokemon": pokemon_dict
    }

"""
@app.post("/pokemon")
def crear(nuevo_pokemon: Pokemon):

    pokemon_dict = nuevo_pokemon.dict()

    pokemon.append(pokemon_dict)

    with open(archivo_json, "w", encoding="utf-8") as archivo:
        json.dump(pokemon, archivo, indent=4, ensure_ascii=False)

    return {
        "mensaje": "ha creado el Pokemon, valgame dios majaris lo tuyo que fuerte",
        "pokemon": pokemon_dict
    }
"""
@app.put("/pokemon/{item_id}") # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
def actualizar(item_id: int):
    return {"mensaje": f"Se ha actualizado el Pokemon {item_id}"}


@app.patch("/pokemon/{item_id}") # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
def actualizar_parte(item_id: int):
    return {"mensaje": f"Se ha actualizado parte del Pokemon {item_id}"}

@app.delete("/pokemon/{item_id}") # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
def eliminar(item_id: int):
    return {"mensaje": f"Se ha eliminado el Pokemon {item_id}"}
