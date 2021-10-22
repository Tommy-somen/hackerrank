# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n = int(input())

phone_number = {}

for _ in range(n):

    man, number = list(map(str,input().split()))
    #print(man)
    phone_number[man] = number

#入力行数がわからない場合はこの書き方を使う
for i in sys.stdin.readlines():

    man = (i.rstrip())
    
    if phone_number.get(man) != None:
        print(man+"="+phone_number[man])
    else:
        print("Not found")
