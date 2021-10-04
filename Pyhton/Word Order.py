# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
s = []

for _ in range(n):
    S = input()
    s.append(S)
    
set_s = list(set(s))
ans_len = len(set_s)

ans_cmp = []
exist_s = {}
for i in range(ans_len):
    if exist_s.get(set_s[i]) == None:
        exist_s[set_s[i]] = 0
        
for k in range(n):
    exist_s[s[k]] += 1


ans_box = []
for j in range(ans_len):
    ans_box.append(exist_s[set_s[j]])
    
    
print(ans_len)
print(*ans_box)
