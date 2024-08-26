import random
'''
1 for snake
-1 for water
0 for gun
'''
# Uses random module for computer choice
computer=random.choice([-1,0,1])
# Taking the choice from the user
youstr=input("Enter your choice: (s/w/g) :  ")

youDict={"s":1,"w":-1,"g":0}
# Reverse Dictionary for 
reverseDict={1:"Snake",-1:"Water",0:"Gun"}

you=youDict[youstr]

# By now we have two numbers (variables), you and computer

print(f"You choose :    {reverseDict[you]}\nComputer choose :   {reverseDict[computer]}")
if(computer==you):
    print("Result:  It's a draw!")
else:
    if(computer==-1 and you ==1):
        print("Result:      You win!")
        print("Congratulations !")
    elif(computer==-1 and you==0):
        print("Result:      You lose!")
        print("Better luck next time !")
    elif(computer==1 and you ==-1):
        print("Result:      You lose!")
        print("Better luck next time !")
    elif(computer==1 and you==0):
        print("Result:      You win!")
        print("Congratulations !")
    elif(computer==0 and you==-1):
        print("Congratulations !")
        print("Result:      You win!")
    elif(computer==0 and you==1):
        print("Better luck next time !")
        print("Result:      You lose!")
    
    else:
        print("Something went wrong!")