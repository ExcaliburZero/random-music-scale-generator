"""

Random Music Scale Generator

Purpose: Selects a random music scale from a list of scales
Programer: ExcaliburZero / Rocketslime_1_1

"""

#Imports
from tkinter import *
from random import *
import json
import ast

#Grab random scale
def grab_scale():

    #Grab scale list
    nscales = list(scales["Scales"])

    #Fix list so it is a useable list
    current_item = 0
    for item in nscales:
        print(current_item)

        #Remove spaces
        if item == " ":
            nscales.remove(" ")
            current_item = current_item + 1

        #Fix sharps
        elif item == "#":
            nscales[current_item] = nscales[current_item - 1] + "#"
            current_item = current_item + 1

        #Fix flats
        elif item == "b":
            nscales[current_item] = nscales[current_item - 1] + "b"
            current_item = current_item + 1
        else:
            current_item = current_item + 1
    
    #Put together output
    output = nscales[int(random() * len(nscales))]
    print(nscales)
    print(output)

    #Output template code
    output_scale = Label(theGUI, text=output).grid(row = 3, column = 0)
    
    return

#Generate GUI
theGUI = Tk()
theGUI.geometry("400x550+100+200")
theGUI.title("Random Music Scale Generator")

#Setup variables
scales_file = "My_Scales.txt"
scales = json.load(open("My_Scales.txt"))

#Setup labels
scale_list = "Your scales are: " + scales["Scales"]
label_intro = Label(theGUI, text="Welcome to the Random Music Scale Generator").grid(row = 0, columnspan = 1)
list_of_scales = Label(theGUI, text=scale_list).grid(row = 1, column = 0)

#Setup button
button_generate = Button(theGUI, text = "Random Scale", command = grab_scale).grid(row = 2, column = 0)

#Add GUI to main loop
theGUI.mainloop()
