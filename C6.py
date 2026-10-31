user_input=input("Enter Comma Seprated Numbers : ")
list_var=user_input.split(",")
print(list_var)
list_int=[]
index=0
while index<len(list_var):
    list_int.append(int(list_var[index]))
    index+=1
print(list_var)
print(list_int)