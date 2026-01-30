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

from Personaje_pokemon import Pokemon # Importamos la clase Pokemon desde el archivo Personaje_pokemon.py

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

impactrueno = Movimiento("Impactrueno", "Electrico", 50)
ataque_rapido = Movimiento("Ataque rapido", "Normal", 20)
placaje = Movimiento("Placaje", "Normal", 10)
chispa = Movimiento("Chispa", "Electrico", 80)

pokemon1 = Pokemon(
    nombre="Pikachu",
    tipo="Electrico",
    nivel=10,
    vida=200,
    ataque=25,
    defensa=10,
    velocidad=90,
    movimientos=[impactrueno, ataque_rapido, placaje, chispa]
)

pokemon2 = Pokemon(               # Crea el segundo pokemon para no dejarlo solo
   
    nombre="Charmander",
   
    tipo="Fuego",
   
    nivel = 10,
   
    vida = 220,
    
    ataque = 28,
    
    defensa = 12,
   
    velocidad = 65,
   
    movimientos=["Ascuas", "Arañazo", "Lanzallamas", "Placaje"]
)



print("¡Comienza el combate!")                          # Muestra Que empieza el combate

print(pokemon1.nombre, "VS", pokemon2.nombre)

print("--------------------------------------------------")



if pokemon1.velocidad > pokemon2.velocidad:             # Decidimos quién ataca primero según la velocidad
    
    atacante = pokemon1
   
    defensor = pokemon2

else:
    
    atacante = pokemon2
   
    defensor = pokemon1




while pokemon1.vida > 0 and pokemon2.vida > 0:          # Bucle principal del combate Se repite mientras los dos pokemons tengan vida

    
    atacante.ejecutar_movimiento(defensor)              # El atacante ejecuta un movimiento

    
    if defensor.vida <= 0:                              # Si el defensor se queda sin vida, termina el combate
       
        print(defensor.nombre, "ha sido derrotado")
      
        break

    
    atacante, defensor = defensor, atacante    # Cambia los roles: el defensor pasa a atacar

   
    print("--------------------------------------------------") # Línea para que se vea más claro el turno



print("El combate ha terminado") # Muestra el resultado final

