#!/usr/bin/env python

#imports
import time
import paho.mqtt.client as paho
from pygame import mixer
from tkinter import *
from tkinter import ttk
import subprocess

#variables
window = Tk()
cmd = "No"
broker="x.x.x.x" #address for the MQTT Broker
port=1883 #port on the MQTT Broker
mixer.init()
buttonFont = ("Verdana", 24) # Sets the font size of the buttons

#tab fonts
tabFont = ("Verdana", 18)
tabStyle = ttk.Style()
tabStyle.configure('.', font=tabFont)

#create functions for callback in MQTT
def on_publish(client,userdata,result):
    print("Command", cmd, "published")

def on_disconnect(client, userdata, rc):
    print("client disconnected ok")

#Time machine button Commands
def btnIdle():
    client1.connect(broker,port)                      #establish connection
    global cmd
    cmd = "idle"
    ret= client1.publish("lights","idle")             #publish
    client1.disconnect()                              #disconnect until next command

def btnClear():
    client1.connect(broker,port)                      #establish connection
    global cmd
    cmd = "clear"
    ret= client1.publish("lights","clear")             #publish
    client1.disconnect()                              #disconnect until next command

def btnFail():
    client1.connect(broker,port)                      #establish connection
    global cmd
    cmd = "fail"
    mixer.music.load('/home/pi/Music/Time Machine Malfunction.mp3')
    mixer.music.play()
    ret= client1.publish("lights","fail")             #publish
    client1.disconnect()                              #disconnect until next command
    
def btn4000BC():
    client1.connect(broker,port)                      #establish connection
    global cmd
    cmd = "4000bc"
    ret= client1.publish("lights","4000bc")           #publish
    mixer.music.load('/home/pi/Music/Time Machine.mp3')
    mixer.music.play()
    client1.disconnect()                              #disconnect until next command
    
def btn3000BC():
    client1.connect(broker,port)                      #establish connection
    global cmd
    cmd = "3000bc"
    ret= client1.publish("lights","3000bc")           #publish
    mixer.music.load('/home/pi/Music/Time Machine.mp3')
    mixer.music.play()
    client1.disconnect()                              #disconnect until next command

def btn2000BC():
    client1.connect(broker,port)                      #establish connection
    global cmd
    cmd = "2000bc"
    ret= client1.publish("lights","2000bc")           #publish
    mixer.music.load('/home/pi/Music/Time Machine.mp3')
    mixer.music.play()
    client1.disconnect()                              #disconnect until next command

def btn1000BC():
    client1.connect(broker,port)                      #establish connection
    global cmd
    cmd = "1000bc"
    ret= client1.publish("lights","1000bc")           #publish
    mixer.music.load('/home/pi/Music/Time Machine.mp3')
    mixer.music.play()
    client1.disconnect()                              #disconnect until next command

def btnZero():
    client1.connect(broker,port)                      #establish connection
    global cmd
    cmd = "zero"
    ret= client1.publish("lights","zero")           #publish
    mixer.music.load('/home/pi/Music/Time Machine.mp3')
    mixer.music.play()
    client1.disconnect()                              #disconnect until next command

def btn1000AD():
    client1.connect(broker,port)                      #establish connection
    global cmd
    cmd = "1000ad"
    ret= client1.publish("lights","1000ad")           #publish
    mixer.music.load('/home/pi/Music/Time Machine.mp3')
    mixer.music.play()
    client1.disconnect()                              #disconnect until next command

def btn2000AD():
    client1.connect(broker,port)                      #establish connection
    global cmd
    cmd = "2000ad"
    ret= client1.publish("lights","2000ad")           #publish
    mixer.music.load('/home/pi/Music/Time Machine.mp3')
    mixer.music.play()
    client1.disconnect()                              #disconnect until next command

#sound Effects Button Commands
def btnBicycle():
    mixer.music.load('/home/pi/Music/Bicycle Cling.mp3')
    mixer.music.play()
    print("Played Bicycle Cling")
    
def btnCell():
    mixer.music.load('/home/pi/Music/Cellphone.mp3')
    mixer.music.play(loops=-1)
    print("Played Cellphone")
    
def btnDragon():
    mixer.music.load('/home/pi/Music/Dragon Roar.mp3')
    mixer.music.play()
    print("Played Dragon Roar")
    
def btnCreak1():
    mixer.music.load('/home/pi/Music/Floor Creak 1.mp3')
    mixer.music.play()
    print("Played Floor Creak 1")
    
def btnCreak2():
    mixer.music.load('/home/pi/Music/Floor Creak 2.mp3')
    mixer.music.play()
    print("Played Floor Creak 2")
    
def btnCreak3():
    mixer.music.load('/home/pi/Music/Floor Creak 3.mp3')
    mixer.music.play()
    print("Played Floor Creak 3")
    
def btnHead():
    mixer.music.load('/home/pi/Music/Head Bang.mp3')
    mixer.music.play()
    print("Played Head Bang")
    
def btnGirl():
    mixer.music.load('/home/pi/Music/Little Girl Voice.mp3')
    mixer.music.play()
    print("Played Little Girl Voice")
    
def btnOda():
    mixer.music.load('/home/pi/Music/Oda Grim.mp3')
    mixer.music.play()
    print("Played Oda Grim")
    
def btnDrill():
    mixer.music.load('/home/pi/Music/Power Drill.mp3')
    mixer.music.play()
    print("Played Power Drill")
    
def btnScan1():
    mixer.music.load('/home/pi/Music/Robot Scan.mp3')
    mixer.music.play()
    print("Played Robot Scan")

def btnScan2():
    mixer.music.load('/home/pi/Music/Robot Scan Slower.mp3')
    mixer.music.play()
    print("Played Robot Scan Slower")

def btnScan3():
    mixer.music.load('/home/pi/Music/Robot Scan Slowest.mp3')
    mixer.music.play()
    print("Played Robot Scan Slowest")

def btnZap():
    mixer.music.load('/home/pi/Music/Shrink Zapper.mp3')
    mixer.music.play()
    print("Played Shrink Zapper")
    
def btnTiny():
    mixer.music.load('/home/pi/Music/Tiny Oda Grim.mp3')
    mixer.music.play()
    print("Played Tiny Oda Grim")
    
def btnAlarm():
    mixer.music.load('/home/pi/Music/Watch Alarm.mp3')
    mixer.music.play(loops=-1)
    print("Played Watch Alarm")
    
def btnBegin():
    mixer.music.load('/home/pi/Music/Theme Music Beginning.mp3')
    mixer.music.play()
    print("Played Beginning Theme")
    
def btnEnd():
    mixer.music.load('/home/pi/Music/Theme Music Ending.mp3')
    mixer.music.play()
    print("Played Ending Theme")
    
def btnTrumpet():
    mixer.music.load('/home/pi/Music/Trumpet Fanfare.mp3')
    mixer.music.play()
    print("Played Trumpet")

#Computer Voice Button Commands
def btnComp1():
    mixer.music.load('/home/pi/Music/Comp01 - How May I Help.mp3')
    mixer.music.play()
    print("Played Computer Voice 1")
    
def btnComp2():
    mixer.music.load('/home/pi/Music/Comp02 - Fluffy.mp3')
    mixer.music.play()
    print("Played Computer Voice 2")
    
def btnComp3():
    mixer.music.load('/home/pi/Music/Comp03 - Mephibosheth.mp3')
    mixer.music.play()
    print("Played Computer Voice 3")
    
def btnComp4():
    mixer.music.load('/home/pi/Music/Comp04 - Computer Serious.mp3')
    mixer.music.play()
    print("Played Computer Voice 4")
    
def btnComp5():
    mixer.music.load('/home/pi/Music/Comp05 - Dont Be Silly.mp3')
    mixer.music.play()
    print("Played Computer Voice 5")

def btnComp6():
    mixer.music.load('/home/pi/Music/Comp06 - Mephibosheth is Cool.mp3')
    mixer.music.play()
    print("Played Computer Voice 6")

def btnComp7():
    mixer.music.load('/home/pi/Music/Comp07 - Here to Help.mp3')
    mixer.music.play()
    print("Played Computer Voice 7")

def btnComp8():
    mixer.music.load('/home/pi/Music/Comp08 - Snippy.mp3')
    mixer.music.play()
    print("Played Computer Voice 8")
    
def btnComp9():
    mixer.music.load('/home/pi/Music/Comp09 - Heard That.mp3')
    mixer.music.play()
    print("Played Computer Voice 9")
    
def btnComp10():
    mixer.music.load('/home/pi/Music/Comp10 - Funny Joke.mp3')
    mixer.music.play()
    print("Played Computer Voice 10")
    
def btnComp11():
    mixer.music.load('/home/pi/Music/Comp11 - Chase the Mouse.mp3')
    mixer.music.play()
    print("Played Computer Voice 11")
    
def btnComp12():
    mixer.music.load('/home/pi/Music/Comp12 - Right Away.mp3')
    mixer.music.play()
    print("Played Computer Voice 12")
    
#debug Commands
def btnTest():
    client1.connect(broker,port)                      #establish connection
    global cmd
    cmd = "test"
    ret= client1.publish("lights","test")             #publish
    mixer.music.load('/home/pi/Music/1-Minute Audio Test for Stereo Speakers  Headphones.mp3')
    mixer.music.play()
    client1.disconnect()                              #disconnect until next command

def btnClose():
    client1.connect(broker,port)                      #establish connection
    global cmd
    cmd = "close"
    ret= client1.publish("lights","close")             #publish
    client1.disconnect()                              #disconnect until next command
    subprocess.call(['shutdown', '-h', 'now'], shell=False)
    
def btnStop():
    mixer.music.stop()
    print("Stopped Sounds")
##
#establish MQTT stuff
pass
client1= paho.Client("control1")                    #create client object
client1.on_publish = on_publish                     #assign function to callbacks
client1.on_disconnect = on_disconnect

#GUI
#Window Settings
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.title("Time Lab")
window.configure(bg="#a9a9a9")
window.geometry("%dx%d+0+0" % (w, h))

# gives weight to the cells in the grid
rows = 0
while rows < 50:
    window.rowconfigure(rows, weight=1)
    window.columnconfigure(rows, weight=1)
    rows += 1

# Defines and places the notebook widget
nb = ttk.Notebook(window)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

# Adds tab 1 of the notebook
page1 = ttk.Frame(nb)
nb.add(page1, text='Day One')
 
# Adds tab 2 of the notebook
page2 = ttk.Frame(nb)
nb.add(page2, text='Day Two')

# Adds tab 3 of the notebook
page3 = ttk.Frame(nb)
nb.add(page3, text='Day Three')

# Adds tab 4 of the notebook
page4 = ttk.Frame(nb)
nb.add(page4, text='Day Four')

# Adds tab 5 of the notebook
page5 = ttk.Frame(nb)
nb.add(page5, text='Day Five')

# Adds tab 6 of the notebook
page6 = ttk.Frame(nb)
nb.add(page6, text='Debug')

#buttons on tab 1
btn01 = Button(page1, text="Begining Theme", bg="blue", font=buttonFont, command=btnBegin)
btn01.grid(column=0, row=0)
btn02 = Button(page1, text="Oda Grim", font=buttonFont, command=btnOda)
btn02.grid(column=0, row=1)
btn03 = Button(page1, text="Computer 1", bg="#daa520", font=buttonFont, command=btnComp1)
btn03.grid(column=0, row=2)
btn04 = Button(page1, text="Computer 2", bg="#daa520", font=buttonFont, command=btnComp2)
btn04.grid(column=0, row=3)
btn05 = Button(page1, text="Computer 3", bg="#daa520", font=buttonFont, command=btnComp3)
btn05.grid(column=0, row=4)
btn06 = Button(page1, text="Computer 4", bg="#daa520", font=buttonFont, command=btnComp4)
btn06.grid(column=1, row=2)
btn07 = Button(page1, text="Computer 5", bg="#daa520", font=buttonFont, command=btnComp5)
btn07.grid(column=1, row=3)
btn08 = Button(page1, text="Computer 6", bg="#daa520", font=buttonFont, command=btnComp6)
btn08.grid(column=1, row=4)
btn09 = Button(page1, text="Computer 7", bg="#daa520", font=buttonFont, command=btnComp7)
btn09.grid(column=2, row=2)
btn10 = Button(page1, text="Computer 8", bg="#daa520", font=buttonFont, command=btnComp8)
btn10.grid(column=2, row=3)
btn11 = Button(page1, text="Computer 9", bg="#daa520", font=buttonFont, command=btnComp9)
btn11.grid(column=2, row=4)
btn12 = Button(page1, text="Watch Alarm", font=buttonFont, command=btnAlarm)
btn12.grid(column=0, row=5)
btn13 = Button(page1, text="Stop Sounds", bg="red", font=buttonFont, command=btnStop)
btn13.grid(column=1, row=5)
btn14 = Button(page1, text="Ending Theme", bg="blue", font=buttonFont, command=btnEnd)
btn14.grid(column=1, row=0)
btn64 = Button(page1, text="Idle", bg="green", fg="white", font=buttonFont, command=btnIdle)
btn64.grid(column=2, row=5)
btn65 = Button(page1, text="Clear", bg="green", fg="white", font=buttonFont, command=btnClear)
btn65.grid(column=2, row=6)

#buttons on tab 2
btn15 = Button(page2, text="Begining Theme", bg="blue", font=buttonFont, command=btnBegin)
btn15.grid(column=0, row=0)
btn16 = Button(page2, text="Floor Creak 1", font=buttonFont, command=btnCreak1)
btn16.grid(column=0, row=1)
btn17 = Button(page2, text="Floor Creak 2", font=buttonFont, command=btnCreak2)
btn17.grid(column=0, row=2)
btn18 = Button(page2, text="Floor Creak 3", font=buttonFont, command=btnCreak3)
btn18.grid(column=0, row=3)
btn19 = Button(page2, text="Little Girl Voice", font=buttonFont, command=btnGirl)
btn19.grid(column=0, row=4)
btn20 = Button(page2, text="Professor Normal", bg="green", fg="white", font=buttonFont, command=btn2000AD)
btn20.grid(column=1, row=1)
btn21 = Button(page2, text="Machine Failure", bg="green", fg="white", font=buttonFont, command=btnFail)
btn21.grid(column=1, row=2)
btn22 = Button(page2, text="Queen Arrives", bg="green", fg="white", font=buttonFont, command=btn1000AD)
btn22.grid(column=1, row=3)
btn23 = Button(page2, text="Stop Sounds", bg="red", font=buttonFont, command=btnStop)
btn23.grid(column=1, row=5)
btn24 = Button(page2, text="Ending Theme", bg="blue", font=buttonFont, command=btnEnd)
btn24.grid(column=1, row=0)
btn66 = Button(page2, text="Idle", bg="green", fg="white", font=buttonFont, command=btnIdle)
btn66.grid(column=2, row=4)
btn67 = Button(page2, text="Clear", bg="green", fg="white", font=buttonFont, command=btnClear)
btn67.grid(column=2, row=5)

#buttons on tab 3
btn25 = Button(page3, text="Begining Theme", bg="blue", font=buttonFont, command=btnBegin)
btn25.grid(column=0, row=0)
btn26 = Button(page3, text="Bicycle", font=buttonFont, command=btnBicycle)
btn26.grid(column=0, row=1)
btn27 = Button(page3, text="Scan", font=buttonFont, command=btnScan1)
btn27.grid(column=0, row=2)
btn28 = Button(page3, text="Oda Grim", font=buttonFont, command=btnOda)
btn28.grid(column=0, row=3)
btn29 = Button(page3, text="Slower Scan", font=buttonFont, command=btnScan2)
btn29.grid(column=0, row=4)
btn30 = Button(page3, text="Slowest Scan", font=buttonFont, command=btnScan3)
btn30.grid(column=0, row=5)
btn31 = Button(page3, text="Computer 1", bg="#daa520", font=buttonFont, command=btnComp1)
btn31.grid(column=1, row=1)
btn32 = Button(page3, text="Computer 10", bg="#daa520", font=buttonFont, command=btnComp10)
btn32.grid(column=1, row=2)
btn33 = Button(page3, text="Computer 11", bg="#daa520", font=buttonFont, command=btnComp11)
btn33.grid(column=1, row=3)
btn34 = Button(page3, text="Computer 12", bg="#daa520", font=buttonFont, command=btnComp12)
btn34.grid(column=1, row=4)
btn35 = Button(page3, text="Stop Sounds", bg="red", font=buttonFont, command=btnStop)
btn35.grid(column=1, row=5)
btn36 = Button(page3, text="Ending Theme", bg="blue", font=buttonFont, command=btnEnd)
btn36.grid(column=1, row=0)
btn68 = Button(page3, text="Idle", bg="green", fg="white", font=buttonFont, command=btnIdle)
btn68.grid(column=2, row=4)
btn69 = Button(page3, text="Clear", bg="green", fg="white", font=buttonFont, command=btnClear)
btn69.grid(column=2, row=5)

#buttons on tab 4
btn37 = Button(page4, text="Begining Theme", bg="blue", font=buttonFont, command=btnBegin)
btn37.grid(column=0, row=0)
btn38 = Button(page4, text="Power Drill", font=buttonFont, command=btnDrill)
btn38.grid(column=0, row=1)
btn39 = Button(page4, text="Cellphone", font=buttonFont, command=btnCell)
btn39.grid(column=0, row=2)
btn40 = Button(page4, text="Head Bang", font=buttonFont, command=btnHead)
btn40.grid(column=0, row=3)
btn41 = Button(page4, text="Professor Leaves", bg="green", fg="white", font=buttonFont, command=btn1000AD)
btn41.grid(column=1, row=1)
btn42 = Button(page4, text="Professor Return", bg="green", fg="white", font=buttonFont, command=btn2000AD)
btn42.grid(column=1, row=2)
btn43 = Button(page4, text="30AD Trip", bg="green", fg="white", font=buttonFont, command=btnZero)
btn43.grid(column=1, row=3)
btn44 = Button(page4, text="Scan", font=buttonFont, command=btnScan1)
btn44.grid(column=0, row=4)
btn45 = Button(page4, text="Stop Sounds", bg="red", font=buttonFont, command=btnStop)
btn45.grid(column=1, row=5)
btn46 = Button(page4, text="Ending Theme", bg="blue", font=buttonFont, command=btnEnd)
btn46.grid(column=1, row=0)
btn70 = Button(page4, text="Idle", bg="green", fg="white", font=buttonFont, command=btnIdle)
btn70.grid(column=2, row=4)
btn71 = Button(page4, text="Clear", bg="green", fg="white", font=buttonFont, command=btnClear)
btn71.grid(column=2, row=5)
           
#buttons on tab 5
btn47 = Button(page5, text="Begining Theme", bg="blue", font=buttonFont, command=btnBegin)
btn47.grid(column=0, row=0)
btn48 = Button(page5, text="Professor Return", bg="green", fg="white", font=buttonFont, command=btn2000AD)
btn48.grid(column=0, row=1)
btn49 = Button(page5, text="Roman Returns", bg="green", fg="white", font=buttonFont, command=btnZero)
btn49.grid(column=0, row=2)
btn50 = Button(page5, text="Oda Grim", font=buttonFont, command=btnOda)
btn50.grid(column=0, row=3)
btn51 = Button(page5, text="Shrink Zapper", font=buttonFont, command=btnZap)
btn51.grid(column=0, row=4)
btn52 = Button(page5, text="Tiny Oda", font=buttonFont, command=btnTiny)
btn52.grid(column=0, row=5)
btn53 = Button(page5, text="Trumpet", font=buttonFont, command=btnTrumpet)
btn53.grid(column=1, row=1)
btn54 = Button(page5, text="Queen Leaves", bg="green", fg="white", font=buttonFont, command=btn1000AD)
btn54.grid(column=1, row=2)
btn55 = Button(page5, text="Dragon Arival", bg="green", fg="white", font=buttonFont, command=btn4000BC)
btn55.grid(column=1, row=3)
btn56 = Button(page5, text="Dragon Roar", font=buttonFont, command=btnDragon)
btn56.grid(column=1, row=4)
btn57 = Button(page5, text="Stop Sounds", bg="red", font=buttonFont, command=btnStop)
btn57.grid(column=1, row=5)
btn58 = Button(page5, text="Ending Theme", bg="blue", font=buttonFont, command=btnEnd)
btn58.grid(column=1, row=0)
btn72 = Button(page5, text="Idle", bg="green", fg="white", font=buttonFont, command=btnIdle)
btn72.grid(column=2, row=4)
btn73 = Button(page5, text="Clear", bg="green", fg="white", font=buttonFont, command=btnClear)
btn73.grid(column=2, row=5)

#buttons on tab 6
btn59 = Button(page6, text="Stop Sounds", bg="red", font=buttonFont, command=btnStop)
btn59.grid(column=0, row=0)
btn60 = Button(page6, text="Test", bg="black", fg="white", font=buttonFont, command=btnTest)
btn60.grid(column=0, row=1)
btn61 = Button(page6, text="Shutdown", bg="black", fg="white", font=buttonFont, command=btnClose)
btn61.grid(column=0, row=2)
btn62 = Button(page6, text="Idle", bg="green", fg="white", font=buttonFont, command=btnIdle)
btn62.grid(column=0, row=3)
btn63 = Button(page6, text="Clear", bg="green", fg="white", font=buttonFont, command=btnClear)
btn63.grid(column=0, row=4)

#starting the Window
window.mainloop()
