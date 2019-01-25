# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 17:18:15 2018

@author: AstroEduardo
"""

a=([4,3,4,1,3,5,1,'+'],[5,5,1,7,3,7,3,6,4,6,2,2,4,2,5]) #la tupla con las listas
b=([3,5,6,7,1,2,5,3,2,1,'-'],[6,7,6,2,2,5,7,3,7,3,6,4,6,2,7,3,7,3,6,4,6,2])

def imprimir(a):
    a0=a[0]
    a1=a[1]
    
    b0=b[0]
    b1=b[1]
        
    a0.reverse()  
    b0.reverse()
    acoma=[',']    
    
    resul=a0+acoma+a1           
    return (''.join(map(str,resul)))

def suma(a,b):
    a0=a[0]
    a1=a[1]
    
    b0=b[0]
    b1=b[1]
         
    while (len(a1)>len(b1)):
        b1.append(0)
    while (len(b1)>len(a1)):
        a1.append(0)
    
    if a0[0]=='+' and b0[0]=='+':
        del a0[0]
        del b0[0]
        while (len(a0)>len(b0)):
            b0.insert(0,0)
        while (len(b0)>len(a0)):
            a0.insert(0,0)
    if a0[0]=='-' and b0[0]=='-':
        del a0[0]
        del b0[0]
        while (len(a0)>len(b0)):
            b0.insert(0,0)
        while (len(b0)>len(a0)):
            a0.insert(0,0)
        a0.insert(0,'-')
        b0.insert(0,'-')
    if a0[0]=='+' and b0[0]=='-':
        del a0[0]
        del b0[0]
        while (len(a0)>len(b0)):
            b0.insert(0,0)
        while (len(b0)>len(a0)):
            a0.insert(0,0)
        
    if a0[0]=='-' and b0[0]=='+':
        del a0[0]
        del b0[0]
        while (len(a0)>len(b0)):
            b0.insert(0,0)
        while (len(b0)>len(a0)):
            a0.insert(0,0)
        a0.insert(0,'-')
    coma=[',']    
    
    resula=a0+coma+a1           
    resulb=b0+coma+b1
    return (''.join(map(str,resula)))
    return (''.join(map(str,resulb)))
   
    
       

print (imprimir(a))
print (suma(a,b))