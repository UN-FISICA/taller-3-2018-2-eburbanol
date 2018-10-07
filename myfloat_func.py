# -*- coding: utf-8 -*-

a=([3,2,1,4,1,"+"],[2,4,6,2,6,2,4])
a=str(a)


def imprimir(a):
    a0=a[0]
    a1=a[1]

    #print (type(a0))

    a0.reverse()
    a0.append(',')

    #b0=str(a0)
    #print (type(b0[3]))

    #print (a0)
    resul=a0+a1

    #print (resul)

    print (''.join(map(str,resul)))  
                                
        
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
            resul_int=int(c_resul)
            resul_deci=c_resul-int(c_resul)
            E="+"+str(resul_int)
            D=list(resul_deci)
            E=list(e)
            D=list(D)
        else:
        resul_int=int(c_resul)
        resul_deci=c_resul+int(c_resul)           
        E=str(resul_int)     
        D=str(resul_deci)
        E=list(E)
        D=list(D)
    c=(E,D)
    return c
                  
                  
def resta(a, b):
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
        c_resul=a_new-b_new
                  
        if c_resul>0:
            resul_int=int(c_resul)
            resul_deci=c_resul-int(c_resul)
            E="+"+str(resul_int)
            D=list(resul_deci)
            E=list(e)
            D=list(D)
        else:
        resul_int=int(c_resul)
        resul_deci=c_resul+int(c_resul)           
        E=str(resul_int)     
        D=str(resul_deci)
        E=list(E)
        D=list(D)
    c=(E,D)
    return c


def multiplicacion(a, b):
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
        c_resul=a_new*b_new
                  
        if c_resul>0:
            resul_int=int(c_resul)
            resul_deci=c_resul-int(c_resul)
            E="+"+str(resul_int)
            D=list(resul_deci)
            E=list(e)
            D=list(D)
        else:
        resul_int=int(c_resul)
        resul_deci=c_resul+int(c_resul)           
        E=str(resul_int)     
        D=str(resul_deci)
        E=list(E)
        D=list(D)
    c=(E,D)
    return c


def division(a, b):
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
        c_resul=a_new/b_new
                  
        if c_resul>0:
            resul_int=int(c_resul)
            resul_deci=c_resul-int(c_resul)
            E="+"+str(resul_int)
            D=list(resul_deci)
            E=list(e)
            D=list(D)
        else:
        resul_int=int(c_resul)
        resul_deci=c_resul+int(c_resul)           
        E=str(resul_int)     
        D=str(resul_deci)
        E=list(E)
        D=list(D)
    c=(E,D)
    return c


def comparacion(a, b):
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
        if a_new==b_new
            return ("true")
        else
            return ("false")
    


def pi():
    pass


if __name__ == "__main__":
    print(imprimir(pi()))


print (a)
imprimir (a)
