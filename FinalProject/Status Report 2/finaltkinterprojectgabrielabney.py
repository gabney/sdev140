"""
Final Tkinter Project
Gabriel Abney
This program creates several HTML files and one CSS file
for the user to use for a basic web page.
"""


import tkinter as tk                                #Imports the Tkinter library for GUI development
from tkinter import Toplevel, StringVar, IntVar     #Import specific widgets and data types
from PIL import Image, ImageTk                      #Imports Pillow Image and ImageTK for handling image display in Tkinter


"""
The section below handles the functions that the buttons in the project will use.
"""
#Sets the destination locations for the html and CSS files
def fileLocation():
    fileLocation = 1 #temporary placeholder

#Function to create the Help and Documentation Window
def helpWindow():
    helpWindow = 1 #temporary placeholder

#Function to create the navigation sectio


#image source (public domain): https://commons.wikimedia.org/wiki/File:Website-icon.png


#Button to open the Help Window


#Creates the main window
window = tk.Tk()
window.title("") #gives a title to the main window
window.configure(bg='#555555') #main window background color to grayish color

#This line runs the main window of the application
window.mainloop() #start the tkinter event loop to display the window and wait for user interactions