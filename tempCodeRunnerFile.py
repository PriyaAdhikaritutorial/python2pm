print("=================welcome to ATM========")
pin =int(input("Enter your pin: "))
if pin==1234:
    amount=10000
    print("1. withdraw  2. Balance Enquiry ")
    option =int(input("select your option: "))
    if option==1:
        namount=int(input("Enter amount to withdraw: "))
        if namount>amount:
            print("insufficiemt balance")
        else:
            wamount= amount- namount
            print(f"please collect your cash")
            print(f"withdraw amount is :{namount}")
            print(f"your remaining bakance is  :{wamount}")
    elif option==2:
        print(f"your balance is : {amount}")
    else:
        print("Invalid option")
else:
    print("Incorrect pin")