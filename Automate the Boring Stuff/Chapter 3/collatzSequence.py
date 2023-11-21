# Practice project from Chapter 3 of Automate the Boring Stuff

# Create a function that will do the following:
# Write a function named collatz() that has one parameter named number. 
# If number is even, then collatz() should print number // 2 and return this value. 
# If number is odd, then collatz() should print and return 3 * number + 1.

def collatz(number):

    # Checks if number is even by seeing if there is no remainder when dividing by 2
    if number % 2 == 0:
        # Divides the number by 2 and prints it.
        number = number / 2
        print(number)
        
        # Returns the number after it has been modified.
        return number

    # Performs seperate operation on a number if it is odd.
    else:
        number = 3 * number + 1
        print(number)
        
        # Returns the number after it has been modified.
        return number

print('Enter number:')

userNumber = int(input())

while True:
    userNumber = collatz(userNumber)

    if userNumber == 1:
        break        