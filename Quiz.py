from tkinter import *
import random
from tkinter.font import Font
from unittest import skip
from matplotlib.pyplot import close

questionsList = [["Earth is the 3rd planet from the Sun.","True","False"],["How many days does it take for the Earth to revolve around the Sun?","365","366","364","356"],["How long does it take for the Earth to fully rotate around its own axis?","24 hours","25 hours","23 hours","42 hours"],["The moon takes 29.5 days to complete one orbit around the Earth.","True","False"],["Why does the Moon have a greater effect on tides on Earth compared to the Sun?","Because the Moon is closer to the Earth","Because the Sun is too hot","Because the Moon is smaller","Because the Sun is bright"],["Who was the first human to set foot on the Moon?","Neil Armstrong","Sergey Korsakov","Robert Hines","Samantha Cristoforetti"],["How many kilometres is 1 Astronomical Unit (A.U.)?","150 000 000 km","100 000 000 km","999 999 999 km","500 000 km"],["The moon produces light of its own.","False","True"],["'Gibbous' is used to describe the Moon when more than half (but not all) of the Moon is illuminated.","True","False"],["'Waxing' is used to describe the area of the Moon you can see becoming larger each night.","True","False"],["'Waning' is used to describe the area of the Moon you can see becoming smaller each night.","True","False"],["What causes the seasons on Earth?","The Earth's tilt with respect to the Sun","The gravitational pull of the Sun","The speed of which the Earth orbits the Sun","The distance between the Earth and the Sun"],["Regular changes in sea levels (tides) occur due to the gravitational pull of the Moon and the Sun.","True","False"],["Which two pieces of evidence did the people use to believe that the Apollo 11 Moon landing was a hoax?","The flag and the stars","The flag and the Sun","The stars and the Sun","Their footprints and astronaut suits"],["How many phases of the Moon are there?","8","6","12","10"],["Which element does the Sun consume to release energy?","Hydrogen","Carbon","Nitrogen","Oxygen"],["Sunspots are areas that appear dark on the Sun.","True","False"],["Which of the following is Pluto considered as?","A dwarf planet","A planet","An asteroid","A comet"],["Is Astrology a psuedoscience?","True","False"],["How many planets are there in our solar system?","8","4","15","9"]]
questions = []
resultsMsg = ["TOUGH LUCK","NICE TRY","WELL DONE","SPECTACULAR"]
overallMark = ["NOT ACHIEVED","ACHIEVED","MERIT","EXCELLENCE"]
requiredScore = [0,4,7,10,12]

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


#def CALC.SCORE():

#def CALC.MARK():






setUp()



