# import os
# if __name__=='__main__':
#     print("Welcome to Robo Speaker ")
#     x=input("Enter what you want me to speak")
#     command=f"say {x}"
#     os.system(command)
# import pyttsx3

# if __name__ == '__main__':      
#     print("Welcome to Robo Speaker ")
#     # if(x=='q'):
#     #     break
    
#     while True:
#         x = input("Enter what you want me to speak (q to exit): ")
#         if x=='q':
#             print("Exiting the Robo Speaker")
#             break
#         # Initialize text-to-speech engine
#         engine = pyttsx3.init()

#         # Speak the text
#         engine.say(x)
#         engine.runAndWait()
import pyttsx3          
def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
def poem():
    return '''Twinkle Twinkle little start
How i wonder what you are
Up about the world so high
Like a diamond in the sky'''

def story():
    return '''Once upon a time. There was a crow.He was very thirsty. He flew here and there in search of water.
He saw a pot in the garden. There was a little water in it. He could not drink it. He thought of a plan.
He put some stones into it. The water rose up. He drank it and flew away
MORAL: 
	NECESSITY IS THE MOTHER OF INVENTION'''
def wrong():
    return '''Something went wrong 
Please enter a valid key and then try again'''
if __name__=='__main__':
    welcome="Welcome to the robo speaker"
    intro="Please tell me what you want me to speak "
    speak(welcome)
    speak(intro)
    while True:
        n=input("Enter what you want me to sing\n (Type 's' for song, 'p' for poem, 'st' for story) or (Press 'q' to exit): ")
        # speak(n)
        if n.lower()=='q':
            thanks='''Thank you for using Robo Speaker.
            Have a nice day!'''
            speak(thanks)
            break
        if n.lower()=='s':
            song="i don't remember song at this time, Please try again later"
            speak(song)
        elif n.lower()=='p':
            speak(poem())
        elif n.lower()=='st':
            speak(story())
        else:
            speak(wrong())
        
            
    
    