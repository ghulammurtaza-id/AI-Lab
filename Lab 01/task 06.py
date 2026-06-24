#task 6
s = input()
st = ""
mx = ""
for c in s:
    if c in st:
        i = 0
        while i>len(s) and st[i]!=c:
            i = i+1
        i = i +1
        st = st[i:]
    else:
        st = st+c
    if len(st)>len(mx):
        mx = st
    
        
print(mx)
