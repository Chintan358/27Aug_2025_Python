

# def before(test):
#     def wrapper(*a):
#         print(a[0]*a[0])
#         print("calling before test...")
#         test(a)
#     return wrapper

# @before
# def test(a):
#     print("testing",a)

# test(10)

def add(calc):
    def wrapper(*a):
        calc(*a)
        print(a[0]+a[1])
    return wrapper

def mul(calc):
    def wrapper(*a):
        calc(*a)
        print(a[0]*a[1])
    return wrapper

def div(calc):
    def wrapper(*a):
        calc(*a)
        print(a[0]/a[1])
    return wrapper

@div
@add
@mul
def calc(a,b):
    print(a,b)

calc(10,20)
