#selection sort

#read input
input_string=input('Please enter a sequence of number:')
input_array=input_string.split()
sort_array=[]
for i in range(len(input_array)):
    sort_array.append(int(input_array[i]))
print(sort_array)

array_len=len(sort_array)
#最小數的index
min_index=0
#目前第幾輪
round_number=0
while round_number<array_len:
    min_number=sort_array[round_number]
    for i in range(round_number+1, array_len):
        if sort_array[i]<min_number:
            min_index=i
            min_number=sort_array[i]
#swap the values of round_number and min_index
    sort_array[min_index]=sort_array[round_number]
    sort_array[round_number]=min_number
    min_index=round_number+1
    round_number=round_number+1
print(sort_array)



