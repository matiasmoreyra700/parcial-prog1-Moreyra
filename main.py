from procesamiento import*
from validaciones import*


#Contador para verificar el ingreso de datos
carga = 1
#Contador para imprimir una sola vez el menu
menu = 0
#Mensaje por si no se ingresaron los votos
MENSAJE_ERROR = "Primero debe cargar los datos"


while True:
    if menu == 0:
        #Muestra el menu
        print(f"\n===== NOTAFÁCIL =====\n\n1. Cargar alumnos\n2. Mostrar listado\n3. Mostrar estadísticas\n4. Ver ranking (ordenado)\n5. Buscar alumno\n6. Juegos con un nombre\n0. Salir")
        menu += 1
    #Elige una opcion
    opcion = input("\nIngrese una opcion: ")
    match opcion:
        case "1":
            #Carga los datos
            cantidad_alumnos = validar_cantidad_alumnos()
            lista_cantidad_alumnos = inicializar_lista(cantidad_alumnos)
            lista_nombres = cargar_nombres(lista_cantidad_alumnos)
            
            print("\nIngrese las notas del primer parcial:")
            lista_primer_parcial = cargar_notas(lista_cantidad_alumnos, lista_nombres)

            print("\nIngrese las notas del segundo parcial:")
            lista_segundo_parcial = cargar_notas(lista_cantidad_alumnos, lista_nombres)
            lista_promedios = calcular_promedios(lista_cantidad_alumnos, lista_primer_parcial, lista_segundo_parcial)
            carga += 1
        case "2":
            #Muestra el listado
            if carga >= 1:
                
                mostrar_estadisticas(lista_nombres, lista_primer_parcial, lista_segundo_parcial, lista_promedios)
                
            else:
                print(MENSAJE_ERROR)
        case "3":
            #Muestra las estadisticas
            if carga >= 1:
                promedio_general = calcular_promedio_general(lista_promedios, cantidad_alumnos)
                menor_promedio = encontrar_menor(lista_promedios)
                mayor_promedio = encontrar_mayor(lista_promedios)
                
                print(f"\nPromedio general del curso: {promedio_general}\nMejor promedio: {mayor_promedio}\nPeor promedio: {menor_promedio}")
                
                cantidad_alumnos_condicion(lista_promedios)
                
            else:
                print(MENSAJE_ERROR)
        case "4":
            #Muestra el ranking
            if carga >= 1 :
                
                ordenar_promedios(lista_promedios, lista_nombres, lista_primer_parcial, lista_segundo_parcial)
                
                print(f"\nRanking:")
                mostrar_estadisticas(lista_nombres, lista_primer_parcial, lista_segundo_parcial, lista_promedios)
            else:
                print(MENSAJE_ERROR)
        case "5":
            #Busca un alumno
            if carga >= 1:
                alumno = input("Buscar alumno: ")
                encontrado = buscar_alumno(lista_nombres, alumno)
                if encontrado == True:
                    mostrar_alumno(lista_nombres, lista_primer_parcial, lista_segundo_parcial, lista_promedios, alumno)
                else:
                    print("Alumno no encontrado")
                
                
            else:
                print(MENSAJE_ERROR)
                
        case "6":
            #Juegos con un nombre
            if carga >= 1:
                nombre = input("Ingrese un nombre: ")
                vocales = contar_vocales(nombre)
                nombre_invertido = invertir_nombre(nombre)
                
                print(f"\nNombre: {nombre}\nCantidad de vocales: {vocales}\nNombre invertido: {nombre_invertido}")
                
                
            else:
                print(MENSAJE_ERROR)
        case "0":
            #Sale del programa
            print("Saliendo...")
            break
        
        case _:
            #Mensaje en caso de error
            print("Ingrese una opcion adecuada")