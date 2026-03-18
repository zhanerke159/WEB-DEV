def average(arr):
    s = set(arr)          
    avg = sum(s) / len(s) 
    return round(avg, 3)  

n = int(input())
arr = list(map(int, input().split()))

print(average(arr))