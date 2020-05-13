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
from ADT import list as lt
from ADT import graph as g
from ADT import map as map
from ADT import list as lt
from DataStructures import listiterator as it
from datetime import datetime
from DataStructures import dijkstra as dj
"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo y retorna el catalogo inicializado.
    """
    libgraph = g.newGraph(7235,compareByKey,directed=True)
    catalog = {'librariesGraph':libgraph}
    #rgraph = g.newGraph(5500,compareByKey)
    fgraph = g.newGraph(111353,compareByKey)
    #catalog['reviewGraph'] = rgraph
    catalog['flightGraph'] = fgraph
    return catalog

def addLibraryNode (catalog, row):
    """
    Adiciona un nodo para almacenar una biblioteca
    """
    if not g.containsVertex(catalog['librariesGraph'], row['ID_src']):
        g.insertVertex (catalog['librariesGraph'], row['ID_src'])
    if not g.containsVertex(catalog['librariesGraph'], row['ID_dst']):
        g.insertVertex (catalog['librariesGraph'], row['ID_dst'])

def addLibraryEdge  (catalog, row):
    """
    Adiciona un enlace entre bibliotecas
    """
    g.addEdge (catalog['librariesGraph'], row['ID_src'], row['ID_dst'], float(row['dist']))

def addFlightNode(catalog, row):
    """
    Adiciona un nodo para almacenar un vuelo. 
    """
    if not g.containsVertex(catalog['flightGraph'], row['VERTEX']):
        g.insertVertex (catalog['flightGraph'], row['VERTEX'])

def addFlightEdge (catalog, row):
    """
    Adiciona un enlace para conectar dos vuelos
    """
    if row['AIR_TIME'] != "" :
        air_time = float(row['AIR_TIME'])
    else:
        air_time = 0
    g.addEdge (catalog['flightGraph'], row['SOURCE'], row['DEST'], air_time)

def countNodesEdges (catalog):
    """
    Retorna la cantidad de nodos y enlaces del grafo de bibliotecas
    """
    nodes = g.numVertex(catalog['librariesGraph'])
    edges = g.numEdges(catalog['librariesGraph'])

    return nodes,edges

def getShortestPath (catalog, source, dst):
    """
    Retorna el camino de menor costo entre vertice origen y destino, si existe 
    """
    print("vertices: ",source,", ",dst)

    dijkstra= dj.newDijkstra(catalog['flightGraph'], source)

    Path= dj.pathTo(dijkstra, dst)
    # ejecutar Dijkstra desde source
    # obtener el camino hasta dst
    # retornar el camino
    return Path
    
# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element['key'] )  

def ComponentesConectados (grafo):
    dicc_vertices = {}
    contador_componentes = 1
    vertices = g.vertices(grafo)
    if len(vertices) == 0:
        return 0
    else:
        iterator = it.newIterator(vertices)
        vertice = it.next(iterator)
        dicc_vertices = contar_conectados(grafo, dicc_vertices, vertice)
        while  it.hasNext(iterator):
            vertice_siguiente = it.next(iterator)
            esta_visitado = dicc_vertices.get(vertice_siguiente)
            if esta_visitado != "visited":
                dicc_vertices[vertice_siguiente] = "visited"
                contador_componentes += 1
                dicc_vertices = contar_conectados(grafo, dicc_vertices, vertice_siguiente)
        return contador_componentes
        
def contar_conectados(grafo, dicc_vertices, vertice):
    adjacentes = g.adjacents(grafo, vertice)
    if adjacentes != None:
        iterator2 = it.newIterator(adjacentes)
        while  it.hasNext(iterator2):
            vertice_adj = it.next(iterator2)
            esta_visitado = dicc_vertices.get(vertice_adj)
            if esta_visitado != "visited":
                dicc_vertices[vertice_adj] = "visited"
                contar_conectados(grafo, dicc_vertices, vertice_adj)
    return dicc_vertices