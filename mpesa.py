class MpesaAccount:
	def __init__(self,name,phone_no,):
		self.name = name
		self.phone_no = phone_no
        self.balance = 0
		self.deposits = []
		self.withdrawals = []
		self.loan = 0
	def deposit(self,amount):
		self.balance = self.balance + amount
		self.deposits.append(amount)
		info1="Hello {},confirmed you have deposited {} kshs in your account.your new Mpesa balance is{},kshs".format(self.name,y,self.balance)
		print(info1)
	def withdrawal(self,amount):
		if amount<self.balance
		   self.balance = self.balance - amount
		   self.withdrawals.append(amount)
		   info2 = "Hello {},confirmed your withdrawal of {}kshs is succesful.your new mpesa balance is {}kshs".format(self.name,x,self.balance)
		   print(info2)
		else:
		   print("you have insufficient balance")  

	def checkbalance(self):
		balance:self.balance
	    info3 = "Hello {},your current balance is{},".format(self.name,self.balance)
	    print(info3)	
	def my_deposits(self):
	    for a in self.deposits:
	    	print (a)
	def my_withdrawals(self):
	    for b in self.withdrawals:
	        print (b)
	def give_loan(self,deposits) :
	    if  len (self.deposits)>=5 and amount<1/3*sum(self.deposits) and self.loan==0:
	    	self.loan=self.loan+amount
	       	print(" Hello {} you qualify for the loan of {}".format(self.name, amount))
	    else:
	        print("Hello {} you dont qualify for the loan".format(self.name)) 

	def pay_loan(self,amount):
	    if self.loan==0:
	       print("you dont have an existing loan") 
	    elif amount<self.loan:
	        self.loan=self.loan-amount
	        print("Hello {}you have paid some part of your loan,{}.your balance remainig is {}".format(self.name,amount,self.loan))
	    elif amount==self.loan:
	        self.loan=self.loan-amount
	        print("you have paid your loan")
	    elif amount>self.loan:
	        more=amount-self.loan
	        self.balance= more+self.balance
	        self.loan=amount-self.loan-more
	        print("Hello {} you have paid more than is required,your current balance is{}".format(self.name,self.balance))




	    			


	                   