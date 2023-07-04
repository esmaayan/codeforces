loop = int(input())
for _ in range(loop):
    n = input()
    if 1 <= len(n) <= 10:
        print(n)    
    else:
        first = n[0]
        end = n[-1]
        num = str(len(n)-2)
        print(first+num+end)
   