#Import libs
import json, math
from tkinter import *

#Load config file
with open("democonfig.json") as jsonfile:
    config = json.load(jsonfile)

#Create window
root = Tk()
window = Canvas(root, width = 150, height = 16)
window.pack()

#Calculate area of circle
radius = config["radius"]
area = math.pi * (radius ** 2)

#Draw stuff on window
window.create_rectangle(0, 0, 150, 16, fill="#000000")
window.create_text(150 / 2, 8, text = str(area), fill="#FF005F")

#Print to console
print("Radius is: " + str(area))

#Enter window loop
root.mainloop()
