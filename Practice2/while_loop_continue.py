#1
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

#2
n = 0
while n < 5:
    n += 1
    if n % 2 == 0:
        continue
    print(n)

#3
x = 0
while x < 5:
    x += 1
    if x == 4:
        continue
    print("x =", x)

#4
y = 1
while y <= 5:
    if y == 2:
        y += 1
        continue
    print(y)
    y += 1
    
#5
count = 0
while count < 4:
    count += 1
    if count == 3:
        continue
    print("Step", count)