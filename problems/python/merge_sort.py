from typing import List

    

# 1. Find the middle, take the length of the list and div by two, round downwards I guess?
# 2. Recurse on the split, i.e., recursively call merge_sort with left and right
# 3. When the length of the list is 1, that is, we have recursed down to a single element then we start returning
# 4. As we return we shall now do a basic sort on the lists
# 5. Finally return the sorted list
def merge_sort(list: List[int]):

    if len(list) <= 1:
        return list
    
    pivot = len(list) // 2

    left = merge_sort(list[0:pivot])
    right = merge_sort(list[pivot:])

    i = 0
    j = 0

    sorted_arr = []

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            sorted_arr.append(right[j])
            j += 1
        else:
            sorted_arr.append(left[i])
            i += 1
        
    if i < len(left):
        sorted_arr += left[i:]
    elif j < len(right):
        sorted_arr += right[j:]

    return sorted_arr


print(merge_sort([2,3,4,6,1,7,5,13,15,200,3,1,5,7,8,2,3,4,5,2,6,78,89,9,3,4,5,3,4,5,2,1]))



        

    
    
    
    # split list

# 1 2 3 4 5, 5 elements // 2  == 2.5 rounded down = 2

# 1 2 | 3 4 5 
#   /         \  
# 1 2         3 | 4 5
#   /              \
# 1 | 2       3   4 |5
#                 4   5