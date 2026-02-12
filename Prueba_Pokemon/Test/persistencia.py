import json
from pathlib import Path

RUTA_JSON = Path(__file__).parent / "lista_pokemon.json"


def cargar_pokemons():
    with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_pokemons(lista):
    with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4, ensure_ascii=False)
