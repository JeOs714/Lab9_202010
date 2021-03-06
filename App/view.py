"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller 
import csv
from ADT import list as lt
from ADT import stack as stk
from ADT import orderedmap as map
from DataStructures import listiterator as it

import sys


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido al Laboratorio 9")
    print("1- Cargar información")
    print("2- Contar nodos y enlances cargados ")
    print("3- Contar componentes conectados")
    print("4- Obtener el camino de menor costo entre dos vértices usando Dijkstra (origen destino)")
    print("0- Salir")


def initCatalog ():
    """
    Inicializa el catalogo
    """
    return controller.initCatalog()


def loadData (catalog):
    """
    Carga las bibliotecas en la estructura de datos
    """
    controller.loadData(catalog)


"""
Menu principal 
""" 
def main():
    datos_cargados = False
    while True: 
        printMenu()
        inputs =input("Seleccione una opción para continuar\n")
        if int(inputs[0])==1: # 1- Cargar información
            if not datos_cargados:
                print("Cargando información de los archivos ....")
                catalog = initCatalog ()
                loadData (catalog)
                datos_cargados = True
            else:
                print("Los datos ya han sido cargados previamente.")
        elif int(inputs[0])==2: # 2- Contar nodos y enlances cargados
            if datos_cargados:
                verticesNum, edgesNum = controller.countNodesEdges(catalog) 
                print("El grafo tiene: ", verticesNum," nodos y", edgesNum," enlaces")
            else:
                print("No se han cargado los datos previamente. Carguelos e intente de nuevo.")

        elif int(inputs[0])==3: # 3- Contar componentes conectados
            if datos_cargados:
                Num_comp_conectados = controller.ComponentesConectados(catalog['flightGraph'])
                print("El grafo tiene: ", Num_comp_conectados," componentes conectados ó Clusters.")
            else:
                print("No se han cargado los datos previamente. Carguelos e intente de nuevo.")

        elif int(inputs[0])==4: # 4- Obtener el camino de menor costo entre dos vértices usando Dijkstra (origen destino)
            if datos_cargados:
                vertices =input("Ingrese el vertice origen y destino\n")
                try:
                    path = controller.getShortestPath(catalog,vertices)
                    print("El camino de menor costo entre los vertices es:")
                    totalDist = 0
                    while not stk.isEmpty (path): 
                        step = stk.pop(path)
                        totalDist += step['weight']
                        print (step['vertexA'] + "-->" + step['vertexB'] + " costo: " + str(step['weight']))
                        print("Total: " + str (totalDist))
                except:
                    print("No existe un camino entre los dos vértices")
            else:
                print("No se han cargado los datos previamente. Carguelos e intente de nuevo.")

        else:
            sys.exit(0)
    sys.exit(0)

if __name__ == "__main__":
    #sys.setrecursionlimit(1100)
    main()