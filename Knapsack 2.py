weights = []
values = []
res = 0
capacity = int(input("Enter the capacity of knapsack : "))
limit = int(input("How many weights are there? "))
for i in range(0,limit):  
    print("\n") 
    w = int(input(f"Enter weight for {(i+1)} weight : "))
    v = int(input(f"Enter value for {(i+1)} weight : "))
    weights.append(w)
    values.append(v)
    
for pair in sorted(zip(weights, values), key = lambda x: x[1]/x[0], reverse=True ):
    if capacity<=0:
        break
    elif pair[0]>capacity:
        res += int(capacity * (pair[1]/pair[0]))
        capacity = 0
    elif pair[0]<capacity:
        res += pair[1]
        capacity-=pair[0]

print("Maximum value obtained is ",res)       