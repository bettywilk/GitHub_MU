user_input=input("Enter Comma Seprated Numbers : ")
list_var=user_input.split(",")
print(list_var)
index=0
sum=0
while index<len(list_var):
    #print(list_var[index])
    sum+=int(list_var[index])
    index+=1
print(sum/len(list_var))
print(list_var)