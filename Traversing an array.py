# arr=[10,20,30,40,50]
# for element in arr:
#     print(element)
n=int(input("Enter the total elements you want to take as input:"))
arr=[]
for i in range(n):
    element=int(input("Enter the elements {i+1}"))
    arr.append(element)
print("The entered elements are:")
for element in arr:
    print(element)