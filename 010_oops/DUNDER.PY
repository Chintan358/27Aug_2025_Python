# class Demo:

#     # def __init__(self,a,b):
#     #     self.a = a
#     #     self.b = b
        

#     def disp(self):
#         print("Hello")

#     def __str__(self):
#         return f"Hello {self.id}"
    
#     def __eq__(self, value):
#         return self.a==value.a and self.b==value.b


# d  =Demo()
# print(d)

# d1 = Demo(10,30)
# d2 = Demo(10,30)

# print(d1==d2)

class Sample:

    def __init__(self,l):
        self.l = l

    def __len__(self):
        return len(self.l)

    def __setitem__(self,index,value):
         self.l[index] = value

    def __getitem__(self,index):
        return self.l[index]
        

s  =Sample([10,20,30,40,50])
# s[2] = 200
# print(len(s))
# print(s.l)

print(s[2])