
import numpy as np
from numpy.core.records import array
import random, csv
import time
from numpy.lib.function_base import insert

#pomocnicza fukcja czasu
def czas(b:list, a:list):
    result = []
    for n in range(len(a)):
        result.append('{:05.3f}'.format(b[n]-a[n]))
    return str(result).strip("[]").replace(",", ";").replace("'","")

#Funkcja budująca graf
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
        #print("macierz: \n", proper_array)
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

# def wczytaj():
#     counter = 0
#     with open('Euler.txt') as f:
#         for line in f:
#             counter += 1
#     #print(counter)
#     a = np.zeros(shape=(counter,counter), dtype=int)
#     #print(a)
#     i1 = 0
#     j1 = 0
#     with open('Euler.txt') as f:
#         for line in f:
#             #print("line", line)
#             i1 = 0
#             for n in line.strip().replace(" ", ""):
#                 #print("n",n)
#                 #print("i1",i1)
#                 a[j1][i1] = n
#                 i1 += 1
#             j1 += 1
#     print (a)
#     return a

#Liczba wierzchołków grafu
c = 10
den = 0.3
maxc = 80

step = 3
print("|Tworzenie macierzy\t" + "|Euler\t|\t" + "|Hamilton|")
with open('Grafy.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Poczatek'])
        thewriter.writerow(["Wartosc kroku;"+ "Euler;",";"+"Hamilton;"])

while c <= maxc:
    a, b, d, e = [],[], [],[]
    for n in range(5):
        start = 1
    
        if c == 0:
            created_matrix = [None]
        else:
            created_matrix = Graph(size= c, density=den)
        eulerCycle = []
        hamiltonCycle = [start-1]

    
        ## Początek liczenia czasu,
        a.append(time.time())
        # Tworzenie listy jednokierunkowej z wylosowanych elementów#Od którego wierzchołka zacząć szukanie

        #Wyszukiwanie cyklu Eulera
        EulerCycle(created_matrix, start-1, eulerCycle)
        eulerCycle.append(eulerCycle[0])
        #Zmiana numeracji wierzchołków (od 1)
        for i in range (len(eulerCycle)):
            eulerCycle[i] = eulerCycle[i]+1
        #print(eulerCycle)
        ## Koniec liczenia czasu
        b.append(time.time())

        # Przeszukiwanie drzewa BST
        ## Początek liczenia czasu
        d.append(time.time())
        while HamiltonCycle(created_matrix, start-1, hamiltonCycle):
            ()
        hamiltonCycle.append(hamiltonCycle[0])
        #Zmiana numeracji wierzchołków (od 1)
        for i in range (len(hamiltonCycle)):
            hamiltonCycle[i] = hamiltonCycle[i]+1
        #print(hamiltonCycle)
        e.append(time.time())

        ## Ozdobniki wydruku
    czas_delta_1 = czas(b,a)
    czas_delta_2 = czas(e,d)
    if len(czas_delta_1) >23 and len(str(c))<=4:
        print("|",c ,"\t|" ,czas_delta_1, "\t\t|", czas_delta_2, "\t\t|")
    else:
        print("|",c ,"|" , czas_delta_1, "\t|",czas_delta_2, "\t|")
    with open('Grafy.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow([(str(c) + "; " + czas_delta_1 + "; X;" + czas_delta_2 + "; X;" )])
    c = c + step

# graph_1_euler = Graph(n,0.7)
# graph_1_hamilton = Graph(n,0.7)



#Od którego wierzchołka zacząć szukanie
start = 1

#Wyszukiwanie cyklu Eulera
# eulerCycle = []
# for n in range(1,100,2):
#     created_matrix = Graph(size= n, density=0.3)
#     EulerCycle(created_matrix, start-1, eulerCycle)
#     eulerCycle.append(eulerCycle[0])
#     #Zmiana numeracji wierzchołków (od 1)
#     for i in range (len(eulerCycle)):
#         eulerCycle[i] = eulerCycle[i]+1
#     print(eulerCycle)

# #Wyszukiwanie cyklu Hamiltona
#     hamiltonCycle = [start-1]
#     while HamiltonCycle(created_matrix, start-1, hamiltonCycle):
#         ()
#     hamiltonCycle.append(hamiltonCycle[0])
#     #Zmiana numeracji wierzchołków (od 1)
#     for i in range (len(hamiltonCycle)):
#         hamiltonCycle[i] = hamiltonCycle[i]+1
#     print(hamiltonCycle)


#