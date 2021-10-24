import sys

class Solution:
    
    def __init__(self,Stack_List=[], Enqueue_List=[]):
        self.Stack_List = Stack_List
        self.Enqueue_List = Enqueue_List

    def pushCharacter(self,s):
        self.Stack_List.append(s)
        
    def enqueueCharacter(self,s):
        self.Enqueue_List.append(s)
        
    def popCharacter(self):
        return self.Stack_List.pop()
        
    def dequeueCharacter(self):
        return self.Enqueue_List.pop(0)
        


# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", 
