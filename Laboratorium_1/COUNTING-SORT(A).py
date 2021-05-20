import random, math, time
 
def basic_counting_sort(tlist, k):
    """ Counting sort algo. Modified existing list. Only for positive integer.
        Args:
            tlist: target list to sort
            k: max value assume known before hand
        Disadv:
            It only does for positive integer and unable to handle more complex sorting (sort by str, negative integer etc)
            It straight away retrieve all data from count_list using count_list index as its ordering.
            Do not have the additional step to modify count_list to capture the actual index in output.
    """
 
    # Create a count list and using the index to map to the integer in tlist.
    count_list = [0]*(k)
 
    # loop through tlist and increment if exists
    for n in tlist:
        count_list[n] = count_list[n] + 1
 
    # Sort in place, copy back into original list
    i=0

    for n in range(len(count_list)):
        while count_list[n] > 0:
            tlist[i] = n
            i+=1
            count_list[n] -= 1
    global b 
    b = time.time()
    
## Create random list for demo counting sort.
random.seed(0)
tgt_list = [random.randint(0,200000000) for n in range(1000000)]
#print("Unsorted List")
#print(tgt_list)

 
## Perform the counting sort.
print("\nSorted list using basic counting sort")
a = time.time()
basic_counting_sort(tgt_list, max(tgt_list)+1)

print("czas sorotowania:" ,b-a)