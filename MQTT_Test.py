#!/usr/bin/env python

import time
import paho.mqtt.client as paho
broker="127.0.0.1"

#define callback
def on_message(client, usrdata, message):
    time.sleep(1)
    print("reveived message =",str(message.payload.decode("utf-8")))

client= paho.Client("client-001") #create client object

#Bind function to callback
client.on_message=on_message

print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process recieved messages
print("Subscribing")
client.subscribe("lights") #subscribe
time.sleep(2)
print("publishing ")
client.publish("lights", "Test") #publish
time.sleep(4)
client.disconnect()  #disconnect
client.loop_stop() #stop loop
