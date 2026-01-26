# pokedex
# Definir entidades que hay en una Pokedex con sus Métodos atributos.

# 1. Pokémon _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# Representa a un Pokémon individual.

# - Atributos:

º id : Identificador único. nombre : Nombre del Pokémon tipo : Tipos Fuego, Agua. nivel : 

º Nivel actual salud : Puntos de vida ataque : Poder de ataque defensa : Poder de defensa

º velocidad : Velocidad del Pokémon habilidades : Lista de habilidades estado : Estado actual (normal, debilitado, etc.)

# - Métodos:

º atacar(objetivo). recibirDanio(cantidad). subirNivel(). usarHabilidad(habilidad). estaDebilitado().

# 2. Pokédex _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# Contenedor principal de información de Pokémon.

# - Atributos:

º listaPokemon : Colección de Pokémon registrados. region : Región de la Pokédex. totalRegistrados : Número de Pokémon almacenados

# - Métodos:

º registrarPokemon(pokemon). eliminarPokemon(id). buscarPokemon(nombre). listarPokemon(). mostrarDetalle(id)

# 3. Entrenador _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

# Representa a un entrenador Pokémon.

# - Atributos:

º nombre. edad. region. equipoPokemon : Pokémon activos (máx. 6). pokedex : Pokédex asociada

# - Métodos:

º capturarPokemon(pokemon). liberarPokemon(pokemon). cambiarPokemon(posicion). verEquipo()

# 4. Batalla _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# Gestiona un combate entre Pokémon.

# - Atributos:

º pokemon1. pokemon2. turnoActual

º estadoBatalla

# - Métodos:

º iniciarBatalla(). atacar(). cambiarTurno(). finalizarBatalla()

# 5. Habilidad _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

# Define habilidades o movimientos.

# - Atributos:

º nombre. tipo. danio. costoEnergia. efectoEspecial

# - Métodos:

º -- ejecutar(objetivo). tieneEfectoEspecial() Paradigma: Programación Orientada a Objetos

º -- Control de versiones: Git & GitHub. Objetivo del Proyecto

º -- Crear una estructura base para una Pokédex que permita:

º -- Registrar y gestionar Pokémon. Simular batallas

# Aplicar principios de POO (encapsulación, herencia, polimorfismo) 
