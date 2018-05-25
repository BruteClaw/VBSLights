#!/usr/bin/env python

#imports
import time
import paho.mqtt.client as paho
from pygame import mixer
from tkinter import *

#variables
window = Tk()
cmd = "No"
broker="192.168.75.4"
port=1883
mixer.init()

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
    mixer.music.play()
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
    mixer.music.play()
    print("Played Watch Alarm")
    
def btnOpen():
    mixer.music.load('/home/pi/Music/Theme Music Beginning.mp3')
    mixer.music.play()
    print("Played Beginning Theme")
    
def btnEnd():
    mixer.music.load('/home/pi/Music/Theme Music Ending.mp3')
    mixer.music.play()
    print("Played Ending Theme")

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
   
#establish MQTT stuff
pass
client1= paho.Client("control1")                    #create client object
client1.on_publish = on_publish                     #assign function to callbacks
client1.on_disconnect = on_disconnect

#GUI
#Window Settings
window.title("Time Lab")
window.geometry('480x800')

#labels
lbl1 = Label(window, text="Time Machine", font=("Arial Bold", 12))
lbl1.grid(column=0, row=0)
lbl2 = Label(window, text="Sound Effects", font=("Arial Bold", 12))
lbl2.grid(column=3, row=0)
lbl3 = Label(window, text="Computer Voice", font=("Arial Bold", 12))
lbl3.grid(column=5, row=0)
lbl4 = Label(window, text="Music", font=("Arial Bold", 12))
lbl4.grid(column=3, row=8)
lbl5 = Label(window, text="Debug", font=("Arial Bold", 12))
lbl5.grid(column=6, row=8)

#time Machine Buttons
btn0 = Button(window, text="Idle", bg="green", fg="white", font=("Arial Bold", 12), command=btnIdle)
btn0.grid(column=0, row=1)
btn1 = Button(window, text="Clear", bg="green", fg="white", font=("Arial Bold", 12), command=btnClear)
btn1.grid(column=0, row=2)
btn2 = Button(window, text="Failure", bg="green", fg="white", font=("Arial Bold", 12), command=btnFail)
btn2.grid(column=0, row=3)
btn3 = Button(window, text="4000 BC", bg="green", fg="white", font=("Arial Bold", 12), command=btn4000BC)
btn3.grid(column=0, row=4)
btn4 = Button(window, text="3000 BC", bg="green", fg="white", font=("Arial Bold", 12), command=btn3000BC)
btn4.grid(column=0, row=5)
btn5 = Button(window, text="2000 BC", bg="green", fg="white", font=("Arial Bold", 12), command=btn2000BC)
btn5.grid(column=0, row=6)
btn6 = Button(window, text="1000 BC", bg="green", fg="white", font=("Arial Bold", 12), command=btn1000BC)
btn6.grid(column=0, row=7)
btn7 = Button(window, text="Zero", bg="green", fg="white", font=("Arial Bold", 12), command=btnZero)
btn7.grid(column=0, row=8)
btn8 = Button(window, text="1000 AD", bg="green", fg="white", font=("Arial Bold", 12), command=btn1000AD)
btn8.grid(column=0, row=9)
btn9 = Button(window, text="2000 AD", bg="green", fg="white", font=("Arial Bold", 12), command=btn2000AD)
btn9.grid(column=0, row=10)

#Sound Effects Buttons
btn10 = Button(window, text="Bicycle", font=("Arial Bold", 12), command=btnBicycle)
btn10.grid(column=2, row=1)
btn11 = Button(window, text="Cellphone", font=("Arial Bold", 12), command=btnCell)
btn11.grid(column=2, row=2)
btn13 = Button(window, text="Dragon", font=("Arial Bold", 12), command=btnDragon)
btn13.grid(column=2, row=3)
btn14 = Button(window, text="Creak 1", font=("Arial Bold", 12), command=btnCreak1)
btn14.grid(column=2, row=4)
btn15 = Button(window, text="Creak 2", font=("Arial Bold", 12), command=btnCreak2)
btn15.grid(column=2, row=5)
btn16 = Button(window, text="Creak 3", font=("Arial Bold", 12), command=btnCreak3)
btn16.grid(column=2, row=6)
btn17 = Button(window, text="Head Bang", font=("Arial Bold", 12), command=btnHead)
btn17.grid(column=2, row=7)
btn18 = Button(window, text="Little Girl", font=("Arial Bold", 12), command=btnGirl)
btn18.grid(column=2, row=8)
btn19 = Button(window, text="Oda Grim", font=("Arial Bold", 12), command=btnOda)
btn19.grid(column=2, row=9)
btn20 = Button(window, text="Power Drill", font=("Arial Bold", 12), command=btnDrill)
btn20.grid(column=2, row=10)
btn21 = Button(window, text="Scan", font=("Arial Bold", 12), command=btnScan1)
btn21.grid(column=3, row=1)
btn22 = Button(window, text="Slower Scan", font=("Arial Bold", 12), command=btnScan2)
btn22.grid(column=3, row=2)
btn23 = Button(window, text="Slowest Scan", font=("Arial Bold", 12), command=btnScan3)
btn23.grid(column=3, row=3)
btn24 = Button(window, text="Shrink Zapper", font=("Arial Bold", 12), command=btnZap)
btn24.grid(column=3, row=4)
btn25 = Button(window, text="Tiny Oda", font=("Arial Bold", 12), command=btnTiny)
btn25.grid(column=3, row=5)
btn26 = Button(window, text="Watch Alarm", font=("Arial Bold", 12), command=btnAlarm)
btn26.grid(column=3, row=6)
btn27 = Button(window, text="Begining", bg="blue", font=("Arial Bold", 12), command=btnOpen)
btn27.grid(column=3, row=9)
btn28 = Button(window, text="Ending", bg="blue", font=("Arial Bold", 12), command=btnEnd)
btn28.grid(column=3, row=10)

#Computer Voice Buttons
btn30 = Button(window, text="How may I Help", bg="red", font=("Arial Bold", 12), command=btnComp1)
btn30.grid(column=5, row=1)
btn31 = Button(window, text="Fluffy", bg="red", font=("Arial Bold", 12), command=btnComp2)
btn31.grid(column=5, row=2)
btn32 = Button(window, text="Mephibosheth", bg="red", font=("Arial Bold", 12), command=btnComp3)
btn32.grid(column=5, row=3)
btn33 = Button(window, text="Serious", bg="red", font=("Arial Bold", 12), command=btnComp4)
btn33.grid(column=5, row=4)
btn34 = Button(window, text="Silly", bg="red", font=("Arial Bold", 12), command=btnComp5)
btn34.grid(column=5, row=5)
btn35 = Button(window, text="Mephibosheth Cool", bg="red", font=("Arial Bold", 12), command=btnComp6)
btn35.grid(column=5, row=6)
btn36 = Button(window, text="Here to Help", bg="red", font=("Arial Bold", 12), command=btnComp7)
btn36.grid(column=5, row=7)
btn37 = Button(window, text="Snippy", bg="red", font=("Arial Bold", 12), command=btnComp8)
btn37.grid(column=5, row=8)
btn38 = Button(window, text="Heard That", bg="red", font=("Arial Bold", 12), command=btnComp9)
btn38.grid(column=5, row=9)
btn39 = Button(window, text="Funny Joke", bg="red", font=("Arial Bold", 12), command=btnComp10)
btn39.grid(column=5, row=10)
btn40 = Button(window, text="Chase Mouse", bg="red", font=("Arial Bold", 12), command=btnComp11)
btn40.grid(column=6, row=4)
btn41 = Button(window, text="Right Away", bg="red", font=("Arial Bold", 12), command=btnComp12)
btn41.grid(column=6, row=5)

#debug Buttons
btn50 = Button(window, text="Test", bg="black", fg="white", font=("Arial Bold", 12), command=btnTest)
btn50.grid(column=6, row=9)
btn51 = Button(window, text="Close", bg="black", fg="white", font=("Arial Bold", 12), command=btnClose)
btn51.grid(column=6, row=10)

#create the window
window.mainloop()