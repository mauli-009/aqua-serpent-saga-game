import win32com.client
import  datetime
import random
def say(i):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    speaker.speak(i)

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
      say("good morning")
    elif hour >= 12 and hour < 18:
        say("good afternoon")
    else:
        say("goood night")

    say("welcome to the game created by MAULI DUDHAT , lets start the game")
wishme()

user_guess=int(input("enter a your choice 1.gun ,2.snake 3.water ::"))
def user(user_guess):


    if user_guess==1 :
        say("your choice is gun")

    elif user_guess==2 :
        say("your choice is snake")

    else:
        say("your choice is water")


def comp(user_guess):
    comp_guess=random.randint(1,3)
    if comp_guess==1 and user_guess==2 :
        say("you lose,computer choice is gun")
    elif comp_guess==2 and user_guess==3:

        say("you lose,computer choice is snake")

    elif comp_guess==2 and user_guess==1 :
        say("you win, computer guess is snake")
    elif comp_guess==3 and user_guess==2 :
        say("you win,computer guess is water")
    elif comp_guess==1 and user_guess==3:
        say("you win,computer guess is gun")
    else:
        say("you lose,computer guess is water")

user(user_guess)
comp(user_guess)

