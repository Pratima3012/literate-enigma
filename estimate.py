
def wallis(n):
        pi=2.0
        for i in range(1,n):
                pi=pi*((4*i*i)/((4*i*i)-1))
        return pi
        
n=int(input())
print(wallis(n))


            
        
        
        
                
   
