# # Define the variables
# number1 = 10
# number2 = 5

# # Perform basic arithmetic operations
# addition = number1 + number2
# subtraction = number1 - number2
# multiplication = number1 * number2

# # Print the results in the specified format
# print(f"Addition of {number1} and {number2} is {addition}")
# print(f"Subtraction of {number1} and {number2} is {subtraction}")
# print(f"Multiplication of {number1} and {number2} is {multiplication}")
# purchase_amount = float(input("Enter your purchase amount: "))

# if purchase_amount >= 1000:
#   discount = 0.1  # 10% discount
# elif purchase_amount >= 500:
#   discount = 0.05  # 5% discount
# else:
#   discount = 0  # No discount

# final_price = purchase_amount * (1 - discount)
# print("Final price after discount: $" + str(final_price))

# message = "good" if purchase_amount >= 10 else " bad"
# print (message)

# days = input("Enter any day of the week: ").lower()

# match days:
#     case "monday" | "tuesday":
#         message = "Good is Good"
#     case "wednesday":
#         message="Wednesday is good"
#     case _:
#         message="wrong inpute"
        
# print(message)

import random
def playgame():
    guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it"))
    

secret_number = random.randint(1,10)

match guess:
    case guess if guess == secret_number:
        message = "You got the secret number"
    case guess if guess > secret_number:
        message ="Your guess is greater than the number"
    case guess if guess < secret_number:
        message = "Guess is lesser that the number"
        
    case _ :
        message = "You just enter a wrong value"
        
print(message)