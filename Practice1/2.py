a=int(input())
b=int(input())
c=int(input())
if a>b and a<c:
    print(a)
elif b>a and b<c:
    print(b)
elif b<a and b>c:
    print(b)
elif a<b and a>c:
    print (a)
else:
    print (c)


