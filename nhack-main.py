rint("This is the money management feature. It helps you manage your finance using the 50-30-20 rule, \n \nBut we tweak it a little.")
print("\n50% of your money will be alloted to spend, 30% of your money can be used to loan out to your frieds or donate to charity \n20% will be used to invest")
print("\nThis feature aims on helping make teens financially aware and independent. \nIt teaches the young minds to be prepared for the future and teaches them real time skills.")

import time

balance = int(input("Enter your balance: "))
overide = int(input("Enter your override code: "))
print("")
expenditure = (balance / 100) * 50
giving = (balance / 100) * 30
invest = (balance / 100) * 20

while True:
    print("Welcome. Your amount is AED: ", balance)
    print("1. Send money")
    print("2. Recieve money")
    print("3. Invest money")

    ask = int(input("What would you like to do? "))
    if ask == 1:
        q1 = int(input("Would you like to \n1. Send money to your friends  \n2. Donate to charity? "))
        if q1 == 1:
            name = input("Enter user's name: ")
            sent = int(input("How much money would you like to send? "))
            if sent <= giving:
                balance -= sent
                expenditure = (balance / 100) * 50
                giving = (balance / 100) * 30
                invest = (balance / 100) * 20
                time.sleep(3)
                print("You have successfully sent ", sent, "to the user: ", name, "and your balance is: ", balance)
            elif sent > giving:
                code = int(input("You have to use the override code as this is against the financial management system algorithm: "))
                if code == overide:
                    time.sleep(3)
                    balance -= sent
                    time.sleep(3)
                    print("You have successfully sent ", sent, "to the user: ", name)
                else:
                    time.sleep(3)
                    print("Wrong code. Cannot execute")

             
    elif ask == 2:
        inq1 = input("Which user is sending money? ")
        inq2 = int(input("How much money have you recieved? "))
        balance += inq2
        print(inq1, "has sent you", inq2, "and your balance now is: ", balance)
        expenditure = (balance / 100) * 50
        giving = (balance / 100) * 30
        invest = (balance / 100) * 20


    elif ask == 3:
        print("1. Raytheon's stock has risen 4.64% since the past week")
        print("2. General Motor's stock has taken a dip of 1.92% in the past week")
        print("3. TATA has recently undergone a merger with Bajaj and its stock has risen by a whoopping 10.07%")
        print("Price of each stock is AED 20")
        in1 = int(input("Which stock would you like to purchase: "))
        if in1 == 1:
            in2 = int(input("How many stocks would you like to buy? "))
            bought = in2 * 20
            balance -= bought
            expenditure = (balance / 100) * 50
            giving = (balance / 100) * 30
            invest = (balance / 100) * 20
            time.sleep(3)
            print("You have successfully purchased", in2, "stocks of Raytheon. Your balance is: ", balance)
        elif in1 == 2:
            in2 = int(input("How many stocks would you like to buy? "))
            bought = in2 * 20
            balance -= bought
            expenditure = (balance / 100) * 50
            giving = (balance / 100) * 30
            invest = (balance / 100) * 20
            time.sleep(3)
            print("You have successfully purchased", in2, "stocks of General motors. Your balance is: ", balance)
        elif in1 == 3:
            in2 = int(input("How many stocks would you like to buy? "))
            bought = in2 * 20
            balance -= bought
            expenditure = (balance / 100) * 50
            giving = (balance / 100) * 30
            invest = (balance / 100) * 20
            time.sleep(3)
            print("You have successfully purchased", in2, "stocks of Tata. Your balance is: ", balance)
    ask3 = input("Would you like to continue? Yes = 'Y' and No = 'N' ")
    if ask3 == "Y":
        continue
    elif ask3 == "N":
        break
