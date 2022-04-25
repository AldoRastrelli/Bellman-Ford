from re import A
from site import addusersitepackages
from tkinter import E

class Grafo:

    aristas = {}
    nodos = set()

    def print(self):
        print(f"Grafo. Aristas: {self.aristas}, nodos: {self.nodos}")
    
    def guardar_nodo(self,nodo):
        self.nodos.add(nodo)

    def guardar_arista(self,par_arista_peso, origen):
        dest = par_arista_peso[0]
        peso = par_arista_peso[1]

        self.guardar_nodo(origen)
        self.guardar_nodo(dest)

        if (not origen in self.aristas):
            self.aristas[origen] = {dest : peso}
        else:    
            self.aristas[origen][dest] = peso
