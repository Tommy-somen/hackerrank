# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

#nCk
def combinations_count(n, k):
    return math.factorial(n) // (math.factorial(n-k) * math.factorial(k))

#nCk*p1**k*p2**n-k    
def binomial_distribution(n,k,p1,p2):
    return combinations_count(n, k)*(p1**k)*(p2**(n-k))

p1, size = list(map(int,input().split()))

p1 /= 100 
p2 = 1-p1

no_more_than_two = 0
at_least_two = 0

for i in range(2,size+1):
    at_least_two += binomial_distribution(size,i,p1,p2)

for j in range(0,3):
    no_more_than_two += binomial_distribution(size,j,p1,p2)

print(round(no_more_than_two,3))
print(round(at_least_two,3))
