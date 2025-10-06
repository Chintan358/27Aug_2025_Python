# l = [1,2,3,4,5,6,7,8]
# # k = []

# # def square(a):
# #     return a*a

# # for i in l:
# #    j =  square(i)
# #    k.append(j)
# # k = map(square,l)

# k = map(lambda a:a*a,l)
# print(list(k))


# a = [10,20,30,40,50,60]
# b = [1,2,3,4,5]

# k = map(lambda x,y:x+y,a,b)
# print(list(k))


l = [1,2,3,45,69,7,84,56,77,8]

# def checkodd(a):
#     if a%2!=0:
#         return a
    
# k = []
# for i in l:
#     j = checkodd(i)
#     if j is not None:
#         k.append(j)
# k = filter(lambda x : x%2!=0,l)
# print(list(k))

# subjects  = ["python",'java','node','android','sql']

# k = filter(lambda x : "a" in x ,subjects)
# print(list(k))

# # k = map(lambda x : len(x),subjects)
# x = list(k)
# print(x)
# m = map(lambda x : len(x),x)
# print(list(m))

# k = [1,2,3,4,5,6,7,8,9,10,16]

# import math

# def checkPsquare(a):
#     k = math.sqrt(a)
#     if k.is_integer():
#         return k

# r  =filter(checkPsquare,k)
# print(list(r))


from functools import reduce

# l = [10,20,34,55,68,974,1,2,30]

# def max(x,y):
   
#     if x>y:
#         return x
#     else:
#         return y
    
# k = reduce(max,l)
# k = reduce(lambda x,y:x if x>y else y,l)
# print(k)