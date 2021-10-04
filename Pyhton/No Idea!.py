# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m = list(map(int,input().split()))
n_array = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

def solver(array,a,b):
    
    happiness = 0

    in_array = {}
    for i in range(n):
        if in_array.get(array[i]) == None:
            in_array[array[i]] = 1
        else:
            in_array[array[i]] += 1

    for j in range(m):
        if in_array.get(a[j]) != None:
            happiness += in_array[a[j]]

    for k in range(m):
        if in_array.get(b[k]) != None:
            happiness -= in_array[b[k]]
    
    return happiness

print(solver(n_array,A,B))
