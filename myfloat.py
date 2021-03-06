class MyFloat:

    def __init__(self, tuple_a,tuple_a0, tuple_a1):
        self.tuple_a0=tuple_a[0]
        self.tuple_a1=tuple_a[1]
        
        self.tuple_a0=self.tuple_a0.reverse()
        self.tuple_a0.append('.')
        
        self.a=self.tuple_a0+self.tuple_a1
        
        
        if self.a[0]=='+':
            self.a.remove('+')        
            self.a_str= ''.join(str(e)for e in self.a)
            self.a_float=float(self.a_str)
            self.a=self.a_float
        
        else:
            self.a.remove('-')        
            self.a_str= ''.join(str(e)for e in self.a)
            self.a_float=float(self.a_str)
            self.a=self.a_float*-1.
        

    def __add__(self, other):
        if isinstance (other, MyFloat):            
            self.sum=self.a+self.other
            if self.sum>=0: 
                c0=int(self.sum)
                c1=abs(self.sum)-abs(int(self.sum))  
                
                c0=str(c0)        
                c0=list(c0)        
                
                c1=str(c1)        
                c1=list(c1)
                  
                c0.insert(0,'+')
                c0.reverse()
               
                   
                c1.remove('0')
                c1.remove('.')
                self.sum=(c0,c1)
        
            
            else:
                c0=int(self.sum)
                c1=abs(self.sum)-abs(int(self.sum))  
                
                c0=str(c0)        
                c0=list(c0)        
            
                c1=str(c1)        
                c1=list(c1)
                      
                c0.insert(0,'-')
                c0.reverse()
           
                   
                c1.remove('0')
                c1.remove('.')
                self.sum=(c0,c1)
            return self.sum
        else: return NotImplemented

    def __sub__(self,other):
        if isinstance (other, MyFloat):            
            self.res=self.a-self.other
            if self.res>=0: 
                c0=int(self.res)
                c1=abs(self.res)-abs(int(self.res))  
                
                c0=str(c0)        
                c0=list(c0)        
                
                c1=str(c1)        
                c1=list(c1)
                  
                c0.insert(0,'+')
                c0.reverse()
               
                   
                c1.remove('0')
                c1.remove('.')
                self.res=(c0,c1)
        
            
            else:
                c0=int(self.res)
                c1=abs(self.res)-abs(int(self.res))  
                
                c0=str(c0)        
                c0=list(c0)        
            
                c1=str(c1)        
                c1=list(c1)
                      
                c0.insert(0,'-')
                c0.reverse()
           
                   
                c1.remove('0')
                c1.remove('.')
                self.res=(c0,c1)
            return self.res
        else: return NotImplemented

    def __mul__(self, other):
        if isinstance (other, MyFloat):            
            self.mul=self.a*self.other
            if self.mul>=0: 
                c0=int(self.mul)
                c1=abs(self.mul)-abs(int(self.mul))  
                
                c0=str(c0)        
                c0=list(c0)        
                
                c1=str(c1)        
                c1=list(c1)
                  
                c0.insert(0,'+')
                c0.reverse()
               
                   
                c1.remove('0')
                c1.remove('.')
                self.mul=(c0,c1)
        
            
            else:
                c0=int(self.mul)
                c1=abs(self.mul)-abs(int(self.mul))  
                
                c0=str(c0)        
                c0=list(c0)        
            
                c1=str(c1)        
                c1=list(c1)
                      
                c0.insert(0,'-')
                c0.reverse()
           
                   
                c1.remove('0')
                c1.remove('.')
                self.mul=(c0,c1)
            return self.mul
        else: return NotImplemented

    def __div__(self, other):
        if isinstance (other, MyFloat):            
            self.div=self.a/self.other
            if self.div>=0: 
                c0=int(self.div)
                c1=abs(self.div)-abs(int(self.div))  
                
                c0=str(c0)        
                c0=list(c0)        
                
                c1=str(c1)        
                c1=list(c1)
                  
                c0.insert(0,'+')
                c0.reverse()
               
                   
                c1.remove('0')
                c1.remove('.')
                self.div=(c0,c1)
        
            
            else:
                c0=int(self.div)
                c1=abs(self.div)-abs(int(self.div))  
                
                c0=str(c0)        
                c0=list(c0)        
            
                c1=str(c1)        
                c1=list(c1)
                      
                c0.insert(0,'-')
                c0.reverse()
           
                   
                c1.remove('0')
                c1.remove('.')
                self.div=(c0,c1)
            return self.div
        else: return NotImplemented

    def __radd__(self,other):
        return self.__add__(other)

    def __rsub__(self,other):
        return self.__sub__(other)

    def __rmul__(self,other):
        return self.__mul__(other)

    def __rdiv__(self,other):
        return self.__div__(other)

    def __str__(self):
        a0=self.a[0]
        a1=self.a[1]
        
        a0.reverse()
        a0.append(',')
       
        self.resul=a0+a1
        
        return (''.join(map(str,self.resul)))

    def __repr__(self):
        pass

    def __eq__(self):
        pass

    def __ne__(self):
        pass

if __name__ == "__main__":
    # Escribir aca el codigo para calcular pi. Al finalizar el calculo solo
    # debe imprimir el valor de pi, sin otros textos ni nada
    pass
