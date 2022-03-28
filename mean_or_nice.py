

##Python Version 3.9.5

#Author: Vicky Jones-Farias

#Purpose:   Demonstrating how to pass variables from function to function.

#           Remember, function_name(variable) means that we pass in the variable.
#           Return variable means we are returning variable back to the calling function.


import pygame
pygame.init()
pygame.mixer.init()

mean_sound = pygame.mixer.Sound("mean_sound.wav")
nice_sound = pygame.mixer.Sound ("nice_sound.wav")
"""
game_win_sound =
game_lose_sound = 
"""
def start(nice=0,mean=0,name=""): #controlling default values
    #get users name
    name = describe_game(name) #name variable equals value of describe_game function
    nice,mean,name = nice_mean(nice,mean,name) #3 variables equal the result of nice_mean function

def describe_game(name):
    """
    check if this is a new game or not.
    If it is new, get the user's name.
    If it is not new, thank the player for
    playing again and continue with the game.
    """

    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop == True:
            if name =="":
                name = input("\nWhat is your name? \n>>>").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted\nby several different people.\nYou can choose to be nice or mean.")
                    print("but at the end of the game your fate \nwill be sealed by your actions")
                    stop = False
    return name #take "name" and return back to function that called it

def nice_mean(nice,mean,name):
    stop = True
    while stop == True:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice\nor mean? (N/M)\n>>>: ").lower()
        if pick == "n":
            pygame.mixer.Sound.play(nice_sound)
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            pygame.mixer.Sound.play(mean_sound)
            print("\nThe stranger glares at you\nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #pass the 3 variable to the score()

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    if nice>2:
        win(nice,mean,name)
    if mean>2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nNice job {}, you win!\nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print("\nAhhhh.... too bad, game over! \n{}, you live in a beat up \nvan by the river, alone!".format(name))
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop == True:
        choice = input("Would you like to play again? y for \"yes\", n for \"no\"").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)

        if choice == "n":
            print("Sorry to see you go! Goodbye")
            stop = False
            quit()#terminates the execution of the program completely

        else:
            print("\nEnter (Y) for 'Yes', or (N) for 'No': \n>>>")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #note: I do not reset the name variable as that same user has elected to play again
    start(nice,mean,name)


    















if __name__ == "__main__":
    start()
