#Shauna Miletty
#04/25/2025
#P4Lab2
#use while loop and for loop together


#get interger from user
#determine if interger is postive or negative
#if number is positive, diplay multiplicaiton table
#if number is negative, tell user program cannot accept it
#ask user to run again?
#if yes run program
#if no, end program

run_again = "yes"

while run_again != "no":
    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        #display multiplication for that value and range (1-12)
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative values")

    run_again = input("Would you like to run the program again? ")

#loop has broken user entered 'no'
print("Program is ending......")
