#Kółko i Krzyżyk THE GAME

import time


    
boardSize = 0
duelCounter = 0
players = ["PLAYER1", "PLAYER2", "CPU"]
player1 = players[0]
player2 = str()
activePlayer = player1
game = "notFinished";
session = "notFinished";
duel = "notFinished";

sessionCount = 0



def SessionDecision():
    global session 
    session = "stupid user"
    while session == "stupid user":
#    while session != "finished":
        print("Czy chcesz kontynuować? (y/n)") 
        playerInput = str(input())
        print ("Player input: " + playerInput)
        if (playerInput == "y"):
            session = "notFinished"
        elif (playerInput == "n"):
            session = "finished"
        else:
#            session = "stupid user..."
            print("Wrong input!")
        print ("Session: " + session)


#                                       GAME LOGIC


while session == "notFinished":
        SessionDecision()
        print("Po SessionDecision")
        print("Session po SessionDecision: " + session)
  
            
#                                           METHODS
            
       

        
        







