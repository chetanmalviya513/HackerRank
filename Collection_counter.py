from collections import Counter

int(input())
sizes = list(map(int,input().split()))
money = 0
stock = Counter(sizes)
for i in range(int(input())):
    x,y = list(map(int,input().split()))
    if stock[x]:
        money+=y
        stock[x]-=1
print(money)
    