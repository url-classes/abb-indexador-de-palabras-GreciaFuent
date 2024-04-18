from binary_search_tree import BinarySearchTree
search_tree = BinarySearchTree()


def crear_diccionario(palabra, ubicacion, repeticion):
    palabra = {"palabra": palabra,
               "ubicacion": [ubicacion],
               "repeticiones": [repeticion]}


def ingresar_en_palabra_repetida(ubicacion, repeticion, node):
    node["ubicacion"].append(ubicacion)
    node["repeticion"].append(repeticion)

    
def leer_archivo():
    # Abre el archivo en modo lectura
    with open('archivo6.txt', 'r') as archivo:
        # Itera sobre cada línea del archivo
        print("Leyendo el archivo:", archivo.name)
        for linea in archivo:
            # aqui estan
            palabras = linea.split(' ')
            print(palabras)


while True:
    menu = int(input('Ingrese la opcion que desea: \n'
                     '1) Buscar palabra\n2) Terminar el programa\n'
                     'Indique que opcion utilizara: '))
    if menu == 1:
        print('Buscar palabra')
        leer_archivo()
    elif menu == 2:
        print('Esperamos que te haya gustado el sistema')
        break
    else:
        raise ReferenceError('No existe esta opcion')



