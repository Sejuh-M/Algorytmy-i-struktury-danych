# Python program for implementation of heap Sort
import random, time, csv
from typing import Counter
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
def czas(b:list, a:list):
    result = []
    for n in range(len(a)):
        result.append('{:05.3f}'.format((b[n]-a[n])))
    return result

## c - liczność listy
c = 10000
## krok zwiększający c
step = 10000
## Maksymalna wartość parametru c 
maxc = 100000
print('Losowe')
with open('multilinia.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Poczatek'])
        thewriter.writerow(['Losowe'])
        thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])

a, b = [0.0 for x in range(5)], [0.0 for x in range(5)]
while c <= maxc:

    czas_delta = str((czas(b,a))).strip('[]').replace(",",";").replace(".",",").replace('\'','')
    

    if len(czas_delta) <= 23 and len(str(c))<=4:
        print("|",c ,"\t|" ,czas_delta.replace(';','  ;'), "\t|")
    elif len(czas_delta) >23 and len(str(c))<=4:
        print("|",c ,"\t|" ,czas_delta, "\t|")
    else:
        print("|",c ,"|" ,czas_delta, "\t|")
    with open('multilinia.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow([str(c) + "; " + czas_delta],)
    a, b = [], []
    for n in range(5):
        my_list = [random.randint(1, 1000000) for n in range(c)]
        print(len(my_list))
        ## Początek liczenia czasu,
        a.append(time.time())
        heapSort(my_list)
        ## Koniec liczenia czasu
        b.append(time.time())
        ## Ozdobniki wydruku
    #print(len(str(c)))
    

    c = c + step
## c - liczność listy
c = 0

