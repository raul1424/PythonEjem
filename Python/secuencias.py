#Lista
nombre = "Cristina"
print(nombre[0])
nombres = ['Raul', 'Ruben', 'Balam', 'Moises', 'Joselyn']
print(nombres)

nombres[0]='max'
print(nombres)
nombres.sort()
print(nombres)

nombres.append('Raul')
nombres.reverse()
print(nombres)

#Tupla
coordenadaX=10
coordenadaY=5.3
coordenadas=(coordenadaX, coordenadaY)

print(coordenadas)
#coordenadas[0]=34
#print(coordenadas)


#Tuplas - secuencias
tuplas = (1 , 2, 3, 4, 5, 3, 5)
print(tuplas)
print(tuplas.count(3))
print(tuplas.index(3))
#tuplas[0]=23

#Set
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5) 

print(s)

s.remove(3)
print(s)

s.add(2)
s.add(2)
s.add(2)
print(s)

#diccionarios
edades = {'paula':21, 'moises':22, 'hector':23, 'balam':24}
print(edades)

print(edades['hector'])

edades['balam']=20
print(edades)

edades['moises']+= 1
print(edades)

#Matrices
m=[[1,2,3],[4,5,6]]
print(m)
m=[[1],[2],[3]]
print(m)
print(m[0:1])