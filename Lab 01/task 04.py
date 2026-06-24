#task 4
def workk(amount):
    if amount<1000:
        return amount - amount*(5/100)
    elif amount<5000:
        return amount - amount*(10/100)
    else:
        return amount - amount*(15/100)

print(workk(500))
print(workk(1050))
print(workk(60000))
        
