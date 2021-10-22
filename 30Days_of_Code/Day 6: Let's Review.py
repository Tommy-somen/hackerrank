# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
box = []

for _ in range(T):
    s = list(input())
    box.append(s)

for item in box:
    odd, even = "",""
    for i in range(len(item)):
        if i%2 != 0:
            odd = odd+item[i]
        else:
            even = even+item[i]
    print(even,odd)
