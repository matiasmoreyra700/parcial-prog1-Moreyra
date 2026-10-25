from procesamiento import*



def validar_cantidad_alumnos() -> int:
    """Pide un numero del 1 al 30

    Returns:
        int: Devuelve el numero ingresado despues de validarlo
    """
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
    """Carga una lista con la cantidad de nombres indicada

    Args:
        cantidad_alumnos (list): La cantidad de nombres a cargar

    Returns:
        list: Devuelve la lista de nombres despues de validarla
    """
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
    """Pide y carla las notas de los alumnos

    Args:
        cantidad_alumnos (list): Lista con la catidad de alumnos
        lista_nombres (list): Lista con los nombres de los alumnos

    Returns:
        list: Devuelve la lista con las notas cargadas
    """
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
    """Muestra la cantidad de alumnos en cada condicion

    Args:
        lista_promedios (list): Lista con los promedios de los parciales
    """
    
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
    """Busca si un nombre esta en la lista de nombres

    Args:
        lista_nombres (list): Lista con los nombres de los alumnos
        nombre (str): Nombre del alumno que se busca

    Returns:
        bool: Devuelve:
            True: Si el nombre estaba en la lista
            False: Si el nombre NO estaba en la lista
    """
    
    encontrado = False
    for i in range(len(lista_nombres)):
        if nombre == lista_nombres[i]:
            encontrado = True
    
    return encontrado