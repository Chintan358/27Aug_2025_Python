number = 155
sum = 0
mul=1
while number !=0:
    rem = number%2
    sum  = sum+(rem*mul)
    number  =number//2
    mul*=10
    
print(sum)