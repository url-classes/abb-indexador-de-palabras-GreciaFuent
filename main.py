from binary_search_tree import BinarySearchTree
search_tree = BinarySearchTree()


def crear_diccionario(palabra, ubicacion, repeticion):
    palabra = {"palabra": palabra,
               "ubicacion": [ubicacion],
               "repeticion": [repeticion]}
    search_tree.insert(palabra)


def ingresar_en_palabra_repetida(ubicacion, repeticion, node):
    for ubi in node.data["ubicacion"]:
        if ubi == ubicacion:
            node.data["repeticion"][0] += 1
        else:
            node.data["ubicacion"].append(ubicacion)
            node.data["repeticion"].append(repeticion)


def leer_archivo():
    # Abre el archivo en modo lectura
    with open('text5.txt', 'r') as archivo:
        # Itera sobre cada línea del archivo
        print("Leyendo el archivo:", archivo.name)
        for a, linea in enumerate(archivo):
            # aqui estan
            palabras = linea.split(' ')
            for b in range(len(palabras)):
                x = search_tree.search(palabras[b])
                if x is None:
                    crear_diccionario(palabras[b], archivo.name, 1)
                    print(palabras)
                else:
                    ingresar_en_palabra_repetida(archivo.name, 1, x)



while True:
    menu = int(input('Ingrese la opcion que desea: \n'
                     '1) Buscar palabra\n2) Terminar el programa\n'
                     'Indique que opcion utilizara: '))
    if menu == 1:
        print('Buscar palabra')
        leer_archivo()
        print("root", search_tree.root.left.right)
    elif menu == 2:
        print('Esperamos que te haya gustado el sistema')
        break
    else:
        raise ReferenceError('No existe esta opcion')


