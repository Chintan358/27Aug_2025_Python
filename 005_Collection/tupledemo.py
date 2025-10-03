
# a = (10,20,40,50,"ss",2223.22)
# b = tuple((1,2,3,4))
# print(a)
# print(len(a))
# print(type(a))


# print(a[1:5])

# x  =list(a)
# x.append("xyz")
# a = tuple(x)
# print(a)

# del a
# print(a)



t = (100,200,300,400,500,600)

# (a,b,c,d,e,f)=t
# (*a,b,c)=t

# print(a)
# print(b)
# print(c)

# k  =[10]
# print(k)
# t = (10,)
# print(t)
# print(type(k))
# print(type(t))

# for i in t:
#     print(i)

# for i in range(len(t)):
#     print(t[i])


# d = {
#     10 : "hello",
#     "name":"tops",
#     (10,20):"abc",
 
# }

# print(d.get("c",45))
# print(d)

# check if numbe ris armstrong or not
num = int(input("Enter a number : "))
temp = num
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10
if temp == sum:
    print("Armstrong")
else:
    print("Not Armstrong")


#list in python
# a = [10,20,30,40,"ss",2223.22]
# b = list((1,2,3,4))
# print(a)
# print(len(a)) 
# print(type(a))

# print(a[1:5])
# a.append("xyz")
# print(a)


#List methods
# a.insert(2,"hello")
# a.remove(30)
# a.pop()
# a.clear()
# a.sort() #only homogenous data
# a.reverse()
# print(a)

# print(a.count(20))
# print(a.index(40))    
# a.extend([100,200,300])
# print(a)
