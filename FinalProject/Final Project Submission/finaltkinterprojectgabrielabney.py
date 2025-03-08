"""
Final Tkinter Project
Gabriel Abney
This program creates several HTML files and one CSS file
for the user to use for a basic web page.
"""


import tkinter as tk                                            #Imports the Tkinter library for GUI development
from tkinter import Toplevel, StringVar, IntVar, PhotoImage, ttk    #Import specific widgets and data types
from PIL import Image, ImageTk                                  #Imports Pillow Image and ImageTK for handling image display in Tkinter
import os

"""
Global dictionary for saving information about the website being built
"""

websiteData = {
    "siteName":"default",
    "siteNav": "default",
    "pageName": "default",
    "pageDetails": "default",
    "fileLocation": "default"
}


"""
The section below handles the functions that the windows in the project will use.
"""

#Function to create the Help and Documentation Window
def openHelpWindow():
    helpWindow = Toplevel()
    helpWindow.title("Help and Documentation") #gives a title to the Help window
    helpWindow.configure(bg='#555555') #Help window background color to grayish color

    #Help text label
    tk.Label(helpWindow, text="This program creates an html document using the details that you enter!\n See how to host this document using GitHub pages: https://pages.github.com/", bg='lightblue').pack()
    #exit button
    tk.Button(helpWindow, text="Exit", command=helpWindow.destroy, bg='red').pack()



#Function to create the Website Builder window
def openWebWindow():
    webWindow = Toplevel(window)
    webWindow.title("Website Builder") #gives a title to the Help window
    webWindow.configure(bg='lightgreen') #Help window background color to light green

    #loads an image in the page creation window
    try:
        img2 = Image.open("webpageIcon.jpg").resize((200,200), Image.LANCZOS)
        photo2 = ImageTk.PhotoImage(img2)             #convert the image to a format suitable for tkinter
        img2_label = tk.Label(webWindow, image=photo2)   #create a label to display the image
        img2_label.image = photo2                    #keep a reference to avoid the image being garbage collected
        img2_label.pack()                            #pack the image label into the main window
    except :
        tk.Label(webWindow, text="Image not found!", fg='red').pack    #show an error message if image is not found


    #Website Builder Window label
    tk.Label(webWindow, text="Build a website in 3 easy steps!").pack()
    
    #Website Name Label
    tk.Label(webWindow, text="1. Choose a website name:").pack()
    #website name entry
    siteNameVar = tk.StringVar(value = websiteData["siteName"])
    siteNameEntry = tk.Entry(webWindow, textvariable=siteNameVar)
    siteNameEntry.pack()
    
    #Website page builder button label
    tk.Label(webWindow, text="2. Add a page to the website:").pack()

    #page name entry label
    tk.Label(webWindow, text="What do you want to call this web page?").pack()
    #page name entry
    pageNameVar = tk.StringVar(value = websiteData["pageName"])
    pageNameEntry = tk.Entry(webWindow, textvariable=pageNameVar)
    pageNameEntry.pack()
    
    #page data entry label
    tk.Label(webWindow, text="What text do you want this web page to display?").pack()
    #page DATA entry
    pageDataVar = tk.StringVar(value = websiteData["pageDetails"])
    pageDataEntry = tk.Entry(webWindow, textvariable=pageDataVar)
    pageDataEntry.pack()


    #function to save details
    def saveDetails():
        websiteData["siteName"] = siteNameEntry.get()
        websiteData["siteNav"] = pageNameVar.get()
        websiteData["pageName"] = pageNameVar.get()   
        websiteData["pageDetails"] = pageDataVar.get()   
        websiteData["fileLocation"] = siteNameVar.get()
        print(websiteData)

    #Save details label
    tk.Label(webWindow, text="3. Save your selections!").pack()
    tk.Button(webWindow, text ="SAVE", command = saveDetails(), bg="green").pack()
    
    #Build it label
    tk.Label(webWindow, text="Press the button below when you're ready to build it!").pack()
    #Button to build website from all entered information
    tk.Button(webWindow, text = "Build it!", command = buildWebsite, bg= "yellow").pack()





"""
Functions to build the website and pages output
"""
#function to create the header section of a web page
def buildHeader(headerEntry):
    header = f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>{headerEntry}</title><link rel="stylesheet" href="{headerEntry}.css"></head>"'
    return header

#Function to create the navigation section of a web page
def buildNav(navEntry):
    nav = f'<nav><a href="{navEntry}">Home</a>&nbsp;&nbsp;</nav>'

#function to create the body section of a web page    
def buildBody(bodyEntry):
    body = f'<main><p>{bodyEntry}</p></main>'
    return body

#function to build website from inputted information saved in global variables
def buildWebsite():
    f = open(f"{websiteData["fileLocation"]}.html", "w")
    f.write(f"{buildHeader(websiteData["siteName"])}\n")
    f.write(f"{buildNav(websiteData["pageName"])}\n")
    f.write(f"{buildBody(websiteData["pageDetails"])}")
    f.close()
    

#Creates the main window
window = tk.Tk()
window.title("Webpage Builder Application") #gives a title to the main window
window.configure(bg='#555555') #main window background color to grayish color


#Image source (public domain): https://commons.wikimedia.org/wiki/File:Website-icon.png
#Loads and displays image in main window, or creates an error message.
try:
    img = Image.open("websiteIcon.png").resize((200,200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)             #convert the image to a format suitable for tkinter
    img_label = tk.Label(window, image=photo)   #create a label to display the image
    img_label.image = photo                     #keep a reference to avoid the image being garbage collected
    img_label.pack()                            #pack the image label into the main window
except FileNotFoundError:
    tk.Label(window, text="Image not found!", fg='red').pack    #show an error message if image is not found


#Label to open website creator
tk.Label(window, text="Press the button below to enter the website creator!").pack()
#Button to open website creator window
tk.Button(window, text = "Start building a website!", command = openWebWindow, bg = 'lightgreen').pack()

#Label to open help window
tk.Label(window, text="Press the button below if you need help!").pack()
#Button to open the Help Window
tk.Button(window, text = "Help and Documentation", command = openHelpWindow, bg = 'lightblue').pack()

#close button
tk.Button(window, text="Exit", command=window.destroy, bg='red').pack()


#This line runs the main window of the application
window.mainloop() #start the tkinter event loop to display the window and wait for user interactions