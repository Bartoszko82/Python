#Kółko i Krzyżyk THE GAME

import time


    
boardSize = int()
players = ["PLAYER1", "PLAYER2", "CPU"]
player1 = players[0]
player2 = str()
activePlayer = player1
game = "notFinished";
session = "notFinished";
duel = "notFinished";
moveCounter = 0
duelCounter = 1

def WelcomeSign():
    print()
    print("             WELCOME TO NEW GAME")
    print()
    

def ChooseBoardSize():
    global boardSize
    numberOfTries = 0
    
    while boardSize != 3 and boardSize != 5:
        print()
        print(">>> Podaj rządaną wielkość planszy (3 lub 5 pól)")
        try: 
            boardSize = int(input())
        except ValueError:
            print("Invalid number")  
        numberOfTries = numberOfTries + 1
        if numberOfTries >= 5:
            boardSize = 3
    print("Wybrana wielkość planszy: " + str(boardSize))
    print()
            
            
def ChooseSecondPlayer():
    global player2
    numberOfTries = 0
    
    while player2 != "PLAYER2" and player2 != "CPU":
        print()
        print(">>> Wybierz drugiego gracza (1 - PLAYER2, 2 - CPU)")
        try:
            chosenNumber = int(input())
        except ValueError:
            print("Invalid number")

        if (chosenNumber == 1): #  TU SIĘ WYWALA JAK UZYSZKODNIK PODA LITERE
            player2 = players[1]
        else:
            player2 = players[2]
            
        numberOfTries = numberOfTries + 1
        if numberOfTries >= 5:
            player2 = players[2]
            
    print("Wybrałeś drugiego gracza: " + player2)
    print()

    
def DrawBoard(): #DO ZAIMPLEMENTOWANIA/PRZENIESIENIA
    print()
    print("Simple drawing board placeholder implementation")
    print()

   
def PlayersMove(): #DO ZAIMPLEMENTOWANIA 
    global activePlayer
    print(activePlayer + "`s turn")
    #    DODAĆ TIMER
    
def SwitchPlayers():
    global player1
    global player2
    global activePlayer
    
    if (activePlayer == player1):
        activePlayer = player2
    else:
        activePlayer = player1
        
        

def DuelDecision(): #DO ZAIMPLEMENTOWANIA
    global duel
    global moveCounter
    
    if (moveCounter >= 5):
        duel = "finished"
    moveCounter = moveCounter + 1 
    
    
def SingleDuel():
    global duelCounter
        
    print()
    print(">>>>> Zaczyna się rozgrywka nr: " + str(duelCounter) + " <<<<<")
    print()
    
    print("Simple single game placeholder implementation")
    
    while duel == "notFinished":
        PlayersMove()
        SwitchPlayers()
        DuelDecision()
    
    print()
    print(">>>>> Koniec rozgrywki nr: " + str(duelCounter) + ", wygrał: <<<<<")
    print()
    
    duelCounter = duelCounter + 1
          

def ShowStats(): #    DO ZAIMPLEMENTOWANIA
    print()
    print("Showing stats placeholder")
    print()

def SessionDecision():  #    DO POPRAWY (DODAĆ RESET PLANSZY)
    global duel
    global moveCounter
    global session
    
    session = "stupid user"
    while session == "stupid user":
        print()
        print(">>> Czy chcesz kontynuować? (y/n)") 
        playerInput = str(input())
        if (playerInput == "y"):
            session = "notFinished"
            print("[DEBUG] session not finished")
        elif (playerInput == "n"):
            session = "finished"
            print("[DEBUG] session finished")
        else:
            print("Wrong input!")
        
        duel = "notFinished"
        moveCounter = 0
        print("[DEBUG] resetting: duel = 'notFinished', moveCounter = 0")
         #            reset drawing board
        print()

def GameDecision(): 
    global game
    global session
    global boardSize
    global player2
    global duelCounter
    global moveCounter
    
    game = "stupid user"
    while game == "stupid user":
        print()
        print(">>> Czy chcesz wyjść z programu? (y/n)")
        playerInput = str(input())
        if playerInput == "y":
            game = "finished"
            print()
            print("             THANK YOU FOR PLYNG THAT GAME")
            print("                     BYE BYE!")
            print()
        elif playerInput == "n":
            game = "notFinished"
            session = "notFinished"
            boardSize = 0
            player2 = str();
            activePlayer = player1
            duelCounter = 1
            moveCounter = 0
            print("[DEBUG] game not finished")
            print("[DEBUG] resetting: session = 'notFinished', moveCounter = 0, duelCounter = 0")
            print("[DEBUG] resetting boardSize and player2: ")
        else:
            Print("Wrong input!")
        print()
    
#                                       GAME LOGIC

while game == "notFinished":
    WelcomeSign()
    ChooseBoardSize()
    ChooseSecondPlayer()
        
    while session == "notFinished":
        DrawBoard()
        SingleDuel()
        ShowStats()
        SessionDecision()
                        
    GameDecision()

            
       

        
        







