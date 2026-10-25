

def inicializar_lista(parametro : int) -> list:
    """
        Genera una lista del tamaño deseado.
    Args:
        parametro (int): El tamaño deseado de la lista

    Returns:
        list: Devuelve la lista del tamaño deseado.
        Todos sus datos son 0
    """
    lista = [0] * parametro
    return lista


def validar_entero(cadena : str) -> bool:
    """Recibe una cadena(str) y verifica que los datos sea un entero(int)

    Args:
        cadena (str): La cadena(str) a verificar

    Returns:
        bool:
        Devuelve True si es un entero.
        Devuelve False si NO es un entero.
    """
    if cadena != "":
        for i in range(len(cadena)):
            if cadena[i] >= "0" and cadena[i] <= "9":
                entero = True
            else:
                entero = False
                break
    else:
        entero = False
    return entero


def validar_cadena(cadena : str) -> bool:
    """Recibe una cadena(str) y determina si su contenido son letras o espacios.
        Revisa que el numero de mayusculas sea 1 o 2 
        Revisa que el numero de espacios sea 1

    Args:
        cadena (str): La cadena(str) a verificar

    Returns:
        bool: 
        Devuelve True si es una cadena.
        Devuelve False si NO es una cadena.
    """
    espacios = 0
    mayusculas = 0
    if cadena != "":
        for i in range(len(cadena)):
            if cadena[i] >= "a" and cadena[i] <= "z":
                retorno = True
            elif cadena[i] >= "A" and cadena[i] <= "Z":
                retorno = True
                mayusculas += 1
                if mayusculas > 2:
                    retorno = False
                    break
            elif cadena[i] == " ":
                retorno = True
                espacios += 1
                if espacios > 1:
                    retorno = False
                    break
            else:
                retorno = False
                break
    else:
        retorno = False
    if mayusculas == 0:
        retorno = False
    return retorno


def calcular_promedios(cantidad_alumnos : list, primer_parcial : list, segundo_parcial : list) -> list:
    """Calcula los promedios de los dos parciales

    Args:
        cantidad_alumnos (list): Lista con la cantidad total de alumnos
        primer_parcial (list): Notas del primer parcial
        segundo_parcial (list): Notas del segundo parcial

    Returns:
        list: Devuelve la lista con los promedios
    """
    lista_promedios = len(cantidad_alumnos) * [0]
    
    for i in range(len(lista_promedios)):
        total = primer_parcial[i] + segundo_parcial[i]
        promedio = total / 2
        lista_promedios[i] = promedio
    return lista_promedios


def mostrar_estadisticas(lista_nombres : list, primer_parcial : list, segundo_parcial : list, lista_promedios :list):
    """Muestra todos los datos de los alumnos

    Args:
        lista_nombres (list): Lista con los nombres de los alumnos
        primer_parcial (list): Notas del primer parcial
        segundo_parcial (list): Notas del segundo parcial
        lista_promedios (list): Lista con los promedios de los parciales
    """
    for i in range(len(lista_nombres)):
        print(f"Notas de {lista_nombres[i]}: \nPrimer parcial: {primer_parcial[i]}\nSegundo parcial: {segundo_parcial[i]}\nPromedio: {lista_promedios[i]}\n")
        

def calcular_promedio_general(lista_promedios : list, cantidad_alumnos : int) -> float:
    """Calcula el promedio de todo el alumnado

    Args:
        lista_promedios (list): Lista con los promedios de los parciales
        cantidad_alumnos (int): Cantidad total de alumnos

    Returns:
        float: Devuelve el promedio de todo el alumnado
    """
    
    for i in range(len(lista_promedios)):
        if i == 0:
            suma = lista_promedios[i]
        else:
            suma += lista_promedios[i]
    
    promedio_general = suma / cantidad_alumnos
    
    return promedio_general


def encontrar_menor(lista : list) -> int:
    """Encuentra el menor elemento en una lista

    Args:
        lista (list): Lista de elementos a revisar

    Returns:
        int: Devuelve el elemento de menor valor
    """
    for i in range(len(lista)):
        if i == 0:
            menor = lista[i]
        else:
            if menor > lista[i]:
                menor = lista[i]
    return menor


def encontrar_mayor(lista : list) -> int:
    """Encuentra el mayor elemento en una lista

    Args:
        lista (list): Lista de elementos a revisar

    Returns:
        int: Devuelve el elemento de mayor valor
    """
    for i in range(len(lista)):
        if i == 0:
            mayor = lista[i]
        else:
            if mayor < lista[i]:
                mayor = lista[i]
    return mayor


def mostrar_alumno(lista_nombres : list, primer_parcial : list, segundo_parcial : list, lista_promedios : list, nombre : str):
    """Muestra el nombre buscado despues de verificarlo

    Args:
        lista_nombres (list): Lista con los nombres de los alumnos
        primer_parcial (list): Notas del primer parcial
        segundo_parcial (list): Notas del segundo parcial
        lista_promedios (list): Lista con los promedios de los parciales
        nombre (str): El nombre que se busca
    """
    for i in range(len(lista_nombres)):
        if nombre == lista_nombres[i]:
            print(f"\nNotas de {lista_nombres[i]}:\nPrimer parcial: {primer_parcial[i]}\nSegundo parcial: {segundo_parcial[i]}\nPromedio: {lista_promedios[i]}")
                 
            
def contar_vocales(nombre : str) -> int:
    """Cuenta las vocales en el nombre dado

    Args:
        nombre (str): Nombre a revisar

    Returns:
        int: Devuelve el numero de vocales encontrado
    """
    vocales = "aeiou"
    contador = 0
    
    for i in range(len(nombre)):
        for j in range(len(vocales)):
            if nombre[i] == vocales[j]:
                contador += 1
    return contador
    
    

def invertir_nombre(nombre : str) -> str:
    """Invierte el nombre dado

    Args:
        nombre (str): El nombre a invertir

    Returns:
        str: Devuelve el nombre invertido
    """
    
    invertido = ""
    for i in range(len(nombre)-1, -1, -1):
        invertido += nombre[i]
    
    return invertido


def ordenar_promedios(lista_promedios : list, lista_nombres : list, primer_parcial : list, segundo_parcial : list):
    """Ordena los elementos de una lista y sus listas paralelas, de mayor a menor, con el metodo de burbuja

    Args:
        lista_promedios (list): Lista con los promedios de los parciales
        lista_nombres (list): Lista con los nombres de los alumnos
        primer_parcial (list): Notas del primer parcial
        segundo_parcial (list): Notas del segundo parcial
    """
    for izq in range(len(lista_promedios) - 1):
        for der in range((izq +1), len(lista_promedios)):
            if lista_promedios[izq] < lista_promedios[der]:
                aux = lista_promedios[izq]
                lista_promedios[izq] = lista_promedios[der]
                lista_promedios[der] = aux
                aux = lista_nombres[izq]
                lista_nombres[izq] = lista_nombres[der]
                lista_nombres[der] = aux
                aux = primer_parcial[izq]
                primer_parcial[izq] = primer_parcial[der]
                primer_parcial[der] = aux
                aux = segundo_parcial[izq]
                segundo_parcial[izq] = segundo_parcial[der]
                segundo_parcial[der] = aux
