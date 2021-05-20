import numpy as np
from numpy.core.records import array
import random

from numpy.lib.function_base import insert

#Funkcja budująca graf
#Kod kradziony od A. Michowski - Translacja na python z dodatkami
def Graph(size: int, density: float):
        
    size_array = (size, size)
    array_of_zeros = np.zeros(size_array, dtype=int)
    #print("array_of_zeros\n", array_of_zeros)

    #maksymalna ilość możliwych krawędzi
    Edges = size * (size - 1) / 2
    #print("Edges", Edges)
    
    #Wymagana ilość krawędzi uwzględniająca density
    reqEdges = Edges * density
    #print("reqEdges", reqEdges)

    #niby prosty sposob na graf spójny
    reqEdges = reqEdges - size
    
    proper_array = array_of_zeros
    
    #print(proper_array)
    def insert_egde(x, y):
        proper_array[x][y] = 1
        proper_array[y][x] = 1

    for i in range(size):
        insert_egde(i, ((i + 1) % size))
    #print("spojny: \n", proper_array)
    i = 0
    while reqEdges//4 > i:
        while True:
            x1 = random.randrange(size)
            x2 = random.randrange(size)
            y1 = random.randrange(size)
            y2 = random.randrange(size)
            #print(x1,y1,x2,y2)
            if x1 == y1 or x2 == y2:
                continue
            if x1 == y2 or x2 == y1:
                continue
            if x1 == x2 or y1 == y2:
                continue
            if proper_array[x1][y1] == 1 or proper_array[x2][y2] == 1 or proper_array[x2][y1] == 1 or proper_array[x1][y2] == 1 :
                continue
            break
        insert_egde(x1, y1)
        insert_egde(x1, y2)
        insert_egde(x2, y1)
        insert_egde(x2, y2)
        i += 1
        print("macierz: \n", proper_array)
    return proper_array

def EulerCycle (Graph, start: int, cycle: list):
    
    for i in range (int(Graph.size**0.5)):   
        while Graph[start][i]:
            Graph[start][i] = 0
            Graph[i][start] = 0
            EulerCycle(Graph, i, cycle)
            cycle.append(i)

def HamiltonCycle (Graph, start: int, cycle: list):
    
    if len(cycle) < int(Graph.size**0.5):
        for i in range (int(Graph.size**0.5)):   
            while Graph[start][i] and i not in cycle:
                cycle.append(i)
                HamiltonCycle(Graph, i, cycle)
    else:
        if Graph[cycle[-1]][cycle[0]]:
            return False
        return True

def wczytaj():
    counter = 0
    with open('Euler.txt') as f:
        for line in f:
            counter += 1
    #print(counter)
    a = np.zeros(shape=(counter,counter), dtype=int)
    #print(a)
    i1 = 0
    j1 = 0
    with open('Euler.txt') as f:
        for line in f:
            #print("line", line)
            i1 = 0
            for n in line.strip().replace(" ", ""):
                #print("n",n)
                #print("i1",i1)
                a[j1][i1] = n
                i1 += 1
            j1 += 1
    print (a)
    return a

#Liczba wierzchołków grafu
n = 6

# graph_1_euler = Graph(n,0.7)
# graph_1_hamilton = Graph(n,0.7)

#Od którego wierzchołka zacząć szukanie
start = 1

#Wyszukiwanie cyklu Eulera
eulerCycle = []
EulerCycle(wczytaj(), start-1, eulerCycle)
eulerCycle.append(eulerCycle[0])
#Zmiana numeracji wierzchołków (od 1)
for i in range (len(eulerCycle)):
    eulerCycle[i] = eulerCycle[i]+1
print(eulerCycle)

#Wyszukiwanie cyklu Hamiltona
hamiltonCycle = [start-1]
while HamiltonCycle(wczytaj(), start-1, hamiltonCycle):
    ()
hamiltonCycle.append(hamiltonCycle[0])
#Zmiana numeracji wierzchołków (od 1)
for i in range (len(hamiltonCycle)):
    hamiltonCycle[i] = hamiltonCycle[i]+1
print(hamiltonCycle)

# #kod Kradziony od Patryk Szkudlarek
# def hamilton(self, vertex, V):
#     V.append(vertex)
#     for x in self.graph[vertex]:
#         if x not in V:
#             self.hamilton(x, V)
#     if all([y in V for y in self.graph.keys()]) and V[0] in self.graph[V[-1]]:
#         return
#     else:
#         V.remove(vertex)