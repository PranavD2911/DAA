def fibonnaci(n1,n2,limit,count):
    n3 = n1 + n2
    count=count+1
    print(n3,end=" ")
    if count<(limit-2):
        fibonnaci(n2,n3,limit,count)

limit = int(input("Enter the limit of the fibonnaci series : "))
count = 0
n1=0
n2=1
print(n1,end=" ")
print(n2,end=" ")


fibonnaci(n1,n2,limit,count)
