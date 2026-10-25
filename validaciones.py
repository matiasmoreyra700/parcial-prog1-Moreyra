from procesamiento import*



def validar_cantidad_alumnos() -> int:

    contador = 0
    while True:
        if contador >= 1:
            print("\nIngrese una cantidad valida (entre 1 y 30)")
        cantidad = input("Ingrese la cantidad de alumnos: ")
        entero = validar_entero(cantidad)
        if entero == True:
            cantidad = int(cantidad)
            contador += 1
            if cantidad >= 1 and cantidad <= 30:
                contador += 1
                break
        contador += 1
    return cantidad


def cargar_nombres(cantidad_alumnos : list) -> list:
    
    nombres = len(cantidad_alumnos) * [0]
    for i in range(len(nombres)):
        while True:
            nombre = input(f"Ingrese el {i+1}° nombre: ")
            cadena = validar_cadena(nombre)
            if cadena == False:
                print("Por favor ingrese un nombre adecuado")
            else:
                if len(nombre) >= 5:
                    break
                else:
                    print("Por favor ingrese un nombre adecuado")
        nombres[i] = nombre
    return nombres


def cargar_notas(cantidad_alumnos : list, lista_nombres : list) -> list:
    
    lista_notas = len(cantidad_alumnos) * [0]
    
    for i in range(len(lista_notas)):
        while True:
            nota = input(f"Ingrese la nota de {lista_nombres[i]}: ")
            entero = validar_entero(nota)
            if entero == False:
                print("Por favor ingrese un valor adecuado")
            else:
                    nota = int(nota)
                    if nota >= 0 and nota <= 10:
                        break
                    else:
                        print("Por favor ingrese un valor adecuado")
        lista_notas[i] = nota
    return lista_notas



def cantidad_alumnos_condicion(lista_promedios : list):
    promociona = 0
    aprueba = 0
    desaprueba = 0
    
    for i in range(len(lista_promedios)):
        if lista_promedios[i] >= 6:
            promociona += 1
        if lista_promedios[i] >= 4 and lista_promedios[i] < 6:
            aprueba += 1
        if lista_promedios[i] < 4:
            desaprueba += 1
    
    print(f"\nCantidad de alumnos por condición:\nPromociona: {promociona}\nAprueba: {aprueba}\nDesaprueba: {desaprueba}")
    
    

def buscar_alumno(lista_nombres : list, nombre : str) -> bool:
    encontrado = False
    for i in range(len(lista_nombres)):
        if nombre == lista_nombres[i]:
            encontrado = True
    
    return encontrado
        