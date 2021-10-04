# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
T = int(input())

block_size = []
block_contents = []

for t in range(T):
    t_size = int(input())
    t_content = list(map(int,input().split()))
    block_size.append(t_size)
    block_contents.append(t_content)

def solver(size,content):
    content = deque(content)
    compare = sorted(content,reverse=True)
    tmp = 0
    box = [max(content[0],content[size-1])]
    if content[0] >= content[size-1]:
        content.popleft()
    else:
        content.pop()

    for i in range(size-2):
        new_size = len(content)
        tmp = max(content[0],content[new_size-1])
        if tmp > box[-1]:
            flg = False
            break
        
        if content[0] >= content[new_size-1]:
            content.popleft()
        else:
            content.pop()

        box.append(tmp)
    box.append(content[0])

    flg = False
    if box == compare:
        flg = True
    
    return flg

for j in range(T):
    if solver(block_size[j],block_contents[j]):
        print("Yes")
    else:
        print("No")
