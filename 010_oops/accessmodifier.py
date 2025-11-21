# class Demo:
#     __id = 10
#     _name = "test"
#     email = "test@gmail.com"

#     def __display(self):
#         print("Runing display")

# class Sample(Demo):

#     def show(self):
#         print(self._name,self.email)


# d  = Demo()

# print(dir(d))
# print(d._Demo__id)
# print(d.__id)
# d.__display()
# d._Demo__display()

# s  =Sample()
# s.show()


class Run:

    __id = 10

    def set(self,id):
        self.__id=id

    def get(self):
        print(self.__id)

r  =Run()
r.set(50)
r.get()
