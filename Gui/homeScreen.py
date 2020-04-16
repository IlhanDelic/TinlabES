from tkinter import  *

homeScreen = Tk()
topFrame = Frame(homeScreen)
topFrame.pack()
bottomFrame = Frame(homeScreen)
bottomFrame = Frame(homeScreen)
bottomFrame.pack(side=BOTTOM)

settings = Button(topFrame, text= "settings", fg="gray")
date = Button(topFrame, text= "d/m/y", fg="black")
day = Button(topFrame, text= "day", fg="black")
time = Button(topFrame, text= "time", fg="black")
wifi = Button(topFrame, text= "wifi", fg="gray")

hostButton = Button(bottomFrame, text= "host a call", fg="red")
joinButton = Button(bottomFrame, text= "join a call", fg="blue")

settings.pack(side=LEFT)
date.pack(side=LEFT)
day.pack(side=LEFT)
time.pack(side=LEFT)
wifi.pack(side=LEFT)

hostButton.pack(side=LEFT)
joinButton.pack(side=LEFT)

homeScreen.mainloop()