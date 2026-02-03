import pytest
#from movimiento import Movimiento
from Prueba_Pokemon.personaje_pokemon import Pokemon, Movimiento

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

class PokemonFuego(Pokemon):                    # Sub clase de Pokemon
    def __init__(self, nombre, vida, ataque):
        super().__init__(nombre, vida, ataque)  # super clase o clase padre
        self.tipo = "Fuego"                     # Tipo fuego
        assert pokemon.tipo == "Fuego"



class PokemonAgua(Pokemon):                     
    def __init__(self, nombre, vida, ataque):
        super().__init__(nombre, vida, ataque)  
        self.tipo = "Agua"                      # Tipo agua
        assert pokemon.tipo == "Agua"

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def test_pokemon_empieza_sin_movimiento():
    pokemon = pokemon("charmander", "fuego")
    assert len(pokemon.get_movimiento()) == 0

def test_anadir_movimiento_correcto():

    movimiento = Movimiento("Lanzallamas", "fuego", 20)

    pokemon = Pokemon("Charmander", "fuego")

    pokemon.set_movimiento(movimiento)

    assert len(pokemon.get.movimientos()) == 1


def test_no_mas_de_cuatro_movimientos():
    pokemon = Pokemon ("charmander,fuego")

    movimientos = [
        Movimiento("Ascuas", "fuego", 10),
        Movimiento("Lanzallamas", "fuego", 20),
        Movimiento("Giro Fuego", "fuego", 15),
        Movimiento("Colmillo Ígneo", "fuego", 25)
    ]

    for m in movimientos:
        pokemon.set_movimiento(m)
    assert len (pokemon.get_movimientos()) == 4

def test_quinto_movimiento_da_error():
    pokemon = Pokemon("Charmander", "fuego")

    for i in range(4):
        pokemon.set_movimiento(Movimiento("Fuego{i}", "fuego", 10))

    with pytest.raises(ValueError):
        pokemon.set_movimiento(Movimiento("Extra", "fuego", 10))

def test_anadir_movimiento_incorrecto():

    movimiento = Movimiento("Pistola Agua", "agua", 10)

    pokemon = Pokemon("Charmander", "fuego")
    
    with pytest.raises(ValueError):

        pokemon.set_movimiento(movimiento)

    with pytest.raises(ValueError):
        pokemon.set_movimiento(movimiento)

def test_varios_movimientos_correctos():

    animacion1 = Movimiento("Ascuas", "fuego", 30)

    animacion2 = Movimiento("Lanzallamas", "fuego", 20)

    pokemon = Pokemon("Charmander", "fuego", [animacion11, animacion2])

    assert len(pokemon.movimientos) == 2


def test_tipo_pokemon_invalido():

    movimiento = Movimiento("Lanzallamas", "fuego", 30)
