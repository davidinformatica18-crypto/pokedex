from fastapi import FastAPI
import json

app = FastAPI()

RUTA_JSON = Path(__file__).parent / "lista_pokemon.json"

with open("lista_pokemon.json", "r", encoding="utf-8") as archivo:
    pokemons = json.load(archivo)

@app.get("/")
def lista_pokemon(): # Lista de pokmovimientos.
    return pokemons

@app.get("/")
def pokemovimientos (): # Lista de pokmovimientos.
     for pokemon in pokemons:
        for movimiento in pokemon["movimientos"]:
            movimientos.append({
                "pokemon": pokemon["nombre"],
                "nombre": movimiento["nombre"],
                "tipo": movimiento["tipo"],
                "poder": movimiento["poder"]
            })
return movimientos

@app.post("/") 
def crear ():
    return
@app.put("/items/{item_id}")
def actualizar():
    return
@app.patch("/items/{item_id}")
def actualizar_parte():
    return

#@app.delete("/items/{item_id}")
    #def eliminar():
        #return