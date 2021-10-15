libros = [
    {'Titulo':'el principito', 'año':1943},
    {'Titulo':'el arte de la guerra', 'año':1772},
    {'Titulo':'la ciudad de las vestias', 'año':2002},
    {'Titulo': 'el hobbit', 'año':1984},
    {'Titulo': 'la grieta', 'año':2007}
]

#libros.sort()
#no podemos comparar objetos sin decir algo mas sobre ellos
#libros.sort(key='año')
#sort no sabe que debemos buscar dentro del diccionario
def ftitulo(libro):
    return libro['Titulo'].upper()

def fanio(libro):
    return libro['año']

#print(ftitulo(libros[0]))
#print(fanio(libros[0]))
#print(libros)
#print()

#print('libros ordenados por año:')
#libros.sort(key=fanio)
#print(libros)

#print('libros ordenados por titulo:')
#libros.sort(key=ftitulo)
#print(libros)

libros.sort(key=lambda libro:libro['año'])
for libro in libros:
    #print(f"El libro {libro['Titulo']} fue publicado en {libro['año']}")
    #print (libros)
     print('El libro {Titulo} fue publicado en {año}'.format (**libro) )

libros.sort(key=lambda libro:libro ['Titulo'])
#print (libros)
