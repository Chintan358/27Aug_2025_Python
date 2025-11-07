# class Demo:

#     def disp(self):
#         print("Demo calling")


# class Sample:
#     d = Demo()
#     pass


# s = Sample()
# s.d.disp()


class Salary:

    def __init__(self,amt,bonus):
        self.amt = amt
        self.bonus = bonus

    def sal_info(self):
        print(self.amt, self.bonus)


class Emp :

    def __init__(self,id,name,s):
        self.id = id
        self.name= name
        self.s = s
    
    def emp_info(self):
        print(self.id,self.name)


s  = Salary(5000,3000)
emp = Emp(10,"Krish",s)
emp.emp_info()
emp.s.sal_info()

emp = Emp(11,"Manthon",s)
emp.emp_info()
emp.s.sal_info()

s1  = Salary(15000,3000)
emp = Emp(12,"Meet",s1)
emp.emp_info()
emp.s.sal_info()


