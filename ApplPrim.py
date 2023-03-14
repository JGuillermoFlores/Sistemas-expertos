def primero_el_mejor(opciones):
    mejor_opcion = opciones[0]
    for opcion in opciones:
        if opcion["Densidad"] < mejor_opcion["Densidad"]:
            mejor_opcion = opcion
    return mejor_opcion

# Ejemplo de uso:
opciones = []
while True:
    nombre = input("Ingrese el nombre de la ciudad: ")
    if not nombre:
        break
    valor = float(input("Ingrese su numero de habitantes: "))
    extensiont = float(input("Ingrese la extension territorial en km2: "))
    densidad = float (valor/extensiont)
    opciones.append({"nombre": nombre, "valor": valor, "Extension":extensiont, "Densidad":densidad})

if not opciones:
    print("No se ingresaron opciones.")
else:
    mejor_opcion = primero_el_mejor(opciones)
    print(f"La ciudad {mejor_opcion['nombre']} tiene la menor densidad de poblacion con un valor de {mejor_opcion['Densidad']}  habitantes por Km2.")
