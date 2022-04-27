from cmath import inf
from dis import dis
from sys import argv 
ANTERIOR = 0
ULTIMA = 1

def obtener_distancias(grafo, destino):
    nodos = grafo.nodos
    distancia_ant = {}

    for n in nodos:
        if n == destino:
            distancia_ant[n] = 0
        else:
            distancia_ant[n] = inf

    distancia_nueva = {}
    return [distancia_ant, distancia_nueva]

def setear_hash_para(grafo):
    hash_aristas_min = {}
    for nodo in grafo:
        hash_aristas_min[nodo] = ""
    return hash_aristas_min

def no_es_ultima_iteración(i,n):
    return i != (n-1)

def costo_aun_no_asignado(costo_vert):
    return costo_vert == inf

def get_diferencias(distancia):
    diferentes = []
    for nodo in distancia[ANTERIOR]:
        if distancia[ANTERIOR][nodo] != distancia[ULTIMA][nodo]:
            diferentes.append(nodo)
    return diferentes

def encontrar_ciclo_en(nodos_cambiados, hash_aristas_min):

    # Toma el primer nodo de nodos_cambiados y lo organiza en formato de árbol con sus aristas.
    # Luego, recorre de forma postorder recursiva buscando que se repita el nodo inicial.
    # Si no lo encuentra, sigue con otro nodo de nodos_cambiados y lo usa como inicial.
    for i in range(len(nodos_cambiados)):
        inicial = nodos_cambiados[i]
        res = []
        arista = hash_aristas_min[inicial]
        res += postorder_encontrar_inicial(arista, inicial, hash_aristas_min, [])
        if esta_vacio(res):
            continue
        return res
    return []

# Complejidad: O(n+m) ; n cantidad de nodos, m cantidad de aristas
# Tomamos las aristas de los nodos_cambiados como si fueran un árbol (no binario)
def postorder_encontrar_inicial(actual, inicial, aristas, visitados):
    if actual == inicial:
        return visitados + [actual]
    res = []

    # Este if elimina la posibilidad de ingresar en un ciclo no negativo y tener stack overflow
    if actual in visitados:
        return res
    visitados.append(actual)

    for n in aristas[actual]:
        obt = postorder_encontrar_inicial(n, inicial, aristas, visitados)
        res += obt

    if esta_vacio(res):
        visitados.pop()

    return res

def calcular_costo_para(ciclo_negativo, grafo, arista):
    costo = 0
    primer_nodo = ciclo_negativo[0]
    primero = primer_nodo
    for i in range(1, len(ciclo_negativo)+1):
        segundo = arista[primero]
        costo += grafo[segundo][primero]
        primero = segundo
    return costo

def esta_vacio(lista):
    return len(lista) == 0

def imprimir_resultado(ciclo_neg, costo):
    if esta_vacio(ciclo_neg):
        print("\nNo existen ciclos negativos en el grafo.\n")
    else:
        print(f"\nExiste al menos un ciclo negativo en el grafo: {imprimir_lista(ciclo_neg)} → costo: {costo}\n")

def imprimir_lista(ciclo):
    return (',').join(ciclo)