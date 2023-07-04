username = input()
liste = []

for harf in username:
    if harf not in liste:
        liste.append(harf)
  
if len(liste) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")