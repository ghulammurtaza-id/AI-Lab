def work(lst):
    d = {}
    l = []
    
    for n in lst:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1

    for num, cnt in d.items():
        if cnt > 1:
            l.append(num)
    
    return l

lst = list(map(int, input().split()))
ans = work(lst)
print(ans)
