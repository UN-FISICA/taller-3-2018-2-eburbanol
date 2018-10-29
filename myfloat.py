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
            if self.num>=0: 
                c0=int(self.c)
                c1=abs(self.c)-abs(int(self.c))  
                
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
                c0=int(self.c)
                c1=abs(self.c)-abs(int(self.c))  
                
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

    def __sub__(self):
        pass

    def __mul__(self):
        pass

    def __div__(self):
        pass

    def __radd__(self):
        pass

    def __rsub__(self):
        pass

    def __rmul__(self):
        pass

    def __rdiv__(self):
        pass

    def __str__(self):
        pass

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
