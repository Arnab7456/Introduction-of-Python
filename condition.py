### LET'S DISCUSS CONDITIONAL STATEMENTS IN PYTHON ### 
# https://www.geeksforgeeks.org/python-if-else/

from queue import PriorityQueue


print("enter your age")
AGE= int(input())
if AGE>18:
    print("you can buy Alcohol ")
else:
    print("it's is a crime and you also spoil your life")

#always execute able
print("always excute")


'''
elif discuss here
'''
print("your marks :")
marks = int(input())

if marks>85:
    print("you are eligible to apt science :")
elif marks>=65:
    print("you are eligible to apt ARTs")
else:
    print("follow your dream , marks cannot define your knowledge")