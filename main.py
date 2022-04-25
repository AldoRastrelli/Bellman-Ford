import os
import copy
from auxiliares import *
from grafo import Grafo

NOMBRE_ARCHIVO = 'test.txt'

def obtener_grafo_destino_de(archivo):
    lineas = [] 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    grafo = Grafo()
       
    with open(dir_path + '/' +archivo) as aristas:
        lineas = aristas.readlines()
        destino = lineas.pop(0).strip()
        for linea in lineas:
            try:
                origen, dest, peso = linea.strip().split(",")
                par_arista_peso = [str(dest), int(peso)]

                grafo.guardar_arista(par_arista_peso, origen)

            except (TypeError, ValueError):
                pass

    return grafo, destino

def encontrar_ciclos_negativos(grafo, destino):
    cant_nodos = len(grafo.nodos)
    hash_aristas = setear_hash_para(grafo.aristas)
    distancias = obtener_distancias(grafo,destino)

    for i in range(cant_nodos):
        if no_es_ultima_iteración(i,cant_nodos):
            iteracion = ANTERIOR
        else:
            iteracion = ULTIMA
            distancias[iteracion] = copy.copy(distancias[ANTERIOR])

        for v in grafo.nodos:
            costo_vert = distancias[iteracion][v]
            if costo_aun_no_asignado(costo_vert):
                continue

            for arista in grafo.aristas[v]:
                peso = grafo.aristas[v][arista]
                costo_min_anterior = distancias[iteracion][arista]
                costo_nuevo = costo_vert + peso

                if costo_min_anterior > costo_nuevo:
                    distancias[iteracion][arista] = costo_nuevo
                    hash_aristas[v].add(arista)

    nodos_cambiados = get_diferencias(distancias)

    if esta_vacio(nodos_cambiados):
        return [], None
    ciclo_negativo = encontrar_ciclo_en(nodos_cambiados, hash_aristas)
    costo = calcular_costo_para(ciclo_negativo, grafo.aristas)

    return ciclo_negativo, costo

def main():

    grafo, destino  = obtener_grafo_destino_de(NOMBRE_ARCHIVO)
    grafo.print()
    ciclo_neg, costo = encontrar_ciclos_negativos(grafo, destino)
    imprimir_resultado(ciclo_neg, costo)

main()