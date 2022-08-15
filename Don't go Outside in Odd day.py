even=0
odd=0
list1=[]
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    list1.append(ele)   
for j in list1:
    if j%2==0:
         even=even+1
    else:
         odd=odd+1
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)
