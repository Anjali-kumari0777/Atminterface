import time
print("please insert your card")
time.sleep(5)
password=1234
balance=5000
transection_history=[]
pin=int(input("enter your atm pin....."))

if pin==password:
 while True:
     print("""
          1== check balance
          2==withdraw balance
          3==deposite balance
          4==Transection history
          5==exit 
           """
         )
     try:
         option=int(input("please enter your choice "))
     except:
         print("invalid option please enter valid option")
 
     if option==1:
         print(f"your current balance is {balance}")

         print("================================================================")
         print("================================================================")
     if option==2:
         withdraw_amount=int(input("please enter withdraw ammount "))
         balance=balance-withdraw_amount
         print(f"{withdraw_amount} debited from your amount")

         print(f"your current balance is {balance}")
         transection_history.append(f"deposited amount is {withdraw_amount}")
         print("================================================================")
         print("================================================================")

     if option==3:
         deposite_amount=int(input("please enter your deposit amount "))
         balance=balance+deposite_amount
         print(f" your deposit amount is {deposite_amount}")
         print(f" your total amount {balance}")
         transection_history.append(f"deposited balance is {deposite_amount}")
         print("================================================================")
         print("================================================================")

     if option==4:
      for transection in transection_history:
         print(f"transection history->{transection}")
      
     if option==5:
         print("thanku for using our service")
         print("have a good day")
         break           


else:
    print("wrong pin please try again")