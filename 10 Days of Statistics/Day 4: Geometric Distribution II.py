# Enter your code here. Read input from STDIN. Print output to STDOUT


#geo
def geometric_distribution(n,p1,p2):
    return (p1**(n-1))*p2

numerator, denominator = list(map(int,input().split()))
n = int(input())
#the ratio of fail
p1 = numerator/denominator
#the ratio of done
p2 = 1 - p1

during_five = 0
for i in range(1,6):
    during_five += geometric_distribution(i,p2,p1)

print(round(during_five,3))
