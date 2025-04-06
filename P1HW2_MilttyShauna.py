#Shauna Miletty
#April,5,2025
#P1HW2
#ask about budget and calulate expenses

#ask user to enter their budget
budget=input("Enter your budget: ")
print("\n")

#ask user their travel destination
destination=input("Enter your travel desination: ")
print("\n")

#ask the user about expenses

gas=input("How much will you spend on gas? ")
hotel=input("How much will you need for accomodation/hotel? ")
food=input("How much will you spend on food? ")

#add up expenses
total_expenses=gas + hotel + food

#subtract expenses from budget
remaining_balance=budget-total_expenses

#display

print("-----Travel Expenses------")
print("Initial Budget" budget")
print("\n")
print("Fuel:"",gas ")
print("Accomodation: "",hotel")
print("Food: "", food")
print("\n")
print("Remaining Balance:, ")
