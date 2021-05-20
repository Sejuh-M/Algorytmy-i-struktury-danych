import random, time, csv
def mergeSort(my_list):
    size = len(my_list)
    if size > 1:
        middle = size // 2
        left_arr = my_list[:middle]
        right_arr = my_list[middle:]
 
        mergeSort(left_arr)
        mergeSort(right_arr)
 
        p = 0
        q = 0
        r = 0
 
        left_size = len(left_arr)
        right_size = len(right_arr)
        while p < left_size and q < right_size:
            if left_arr[p] < right_arr[q]:
              my_list[r] = left_arr[p]
              p += 1
            else:
                my_list[r] = right_arr[q]
                q += 1
             
            r += 1
 
        
        while p < left_size:
            my_list[r] = left_arr[p]
            p += 1
            r += 1
 
        while q < right_size:
            my_list[r]=right_arr[q]
            q += 1
            r += 1
 
## Warunki testu
## c - liczność listy
c = 0
## krok zwiększający c
step = 4000
## Maksymalna wartość parametru c 
maxc = 60000
print('Losowe')
with open('mergeSort.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Losowe'])
    thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):    
    while c <= maxc:
        my_list = [random.randint(1, 100000) for n in range(c)]
        ## Początek liczenia czasu
        a = time.time()
        mergeSort(my_list)
        ## Koniec liczenia czasu
        b = time.time()
        ## Ozdobniki wydruku
        if c == 0:
            print("|",c ,"\t\t|\t" ,b-a, "\t\t\t|")
        elif c < 10000:
            print("|",c ,"\t\t|\t" ,b-a, "\t|")
        else: 
            print("|",c ,"\t|\t" ,b-a, "\t|")
        with open('mergeSort.csv', 'a', newline='') as f:
            thewriter = csv.writer(f)
            thewriter.writerow([c, b-a])
        c = c + step
## c - liczność listy
    c = 0

print('Ponownie posortowany/rosnące')
with open('mergeSort.csv', 'a', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Ponownie posortowany/rosnące'])
    thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):
    while c <= maxc:
        my_list = [random.randint(1, 1000000) for n in range(c)]
        ## Początek liczenia czasu
        mergeSort(my_list)
        a = time.time()
        mergeSort(my_list)
        ## Koniec liczenia czasu
        b = time.time()
        ## Ozdobniki wydruku
        if c == 0:
            print("|",c ,"\t\t|\t" ,b-a, "\t\t\t|")
        elif c < 10000:
            print("|",c ,"\t\t|\t" ,b-a, "\t|")
        else: 
            print("|",c ,"\t|\t" ,b-a, "\t|")

        with open('mergeSort.csv', 'a', newline='') as f:
            thewriter = csv.writer(f)
            thewriter.writerow([c, b-a])
        c = c + step
## c - liczność listy
    c = 0

print('Malejace')
with open('mergeSort.csv', 'a', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Malejace'])
    thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):
    while c <= maxc:
        my_list = [random.randint(1, 100000) for n in range(c)]
        ## Początek liczenia czasu
        mergeSort(my_list)
        my_list = my_list[::-1]
        a = time.time()
        mergeSort(my_list)
        ## Koniec liczenia czasu
        b = time.time()
        ## Ozdobniki wydruku
        if c == 0:
            print("|",c ,"\t\t|\t" ,b-a, "\t\t\t|")
        elif c < 10000:
            print("|",c ,"\t\t|\t" ,b-a, "\t|")
        else: 
            print("|",c ,"\t|\t" ,b-a, "\t|")

        with open('mergeSort.csv', 'a', newline='') as f:
            thewriter = csv.writer(f)
            thewriter.writerow([c, b-a])
        c = c + step
## c - liczność listy
    c = 0   

print('Stale')
with open('mergeSort.csv', 'a', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Stale'])
    thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):
    while c <= maxc:
        rand = random.randint(1, 100000)
        my_list = [rand for n in range(c)]
        ## Początek liczenia czasu
        a = time.time()
        mergeSort(my_list)
        ## Koniec liczenia czasu
        b = time.time()
        ## Ozdobniki wydruku
        if c == 0:
            print("|",c ,"\t\t|\t" ,b-a, "\t\t\t|")
        elif c < 10000:
            print("|",c ,"\t\t|\t" ,b-a, "\t|")
        else: 
            print("|",c ,"\t|\t" ,b-a, "\t|")

        with open('mergeSort.csv', 'a', newline='') as f:
            thewriter = csv.writer(f)
            thewriter.writerow([c, b-a])
        c = c + step
## c - liczność listy
    c = 0

print('Rozklad V')
with open('mergeSort.csv', 'a', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Rozklad V'])
    thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):
    while c <= maxc:
        my_list = [random.randint(1, 100000) for n in range(c)]
        mergeSort(my_list)
        my_list_left = my_list[1::2]
        my_list_right = my_list[0::2]
        my_list = my_list_left[::-1] + my_list_right
        ## Początek liczenia czasu
        a = time.time()
        mergeSort(my_list)
        ## Koniec liczenia czasu
        b = time.time()
        ## Ozdobniki wydruku
        if c == 0:
            print("|",c ,"\t\t|\t" ,b-a, "\t\t\t|")
        elif c < 10000:
            print("|",c ,"\t\t|\t" ,b-a, "\t|")
        else: 
            print("|",c ,"\t|\t" ,b-a, "\t|")

        with open('mergeSort.csv', 'a', newline='') as f:
            thewriter = csv.writer(f)
            thewriter.writerow([c, b-a])
        c = c + step
        ## c - liczność listy
    c = 0