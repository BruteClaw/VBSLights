#!/usr/bin/env python

#imports
import time
import paho.mqtt.client as paho
from pygame import mixer
from tkinter import *

#variables
window = Tk()
cmd = "No"
broker="172.25.16.154"
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

#sound Effects Button Commands
def btnDragon():
    mixer.music.load('/home/pi/Music/Dragon Roar.mp3')
    mixer.music.play()
    print("Played Dragon Roar")
    
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
lbl1 = Label(window, text="Time Machine", font=("Arial Bold", 16))
lbl1.grid(column=0, row=0)
lbl2 = Label(window, text="Sound Effects", font=("Arial Bold", 16))
lbl2.grid(column=3, row=0)

#time Machine Buttons
btn0 = Button(window, text="Idle", bg="green", fg="white", font=("Arial Bold", 16), command=btnIdle)
btn0.grid(column=0, row=1)
btn1 = Button(window, text="Failure", bg="green", fg="white", font=("Arial Bold", 16), command=btnFail)
btn1.grid(column=0, row=2)
btn2 = Button(window, text="4000 BC", bg="green", fg="white", font=("Arial Bold", 16), command=btn4000BC)
btn2.grid(column=0, row=3)
btn3 = Button(window, text="3000 BC", bg="green", fg="white", font=("Arial Bold", 16), command=btn3000BC)
btn3.grid(column=0, row=4)

#Sound Effects Buttons
btn8 = Button(window, text="Dragon", font=("Arial Bold", 16), command=btnDragon)
btn8.grid(column=2, row=1)

#create the window
window.mainloop()