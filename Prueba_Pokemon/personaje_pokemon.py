import random # Importamos la librería random para elegir cosas al azar.
# from movimiento import Movimiento 


class Movimiento:

    def __init__(self, nombre, tipo, nivel):

        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

# Super clases_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

class PokemonFuego(Pokemon):
    def __init__(self, nombre, vida, ataque, defensa, velocidad):
        super().__init__(nombre, "Fuego", vida, ataque, defensa, velocidad)


class PokemonAgua(Pokemon):
    def __init__(self, nombre, vida, ataque, defensa, velocidad):
        super().__init__(nombre, "Agua", vida, ataque, defensa, velocidad)

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

class PokemonFuego(Pokemon): # Definimos la clase Pokemon Una clase es como un molde para crear pokemons y frikadas varias    

    def __init__(self, nombre, tipo, vida, ataque, defensa, velocidad):
        self.nombre = nombre          # Nombre del Pokémon
        self.tipo = tipo              # Tipo del Pokémon
        self.vida = vida              # Vida actual
        self.ataque = ataque          # Ataque
        self.defensa = defensa        # Defensa
        self.velocidad = velocidad    # Velocidad
        self._movimientos = []        # Lista privada de movimientos

        # self.movimientos = movimientos                       # Guarda la lista de movimientos (máximo 4 nombres)

        self.movimientos = []                                  # Empieza sin movimientos

        try:

         @property
         def movimientos(self):
            return self._movimientos
    
        except TypeError:
            print ("el movimiento no es correcto")

    @movimientos.setter
    def movimientos(self, movimiento):
        if movimiento.tipo != self.tipo:
            raise ValueError("movimiento no coincide")

        if len(self._movimientos) >= 4:
            raise ValueError("No puede tener más de 4 movimientos no te engañes")

        self._movimientos.append(movimiento)


    def ejecutar_movimiento(self, otro_pokemon):             # Método para ejecutar un movimiento contra otro pokemon
        movimiento_elegido = random.choice(self.movimientos) # Elege un movimiento al azar de la lista de movimientos
        print(self.nombre, "utiliza", movimiento_elegido)    # Muestra qué movimiento se ha usado
        dano = self.ataque - otro_pokemon.defensa            # Calcula el daño El daño es el ataque menos la defensa del otro pokemon
      
       # movimiento.ejecutar(self, otro_pokemon)

        if dano < 0:                                         # Si el daño es negativo, lo dejamos en 0
            dano = 0

        
        otro_pokemon.recibir_dano(dano)                      # Llama al método recibir_dano del otro pokemon


    
    def recibir_dano(self, dano):                             # Método para recibir daño
 
        self.vida -= dano                                     # Restamos el daño a la vida actual

        print(self.nombre, "recibe", dano, " daño")             # Muestra cuánta vida le queda

        print("vida restante de ", self.nombre, ":", self.vida)
