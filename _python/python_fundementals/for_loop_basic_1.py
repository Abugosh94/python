#Basics
for x in range(0, 151, 1):
    print(x)

#Multiples of Five
for x in range(5, 1001, 5):
    print(x)

#Counting, the Dojo Way
for x in range(1, 101, 1):
    if(x%10==0):
        print("Coding Dojo")
    elif (x%5==0):
        print("Coding")
    else:
        print(x)

#Whoa. That Sucker's Huge
sum=0
for x in range(0, 500001):
    if(x%2!=0):
        sum+=x
print(sum)

#Countdown by Fours
for x in range(2018, 0, -4):
    print(x)

#Flexible Counter
low_num = 2
high_num = 54
mult= 5

for x in range(low_num, high_num+1, 1):
    if(x%mult==0):
        print(x)