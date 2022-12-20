# Basic
for i in range(151):
    print(i)

# Multiples of 5
for i in range(5, 1001):
    if i % 5 == 0:
        print(i)

# Counting, the Dojo Way
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# Whoa that sucker is huge!
sum = 0
for i in range(500_001):
    sum += i

print(sum)

# Countdown by fours
for i in range(2018, 0, -4):
    print(i)

# Flexible counter
lowNum = 1
highNum = 10000
multi = 10

for i in range(lowNum, highNum + 1):
    if i % multi == 0:
        print(i)
