# import random 
import random, time, csv

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


## c - liczność listy
c = 0
## maxc - maksymalna wartość c
maxc = 15000
## step - krok zwiększający ilość elementów w c
step = 1000
# Tworzenie listy z niepowtarzającymi się elementami

print("| c\t"'|Tworzenie listy\t\t\t\t|Średnia|\t' + "|Wyszukiwanie elementów listy jeden po drugim \t|Średnia|\t" + "|Usuwanie listy jednokierunkowej\t|Średnia|")
with open('Linked_List.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Poczatek'])
        thewriter.writerow(["Wartosc kroku;"+
        'Tworzenie listy z niepowtarzajacymi sie elementami;'+5*";"+"Srednia;"
        "Wyszukiwanie elementów listy jeden po drugim;"+5*";"+";Srednia;" + 
        "Usuwanie listy jednokierunkowej;"+5*";"+";Srednia"])

while c <= maxc:
    a, b, d, e, h, g = [],[], [],[], [], []
    for n in range(5):
        my_list = [random.randint(1, 100000) for n in range(c)]
        ## Początek liczenia czasu,
        a.append(time.time())
        # Tworzenie listy jednokierunkowej z wylosowanych elementów
        for i in my_list:
            llist.add_between(Node(i))
        ## Koniec liczenia czasu
        b.append(time.time())
        # Wyszukiwanie elementów listy jeden po drugim w kolejności jak w tablicy my_list
        ## Początek liczenia czasu
        d.append(time.time())
        for i in my_list:
            llist.find(i)
        ## Koniec liczenia czasu
        e.append(time.time())
        # Usuwanie listy jednokierunkowej
        ## Początek liczenia czasu
        h.append(time.time())
        llist.delete_list()
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

    with open('Linked_List.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow([(str(c) + "; " + 
        czas_delta_1 + "; X;" + average_1 + "; X;"+ 
        czas_delta_2 + "; X;" + average_2 + "; X;"+ 
        czas_delta_3 + "; X;" + average_3 + "; X;")])
    c = c + step