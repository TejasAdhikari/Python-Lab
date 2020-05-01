class atm:

    def __init__(self, name):
        self.name = name

    def account_info(self):
        print("\nName:", name)
        print("Account Number:", data[name][0])
        print("Mobile Number:", data[name][1])
        print("Balance:", data[name][3])

    def pin_change(self):
        while 1:
            p1 = int(input("\nEnter the new PIN: "))
            p2 = int(input("Enter the PIN again: "))
            if p1 == p2:
                print("Your PIN has been changed to: ", p1)
                data[name][2] = p1
                break
            else:
                print("PINs don't match")

    def balance_inquiry(self):
        print("\nYour Balance is: ", data[name][3])

    def withdraw(self):
        w = int(input("\nEnter the Amount to be Withdrawn: "))
        data[name][3] -= w
        print("Your balance is: ", data[name][3])

    def deposit(self):
        d = int(input("\nEnter the Amount to be Deposited: "))
        data[name][3] += d
        print("Your balance is: ", data[name][3])

data = {"ABC":[5212485412,123454562,4545,10000], "DEF":[5212485413,123454563,1234,100000], "GHI":[5212485414,123454564,4321,20000], "JKL":[5212485415,123454565,5678,200000], "MNO":[5212485416,123454566,8765,1000000]}
name = input("Enter your name: ")
if name in data:
    a = atm(name)
    trials = 1
    while trials < 4:
        pin = int(input("Enter your PIN: "))
        if pin == data[name][2]:
            while 1:
                choice = int(input("\n1.Account Information \n2.PIN Change \n3.Balance Inquiry \n4.Withdrawal \n5.Deposit \n6.EXIT \nEnter Choice: "))
                if choice == 1:
                    a.account_info()
                elif choice == 2:
                    a.pin_change()
                elif choice == 3:
                    a.balance_inquiry()
                elif choice == 4:
                    a.withdraw()
                elif choice == 5:
                    a.deposit()
                elif choice == 6:
                    print("Task Done")
                    quit()
                else:
                    print("Wrong Choice")
        else:
            if trials == 4:
                del data[name]
                print("Wrong PIN entered three times\nAccount Deleted")
            else:
                print("Wrong PIN\nEnter Again")
                trials+=1
else:
    print("Name not found in the Database")