# -*- coding: utf-8 -*-

a=(['+',3,2,1,4,1],[2,4,6,2,6,2,4])
a=str(a)


def imprimir(a):
    c=''
    for x in a[0] : 
        c = c+''.join(x) 
    print (c)

    
    

def suma(a, b):
    resul=(d,e)
    for i in range(len(a[0])):
      resul.append(a[i])

    for i in range(len(b[0])):
      d[i] = a[i] +b[i]
    
    for i in range(len(a[1])):
      resul.append(a[i])

    for i in range(len(b[1])):
      e[i] = a[i] +b[i]
    resul=(d,e)

    print(resul)
    


def resta(a, b):
    pass


def multiplicacion(a, b):
    pass


def division(a, b):
    pass


def comparacion(a, b):
    pass


def pi():
    pass


if __name__ == "__main__":
    print(imprimir(pi()))


print (a)
imprimir (a)