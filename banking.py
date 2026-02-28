#this class acts as a mini bank acc
class Account:
    def __init__(self,acc_no,bal):
        self.acc_no=acc_no
        self.bal=bal
        print(self.bal)
    #debit method
    def debit(self,bal):
        self.bal-=bal
        print("your remeaning balance is:",self.bal)

    #credit method
    def credit(self,bal):
        self.bal+=bal
        print("your balance is:",self.bal )

s1=Account(332244,70000)
s1.credit(10000)