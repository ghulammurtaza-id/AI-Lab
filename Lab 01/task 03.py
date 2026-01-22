#task 3
import math
lst= list(map(int,input().split()))
query = int(input("which input you want to update index: "))
value = int(input("with what value "))

sum = 0;
mx = -math.inf
mn = math.inf

for i in range(len(lst)):
    print(lst[i],end=" ")
    sum+=lst[i]
    if lst[i]> mx:
        mx = lst[i]
    if lst[i]<mn:
        mn = lst[i]
    if i == query:
        lst[i] = value

print("updated list ")
print(lst)
print("this is max ",mx)
print("this is min ",mn)
