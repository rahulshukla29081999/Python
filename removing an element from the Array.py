import array as arr
x=arr.array("i",[1,2,5,4,5])
print("the new created array is :",end=" ")
for i in range(0,5):
    print(x[i], end=" ")
print("\r")


    #removing an element from the array
#     #using pop()
# print("the poped element is:",end=" ")
# print(x.pop(2))
# print("the array after the poping is done:",end= " ")
# for i in range(0,4):
#     print(x[i],end=" ")

# #using the remove () for 1st occurance of 5---
print(x.remove(5))
print("the array after removing is done:",end=" ")
for i in range(0,4):
    print(x[i],end=" ")
