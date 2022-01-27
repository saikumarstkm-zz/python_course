# Write a program to remove duplicates in a list
list = [5,2,3,5,8 ,5,8,7]
list2 = [6,7,8,9,3,9,8]
unique_list=[]
for number in list:
    if list.count(number) > 1:
        list.remove(number)
print(list)

for number in list2:
    if number not in unique_list:
        unique_list.append(number)
print(unique_list)
