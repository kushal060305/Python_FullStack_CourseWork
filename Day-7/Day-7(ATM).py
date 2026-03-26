print ("-----------Welcome to the ATM---.
acc
num = input ("Enter the account number: ")
pin = input ("Enter the pin: ")
.")
if acc_num in data and data [acc_num]l'pin']==pin:
print ("Login Successful")
while True:
menu ()
ch = input ("Enter your choice: ").lower ()
if ch=='c':
check_balance (acc_num)
elif ch=='d':
deposit (acc_num)
elif ch=='w':
withdraw (acc num)
elif ch=='v':
view transactions (acc num)
elif ch=='p':
change_pin (acc_num)
elif ch=='e':