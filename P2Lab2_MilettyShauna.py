#Shauna Miletty
#04/12/2025
#P2Lab2
#Using dictionaries

cars = {"Camaro" :18.21, "Prius":52.36, "Model S":110, "Silverado":26, }

#get keys from dictonary
cars_keys = cars.keys()

print(cars_keys)

print(*cars_keys, sep = ",")

#ask user to enter car name
car_name = input("Enter a Car?:")

#get mgp for the given car
car_mgp = cars[car_name]
print(f"The {car_name} gets {car_mgp} miles per gallon.")

#get miles from user
miles_driven = float(input(f"How many miles will you drive the {car_name}?"))

#calculate
gallons_needed = miles_driven/car_mgp

#Display results
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles")
