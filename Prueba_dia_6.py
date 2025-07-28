from pathlib import Path
import os
from os import system
import time

ruta = (Path.home() / "Recetas")

#if not ruta.exists():
#    os.makedirs(ruta)

def contar_archivos():

    #contador = len(list(ruta.rglob('*')))
    contador = sum(1 for item in ruta.rglob('*') if item.is_file())
    return contador

def bienvenida():
    print("Bienvenido a nuestro gran RECETARIO")
    print("La ruta de acceso a las recetas es:" + str(ruta))
    print(f"En este momento hay {contar_archivos()} recetas")

def mostrar_menu():
    print("======Menú princial======")
    print("1. Leer receta")
    print("2. Crear receta")
    print("3. Crear categoría")
    print("4. Eliminar receta")
    print("5. Eliminar categoría")
    print("6. Salir")

def leer_carpeta():
    print("Existen las siguientes categorías: ")
    n = 0 
    carpeta = []
    for i in ruta.iterdir():
        n= n + 1
        carpeta.append(i)
        print(f"{n}.{i.stem}")
        
def opcion_leer_receta():
    
    categoria = input("Seleccione una de las categorías: ")
    categorianp = categoria.title()
    eleccion_carpeta = Path.home() / "Recetas" / categorianp
    os.system("clear")
    print(f"En el directorio {categorianp} hay los siguientes archivos: ")
    
    
    leer = [i for i in eleccion_carpeta.iterdir()]
    print("Archivos encontrados")
    
    for n, i in enumerate(leer):
        print(f"{n + 1}.{i.stem}")
        
    opcion_receta = input(f"¿Que receta quieres leer? (1 al {len(leer)}): " )
    ver= int(opcion_receta) - 1
    contenido = open(leer[ver], 'r')
    print(contenido.read())
    time.sleep(2)
    input("\nPresiona Enter para volver al menú...")
    os.system("clear")
    
def crear_receta():
    categoria = input("Seleccione una de las categorías: ")
    categorianp = categoria.title()
    eleccion_carpeta = Path.home() / "Recetas" / categorianp
    os.system("clear")

    #ingresando los datos del nuevo archivo
    nombre_receta = input("Ingrese en nombre de la nueva receta \n")
    contenido_receta = input("Ingrese su contenido \n")
    
    with open(eleccion_carpeta / (nombre_receta + ".txt"), 'w') as f:
        f.write(contenido_receta)
    
    time.sleep(2)
    input("\n----Receta creada----\nPresiona Enter para volver al menú...")
    os.system("clear")
    
    
def crear_categoria():

    os.system("clear")
    Nuevo_nombre_catego = input("Favor ingresa el nuevo nombre de la categorìa a crear: ")
    carpeta = Path(ruta / Nuevo_nombre_catego).mkdir()
    
    print(f"Categorìa creada {carpeta}")
    time.sleep(2)
    return carpeta
    
    
    print("Hola")
    
def check_ruta():

    if not ruta.exists():
        print(f"La carpeta {ruta} no existe")
        exit()
    else:
        print(f"Analizando la carpeta {ruta}")
        
        
        
 



def nueva_categoria(opcion):
    print("Hola")
"""3
def eliminar_receta(opcion):

def eliminar_categoria(opcion):  
"""       
opcion = 0

while opcion != '6':
    bienvenida()
    mostrar_menu()
    opcion = input("====¿Qué opción quieres?==== :  ")
    os.system('clear')
    match opcion:
    
        case "1":
            check_ruta()
            os.system("clear")
            leer_carpeta()
            opcion_leer_receta()
        
        case "2":
            check_ruta()
            os.system("clear")
            leer_carpeta()
            crear_receta()
        
        case "3":
            check_ruta()
            os.system("clear")
            leer_carpeta()
            crear_categoria()
            

"""        
    elif opcion == '23':
        
        
   elif opcion == '3':   
        
    
    elif opcion == '4':
        
        
    elif opcion == '5': 
        
        
        
    elif opcion == '6':
        print("Cerrando el programa)
        
        
    else:
        print("\nOpción no válida. Por favor, intenta de nuevo.")
        
    time.sleep(2)
os.system("clear")

"""
os.system("clear")
time.sleep(1)
print("---Cerrando el programa---")
print("1")   
time.sleep(1)
print("2")   
time.sleep(1)
print("3")   
