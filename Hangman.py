from turtle import *
from random import randint
import time
import math


wordBank = ['Awkward' , 'Bagpipes', 'Banjo' , 'Bungler' , 'Croquet', 'Crypt', 'Dwarves', 
            'Fervid' , 'Fishhook', 'Fjord', 'Gazebo','Gypsy','Haiku','Haphazard','Hyphen', 
            'Ivory','Jazzy','Jiffy','Jinx','Jukebox','Kayak','Kiosk','Klutz','Memento', 
            'Mystify','Numbskull','Ostracize' ,'Oxygen','Pajama','Pixel']

sWidth = 600
sHeight = 800
s = getscreen()
s.setup(sWidth, sHeight)
s.bgcolor('#90ff59')

t=getturtle()
t.color('#ffd559')
t.width(6)
tWriter = Turtle()
tWriter.color('#692cba')
tWriter.hideturtle()
t.speed(0)

tBadLetters = Turtle()
tBadLetters.hideturtle()

#variables needed to play game
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
displayText = "Have A Great Day!!!"
secretWord = ""
lettersWrong = ""
lettersCorrect = ""
fails = 10
fontSize = int(sHeight*0.05)
gameDone = False

def displayText(newText):
    tWriter.clear()
    tWriter.penup()
    tWriter.goto(-int(sWidth*0.4), -int(sHeight*0.375))
    tWriter.write(newText, font =('Arial',fontSize, 'bold'))

def displayBadLetters(newText):
    tBadLetters.clear()
    tBadLetters.penup()
    tBadLetters.goto(-int(sWidth*0.4), int(sHeight*0.375))
    tBadLetters.write(newText, font =('Arial',fontSize, 'bold'))

def chooseWord():
    global secretWord
    secretWord = wordBank[randint(0, len(wordBank) - 1)]
    print("The secret word is: " + secretWord)

def makeDisplay():
    global displayWord, secretWord
    displayWord = ""
    for letter in secretWord:
        if letter in alpha:
            if letter.lower() in lettersCorrect.lower():
                displayWord += letter + " "
            else:
                displayWord += "_" + " "

        else:
            displayWord += letter + " "

def getGuess():
    boxTitle = "Letters Used: " + lettersWrong
    guess = s.textinput(boxTitle, "Enter a guess or type $$ to guess the word")
    return guess


def checkWordGuess():
    global gameDone, fails
    boxTitle = "Guess the word!"
    guess = s.textinput(boxTitle, "Enter your guess for the word...")
    if guess.lower() == secretWord.lower():
        displayText("YOU GOT IT!!! " + secretWord + " is the word!")
        gameDone = True
    else:
        displayText("No, " + guess + " is not the word.")
        time.sleep(1)
        displayText(displayWord)
        fails -= 1
        updateHangmanPerson()

def updateHangmanPerson():
    global fails
    if fails == 9:
        drawHead()
    if fails == 8:
        drawTorso()
    if fails == 7:
        drawLleg()
    if fails == 6:
        drawRleg()
    if fails == 5:
        drawRarm()
    if fails == 4:
        drawLarm()
    if fails == 3:
        drawReye()
    if fails == 2:
        drawLeye()
    if fails == 1:
        drawSmile()
    if fails == 0:
        drawSmile()


def playGame():
    global fails, lettersCorrect, lettersWrong, alpha, gameDone
    while gameDone == False and fails > 0 and "_" in displayWord:
        
        theGuess = getGuess()
        print(theGuess) 
        if theGuess == "$$":
            #print("guess is $$")
            checkWordGuess()
        elif len(theGuess) > 1 or theGuess == "":
            #print("guess not $$ and too many letters")
            displayText("Nooo " + theGuess + " is too many letters")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess not in alpha:
            #print("guess not $$ but just one letter not alpha")
            displayText("Nooo " + theGuess + " not a letter.")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess.lower() in secretWord.lower():
            #print("letter " + theGuess + " is in word")
            lettersCorrect += theGuess.lower()
            makeDisplay()
            displayText(displayWord)
        elif theGuess.lower() not in lettersWrong.lower():
            #print("guess is not a letter in the word")
            displayText("Nooo " + theGuess + " is not in word.")
            time.sleep(1)
            lettersWrong += theGuess.lower() + ", "
            displayBadLetters("Not in word: {" + lettersWrong + "}")
            #lettersWrong += theGuess.lower() -- not needed
            displayText(displayWord)
            fails -=1
            updateHangmanPerson()
            
        else:
        #new will give error
            displayText("No!!!" + theGuess + " is already guesssed")
            time.sleep(1)
            displayText(displayWord)
            
        if fails <= 0: # if you run out of guesses
            displayBadLetters("No more guesses")
            displayText("You lose. The word was " + secretWord)
            gameDone = True
            
        if "_" not in displayWord:
            displayBadLetters("You got it!")
            gameDone = True
                
    
    
def drawGallows():
    t.setheading(0)

    t.penup()
    t.goto(-int(sWidth*0.2), -int(sHeight*0.2) )
    t.pendown()
    t.forward(int(sWidth*0.6) )

    t.left(180)
    t.forward(60)
    t.right(90)
    t.forward(420)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(50)
    
def drawHead():
    t.penup()
    t.goto(-65,160)
    t.pendown()
    t.color('#ffd559')
    t.circle(50)
    
def drawTorso():    
    t.penup()
    t.goto(-20,105)
    t.pendown()
    t.color('#ffd559')
    t.forward(110)
    
def drawLleg():
    t.penup()
    t.goto(-20,-5)
    t.pendown()
    t.color('#ffd559')
    t.left(45)
    t.forward(80)
    
def drawRleg():
    t.penup()
    t.goto(-20,-5)
    t.pendown()
    t.color('#ffd559')
    t.right(90)
    t.forward(80)
    
def drawRarm():
    t.penup()
    t.goto(-20,70)
    t.pendown()
    t.color('#ffd559')
    t.left(160)
    t.forward(80)
    
def drawLarm():
    t.penup()
    t.goto(-20,70)
    t.pendown()
    t.color('#ffd559')
    t.right(230)
    t.forward(80)
    
def drawSmile():
    t.penup()
    t.setheading(0)
    t.goto(-15,130)
    t.pendown()
    t.color('#ffd559')
    t.circle(15,90)
    
    t.penup()
    t.setheading(180)
    t.goto(-15,130)
    t.pendown()
    t.circle(-15,90)
    
def drawReye():
    t.penup()
    t.goto(-35,175)
    t.pendown()
    t.color('#ffd559')
    t.circle(3)
    
def drawLeye():
    t.penup()
    t.goto(10,175)
    t.pendown()
    t.color('#ffd559')
    t.circle(3)


drawGallows()
drawHead()
drawTorso()
drawLleg()
drawRleg()
drawRarm()
drawLarm()
drawSmile()
drawReye()
drawLeye()
hideturtle()

time.sleep(1)
t.clear()
drawGallows()
chooseWord()
makeDisplay()
displayText(displayWord)
displayBadLetters("Not in word: {" + lettersWrong + "}")
#you were playing the game here not in the main loop
#getGuess()
#checkWordGuess()
#updateHangmanPerson()
playGame()
