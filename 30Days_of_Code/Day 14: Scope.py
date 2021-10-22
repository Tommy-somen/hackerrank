class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = None
    
    def computeDifference(self):
        
        L = self.__elements
        len_L = len(L)
        L.sort()
        
        if L == 1:
            self.maximumDifference = L[0]
        else:
            self.maximumDifference = abs(L[0] - L[-1])
        

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
