#task 2
s = input()
print(s)
print(f"First Char is {s[0]}")
print(f"Last Char is {s[-1]}")
print("length is ",len(s))
print(2*s)
spaces = s.count(" ")
exclude_spaces = len(s) - spaces
print("Num of char ",exclude_spaces)
for c in s:
    if(c!=" "):
        print(c,end="")
