"""
Final Tkinter Project
Gabriel Abney
This program creates several HTML files and one CSS file
for the user to use for a basic web page.
"""


import tkinter as tk                                            #Imports the Tkinter library for GUI development
from tkinter import Toplevel, StringVar, IntVar, PhotoImage, ttk    #Import specific widgets and data types
from PIL import Image, ImageTk                                  #Imports Pillow Image and ImageTK for handling image display in Tkinter


"""
The section below handles the functions that the buttons in the project will use.
"""
#Sets the destination locations for the html and CSS files
def fileLocation():
    fileLocation = 1 #temporary placeholder

#Function to create the Help and Documentation Window
def openHelpWindow():
    helpWindow = Toplevel()
    helpWindow.title("Help and Documentation") #gives a title to the Help window
    helpWindow.configure(bg='#555555') #Help window background color to grayish color

    #Help text label
    tk.Label(helpWindow, text="placeholder", bg='lightblue').pack()  #placeholder text


#Function to create the navigation section


#Creates the main window
window = tk.Tk()
window.title("Webpage Builder Application") #gives a title to the main window
window.configure(bg='#555555') #main window background color to grayish color



#Image source (public domain): https://commons.wikimedia.org/wiki/File:Website-icon.png
#Loads and displays image in main window, or creates an error message.
try:
    img = Image.open("C:/Users/Gabe/Documents/GitHub/sdev140/FinalProject/Status Report 2/websiteIcon.png").resize((200,200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)             #convert the image to a format suitable for tkinter
    img_label = tk.Label(window, image=photo)   #create a label to display the image
    img_label.image = photo                     #keep a reference to avoid the image being garbage collected
    img_label.pack()                            #pack the image label into the main window
except FileNotFoundError:
    tk.Label(window, text="Image not found!", fg='red').pack    #show an error message if image is not found


#Label to begin website creation
tk.Label(window, text="Enter the number of web pages: ").pack()  #placeholder text

webPagesNum = tk.Entry(window)  #accepts number of webpages
webPagesNum.pack()

#Button to open page


#Button to open the Help Window
tk.Button(window, text = "Help and Documentation", command = openHelpWindow).pack()



#This line runs the main window of the application
window.mainloop() #start the tkinter event loop to display the window and wait for user interactions