def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
a = int(input("enter : "))
print("the fact is",a,"is",fact(a))