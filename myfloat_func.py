# -*- coding: utf-8 -*-

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
    return (''.join(map(str,resul)))
def suma(a,b):
    a0=a[0]
    a1=a[1]
    a0.reverse()
    a0.append('.')
    a=a0+a1
        
        
    if a[0]=='+':
        a.remove('+')        
        a_str= ''.join(str(e)for e in a)
        a_float=float(a_str)
        a=a_float
        
    else:
        a.remove('-')        
        a_str= ''.join(str(e)for e in a)
        a_float=float(a_str)
        a=a_float*-1.
    #print (type(a))
    #print (a)
        
    """
        
    Para la tupla b
        
        
    """
        
    b0=b[0]
    b1=b[1]    
    b0.reverse()
    b0.append('.')
    b=b0+b1
    if b[0]=='+':
        b.remove('+')        
        b_str= ''.join(str(e)for e in b)
        b_float=float(b_str)
        b=b_float
    else:
        b.remove('-')        
        b_str= ''.join(str(e)for e in b)
        b_float=float(b_str)
        b=b_float*-1.
    #print (type(b))
    #print (b)
        
    c=a+b
    #print (type(c))
       
    if c>=0: 
        c0=int(c)
        c1=abs(c)-abs(int(c))  
            
        c0=str(c0)        
        c0=list(c0)        
            
        c1=str(c1)        
        c1=list(c1)
                  
        c0.insert(0,'+')
        c0.reverse()
           
                   
        c1.remove('0')
        c1.remove('.')
        c=(c0,c1)
        
            
    else:
        c0=int(c)
        c1=abs(c)-abs(int(c))  
            
        c0=str(c0)        
        c0=list(c0)        
            
        c1=str(c1)        
        c1=list(c1)
                  
        c0.insert(0,'-')
        c0.reverse()
           
                   
        c1.remove('0')
        c1.remove('.')
        c=(c0,c1)
        
    print (c)
def resta(a,b):
    a0=a[0]
    a1=a[1]
    a0.reverse()
    a0.append('.')
    a=a0+a1
        
        
    if a[0]=='+':
        a.remove('+')        
        a_str= ''.join(str(e)for e in a)
        a_float=float(a_str)
        a=a_float
        
    else:
        a.remove('-')        
        a_str= ''.join(str(e)for e in a)
        a_float=float(a_str)
        a=a_float*-1.
    #print (type(a))
    #print (a)
        
    """
        
    Para la tupla b
        
        
    """
        
    b0=b[0]
    b1=b[1]    
    b0.reverse()
    b0.append('.')
    b=b0+b1
    if b[0]=='+':
        b.remove('+')        
        b_str= ''.join(str(e)for e in b)
        b_float=float(b_str)
        b=b_float
    else:
        b.remove('-')        
        b_str= ''.join(str(e)for e in b)
        b_float=float(b_str)
        b=b_float*-1.
    #print (type(b))
    #print (b)
        
    c=a-b
    #print (type(c))
       
    if c>=0: 
        c0=int(c)
        c1=abs(c)-abs(int(c))  
            
        c0=str(c0)        
        c0=list(c0)        
            
        c1=str(c1)        
        c1=list(c1)
                  
        c0.insert(0,'+')
        c0.reverse()
           
                   
        c1.remove('0')
        c1.remove('.')
        c=(c0,c1)
        
            
    else:
        c0=int(c)
        c1=abs(c)-abs(int(c))  
            
        c0=str(c0)        
        c0=list(c0)        
            
        c1=str(c1)        
        c1=list(c1)
                  
        c0.insert(0,'-')
        c0.reverse()
           
                   
        c1.remove('0')
        c1.remove('.')
        c=(c0,c1)
        
    print (c)   
def multiplicacion(a,b):
    a0=a[0]
    a1=a[1]
    a0.reverse()
    a0.append('.')
    a=a0+a1
        
        
    if a[0]=='+':
        a.remove('+')        
        a_str= ''.join(str(e)for e in a)
        a_float=float(a_str)
        a=a_float
        
    else:
        a.remove('-')        
        a_str= ''.join(str(e)for e in a)
        a_float=float(a_str)
        a=a_float*-1.
    #print (type(a))
    #print (a)
        
    """
        
    Para la tupla b
        
        
    """
        
    b0=b[0]
    b1=b[1]    
    b0.reverse()
    b0.append('.')
    b=b0+b1
    if b[0]=='+':
        b.remove('+')        
        b_str= ''.join(str(e)for e in b)
        b_float=float(b_str)
        b=b_float
    else:
        b.remove('-')        
        b_str= ''.join(str(e)for e in b)
        b_float=float(b_str)
        b=b_float*-1.
    #print (type(b))
    #print (b)
        
    c=a*b
    #print (type(c))
       
    if c>=0: 
        c0=int(c)
        c1=abs(c)-abs(int(c))  
            
        c0=str(c0)        
        c0=list(c0)        
            
        c1=str(c1)        
        c1=list(c1)
                  
        c0.insert(0,'+')
        c0.reverse()
           
                   
        c1.remove('0')
        c1.remove('.')
        c=(c0,c1)
        
            
    else:
        c0=int(c)
        c1=abs(c)-abs(int(c))  
            
        c0=str(c0)        
        c0=list(c0)        
            
        c1=str(c1)        
        c1=list(c1)
                  
        c0.insert(0,'-')
        c0.reverse()
           
                   
        c1.remove('0')
        c1.remove('.')
        c=(c0,c1)
        
    print (c)
def division(a,b):
    a0=a[0]
    a1=a[1]
    a0.reverse()
    a0.append('.')
    a=a0+a1
        
        
    if a[0]=='+':
        a.remove('+')        
        a_str= ''.join(str(e)for e in a)
        a_float=float(a_str)
        a=a_float
        
    else:
        a.remove('-')        
        a_str= ''.join(str(e)for e in a)
        a_float=float(a_str)
        a=a_float*-1.
    #print (type(a))
    #print (a)
        
    """
        
    Para la tupla b
        
        
    """
        
    b0=b[0]
    b1=b[1]    
    b0.reverse()
    b0.append('.')
    b=b0+b1
    if b[0]=='+':
        b.remove('+')        
        b_str= ''.join(str(e)for e in b)
        b_float=float(b_str)
        b=b_float
    else:
        b.remove('-')        
        b_str= ''.join(str(e)for e in b)
        b_float=float(b_str)
        b=b_float*-1.
    #print (type(b))
    #print (b)
        
    c=a*b
    #print (type(c))
       
    if c>=0: 
        c0=int(c)
        c1=abs(c)-abs(int(c))  
            
        c0=str(c0)        
        c0=list(c0)        
            
        c1=str(c1)        
        c1=list(c1)
                  
        c0.insert(0,'+')
        c0.reverse()
           
                   
        c1.remove('0')
        c1.remove('.')
        c=(c0,c1)
        
            
    else:
        c0=int(c)
        c1=abs(c)-abs(int(c))  
            
        c0=str(c0)        
        c0=list(c0)        
            
        c1=str(c1)        
        c1=list(c1)
                  
        c0.insert(0,'-')
        c0.reverse()
           
                   
        c1.remove('0')
        c1.remove('.')
        c=(c0,c1)
        
    print (c)
def comparacion(a,b):
    a0=a[0]
    a1=a[1]
    a0.reverse()
    a0.append('.')
    a=a0+a1
        
        
    if a[0]=='+':
        a.remove('+')        
        a_str= ''.join(str(e)for e in a)
        a_float=float(a_str)
        a=a_float
        
    else:
        a.remove('-')        
        a_str= ''.join(str(e)for e in a)
        a_float=float(a_str)
        a=a_float*-1.
    #print (type(a))
    #print (a)
        
    """
        
    Para la tupla b
        
        
    """
        
    b0=b[0]
    b1=b[1]    
    b0.reverse()
    b0.append('.')
    b=b0+b1
    if b[0]=='+':
        b.remove('+')        
        b_str= ''.join(str(e)for e in b)
        b_float=float(b_str)
        b=b_float
    else:
        b.remove('-')        
        b_str= ''.join(str(e)for e in b)
        b_float=float(b_str)
        b=b_float*-1.
    if a==b:
        print ("Son iguales")
    else:
        print ("No son iguales")
def pi():
    pass
if __name__=="__main__":
    print (imprimir(pi()))

