from functools import reduce
l = [12,45,7,8,98,3,6,5]

# k = map(lambda x : x*x,l)
# k = filter(lambda x : x%2!=0,l)
k = reduce(lambda x,y : x+y,l)



print(k)