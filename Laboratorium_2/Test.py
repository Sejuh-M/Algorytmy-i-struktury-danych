# import random 
import random, time

# Klasa Node posiadająca wartość oraz wskaźnik
class Node:
    # Tworzenie nowego elementu klasy Node z daną wartością wskazującego na None
    def __init__(self, data):
        self.data = data
        self.next = None

    # Wyświetlenie wartości elementu
    def __repr__(self):
        return self.data


# Klasa LinkedList
class LinkedList:
    # Stworzenie pustej listy wskazującej na None
    def __init__(self):
        self.head = None

    # Wyświetlanie listy
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    # Przejście przez listę
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # Dodawanie elementu na początku listy
    def add_first(self, node):
        node.next = self.head
        self.head = node

    # Dodawanie elementu pomiędzy dwa, gdzie pierwszy jest mniejszy, a drugi jest większy
    def add_between(self, node):
        if self.head is None:
            self.add_first(node)
        elif int(node.data) < int(self.head.data):
            self.add_first(node)
        else:
            temp = node
            prev = self.head
            while prev.next is not None and int(node.data) > int(prev.next.data):
                prev = prev.next

            node.next = prev.next
            prev.next = temp
    
    # Usuwanie pierwszego elementu listy
    def remove_first(self):
        self.head = self.head.next

    # Usuwanie listy
    def delete_list(self):
        while self.head is not None:
            self.remove_first()

    # Znajdowanie elementu w liście jednokierunkowej
    def find(self, value):
        curr = self.head
        while curr is not None:
            if curr.data == value:
                return True
            
            curr = curr.next
        
        return False
            

print("\nStarting")

llist = LinkedList()

## c - liczność listy
c = 100

# Tworzenie listy z niepowtarzającymi się elementami
my_list = random.sample(range(1, 1000000), c)
"""print(my_list)"""

# Tworzenie listy jednokierunkowej z wylosowanych elementów
## Początek liczenia czasu
a = time.time()

for i in my_list:
    llist.add_between(Node(i))

## Koniec liczenia czasu
b = time.time()
print(b-a)

"""print(llist)"""

# Wyszukiwanie elementów listy jeden po drugim w kolejności jak w tablicy my_list
## Początek liczenia czasu
a = time.time()

for i in my_list:
    llist.find(i)

## Koniec liczenia czasu
b = time.time()
print(b-a)


# Usuwanie listy jednokierunkowej
## Początek liczenia czasu
a = time.time()

llist.delete_list()
"""print(llist)"""

## Koniec liczenia czasu
b = time.time()
print(b-a)