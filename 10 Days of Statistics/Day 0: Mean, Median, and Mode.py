import statistics

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

#平均
print(statistics.mean(arr))
#中央値
print(statistics.median(arr))
#最頻値(どれも１回しか出ないのなら一番小さい数字を出力する
if statistics.mode(arr) == 1:
    print(arr[0])
else:
    print(statistics.mode(arr))
