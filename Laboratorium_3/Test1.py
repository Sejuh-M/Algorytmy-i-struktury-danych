import numpy as np
counter = 0
with open('Euler.txt') as f:
    for line in f:
        counter += 1
print(counter)
a = np.zeros(shape=(counter,counter), dtype=int)
print(a)
i1 = 0
j1 = 0
with open('Euler.txt') as f:
    for line in f:
        print("line", line)
        i1 = 0
        for n in line.strip().replace(" ", ""):
            print("n",n)
            print("i1",i1)
            a[j1][i1] = n
            i1 += 1
        j1 += 1
print(a)
