
#Imports Python tools and systems that allow for the GUI and random elements of the code.
from tkinter import *
import random
from tkinter.font import Font

#Function that establishes the quiz questions and answers, end messages, score requirements and marks lists. 
def establishLists():
    global questionsList
    global resultsMsg
    global markList
    global requiredScore    

    #Total number of questions can be changed based on the number of skips used during execution therefore this is not stored as a constant.
    global totQstns
    totQstns = 12
    
    questionsList = [["Earth is the 3rd planet from the Sun.","True","False"],["How many days does it take for the Earth to revolve around the Sun?","365","366","364","356"],["How long does it take for the Earth to fully rotate around its own axis?","24 hours","25 hours","23 hours","42 hours"],["The moon takes 29.5 days to complete one orbit around the Earth.","True","False"],["Why does the Moon have a greater effect on tides\non Earth compared to the Sun?","Because the Moon is closer to the Earth","Because the Sun is too hot","Because the Moon is smaller","Because the Sun is bright"],["Who was the first human to set foot on the Moon?","Neil Armstrong","Sergey Korsakov","Robert Hines","Samantha Cristoforetti"],["How many kilometres is 1 Astronomical Unit (A.U.)?","150 000 000 km","100 000 000 km","999 999 999 km","500 000 km"],["The moon produces light of its own.","False","True"],["'Gibbous' is used to describe the Moon when more than half (but not all)\nof the Moon is illuminated.","True","False"],["'Waxing' is used to describe the area of the Moon you can see\nbecoming larger each night.","True","False"],["'Waning' is used to describe the area of the Moon you can see\nbecoming smaller each night.","True","False"],["What causes the seasons on Earth?","The Earth's tilt with respect to the Sun","The gravitational pull of the Sun","The speed of which the Earth orbits the Sun","The distance between the Earth and the Sun"],["Regular changes in sea levels (tides) occur due to the\ngravitational pull of the Moon and the Sun.","True","False"],["Which two pieces of evidence did people use to believe that the\nApollo 11 Moon landing was a hoax?","The flag and the stars","The flag and the Sun","The stars and the Sun","Their footprints and astronaut suits"],["How many phases of the Moon are there?","8","6","12","10"],["Which element does the Sun consume to release energy?","Hydrogen","Carbon","Nitrogen","Oxygen"],["Sunspots are areas that appear dark on the Sun.","True","False"],["Which of the following is Pluto considered as?","A dwarf planet","A planet","An asteroid","A comet"],["Astrology is a pseudoscience.","True","False"],["How many planets are there in our solar system?","8","4","15","9"]]
    resultsMsg = ["TOUGH LUCK!","NICE TRY!","WELL DONE!","SPECTACULAR!","Invalid"]
    markList = ["NOT ACHIEVED","ACHIEVED","MERIT","EXCELLENCE"]
    requiredScore = [0,4,7,10,12]
    setUp()

#Function that randomises questions and creates question pages. 
def detQstns():
    global root
    root.destroy()
       
    global qLCV
    qLCV = 0
   
    global questions
    questions = random.sample(questionsList, len(questionsList))

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
            
        exitBut = Button(qRoot, text="EXIT", font=pageFont, fg="#ffffff", bg="#cc0000", padx=135, pady=5, borderwidth=0, command=exit)
        exitBut.place(x=20, y=580)

        if skipCount < 3:
            skipBut = Button(qRoot, text="SKIP", font=pageFont, fg="#ffffff", bg="#6aa84f", padx=135, pady=5, borderwidth=0, command=skipQstn)
            skipBut.place(x=645, y=580)
        
        if len(questions[qLCV]) == 5:
            global temp
            temp = []
            temp.append(questions[qLCV][1])
            temp.append(questions[qLCV][2])
            temp.append(questions[qLCV][3])
            temp.append(questions[qLCV][4])
            temp = random.sample(temp, len(temp))
            
            loop = 0 
            while loop < (len(temp)):
                if len(temp[loop]) > 21:
                    smallFont = Font(family="Calibri", size=15, weight="bold")
                    evenPlacement = 730
                    oddPlacement = 270
                    loop += 10
                else:
                    smallFont = Font(family="Calibri", size=20, weight="bold")
                    evenPlacement = 630
                    oddPlacement = 370 
                loop += 1
            
            ansOne = Button(qRoot, text=temp[0], font=smallFont, fg="#4a86e8", bg="#cfe2f3", padx=30, pady=30, borderwidth=0, command=lambda:calcScore(0))
            ansOne.place(x=oddPlacement, y=300, anchor="center")

            ansTwo = Button(qRoot, text=temp[1], font=smallFont, fg="#4a86e8", bg="#cfe2f3", padx=30, pady=30, borderwidth=0, command=lambda:calcScore(1))
            ansTwo.place(x=evenPlacement, y=300, anchor="center")

            ansThree = Button(qRoot, text=temp[2], font=smallFont, fg="#4a86e8", bg="#cfe2f3", padx=30, pady=30, borderwidth=0, command=lambda:calcScore(2))
            ansThree.place(x=oddPlacement, y=440, anchor="center")

            ansFour = Button(qRoot, text=temp[3], font=smallFont, fg="#4a86e8", bg="#cfe2f3", padx=30, pady=30, borderwidth=0, command=lambda:calcScore(3))
            ansFour.place(x=evenPlacement, y=440, anchor="center")
        
        else:
            temp = []
            temp.append(questions[qLCV][1])
            temp.append(questions[qLCV][2])
            temp = random.sample(temp, len(temp))
            
            ansOne = Button(qRoot, text=temp[0], font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=80, pady=30, borderwidth=0, command=lambda:calcScore(0))
            ansOne.place(x=380, y=400, anchor="center")

            ansTwo = Button(qRoot, text=temp[1], font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=80, pady=30, borderwidth=0, command=lambda:calcScore(1))
            ansTwo.place(x=620, y=400, anchor="center")
                    

        qRoot.mainloop()
        qLCV += 1
    
    calcMark()

#Function that codes for the skip button to skip the current question page. 
def skipQstn():
    global skipCount
    skipCount += 1
    
    global totQstns
    totQstns +=1
    
    qRoot.destroy()

#Function that codes for the main menu page. 
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

    menuImageFile = PhotoImage(file="atom.png")
    menuImageFile = menuImageFile.subsample(2,2)
    menuImageInput = Label(root, image=menuImageFile, bg="#4a86e8")
    menuImageInput.place(x=500, y=330, anchor="center")

    root.mainloop()

#Function that determines if a question is correct or incorrect, and increments the user's score if correct.
def calcScore(answer):
    pageFont = Font(family="Calibri", size=20, weight="bold")
    global score

    if temp[answer] == questions[qLCV][1]:
        ansMsg = Label(qRoot, text="Correct!", font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=80, pady=5, borderwidth=0,)
        ansMsg.place(x=500, y=250, anchor="center")
        score += 1

    else:
        ansMsg = Label(qRoot, text="Incorrect!", font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=80, pady=5, borderwidth=0,)
        ansMsg.place(x=500, y=250, anchor="center") 
    
    ansOne.destroy()
    ansTwo.destroy()

    if skipCount < 3:
        skipBut.destroy()

    if len(questions[qLCV]) == 5:
        ansThree.destroy()
        ansFour.destroy()

    nextBut = Button(qRoot, text="NEXT", font=pageFont, fg="#ffffff", bg="#6aa84f", padx=135, pady=5, borderwidth=0, command=nextQstn)
    nextBut.place(x=645, y=580)

#Function that codes for "NEXT" button to move on to the next question after an answer is clicked. 
def nextQstn():
    qRoot.destroy()

#Function that codes for the "RETRY" button on the results page for the user to re-attempt the quiz. 
def retry():
    resultsRoot.destroy()
    establishLists()

#Function that calculates the user's final score, mark and displays the corresponding encouraging message, creating the results page. 
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
    
    endTitle = Label(resultsRoot, text="QUIZ FINISHED!", font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=170, pady=30)
    endTitle.place(x=500, y=90, anchor="center")

    endResults = Label(resultsRoot, text="QUESTIONS CORRECT:\n"+str(score)+"/12\n\nOVERALL MARK:\n"+str(overallMark)+"\n\n"+str(endMsg), font=pageFont, fg="#4a86e8", bg="#cfe2f3", padx=60, pady=50)
    endResults.place(x=500, y=350, anchor="center")

    retryBut = Button(resultsRoot, text="RETRY", font=pageFont, fg="#ffffff", bg="#6aa84f", padx=150, pady=10, borderwidth=0, command=retry)
    retryBut.place(x=90, y=560)

    exitBut = Button(resultsRoot, text="EXIT", font=pageFont, fg="#ffffff", bg="#cc0000", padx=161, pady=10, borderwidth=0, command=exit)
    exitBut.place(x=510, y=560)

#Calls the establishLists function that initiates the program.  
establishLists()




