#task 1
name = input("Enter your Name : ")
age = int(input("Enter your Age : "))
city = input("Enter your City Name : ")
data = dict()
data["name"] = name
data["age"] = age
data["city"] = city

for key,val in data.items():
    print(key," ",val)

if "age" in data:
    if data["age"]>=18:
        print("you are eligible for vote")
    else:
        print("you are not eligible for vote ")

