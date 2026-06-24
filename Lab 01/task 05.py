#task 5
def dit_task(s):
    d = {
        "vowels" : 0,
        "consonants" : 0,
        "total" :len(s)
    }
    for c in s:
        if c=='o' or c=='O' or c=='A' or c=='a' or c=='e' or c=='E' or c=='e' or c=='I' or c=='i' or c=='u' or c=='U':
            d["vowels"] += 1
        else:
            d["consonants"] +=1
    return d

dowork = dit_task("Artificial Intellegnce")
for key,val in dowork.items():
    print(key," ",val)
    
