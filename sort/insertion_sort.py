#insertion sort
input_string=input('Please enter a sequence of number:')
input_array=input_string.split()
sort_array=[]
for i in range(len(input_array)):
    sort_array.append(int(input_array[i]))
print(sort_array)
for j in range(1,len(sort_array)):
    sort_element=sort_array[j]
    i=j-1
    while i>0 and sort_array[i]>sort_element:
        sort_array[i+1]=sort_array[i]
        i=i-1
    sort_array[i+1]=sort_element
print(sort_array)
