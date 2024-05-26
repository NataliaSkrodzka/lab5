import numpy as np

a = np.array([20, 30, 40, 50]) #jak chcemy wykonywac dzialania to musza byc tej samej dlugosci
b = np.arange(4)
# print(a)
# print(b)
#
# c = a - b
# print(c)
#
# print(b**2)
#
# print(a)
# a += b
# print(a)
# a -= b
# print(a)


# a = np.arange(3) #mniozenie macierzy - liczba wierszy z pierwszej musi sie zgadzac z liczba wierszy drugij
# b = np.arange(3)
# print(a)
# print(b)
# print(a.dot(b)) #dot mnozenie macierzy
# print(np.dot(a,b))
# c = np.array([[1,2,3],[4,5,6]])
# d = np.array([[1,5], [2,6], [1,4]])
# print(c)
# print(d)
# print(np.dot(c,d))
#
# a = np.arange(12).reshape((3,4))
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.min(axis=1))

a = np.arange(6).reshape((3,2))
print(a)
for b in a:
    print(b) #element b to pojedynczy wiersz

for b in a:
    for i in range(len(b)):
        print(b[i],end=' ')
    print(" ")

print(a.shape)
print(type(a.shape))
for i in range(0, a.shape[0]):
    for j in range(0, a.shape[1]):
        print(a[i][j], end=' ')
    print(" ")

a = np.arange(6)
print(a)
print(a.shape)
print("")
b = a.reshape((2,3))
print(b)
print(b.shape)
print("")
c = b.reshape((3,2))
print(c)
print(c.shape)
print("")
d = c.ravel() #odtwarza wektor wejsciowy czyli splaszcza macierz do wektora
e = b.T #transpozycja czyli zamiana wierszy z kolumnami
print(e)





