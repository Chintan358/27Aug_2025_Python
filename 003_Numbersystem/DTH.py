number = 155
sum = ""
k = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
while number!=0:
    rem = number%16
    sum = str(k[rem])+sum
    number//=16
    
print(sum)




