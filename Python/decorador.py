#https://code.visualstudio.com/docs/editor/versioncontrol
def decora(f):
    def envuelve():
        print('estoy apunto de ejecutar la funcion')
        f()
        print('termine de jeutar la funcion')
    return envuelve

@decora
def hola():
    print('Hola mundo!')

hola()
