# Enter your code here. Read input from STDIN. Print output to STDOUT
s = list(input())

box = []
s.append("x")

tmp = s[0]
cnt = 1

for i in range(1,len(s)):
    
    if tmp == s[i]:
        cnt += 1

    else:
        box.append([cnt,int(tmp)])
        tmp = s[i]
        cnt = 1
        
for j in range(len(box)):
    box[j] = tuple(box[j])

print(*box)
