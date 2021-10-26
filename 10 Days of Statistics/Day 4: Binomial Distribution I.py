# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def combinations_count(n, k):
    return math.factorial(n) // (math.factorial(n-k) * math.factorial(k))

def binomial_distribution(n,k,p1,p2):
    return combinations_count(n, k)*(p1**k)*(p2**(n-k))

data = list(map(float,input().split()))

total = sum(data)
data[0] /= total 
data[1] /= total

at_least_three = 0
for i in range(3,7):
    at_least_three += binomial_distribution(6,i,data[0],data[1])

print(round(at_least_three,3))
