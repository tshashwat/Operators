#fibonacci

n=50
a=0
b=1
c=0
print("Fibonacci series till",n,"is: ",a,end=" ")
print(b,end=" ")
for i in range(n-2):
    c=a+b
    a=b
    b=c
    print(b,end=" ")
