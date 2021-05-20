# Python program for implementation of heap Sort
import random, time, csv
# To heapify subtree rooted at index i.
# n is size of heap
def heapify(my_list, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < n and my_list[i] < my_list[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < n and my_list[largest] < my_list[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		my_list[i],my_list[largest] = my_list[largest],my_list[i] # swap

		# Heapify the root.
		heapify(my_list, n, largest)

# The main function to sort an my_listay of given size
def heapSort(my_list):
	n = len(my_list)

	# Build a maxheap.
	# Since last parent will be at ((n//2)-1) we can start at that location.
	for i in range(n // 2 - 1, -1, -1):
		heapify(my_list, n, i)

	# One by one extract elements
	for i in range(n-1, 0, -1):
		my_list[i], my_list[0] = my_list[0], my_list[i] # swap
		heapify(my_list, i, 0)

# Driver code to test above



# This code is contributed by Mohit Kumra
## Warunki testu
## c - liczność listy
c = 0
## krok zwiększający c
step = 4000
## Maksymalna wartość parametru c 
maxc = 60000
print('Losowe')
with open('heapSort.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Poczatek'])
        thewriter.writerow(['Losowe'])
        thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):
    with open('heapSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        while c <= maxc:
            my_list = [random.randint(1, 1000000) for n in range(c)]
            ## Początek liczenia czasu
            a = time.time()
            heapSort(my_list)
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
with open('heapSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Ponownie posortowany/rosnące'])
        thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):
    with open('heapSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        while c <= maxc:
            my_list = [random.randint(1, 100000) for n in range(c)]
            ## Początek liczenia czasu
            heapSort(my_list)
            a = time.time()
            heapSort(my_list)
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
with open('heapSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Malejace'])
        thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):
    with open('heapSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        while c <= maxc:
            my_list = [random.randint(1, 100000) for n in range(c)]
            ## Początek liczenia czasu
            heapSort(my_list)
            my_list = my_list[::-1]
            a = time.time()
            heapSort(my_list)
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
with open('heapSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Stale'])
        thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):
    with open('heapSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        while c <= maxc:
            rand = random.randint(1, 100000)
            my_list = [ rand for n in range(c)]
            ## Początek liczenia czasu
            a = time.time()
            heapSort(my_list)
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
with open('heapSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Rozklad V'])
        thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):
    with open('heapSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        while c <= maxc:
            my_list = [random.randint(1, 100000) for n in range(c)]
            heapSort(my_list)
            my_list_left = my_list[1::2]
            my_list_right = my_list[0::2]
            my_list = my_list_left[::-1] + my_list_right
            ## Początek liczenia czasu
            a = time.time()
            heapSort(my_list)
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

    