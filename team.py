loop = int(input())
result = 0

for _ in range(loop):
    n = input()
    nListesi = n.split()
    count = 0  
    for num in nListesi:
        if num == "1":
            count += 1
    if count >= 2:
        result+=1

print(result)
