#this class acts as a mini bank acc
class Account:
    def __init__(self,acc_no,bal):
        self.acc_no=acc_no
        self.bal=bal
    #debit method
    def debit(self,bal):
        self.bal-=bal
        print(bal,"was debit from your account")
        print("your remeaning balance is:",self.bal)

    #credit method
    def credit(self,bal):
        self.bal+=bal
        print("your balance is:",self.bal )
    #balance check
    def check_bal(self):
        return print("your available balance is:",self.bal)

s1=Account(332244,70000)
s1.debit(60000)