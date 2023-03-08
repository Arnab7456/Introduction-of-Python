### LET'S DISCUSS CONDITIONAL STATEMENTS IN PYTHON ### 
# https://www.geeksforgeeks.org/python-if-else/

from queue import PriorityQueue
from re import I


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


# example
print("enter your marks :")
marks = int(input())
if marks >90 and marks<100 :
    print("TOPPER")
elif marks >80 and marks<90:
    print("1 st runner up")
elif marks>70 and marks<80:
    print("best result")
elif marks>60 and marks<70:
    print("good")
elif marks >50 and marks<60:
    print("hard work needed")
else :
    print("bhi tui youtuber hai na bro")


n = int(input())
if n%2==0 :
    print("even")
else:
    print("odd")