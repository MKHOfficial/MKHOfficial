'''
rock  1
paper -1
scissor 0
'''
import random
# taking computer's choice
Computer=random.choice([-1,0,1])
# Taking user's choice
print("\n's' for scissor,'r' for rock,'p' for paper ")
Youstr= input("Enter your choice:")
youDict={"r":1,"p":-1,"s":0}

you=youDict[Youstr]

# reverse Dictionary
reverseDict={1:"Rock",-1:"Paper",0:"Scissor"}

# printing your's and computer's choice
print(f"You choose: {reverseDict[you]}\nComputer choose: {reverseDict[Computer]}")
# Checking the condition
if(Computer==you):
    print("It's draw!")

else:
    if(Computer==1 and you==-1):
        print("Result:  You lose !")
    elif(Computer==1 and you==0):
        print("Result:  You lose!")
    elif(Computer==-1 and you==1):
        print("Result:  You lose!")
    elif(Computer==-1 and you==0):
        print("Result:  You win!")
    elif(Computer==0 and you==1):
        print("Result:  You win!")
    elif(Computer==0 and you==-1):
        print("Result:  You lose!")
    
    else:
        print("Something went wrong !") 

# Short way of the logic
    # if(Computer-you==-1):
    #     print("You win!")
    # else:
    #     print("You lose!")