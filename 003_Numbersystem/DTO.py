number = 158
sum = 0
mul = 1
while number!=0:
    rem = number%8
    sum  = sum + rem*mul
    number//=8
    mul*=10
print(sum)




