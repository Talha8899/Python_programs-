#this class acts as a mini bank acc
class Account:
    def __init__(self,acc_no,bal):
        self.acc_no=acc_no
        self.bal=bal
    #debit method
    def debit(self,bal):
        self.bal-=bal
        print("Rs",bal,"was debit from your account")
        print("your remeaning balance is Rs",self.bal)

    #credit method
    def credit(self,bal):
        self.bal+=bal
        print("Rs",bal,"was credit in your account")
        print("your balance is Rs",self.bal )
    #balance check
    def check_bal(self):
        return print("your available balance is Rs",self.bal)

s1=Account(332244,70000)
s1.credit(60000)