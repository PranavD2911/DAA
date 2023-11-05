limit = int(input("Enter the limit of the fibonnaci series : "))

n1 = 0
n2 = 1
print(n1, end=" ")
print(n2, end=" ")

for _ in range(limit-2): 
    n3 = n1 + n2
    print(n3, end=" ")
    n1= n2
    n2 = n3
  