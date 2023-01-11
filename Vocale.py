# Realizat de /Produced by Casiu George Valentin
"""
Realizați un program care afișează de câte ori apare fiecare vocală în textul citit și apoi la final, totalul aparițiilor lor.
Make a program that display the number of time each vowel appears in the read text and then at the end, total of the occurrences.
Afiseaza: /Display:
Introduceti textul/Enter the text:Ana are ouă și piersici în veșmânt
Vocalele sunt/Vowels are:
a=3
ă=1
â=1
e=3
i=4
î=1
o=1
u=1
Numarul total de vocale este/Total number of vowels is:15
........
"""

s=input("Introduceti textul/Enter the text:")
l='aAăĂâÂeEiIîÎoOuU'
t=0
print("Vocalele sunt/Vowels are:")
for i in range(0,len(l),2):
    v=s.count(l[i])+s.count(l[i+1])
    print(l[i]+"="+str(v))
    t+=v
print('Numarul total de vocale este/Total number of vowels is:'+str(t))