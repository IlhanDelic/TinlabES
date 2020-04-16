from tkinter import  *

def doFunction():
    print("do function")

settings = Tk() # main window

menu = Menu(settings) # setting a menu at the top
settings.config(menu=menu) #configure menu

subMenu = Menu(menu) #dropdown menu submenu in a menu
menu.add_cascade(label="settings", menu=subMenu) #what would you want to appear in the menu
subMenu.add_command(label="wifi", command=doFunction)
subMenu.add_command(label="brightness", command=doFunction)
subMenu.add_separator()
subMenu.add_command(label="time", command=doFunction)
subMenu.add_command(label="day", command=doFunction)
subMenu.add_command(label="date", command=doFunction)
subMenu.add_separator()
subMenu.add_command(label="exit", command=doFunction)

dateMenu = Menu(menu)
menu.add_cascade(label="d/m/y", menu=dateMenu)

dayMenu = Menu(menu)
menu.add_cascade(label="mon", menu=dayMenu)

timeMenu = Menu(menu)
menu.add_cascade(label="13:43", menu=timeMenu)


settings.mainloop()