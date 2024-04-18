from binary_search_tree import BinarySearchTree
search_tree = BinarySearchTree()


def crear_diccionario(palabra, ubicacion, repeticion):
    palabra = {"palabra": palabra,
               "ubicacion": [ubicacion],
               "repeticiones": [repeticion]}


def ingresar_en_palabra_repetida(ubicacion, repeticion, node):
    node["ubicacion"].append(ubicacion)
    node["repeticion"].append(repeticion)