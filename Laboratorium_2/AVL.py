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
    if not root:
        return
    in_order_print(root.l_child)
    print (root.data)
    in_order_print(root.r_child)

# Wypisanie drzewa od góry do dołu (na poziomie od lewej do prawej)
def pre_order_print(root):
    if not root:
        return        
    print (root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)  

# Usuwanie drzewa
def delete_recursively(node):
    if node.l_child is not None:
         delete_recursively(node.l_child)
         node.l_child = None
    if node.r_child is not None: 
        delete_recursively(node.r_child)
        node.r_child = None
    node = None

# Tworzenie listy AVL
def avl_list(lista1, lista2):
    mid = len(lista1)//2
    lista2.append(lista1[mid])
    if len(lista1[ : (mid)]) > 0:
        avl_list(lista1[ : (mid)], lista2)
    if len(lista1[(mid+1) : ]) > 0:
        avl_list(lista1[(mid+1) : ], lista2)

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


## c - liczność listy
c = 0
## maxc - maksymalna wartość c
maxc = 150000
## step - krok zwiększający ilość elementów w c
step = 2
# Tworzenie listy z niepowtarzającymi się elementami

print("| c\t|\t"'|BST|\t' + "|AVL|" )
with open('Wysokosc.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Poczatek'])
        thewriter.writerow(["Wartosc kroku,"+ 'BST,'+"AVL"])

while c <= maxc:
    if c == 0:
        my_list = [None]
    else:
        my_list = random.sample(range(1, 10000000), c)
    
    tree = Node(my_list[0])
    for i in range(1, len(my_list)):
        binary_insert(tree, Node(my_list[i]))
    # print(hight(tree))
    h_BST = hight(tree)
    # Lista do połowienia binarnego
    sorted_list = sorted(my_list)

    avl_lista = [] 
    avl_list(sorted_list, avl_lista)

    avl_tree = Node(avl_lista[0])
    for i in range(1, len(avl_lista)):   
        binary_insert(avl_tree, Node(avl_lista[i]))

    h_AVL = hight(avl_tree)
    # print(hight(avl_tree))
    if len(str(c)) == 1:
        print("|",str(c),"\t|\t|", str(h_BST), " |\t|", str(h_AVL)," |")
    elif len(str(c)) == 4:
        print("|",str(c),"\t|\t|", str(h_BST), "|\t|", str(h_AVL),"|")
    else:
        print("|",str(c),"|\t|", str(h_BST), "|\t|", str(h_AVL),"|")
    
    with open('Wysokosc.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(((c), (h_BST), (h_AVL)))
    if c == 0 or c == 2 or c == 4:
        c = c + step
    else:
        c = c + c//3






# ## c - liczność listy
# c = 100

# # Tworzenie listy z niepowtarzającymi się elementami
# my_list = random.sample(range(1, 1000000), c)
# #my_list = [10 , 7, 9, 12, 17, 4, 8, 11, 5, 16, 1, 15]
# # Tworzenie drzewa BST
# tree = Node(my_list[0])
# for i in range(1, len(my_list)):
#     binary_insert(tree, Node(my_list[i]))

# print(hight(tree))
# # Lista do połowienia binarnego
# sorted_list = sorted(my_list)

# avl_lista = [] 
# avl_list(sorted_list, avl_lista)

# avl_tree = Node(avl_lista[0])
# for i in range(1, len(avl_lista)):   
#     binary_insert(avl_tree, Node(avl_lista[i]))

# print(hight(avl_tree))
# # print ("pre order:")
# # pre_order_print(avl_tree)

# # Usuwanie drzewa BST
# delete_recursively(tree)
# tree = None

# delete_recursively(avl_tree)
# avl_tree = None

# # print ("in order:")
# # in_order_print(tree)
