from fastapi import FastAPI
from pathlib import Path
import json

app = FastAPI()


archivo_json = Path(__file__).parent / "lista_pokemon.json" # Ruta del JSON


with open(archivo_json, "r") as archivo: # Archivo el JSON
    pokemons = json.load(archivo)

@app.get("/pokemon") # Lista de Pokemon
def lista_pokemon():
    return pokemons

@app.get("/movimientos") # Lista de movimientos
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


@app.post("/pokemon")
def crear():
    return {"mensaje": "Se ha creado el Pokemon"}

@app.put("/pokemon/{item_id}")
def actualizar(item_id: int):
    return {"mensaje": f"Se ha actualizado el Pokemon {item_id}"}


@app.patch("/pokemon/{item_id}")
def actualizar_parte(item_id: int):
    return {"mensaje": f"Se ha actualizado parte del Pokemon {item_id}"}

@app.delete("/pokemon/{item_id}")
def eliminar(item_id: int):
    return {"mensaje": f"Se ha eliminado el Pokemon {item_id}"}
