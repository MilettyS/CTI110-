#MilettyShauna
#04/18/2024
#P3HW2
#elvautate emplyee information

#request employee info
name= input("enter employee name ")
hours_worked = float(input("Enter number of hours worked?: "))
pay_rate = float(input("Enter employees pay rate; "))

#evaluate overtime
if hours_worked >40:
    #calculate overtime
    overtime_hours = hours_worked -40
    #calculate overpay
    over_pay = overtime_hours * (pay_rate * 1.5)
    #calcuate regular hours
    reg_pay = 40 * pay_rate

else:
    over_pay = 0
    overtime_hours = 0
    reg_pay = hours_worked * pay_rate

#calcuate gross pay
gross_pay = reg_pay + over_pay

#output
print("\n")
print("-----------------------------------------------")
print("Employee name: ", name,)
print("Hours worked: ", hours_worked,)
print("Enter employees pay rate: ", pay_rate,)
print("-----------------------------------------------")
print(f"Employee Name:\t{name}")
print("\n")
print("Hours Worked\tPay Rate\tOver Time\tOver Time Pay\tRegHour Pay\tGross Pay")
print("-" * 100)
print(f"{hours_worked:.1f}\t\t${pay_rate:.2f}\t\t{overtime_hours:.1f}\t\t${over_pay:.2f}\t\t${reg_pay:.2f}\t\t$f{gross_pay:.2f}")
