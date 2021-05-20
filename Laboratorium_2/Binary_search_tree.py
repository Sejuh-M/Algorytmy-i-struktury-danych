# import random 
import random, time, csv

# Klasa Node reprezentująca drzewo BST
class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

# Dodanie wartości
def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

# Wypisanie drzewa posortowanego
def in_order_print(root):
    drzewo_inorder = []
    if not root:
        return
    in_order_print(root.l_child)
    drzewo_inorder.append(root.data)
    in_order_print(root.r_child)

# Wypisanie drzewa od góry do dołu (na poziomie od lewej do prawej)
def pre_order_print(root):
    if not root:
        return        
    print (root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)  

# Wyszukiwanie elementu drzewa
def search_recursively(val, node):
    if node == None or node.data == val:
        return
    if val < node.data:
        return search_recursively(val, node.l_child)
    if val > node.data:
        return search_recursively(val, node.r_child)

def delete_recursively(node):
    if node.l_child is not None:
         delete_recursively(node.l_child)
         node.l_child = None
    if node.r_child is not None: 
        delete_recursively(node.r_child)
        node.r_child = None
    node = None
    
# Wysokość drzewa
def hight(root):
    if root is None:
        return 0 
    else:
        left_hight = hight(root.l_child)
        right_hight = hight(root.r_child)
        return 1 + max(left_hight, right_hight)


# MODUŁ DO WCZYTYWANIA LISTY Z PLIKU
# SPRAWDZENIE Z TXT STRONY
a = []
with open('readme.txt') as f:
    for line in f:
        a.append(int(line.strip()))


#pomocnicza fukcja czasu
def czas(b:list, a:list):
    result = []
    for n in range(len(a)):
        result.append('{:05.3f}'.format(b[n]-a[n]))
    return str(result).strip("[]").replace(",", ";").replace("'","")

#pomocnicza funckja sredniej
def average(b:list, a:list):
    temp = []
    for n in range(len(a)):
        temp.append(b[n]-a[n])
    result = ('{:05.3f}'.format(sum(temp)/len(temp)))
    return str(result).strip("[]").replace(",", ";").replace("'","")

# Wysokość drzewa
def hight(root):
    if root is None:
        return 0 
    else:
        left_hight = hight(root.l_child)
        right_hight = hight(root.r_child)
        return 1 + max(left_hight, right_hight)

## c - liczność listy
c = 0
## maxc - maksymalna wartość c
maxc = 15000
## step - krok zwiększający ilość elementów w c
step = 1000
# Tworzenie listy z niepowtarzającymi się elementami

print("| c\t"'|Tworzenie listy\t\t\t\t|Średnia|\t' + "|Wyszukiwanie elementów listy jeden po drugim \t|Średnia|\t" + "|Usuwanie listy jednokierunkowej\t|Średnia|")
with open('Binary_search_tree.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Poczatek'])
        thewriter.writerow(["Wartosc kroku;"+
        'Tworzenie listy z niepowtarzajacymi sie elementami;'+5*";"+"Srednia;"
        "Wyszukiwanie elementów listy jeden po drugim;"+5*";"+";Srednia;" + 
        "Usuwanie listy jednokierunkowej;"+5*";"+";Srednia"])

while c <= maxc:
    a, b, d, e, h, g = [],[], [],[], [], []
    for n in range(5):
        if c == 0:
            my_list = [None]
        else:
            my_list = [random.randint(1, 100000) for n in range(c)]

        tree = Node(my_list[0])
        ## Początek liczenia czasu,
        a.append(time.time())
        # Tworzenie listy jednokierunkowej z wylosowanych elementów
        tree = Node(my_list[0])
        for i in range(1, len(my_list)):
            binary_insert(tree, Node(my_list[i]))
        ## Koniec liczenia czasu
        b.append(time.time())

        # Przeszukiwanie drzewa BST
        ## Początek liczenia czasu
        d.append(time.time())
        # Przeszukiwanie drzewa BST
        for i in my_list:   
            search_recursively(i, tree)
        ## Koniec liczenia czasu
        e.append(time.time())

        # Usuwanie drzewa BST
        ## Początek liczenia czasu
        h.append(time.time())
        delete_recursively(tree)
        tree = None
        ## Koniec liczenia czasu
        g.append(time.time())
        ## Ozdobniki wydruku
    czas_delta_1 = czas(b,a)
    czas_delta_2 = czas(e,d)
    czas_delta_3 = czas(g,h)
    average_1 = average(b,a)
    average_2 = average(e,d)
    average_3 = average(g,h)
    if len(czas_delta_1) >23 and len(str(c))<=4:
        print("|",c ,"\t|" ,
        czas_delta_1, "\t\t|", average_1, "|\t|",
        czas_delta_2, "\t\t|", average_2, "|\t|", 
        czas_delta_3, "\t|", average_3, "|\t")
    else:
        print("|",c ,"|" ,
        czas_delta_1, "\t|", average_1, "|\t|",
        czas_delta_2, "\t|", average_2, "|\t|", 
        czas_delta_3, "\t|", average_3, "|\t")

    with open('Binary_search_tree.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow([(str(c) + "; " + 
        czas_delta_1 + "; X;" + average_1 + "; X;"+ 
        czas_delta_2 + "; X;" + average_2 + "; X;"+ 
        czas_delta_3 + "; X;" + average_3 + "; X;")])
    c = c + step




## c - liczność listy
# c = 10

# # Tworzenie listy z niepowtarzającymi się elementami
# #my_list = random.sample(range(1, 1000000), c)
# my_list = [10 , 7, 9, 12, 17, 4, 8, 11, 5, 16, 1, 15]
# # Tworzenie drzewa BST
# tree = Node(my_list[0])
# for i in range(1, len(my_list)):
#     binary_insert(tree, Node(my_list[i]))
#     #print(tree)

# # Przeszukiwanie drzewa BST
# for i in my_list:
#     search_recursively(i, tree)

# # Usuwanie drzewa BST
# delete_recursively(tree)
# tree = None

# # Print inoder traversal of the BST

# print ("in order:")
# in_order_print(tree)

# print ("pre order")
# pre_order_print(tree)