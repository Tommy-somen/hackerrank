import math

class Calculator():

    def power(self,n,p):
        
        if n >= 0 and p >= 0:
            num = math.pow(n,p)
            return int(num)
        
        else:
            e = "n and p should be non-negative"
            return e
            

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
