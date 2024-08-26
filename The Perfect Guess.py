
import random
# Uses random module to take the number from the computer
n=random.randint(1,100)
a=-1
guesses=0
# Checking the condition
while(a!=n):
    guesses+=1
    # Taking input from the user
    a=int(input("Guess the number: "))
    if(a>n):
        print("Lower number please !")
    else:
        print("Higher number please !")
# Printing the number of attempts after guessing the number
print(f"You have guessed the number correctly in {guesses} attempts")
        