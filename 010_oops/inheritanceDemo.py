
class A:

    def __init__(self):
        print("A calling")

    def display(self):
        print("Display calling")

class B(A) : 
    def __init__(self):
        print("B Calling")
        super().__init__()
        

    def sample(self):
        print("Sample calling")

# class C(B):
#     print("multilevel")

# class C(B,A):
#     print("multiple")

# class C(A):
#     print("Hirarchicle")

# b  = B()
# b.sample()
# b.display()