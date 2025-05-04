#Shauna Miletty
#05/05/2025
#P5Lab1
#Using user-defined functions
import random

def dispersed_change(change):

    #convert the value to a integer
    change = round(change * 100)
    print(f"Change Amount as an interger: {change}")

    #determine how many coins are needed
    num_dollars = change // 100
    change= change - (num_dollars * 100)

    num_quarters = change // 25
    change= change - (num_quarters * 25)

    num_dimes = change // 10
    change= change - (num_dimes * 10)

    num_nickels = change // 5
    change= change - (num_nickels * 5)

    num_pennies = change

    #determine

    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} Dollar")
        else:
            print(f"{num_dollars} Dollars")

    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} Quarter")
        else:
            print(f"{num_quarters} Quarters")

    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes} Dime")
        else:
            print(f"{num_dimes} Dimes")

    if num_nickels > 0:
        if num_nickels == 1:
            print(f"{num_nickels} Nickel")
        else:
            print(f"{num_nickels} Nickels")

    if num_pennies > 0:
        if num_pennies == 1:
            print("f{num_pennies} Penny")
        else:
            print(f"{num_pennies} Pennies")


def main():
    #logic goes here

    #generate the amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed:.2f}")

    #ask about amount of money put in
    money_in = float(input("How much cash will you put in the self-checkout? "))

    #calculate change owed to the customer
    change = money_in - amount_owed
    print(f"Change owed: ${change:.2f}")

    #call the disperse_change function
    dispersed_change(change)
    
#call the main function
main()


    
