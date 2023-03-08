# for loop

for c in range(10):
    print(2*c , end=",")
print(" ")
print()

#using list 
fruit = ["apple","mango","bannana" , "cherry"]
for x in fruit:
    print(x)

for y in " Apple ":
    z=y.rstrip() # use to gap
    print(z)
fruits = ["apple","mango","bannana" , "cherry"]

for list in fruits:
    print(fruits)

# for loop with else 
for i in range(10):
    print(i , end=(","))
    
else: 
    print()
    print("invalid")

#### discuss about BREAK
for i in range(12):
    print(i)
    if i == 10:
        break
else:
    print("check your code")

### lets dicuss about CONTINUE
for i in range(55):
    print(i , end=(","))
    if i == 25:
        continue
    elif i == 35:
        break
else: 
    print("check your programe bro")


# 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