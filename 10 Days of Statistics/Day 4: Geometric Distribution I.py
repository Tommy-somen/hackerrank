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

print(round(geometric_distribution(n,p2,p1),3))

