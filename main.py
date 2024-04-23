from binary_search_tree import BinarySearchTree
search_tree = BinarySearchTree()

verificacion_entro = False


def crear_diccionario(palabra, ubicacion, repeticion):
    palabra = {"palabra": palabra,
               "ubicacion": [ubicacion],
               "repeticion": [repeticion]}
    search_tree.insert(palabra)


def ingresar_en_palabra_repetida(ubicacion, repeticion, node):
    global verificacion_entro
    for i, ubi in enumerate(node.data["ubicacion"]):
        if ubi is ubicacion:
            node.data["repeticion"][i] += 1
            verificacion_entro = True

    if verificacion_entro is False:
        node.data["ubicacion"].append(ubicacion)
        node.data["repeticion"].append(repeticion)
    else:
        verificacion_entro = False


def leer_archivo(nombre_archivo):
    # Abre el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        # Itera sobre cada línea del archivo
        for a, linea in enumerate(archivo):
            # aqui estan
            palabras = linea.split(' ')
            for b in range(len(palabras)):
                x = search_tree.search(palabras[b])
                if x is None:
                    crear_diccionario(palabras[b], archivo.name, 1)
                    # Si desea ver las oraciones print(palabras) descomente el print
                else:
                    ingresar_en_palabra_repetida(archivo.name, 1, x)


leer_archivo("text1.txt")
leer_archivo("text2.txt")
leer_archivo("text3.txt")
leer_archivo("text4.txt")
leer_archivo("text5.txt")
leer_archivo("archivo6.txt")
leer_archivo("archivo7.txt")
leer_archivo("archivo8.txt")
leer_archivo("archivo9.txt")
leer_archivo("archivo10.txt")


while True:
    menu = int(input('Ingrese la opcion que desea: \n'
                     '1) Buscar palabra\n2) Terminar el programa\n'
                     'Indique que opcion utilizara: '))
    if menu == 1:
        print('Buscar palabra')
        palabra_buscar = input('Ingrese la palabra que desea buscar: ')
        print(palabra_buscar, search_tree.search(palabra_buscar))
    elif menu == 2:
        print('Esperamos que te haya gustado el sistema')
        break
    else:
        raise ReferenceError('No existe esta opcion')



