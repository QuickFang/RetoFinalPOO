class PersonajeBase:
    def __init__(self, nombre, fuerza, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.defensa = defensa
        self.vida = vida

    def atacar(self, enemigo):
        dano = self.fuerza - enemigo.defensa
        if dano < 0:
            dano = 0
        enemigo.vida -= dano
        print(f"{self.nombre} ataca a {enemigo.nombre} y causa {dano} puntos de daño.")
        if enemigo.vida <= 0:
            print(f"{enemigo.nombre} ha sido derrotado.")


class Personaje(PersonajeBase):
    def __init__(self, nombre, fuerza, defensa, vida, mana, hadas):
        super().__init__(nombre, fuerza, defensa, vida)
        self.mana = mana
        self.hadas = hadas 

    def usar_hechizo(self, enemigo):
        if self.mana >= 10:
            dano = self.fuerza * 2 - enemigo.defensa
            if dano < 0:
                dano = 0
            enemigo.vida -= dano
            self.mana -= 10
            print(f"{self.nombre} usa un hechizo contra {enemigo.nombre} y causa {dano} puntos de daño.")
            if enemigo.vida <= 0:
                print(f"{enemigo.nombre} ha sido derrotado.")
                print("¡Felicidades, has salvado a 2 hadas!")
                # Aumentar el contador de hadas rescatadas
                self.hadas += 2
        else:
            print(f"{self.nombre} no tiene suficiente mana para usar un hechizo.")

    def curar(self):
        if self.mana >= 5:
            curacion = self.fuerza * 2
            self.vida += curacion
            self.mana -= 5
            print(f"{self.nombre} se cura y recupera {curacion} puntos de vida.")
        else:
            print(f"{self.nombre} no tiene suficiente mana para curarse.")


class Enemigo(PersonajeBase):
    def __init__(self, nombre, fuerza, defensa, vida):
        super().__init__(nombre, fuerza, defensa, vida)

    def atacar(self, jugador):
        super().atacar(jugador)


class RescateDeHadas:
            print("¡Felicidades has derrotado al hechizero!")
            print("Fin del juego")  
        
