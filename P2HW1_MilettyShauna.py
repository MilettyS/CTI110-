#MilettyShauna
#04/12/2025
#P2HW2
#Calculate and display math expressions



#ask user what their budget is
print("This program calculates and displays travel expenses")

budget = float(input("Enter Budget: "))

destination = input("Enter your travel destination: ")

gas = float(input("How much do you think you will spend on gas?: "))

travel = float(input("How much will you need for accomodation/hotel?: "))

food = float(input("How much do you need for food?: "))
             
#calculate the balance
total_expenses = gas + travel + food
remaining_balance = budget - total_expenses

#display results

print("---------Travel Expenses----------")
print(f"{'Location:':20} {destination}")
print(f"{'Initial Budget:':20} ${budget:.2f}")
print(f"{'Gas:':20} ${gas:.2f}")
print(f"{'Accomodation:':20} ${travel:.2f}")
print(f"{'Food:':20} ${food:.2f}")
print("---------------------------------------")
print(f"{'Remaining Balance:':20} ${remaining_balance:.2f}")
