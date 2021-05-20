# Python program for implementation of Selection
# Sort
import sys, time, csv, random

# Traverse through all array elements
def selectionSort(my_list):
	for i in range(1, len(my_list)):
		
		# Find the minimum element in remaining
		# unsorted array
		min_idx = i
		for j in range(i+1, len(my_list)):
			if my_list[min_idx] > my_list[j]:
				min_idx = j
				
		# Swap the found minimum element with
		# the first element		
		my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
	return my_list

## Warunki testu
## c - liczność listy
c = 0
## krok zwiększający c
step = 1000
## Maksymalna wartość parametru c 
maxc = 15000
with open('selectionSort.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Poczatek'])

print('Losowe')
with open('selectionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)   
        thewriter.writerow(['Losowe'])
        thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):
    with open('selectionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        while c <= maxc:
            my_list = [random.randint(1, 1000000) for n in range(c)]
            ## Początek liczenia czasu
            a = time.time()
            selectionSort(my_list)
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
with open('selectionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Ponownie posortowany/rosnące'])
        thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):
    with open('selectionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        while c <= maxc:
            my_list = [random.randint(1, 100000) for n in range(c)]
            ## Początek liczenia czasu
            selectionSort(my_list)
            a = time.time()
            selectionSort(my_list)
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

with open('selectionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Malejace'])
        thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
        
print('Malejace')
for n in range(5):
    with open('selectionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        while c <= maxc:
            my_list = [random.randint(1, 100000) for n in range(c)]
            ## Początek liczenia czasu
            selectionSort(my_list)
            my_list = my_list[::-1]
            a = time.time()
            selectionSort(my_list)
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

with open('selectionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Stale'])
        thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
print('Stale')
for n in range(5):
    with open('selectionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        while c <= maxc:
            rand = random.randint(1, 100000)
            my_list = [ rand for n in range(c)]
            ## Początek liczenia czasu
            a = time.time()
            selectionSort(my_list)
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

with open('selectionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Rozklad V'])
        thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
print('Rozklad V')
for n in range(5):
    with open('selectionSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        while c <= maxc:
            my_list = [random.randint(1, 100000) for n in range(c)]
            selectionSort(my_list)
            my_list_left = my_list[1::2]
            my_list_right = my_list[0::2]
            my_list = my_list_left[::-1] + my_list_right
            ## Początek liczenia czasu
            a = time.time()
            selectionSort(my_list)
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

    