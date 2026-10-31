list_var=[7,4,3,21,9,7,6,7,2]
print(list_var)
for i in range(len(list_var)):
    for j in range(len(list_var)-1):
        if list_var[j]>list_var[j+1]:
           temp=list_var[j+1]
           list_var[j+1]=list_var[j]
           list_var[j]=temp
print(list_var)
