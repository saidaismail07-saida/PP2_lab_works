#1
i = 1
while True:
    print(i)
    if i == 3:
        break
    i += 1

#2
n = 0
while n < 10:
    if n == 5:
        break
    print(n)
    n += 1

#3
x = 10
while x > 0:
    if x == 4:
        break
    print(x)
    x -= 1

#4
y = 1
while y <= 5:
    if y % 2 == 0:
        break
    print(y)
    y += 1
    
#5
count = 0
while True:
    count += 1
    if count > 3:
        break
    print("Step", count)