#merge_sort

import math

#merge two arrays
def merge_two_array(array_1,array_2):
    merge_array=[]
    i=0
    j=0
    while i<len(array_1) and  j<len(array_2):
        if array_1[i]< array_2[j]:
            merge_array.append(array_1[i])
            i=i+1
        else:
            merge_array.append(array_2[j])
            j=j+1
    while i<len(array_1):
        merge_array.append(array_1[i])
        i=i+1
    while j<len(array_2):
        merge_array.append(array_2[j])
        j=j+1
         
    return merge_array

#applying merge sort
def merge_sort(sort_array):
    n=len(sort_array)
    if n<2:
        return sort_array
    array_1=merge_sort(sort_array[:math.floor(n/2)])
    array_2=merge_sort(sort_array[math.floor(n/2):])            
    return merge_two_array(array_1,array_2)     



input_string=input('Please enter a sequence of number:')
input_array=input_string.split()
sort_array=[]
for i in range(len(input_array)):
    sort_array.append(int(input_array[i]))

sort_array=merge_sort(sort_array)
print(sort_array)



    
    
