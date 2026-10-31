list_var=[7,4,3,21,9,7,6,7,2]
print(list_var)
for index in range(9):
    print(list_var[index])
    if list_var[index]==7:
        print("This is value 7")
        list_var[index]=8
print(list_var)