def prime(t):
    y=int(t)
    if y<2:
        return False
    for i in range(2,y):
        if y%i==0:
            return False
    return True         

def prime_product(z):
    m=int(z)
    for i in range(1,m):
        if m%i==0:
            if prime(i)==True:
                x=m/i
                if prime(x)==True:
                    return True 
               
    return False        
        
n = int(input())
print(prime_product(int(n)))