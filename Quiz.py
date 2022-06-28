from ast import And
from doctest import SkipDocTestCase
from tkinter import *
import random
from tkinter import scrolledtext
from tkinter.font import Font
from unittest import skip
from kivy import require
from matplotlib.markers import MarkerStyle
from matplotlib.pyplot import close
from numpy import append

def establishLists():
    global questionsList
    global resultsMsg
    global markList
    global requiredScore
    questionsList = [["Earth is the 3rd planet from the Sun.","True","False"],["How many days does it take for the Earth to revolve around the Sun?","365","366","364","356"],["How long does it take for the Earth to fully rotate around its own axis?","24 hours","25 hours","23 hours","42 hours"],["The moon takes 29.5 days to complete one orbit around the Earth.","True","False"],["Why does the Moon have a greater effect on tides\non Earth compared to the Sun?","Because the Moon is closer to the Earth","Because the Sun is too hot","Because the Moon is smaller","Because the Sun is bright"],["Who was the first human to set foot on the Moon?","Neil Armstrong","Sergey Korsakov","Robert Hines","Samantha Cristoforetti"],["How many kilometres is 1 Astronomical Unit (A.U.)?","150 000 000 km","100 000 000 km","999 999 999 km","500 000 km"],["The moon produces light of its own.","False","True"],["'Gibbous' is used to describe the Moon when more than half (but not all)\nof the Moon is illuminated.","True","False"],["'Waxing' is used to describe the area of the Moon you can see\nbecoming larger each night.","True","False"],["'Waning' is used to describe the area of the Moon you can see\nbecoming smaller each night.","True","False"],["What causes the seasons on Earth?","The Earth's tilt with respect to the Sun","The gravitational pull of the Sun","The speed of which the Earth orbits the Sun","The distance between the Earth and the Sun"],["Regular changes in sea levels (tides) occur due to the\ngravitational pull of the Moon and the Sun.","True","False"],["Which two pieces of evidence did people use to believe that the\nApollo 11 Moon landing was a hoax?","The flag and the stars","The flag and the Sun","The stars and the Sun","Their footprints and astronaut suits"],["How many phases of the Moon are there?","8","6","12","10"],["Which element does the Sun consume to release energy?","Hydrogen","Carbon","Nitrogen","Oxygen"],["Sunspots are areas that appear dark on the Sun.","True","False"],["Which of the following is Pluto considered as?","A dwarf planet","A planet","An asteroid","A comet"],["Astrology is a psuedoscience.","True","False"],["How many planets are there in our solar system?","8","4","15","9"]]
    resultsMsg = ["TOUGH LUCK!","NICE TRY!","WELL DONE!","SPECTACULAR!","Invalid"]
    markList = ["NOT ACHIEVED","ACHIEVED","MERIT","EXCELLENCE"]
    requiredScore = [0,4,7,10,12]
    setUp()

def detQstns():
    global root
    root.destroy()
       
    global qLCV
    qLCV = 0
   
    global questions
    questions = random.sample(questionsList,15)

    global totQstns
    totQstns = 12

    global score
    score = 0 

    global skipCount
    skipCount = 0

    global ansOne
    global ansTwo
    global ansThree
    global ansFour
    global skipBut

    while qLCV < totQstns:
        global qRoot
        qRoot = Tk()
        qRoot.title("BALAZO SCIENCE QUIZ")
        qRoot.configure(bg="#4a86e8")
        qRoot.geometry('1000x700')
        pageFont = Font(family="Calibri", size=20, weight="bold")

        qLabel = Label(qRoot, text="Question "+str(qLCV+1-skipCount)+"."+"\n"+questions[qLCV][0], font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=80, pady=25)
        qLabel.place(x=500, y=100,anchor="center")
            
        exitBut = Button(qRoot, text="EXIT", font=pageFont, fg="#ffffff", bg="#cc0000", padx=80, pady=5, borderwidth=0, command=exit)
        exitBut.place(x=100, y=600)

        if skipCount < 3:
            skipBut = Button(qRoot, text="SKIP", font=pageFont, fg="#ffffff", bg="#6aa84f", padx=80, pady=5, borderwidth=0, command=skipQstn)
            skipBut.place(x=700, y=600)
        
        if len(questions[qLCV]) == 5:
            global temp
            temp = []
            temp.append(questions[qLCV][1])
            temp.append(questions[qLCV][2])
            temp.append(questions[qLCV][3])
            temp.append(questions[qLCV][4])
            temp = random.sample(temp, len(temp))
            
            ansOne = Button(qRoot, text=temp[0], font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=80, pady=5, borderwidth=0, command=lambda:calcScore(0))
            ansOne.place(x=270, y=400)

            ansTwo = Button(qRoot, text=temp[1], font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=80, pady=5, borderwidth=0, command=lambda:calcScore(1))
            ansTwo.place(x=500, y=400)

            ansThree = Button(qRoot, text=temp[2], font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=80, pady=5, borderwidth=0, command=lambda:calcScore(2))
            ansThree.place(x=270, y=500)

            ansFour = Button(qRoot, text=temp[3], font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=80, pady=5, borderwidth=0, command=lambda:calcScore(3))
            ansFour.place(x=500, y=500)
        
        else:
            temp = []
            temp.append(questions[qLCV][1])
            temp.append(questions[qLCV][2])
            temp = random.sample(temp, len(temp))
            ansOne = Button(qRoot, text=temp[0], font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=80, pady=5, borderwidth=0, command=lambda:calcScore(0))
            ansOne.place(x=270, y=400)

            ansTwo = Button(qRoot, text=temp[1], font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=80, pady=5, borderwidth=0, command=lambda:calcScore(1))
            ansTwo.place(x=500, y=400)
                    

        qRoot.mainloop()
        qLCV += 1
    
    calcMark()

def skipQstn():
    global skipCount
    skipCount += 1
    
    global totQstns
    totQstns +=1
    
    qRoot.destroy()

def setUp():
    global root
    root = Tk()
    root.title("BALAZO SCIENCE QUIZ")
    root.configure(bg="#4a86e8")
    root.geometry('1000x700')

    global pageFont
    pageFont = Font(family="Calibri", size=20, weight="bold")

    menuTitle = Label(root, text="BALAZO SCIENCE QUIZ", font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=80, pady=25)
    menuTitle.place(x=300, y=60)

    menuPlay = Button(root, text="PLAY", font=pageFont, fg="#ffffff", bg="#6aa84f", padx=130, pady=5, borderwidth=0, command=detQstns)
    menuPlay.place(x=340, y=500)

    menuExit = Button(root, text="EXIT", font=pageFont, fg="#ffffff", bg="#cc0000", padx=134, pady=5, borderwidth=0, command=exit)
    menuExit.place(x=340, y=580)

    root.mainloop()

def calcScore(answer):
    pageFont = Font(family="Calibri", size=20, weight="bold")
    global score

    if temp[answer] == questions[qLCV][1]:
        ansMsg = Label(qRoot, text="Correct!", font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=80, pady=5, borderwidth=0,)
        ansMsg.place(x=400, y=200)
        score += 1

    else:
        ansMsg = Label(qRoot, text="Incorrect!", font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=80, pady=5, borderwidth=0,)
        ansMsg.place(x=400, y=200) 
    
    ansOne.destroy()
    ansTwo.destroy()

    if skipCount < 3:
        skipBut.destroy()

    if len(questions[qLCV]) == 5:
        ansThree.destroy()
        ansFour.destroy()

    nextBut = Button(qRoot, text="NEXT", font=pageFont, fg="#ffffff", bg="#6aa84f", padx=80, pady=5, borderwidth=0, command=nextQstn)
    nextBut.place(x=700, y=600)

def nextQstn():
    qRoot.destroy()

def retry():
    resultsRoot.destroy()
    establishLists()


def calcMark():
    global endMsg
    global overallMark
    global resultsRoot
    resultsRoot = Tk()
    resultsRoot.title("BALAZO SCIENCE QUIZ")
    resultsRoot.configure(bg="#4a86e8")
    resultsRoot.geometry('1000x700')
    pageFont = Font(family="Calibri", size=20, weight="bold")

    if score >= requiredScore[0] and score < requiredScore[1]:  
        overallMark = markList[0]
        endMsg = resultsMsg[0]
    elif score >= requiredScore[1] and score < requiredScore[2]:
        overallMark = markList[1]
        endMsg = resultsMsg[1]
    elif score >= requiredScore[2] and score < requiredScore[3]:
        overallMark = markList[2]
        endMsg = resultsMsg[2]
    elif score >= requiredScore[3] and score <= requiredScore[4]:
        overallMark = markList[3]
        endMsg = resultsMsg[3]
    else:
        endMsg = resultsMsg[4]
        overallMark = "Invalid"
    
    endTitle = Label(resultsRoot, text="QUIZ FINISHED!", font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=80, pady=25)
    endTitle.place(x=300, y=60)

    endResults = Label(resultsRoot, text="QUESTIONS CORRECT:\n"+str(score)+"/12\n\nOVERALL MARK:\n"+str(overallMark)+"\n\n"+str(endMsg), font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=80, pady=25)
    endResults.place(x=300, y=400)

    retryBut = Button(resultsRoot, text="RETRY", font=pageFont, fg="#ffffff", bg="#6aa84f", padx=80, pady=5, borderwidth=0, command=retry)
    retryBut.place(x=100, y=600)

    exitBut = Button(resultsRoot, text="EXIT", font=pageFont, fg="#ffffff", bg="#cc0000", padx=80, pady=5, borderwidth=0, command=exit)
    exitBut.place(x=700, y=600)

establishLists()



