#Shauna Miletty
#04/26/2025
#P4HW2
#looping salary information


"""
This program will ask user to enter employee name and pay rate,
calculate regular and overtime pay, display details,
and ask if they would like to add another employee or terminate.
At the end, it displays a final report of all employees entered.
"""

# starting totals
total_employees = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

# Ask for employee name first
employee_name = input("Enter employee's name or 'Done' to terminate: ")

# the starting loop 
while employee_name != "Done":
    # Get pay rate and hours worked
    pay_rate = float(input(f"Enter {employee_name}'s pay rate: "))
    hours_worked = float(input(f"Enter number of hours {employee_name} worked: "))

    # Calculate regular and overtime pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay

    # Display pay information for this employee
    print("\n")
    print("-----------------------------------------------")
    print(f"Employee Name: {employee_name}")
    print(f"Hours Worked: {hours_worked}")
    print(f"Pay Rate: ${pay_rate:.2f}")
    print("---------------------------------------------")
    print("Hours Worked\tPay Rate\tOver Time\tOver Time Pay\tReg Hour Pay\tGross Pay")
    print("-" * 75)
    print(f"{hours_worked:.1f}\t\t${pay_rate:.2f}\t\t{overtime_hours:.1f}\t\t${overtime_pay:.2f}\t\t${regular_pay:.2f}\t\t${gross_pay:.2f}")
    print("\n")

    # updated totals
    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    # Ask for next employee
    employee_name = input("Enter employee's name or 'Done' to terminate: ")

# After loop, show final totals
print()
print("Total number of employees entered:", total_employees)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
