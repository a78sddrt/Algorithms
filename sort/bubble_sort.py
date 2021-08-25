#bubble_sort

def bubble_sort(sort_array):
    for i in range(len(sort_array)):
        for j in range(len(sort_array)-1,i,-1):
            if sort_array[j] < sort_array[j-1]:
                swap=sort_array[j]
                sort_array[j]=sort_array[j-1]
                sort_array[j-1]=swap

    return sort_array


input_string=input('Please enter a sequence of number:')
input_array=input_string.split()
sort_array=[]
for i in range(len(input_array)):
    sort_array.append(int(input_array[i]))

sort_array=bubble_sort(sort_array)
print(sort_array)
