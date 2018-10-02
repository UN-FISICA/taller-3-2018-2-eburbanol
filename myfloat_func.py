# -*- coding: utf-8 -*-

a=([3,2,1,4,1,"+"],[2,4,6,2,6,2,4])
a=str(a)


def imprimir(a):
    for i in range(len(a[0]),0,-1):
        print (a[0][i-1], end='',)
    print (',', end='')
    for i in range (len(a[1],0,-1):
        print (a[1][i-1],end='',)
                                
        
def suma(a, b):
    a[0].reverse()
    b[0].reverse()
    a_deci=''.join(str(e) for e in a[1]
    b_deci=''.join(str(e) for e in a[1]
    a_int=''.join(str(e) for e in a[1]
    b_int=''.join(str(e) for e in a[1]
        if a[0][1]=="-":              
            a_deci=float(a_int.replace("-",""))
            a_int=float("0."+a_int)
            a_deci=a_deci*-1
            a_int=a_int*-1
        else:
            a_deci=float(a_deci.replace("+",""))
            a_int=float("0."+a_int)
        if b[0][1]=="-":              
            b_deci=float(a_int.replace("-",""))
            b_int=float("0."+b_int)
            b_deci=b_deci*-1
            b_int=b_int*-1
        else:
            b_deci=float(b_deci.replace("+",""))
            b_int=float("0."+b_int)
        a[0].reverse()               
        b[0].reverse()
                  
        a_new=a_int+a_deci
        b_new=b_int+b_deci
        c_resul=a_new+b_new
                  
        if c_resul>0:
            
                  
                  
                  
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
