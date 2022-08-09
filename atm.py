print('Welcome to State bank')
Pin=1234
Balance=10000
lang=input("Enter your language:\n1.Hindi\n2.English:-")
if lang=='1' or '2':
	print ('your language has been updated in English')
else:
	print('you enterd something wrong')
option=int(input('Enter the option you want to select:\n1.deposit\n2.withdraw\n3.balance enquiry:- '))

Pin1=int(input("Enter your pin"))
if Pin1==Pin:
	print("correct password")
else:
	print("wrong password")
	if option==1:
	  	  deposit=int(input('Enter ammount to    deposit:-'))
	  	  to=(Balance+deposit)
	  	  print(to)
	  	  withdraw=int(input("Enter amount to withdraw"))
	  	  print(to-withdraw)



if option==2:
	withdraw=int(input("enter your amount:-"))
	print(Balance-withdraw)
	  	  
				
elif option==3:
	print(Balance)


else:
		print("wrong enterd")