from abc import ABC,abstractmethod

class Sample(ABC):

    @abstractmethod
    def show(self):
        pass

class Demo(Sample):
     def show(self):
         print("show callng")


# s  = Sample()
# s.show()

d  =Demo()
d.show()