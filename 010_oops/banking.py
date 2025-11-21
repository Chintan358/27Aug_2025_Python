from abc import ABC,abstractmethod

class Account(ABC):
    balance=0

    def checkBalance(self):
        print("Current balaance is : ",self.balance)
    
    @abstractmethod
    def diposite(self, amt):
        pass

    @abstractmethod
    def withdrow(self,amt):
        pass


class Saving(Account):

    def diposite(self,amt):
        self.balance=self.balance+amt

    def withdrow(self, amt):
        if(amt>self.balance):
            print("Insuffcient amount")
        else:
            self.balance-=amt

class Loan(Account):

    def diposite(self,amt):
        if amt>self.balance:
            print("U dont have any loan")
        else:   
            self.balance=self.balance-amt

    def withdrow(self, amt):
        self.balance+=amt


s  =Saving()
s.checkBalance()
s.diposite(5000)
s.diposite(3000)
s.checkBalance()
s.withdrow(15000)
s.checkBalance()

print("****************")

s1  =Loan()
s1.checkBalance()
s1.diposite(5000)
s1.diposite(3000)
s1.checkBalance()
s1.withdrow(15000)
s1.checkBalance()