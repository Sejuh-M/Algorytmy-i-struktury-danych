import random
my_list = [random.randint(1, 10000) for n in range(100)]
my_list.sort()

print(my_list)
print(sorted(my_list))
my_list = my_list[::-1]
my_list_left = my_list[1::2]
print(my_list_left)

my_list_right = my_list[0::2]
print(my_list_right)

my_list = my_list_left + my_list_right[::-1]
print(my_list)