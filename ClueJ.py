# -*- coding: utf-8 -*-
import random

class JuegoClue:
    def __init__(self):
        self.personajes = ['Juan', 'Lucas', 'Pedro', 'Marcos', 'Simon']
        self.locaciones = ['Cocina', 'Sala', 'Habitacion', 'Jardin', 'Comedor']
        self.armas = ['Picahielo', 'Cuchillo', 'Pistola', 'Soga', 'Martillo']
        self.asesino = random.choice(self.personajes)
        self.locacion = random.choice(self.locaciones)
        self.arma = random.choice(self.armas)

    def mostrar_opciones(self):
        print("Las opciones son:")
        print("Personajes:", self.personajes)
        print("Locaciones:", self.locaciones)
        print("Armas:", self.armas)

    def hacer_pregunta(self):
        print("Selecciona una categoría:")
        print("1. Personajes")
        print("2. Locaciones")
        print("3. Armas")

        categoria = input("Selecciona una opción (1, 2 o 3): ")

        if categoria == "1":
            print("Selecciona un personaje para preguntar:")
            for p in self.personajes:
                print(p)
            personaje_pregunta = input("Selecciona un personaje: ")
            if personaje_pregunta == self.asesino:
                print("El asesino es", self.asesino)
            else:
                print(personaje_pregunta, "no es el asesino.")

        elif categoria == "2":
            print("Selecciona una locación para preguntar:")
            for l in self.locaciones:
                print(l)
            locacion_pregunta = input("Selecciona una locación: ")
            if locacion_pregunta == self.locacion:
                print("El crimen sucedió en", self.locacion)
            else:
                print(locacion_pregunta, "no es la locación del crimen.")

        elif categoria == "3":
            print("Selecciona un arma para preguntar:")
            for a in self.armas:
                print(a)
            arma_pregunta = input("Selecciona un arma: ")
            if arma_pregunta == self.arma:
                print("El arma utilizada fue", self.arma)
            else:
                print(arma_pregunta, "no fue el arma utilizada.")

        else:
            print("Opción inválida.")

    def hacer_acusacion(self):
        print("Haz tu acusación:")
        acusacion_personaje = input("¿Quién es el asesino?: ")
        acusacion_locacion = input("¿Dónde sucedió el crimen?: ")
        acusacion_arma = input("¿Qué arma se utilizó?: ")

        if acusacion_personaje == self.asesino and acusacion_locacion == self.locacion and acusacion_arma == self.arma:
            print("¡Felicidades! Has resuelto el crimen.")
            return True
        else:
            print("Lo siento, tu acusación es incorrecta.")
            return False

    def jugar(self):
        print("¡Bienvenido a Clue!")
        print("Debes encontrar al asesino, el arma y la locación del crimen.")
        self.mostrar_opciones()

        # Comenzamos el juego
        while True:
            print("¿Qué te gustaría hacer?")
            print("1. Hacer una pregunta.")
            print("2. Hacer una acusación.")
            print("3. Rendirse.")

            opcion = input("Selecciona una opción (1, 2 o 3): ")

if opcion == "1":
    print("Selecciona una categoría:")
    print("1. Personajes")
    print("2. Locaciones")
    print("3. Armas")
    
    categoria = input("Selecciona una opción (1, 2 o 3): ")
    
    if categoria == "1":
        print("Selecciona un personaje para preguntar:")
        [print(p) for p in personajes]
        personaje_pregunta = input("Selecciona un personaje: ")
        if personaje_pregunta == asesino:
            print("El asesino es", asesino)
        else:
            print(personaje_pregunta, "no es el asesino.")
            
    elif categoria == "2":
        print("Selecciona una locación para preguntar:")
        [print(l) for l in locaciones]
        locacion_pregunta = input("Selecciona una locación: ")
        if locacion_pregunta == locacion:
            print("El crimen sucedió en", locacion)
        else:
            print(locacion_pregunta, "no es la locación del crimen.")
            
    elif categoria == "3":
        print("Selecciona un arma para preguntar:")
        [print(a) for a in armas]
        arma_pregunta = input("Selecciona un arma: ")
        if arma_pregunta == arma:
            print("El arma utilizada fue", arma)
        else:
            print(arma_pregunta, "no fue el arma utilizada.")
    
    else:
        print("Opción inválida.")

elif opcion == "2":
    print("Haz tu acusación:")
    acusacion_personaje = input("¿Quién es el asesino?: ")
    acusacion_locacion = input("¿Dónde sucedió el crimen?: ")
    acusacion_arma = input("¿Qué arma se utilizó?: ")
    
    if acusacion_personaje == asesino and acusacion_locacion == locacion and acusacion_arma == arma:
        print("¡Felicidades! Has resuelto el crimen.")
       
    else:
        print("Lo siento, tu acusación es incorrecta.")
        
elif opcion == "3":
    print("La solución era:")
    print("El asesino era", asesino)
    print("El crimen sucedió en", locacion)
    print("El arma utilizada fue", arma)
  
    
else:
    print("Opción inválida.")
