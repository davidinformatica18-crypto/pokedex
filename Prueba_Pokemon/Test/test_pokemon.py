import pytest
#from movimiento import Movimiento
from pokedex.personaje_pokemon import Pokemon, Movimiento

def test_anadir_movimiento_correcto():

    movimiento = Movimiento("Lanzallamas", "fuego", 20)

    pokemon = Pokemon("Charmander", "fuego")

    pokemon.set_movimiento(movimiento)

    assert len(pokemon.movimientos) == 1


def test_anadir_movimiento_incorrecto():

    movimiento = Movimiento("Pistola Agua", "agua", 10)

    pokemon = Pokemon("Charmander", "fuego")
    
    with pytest.raises(ValueError):

        pokemon.set_movimiento(movimiento)


def test_varios_movimientos_correctos():

    animacion1 = Movimiento("Ascuas", "fuego", 30)

    animacion2 = Movimiento("Lanzallamas", "fuego", 20)

    pokemon = Pokemon("Charmander", "fuego", [animacion11, animacion2])

    assert len(pokemon.movimientos) == 2


def test_tipo_pokemon_invalido():

    movimiento = Movimiento("Lanzallamas", "fuego", 30)