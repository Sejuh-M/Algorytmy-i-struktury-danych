## Insertion Sort In Python
## Performance Complexity = O(n^2)
## Space Complexity = O(n)
import random, time, csv

def insertionSort(my_list):
    ## for every element in our array
    for index in range(1, len(my_list)):
        current = my_list[index]
        position = index

        while position > 0 and my_list[position-1] > current:
            my_list[position] = my_list[position-1]
            position -= 1

        my_list[position] = current

    return my_list
## Warunki testu
## c - liczność listy
c = 0
## krok zwiększający c
step = 1000
## Maksymalna wartość parametru c 
maxc = 15000

with open('insertionSort.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Poczatek'])

print('Losowe')
with open('insertionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)   
        thewriter.writerow(['Losowe'])
        thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):
    with open('insertionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        while c <= maxc:
            my_list = [random.randint(1, 1000000) for n in range(c)]
            ## Początek liczenia czasu
            a = time.time()
            insertionSort(my_list)
            ## Koniec liczenia czasu
            b = time.time()
            ## Ozdobniki wydruku
            if c == 0:
                print("|",c ,"\t\t|\t" ,b-a, "\t\t\t|")
            elif c < 10000:
                print("|",c ,"\t\t|\t" ,b-a, "\t|")
            else: 
                print("|",c ,"\t|\t" ,b-a, "\t|")

            thewriter.writerow([c, b-a])
            c = c + step
    ## c - liczność listy
    c = 0

print('Ponownie posortowany/rosnące')
with open('insertionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Ponownie posortowany/rosnące'])
        thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):
    with open('insertionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        while c <= maxc:
            my_list = [random.randint(1, 100000) for n in range(c)]
            ## Początek liczenia czasu
            insertionSort(my_list)
            a = time.time()
            insertionSort(my_list)
            ## Koniec liczenia czasu
            b = time.time()
            ## Ozdobniki wydruku
            if c == 0:
                print("|",c ,"\t\t|\t" ,b-a, "\t\t\t|")
            elif c < 10000:
                print("|",c ,"\t\t|\t" ,b-a, "\t|")
            else: 
                print("|",c ,"\t|\t" ,b-a, "\t|")

            thewriter.writerow([c, b-a])
            c = c + step
    ## c - liczność listy
    c = 0

print('Malejace')
with open('insertionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Malejace'])
        thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):
    with open('insertionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        while c <= maxc:
            my_list = [random.randint(1, 100000) for n in range(c)]
            ## Początek liczenia czasu
            insertionSort(my_list)
            my_list = my_list[::-1]
            a = time.time()
            insertionSort(my_list)
            ## Koniec liczenia czasu
            b = time.time()
            ## Ozdobniki wydruku
            if c == 0:
                print("|",c ,"\t\t|\t" ,b-a, "\t\t\t|")
            elif c < 10000:
                print("|",c ,"\t\t|\t" ,b-a, "\t|")
            else: 
                print("|",c ,"\t|\t" ,b-a, "\t|")

            thewriter.writerow([c, b-a])
            c = c + step
    ## c - liczność listy
    c = 0

print('Stale')
with open('insertionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Stale'])
        thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):
    with open('insertionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        while c <= maxc:
            rand = random.randint(1, 100000)
            my_list = [ rand for n in range(c)]
            ## Początek liczenia czasu
            a = time.time()
            insertionSort(my_list)
            ## Koniec liczenia czasu
            b = time.time()
            ## Ozdobniki wydruku
            if c == 0:
                print("|",c ,"\t\t|\t" ,b-a, "\t\t\t|")
            elif c < 10000:
                print("|",c ,"\t\t|\t" ,b-a, "\t|")
            else: 
                print("|",c ,"\t|\t" ,b-a, "\t|")

            thewriter.writerow([c, b-a])
            c = c + step
    ## c - liczność listy
    c = 0

print('Rozklad V')
with open('insertionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Rozklad V'])
        thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):
    with open('insertionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        while c <= maxc:
            my_list = [random.randint(1, 100000) for n in range(c)]
            insertionSort(my_list)
            my_list_left = my_list[1::2]
            my_list_right = my_list[0::2]
            my_list = my_list_left[::-1] + my_list_right
            ## Początek liczenia czasu
            a = time.time()
            insertionSort(my_list)
            ## Koniec liczenia czasu
            b = time.time()
            ## Ozdobniki wydruku
            if c == 0:
                print("|",c ,"\t\t|\t" ,b-a, "\t\t\t|")
            elif c < 10000:
                print("|",c ,"\t\t|\t" ,b-a, "\t|")
            else: 
                print("|",c ,"\t|\t" ,b-a, "\t|")

            thewriter.writerow([c, b-a])
            c = c + step
            ## c - liczność listy
    c = 0

    