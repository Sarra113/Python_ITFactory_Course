# # Afisam un mesaj in consola
print('Hello world!')

print('verde', 'alb', sep = ', ')

print('text1')

print('text3', 'text2', sep = ',', end = '***')
# # by default, print se termina cu un newline character '\n'; cand adaugi altul cu end nu mai trece pe rand nou
# # la fel si la sep, by default intre strings e un spatiu
#
#
a = b = c = 'Apple'
print(a)

#
nume = input('Cum te numesti?')
age = input('Ce varsta ai?')
#
# print(f'Te numesti{nume} si ai{age} ani') #aici, age e deja un string; nu avem nevoie sa fie int
#
latura = int(input('Cat e latura?'))
arie = latura ** 2  #aici trebuie sa fie int ca sa putem face calculul
#
print(arie)
#
#
#
a = b = 13
c, d = '10', '11'

print(a)
print(c)
#
masini = 23
print(masini, type(masini))

garaj = float(masini)
print(garaj)
#
oras = '233'
print(oras, type(oras))
populatie = int(oras)
print(populatie)
#nu putem schimba un string intr-un int

produs = input('Nume de produs')
print('Azi mi-am luat un', produs)

pret = float(input('Care e pretul'))
print('Pretul este:', pret)

print('text6', 'text5') #fara virgula
print('text6', 'text5', sep = ',')
print('text6,', 'text5')  #mai mult spatiu pt ca am pus si virgula + separatorul spatiu by default


