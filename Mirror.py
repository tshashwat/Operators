a=input("Enter the string :")
print("Mirrored string :",end="")
for i in range(len(a),0,-1):
    print(a[i-1],end="")
