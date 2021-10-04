

# Complete the solve function below.
def solve(s):
    
    tmp = ""
    box = []
    
    for k in range(len(s)):
        if s[k] == " ":
            box.append(tmp)
            tmp = ""
        else:
            tmp = tmp+s[k]
    box.append(tmp)
    
    for i in range(len(box)):
        box[i] = box[i].capitalize()
    
    ans = ""
    ans = ans + box[0]
    
    for j in range(1,len(box)):
        ans = ans + " " + box[j]
        
    return ans
