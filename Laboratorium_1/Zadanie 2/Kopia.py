from math import e
import random, time, csv

def pivot(my_list, start, end):
 
#initializing 
    wartosc = int(c/2)
    pivot = my_list[wartosc]
    low = start + 1
    high = end
 
 
    while True:
   
#moving high towards left
        while low <= high and my_list[high] >= pivot:
            high = high - 1
 
#moving low towards right 
        while low <= high and my_list[low] <= pivot:
            low = low + 1
 
#checking if low and high have crossed
        if low <= high:
 
#swapping values to rearrange
            my_list[low], my_list[high] = my_list[high], my_list[low]
          
        else:
#breaking out of the loop if low > high
            break
 
#swapping pivot with high so that pivot is at its right # #position 
    my_list[wartosc], my_list[high] = my_list[high], my_list[wartosc
    ]
 
#returning pivot position
    return high
 
 
def quick_sort(my_list, start, end):
    if start >= end:
        return
 
#call pivot 
    p = pivot(my_list, start, end)
#recursive call on left half
    quick_sort(my_list, start, p-1)
#recursive call on right half
    quick_sort(my_list, p+1, end)
 
 

## Warunki testu
## c - liczność listy
c = 0
## krok zwiększający c
step = 1000
## Maksymalna wartość parametru c 
maxc = 15000
with open('QuickSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Losowy'])
        thewriter.writerow(['Wartosc kroku','Czas wykonywania algorytmu'])
for n in range(5):
    with open('QuickSort.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        while c <= maxc:
            my_list = [random.randint(1, 100000) for n in range(c)]
            my_list.sort
            my_list = my_list[::-1]
            my_list_left = my_list[1::2]
            my_list_right = my_list[0::2]
            my_list = my_list_left + my_list_right[::-1]
            ## Początek liczenia czasu
            a = time.time()
            quick_sort(my_list, 0, (len(my_list)-1))
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