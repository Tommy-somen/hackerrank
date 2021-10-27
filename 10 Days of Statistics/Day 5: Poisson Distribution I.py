import math

def poison_distribution(k,lam):

    return round((((lam**k)*(math.exp(-lam)))/math.factorial(k)),3)  

lam = float(input())
k = int(input())

print(poison_distribution(k,lam))
