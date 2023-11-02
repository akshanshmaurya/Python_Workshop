import random 
def guess_number():
    return random.randint(1,100)

target_number = guess_number()
attempts = 0

while True:
    user_guess = int(input("Guess The Number: "))
    attempts+=1

    if user_guess == target_number:
        print("Congratulation you have guessed the number in",attempts,"attempts.")
        break
    elif user_guess < target_number:
        print("Try a higher no.")
    elif user_guess > target_number:
        print("Try a lower no.")

