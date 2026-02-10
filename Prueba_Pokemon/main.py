# Script que me va a ejecutar la logica siguiente:

# Escenario
# Definir que pokemons van a combatir (2 -> p1 y p2)
# Definir quien inicia el ataque: el que tenga más velocidad
# Logica de turno: 
# - 1 accion por turno para cada pokemon
# - ataca 1 pokemon el 2 recibe daño en función del p1.ataque - p2.defensa
# - ataca 2 pokemon el 1 recibe daño en función del p2.ataque - p1.defensa

# condiciones victoria o derrota
# El primer pokemon que se queda a vvida <= 0 pierde

from personaje_pokemon import PokemonFuego, PokemonAgua, Movimiento # Importamos la clase Pokemon desde el archivo Personaje_pokemon.py

"""
pokemon1 = Pokemon(                   # Crea el primer pokemon en teoria 
    
    nombre="Pikachu",
    
    tipo="Eléctrico",
    
    nivel = 10,
    
    vida = 200,
    
    ataque = 25,
    
    defensa = 10,
    
    velocidad = 90,
    
    Impactrueno = 50,

    Ataque_rápido = 20,

    Placaje = 10,

    Chispa = 80,

   movimientos = [
    
        ("Impactrueno", 50),

        ("Ataque rapido", 20),

        ("Placaje", 10),

        ("Chispa", 80)

)

"""
# MOVIMIENTOS DE LOS DICHOSOS POKEMON _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

impactrueno = Movimiento("Impactrueno", "Electrico", 50)
ataque_rapido = Movimiento("Ataque rapido", "Normal", 20)
placaje = Movimiento("Placaje", "Normal", 10)
chispa = Movimiento("Chispa", "Electrico", 80)

pokemon1 = PokemonFuego(
    nombre = "Charmander",
    vida = 110,
    ataque = 30,
    defensa = 10,
    velocidad = 20
)

pokemon2 = PokemonAgua(
    nombre = "Squirtle",
    vida = 110,
    ataque = 25,
    defensa = 15,
    velocidad = 15
)


# AÑADIR LOS MOVIMIENTOS _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _  _ _

if pokemon1.velocidad > pokemon2.velocidad:             # Decidimos quién ataca primero según la velocidad

    pokemon1.movimientos = ascuas
    pokemon1.movimientos = lanzallamas

    pokemon2.movimientos = pistola_agua
    pokemon2.movimientos = hidrobomba

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

while pokemon1.vida > 0 and pokemon2.vida > 0: # Bucle principal del combate Se repite mientras los dos pokemons tengan vida
    atacante.ejecutar_movimiento(defensor)     # El atacante ejecuta un movimiento

    if defensor.vida <= 0:                     # Si el defensor se queda sin vida, termina el combate
     print(defensor.nombre, "ha sido derrotado")
    break

    atacante, defensor = defensor, atacante
    print("----------------------------------")

print("Ha sido derrotado")        

print("El combate ha terminado") # Muestra el resultado final

