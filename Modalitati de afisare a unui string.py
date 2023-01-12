# Realizat de /Produced by Casiu George Valentin
"""
Modalitati de afisare a unui string/Ways to display a string.

Afiseaza/Display:
Introduceti textul/Enter the text:Ana are mere.
1. Ana are mere.
2. Ana are mere.
3. Ana are mere.
4. Ana are mere.
5. Ana are mere.
6. Ana are mere.
7. Ana are mere.
8. Ana are mere.
9. Ana are mere.
10. Ana are mere.
"""


s=input("Introduceti textul/Enter the text:")

#varianta/version 1
print('1. ',end='')
print(s)

#varianta/version 2
print('2. ',end='')
print(s[:])

#varianta/version 3
print('3. ',end='')
print(s[::])

#varianta/version 4
print('4. ',end='')
print(s[::1])

#varianta/version 5
print('5. ',end='')
print(s[0:])

#varianta/version 6
print('6. ',end='')
print(s[:len(s)])

#varianta/version 7
print('7. ',end='')
print(s[0:len(s)])

#varianta/version 8
print('8. ',end='')
print(s[0:len(s):1])

#varianta/version 9
print('9. ',end='')
for i in range(len(s)):
    print(s[i], end='')
print()

#varianta/version 10
print('10. ',end='')
i=0
while i<len(s):
    print(s[i], end='')
    i+=1
print()
