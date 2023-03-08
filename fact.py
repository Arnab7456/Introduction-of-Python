int_num = list(map(int,input().split()))
x,y,z = sorted(int_num)
if pow(x,2) + pow(y,2) == pow(z,2) :
    print("yes")
else:
    print("no")