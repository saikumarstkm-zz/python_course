#To find the largest number in a list
list = [0,0,0,1,0]
large_number = 0
for number in list:
    if number > large_number:
        large_number = number
print(large_number)
