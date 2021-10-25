class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        
        divider = []
        divided = []
        
        i = 1
        while i**2 <= n:
            if n%i == 0:
                divider.append(i)
                divided.append(n//i)
            i += 1
        
        divider.extend(divided)
        
        return sum(list(set(divider)))


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
