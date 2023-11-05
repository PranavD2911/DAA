str = input("Enter a string : ")

def findOccurence(str):
    s = []

    for el in str:
        s.append(el)

    s.sort()
    print(s)
    visited = []

    for i in range(len(s)):
        if s[i] not in visited:
            temp = s.count(s[i])
            print(s[i], " : ", temp)
            visited.append(s[i])
            
findOccurence(str)