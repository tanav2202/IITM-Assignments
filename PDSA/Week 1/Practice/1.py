def prime(n):
    if n<2:
        return False
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True         
        
def Twin_Primes(n,m):
    Ans=[]
    for i in range(n,m):
        if prime(i)==True:
            if prime(i+2)==True:
                Ans.append((i,i+2))
    
    return(Ans)            
    
n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))