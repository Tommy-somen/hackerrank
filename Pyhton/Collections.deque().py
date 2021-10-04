# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

n = int(input())
inst = []
for _ in range(n):
    s = list(map(str,input().split()))
    inst.append(s)

box = deque()

for instruction in inst:
    length = len(instruction)
    if length == 2:
        if instruction[0] == "append":
            box.append(int(instruction[1]))
        elif instruction[0] == "appendleft":
            box.appendleft(int(instruction[1]))        
    else:
        if instruction[0] == "pop":
            box.pop()
        else:
            box.popleft()
            
print(*box)
