the_number = 5
guess = 0

print("You will have to a chance to guess a number.")
print("The winning number will be between 1 and 10.")
print("You have three tries.")

ran = 3

for i in range(ran):
    guess_string = input("Enter your guess: ")
    guess = int(guess_string)
    if any(c.isalpha() for c in guess_string):
        print("Your answer must be a number.")
    else:
        if guess >= 1 and guess <= 10:
            if guess < the_number:
                print("You guessed too low.")
            if guess > the_number:
                print("You guessed too high.")
        else:
            print("The guess must be between 1 and 10")


    if guess == the_number:
        print("Congratulations, you guessed the number.")
        break
    else:
        print("Sorry, you didn't guess the number. Try playing the game again.")

