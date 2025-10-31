number = 155
hex =''


l = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

while number !=0:
    rem = number%16
    hex=l[rem]+hex
    number  =number//16
   
    
print(hex)