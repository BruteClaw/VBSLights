#!/usr/bin/env python

import time
import paho.mqtt.client as paho
broker="172.25.16.154"
port=1883

def on_publish(client,userdata,result):             #create function for callback
    print("data published")

def on_disconnect(client, userdata, rc):
    print("client disconnected ok")

    
pass

client1= paho.Client("control1")                    #create client object
client1.on_publish = on_publish                     #assign function to callback
client1.on_disconnect = on_disconnect
while True:
    client1.connect(broker,port)                        #establish connection
    ret= client1.publish("lights","fail")               #publish
    client1.disconnect()                                #disconnect until idle
    time.sleep(18)                                      #pause until Idle
    client1.connect(broker,port)                        #re-establish connection
    ret= client1.publish("lights","idle")               #publish Idle
    client1.disconnect()                                #disconnect until next cycle
    time.sleep(18)                                      #sleep until next command
    client1.connect(broker,port)                        #establish connection
    ret= client1.publish("lights","4000bc")             #publish
    client1.disconnect()                                #disconnect until idle
    time.sleep(18)                                      #pause until Idle
    client1.connect(broker,port)                        #re-establish connection
    ret= client1.publish("lights","idle")               #publish Idle
    client1.disconnect()                                #disconnect until next cycle
    time.sleep(18)                                      #sleep until next command
    client1.connect(broker,port)                        #establish connection
    ret= client1.publish("lights","3000bc")             #publish
    client1.disconnect()                                #disconnect until idle
    time.sleep(18)                                      #pause until Idle
    client1.connect(broker,port)                        #re-establish connection
    ret= client1.publish("lights","idle")               #publish Idle
    client1.disconnect()                                #disconnect until next cycle
    time.sleep(18)                                      #sleep until next command
    client1.connect(broker,port)                        #establish connection
    ret= client1.publish("lights","2000bc")             #publish
    client1.disconnect()                                #disconnect until idle
    time.sleep(18)                                      #pause until Idle
    client1.connect(broker,port)                        #re-establish connection
    ret= client1.publish("lights","idle")               #publish Idle
    client1.disconnect()                                #disconnect until next cycle
    time.sleep(18)                                      #sleep until next command
    client1.connect(broker,port)                        #establish connection
    ret= client1.publish("lights","1000bc")             #publish
    client1.disconnect()                                #disconnect until idle
    time.sleep(18)                                      #pause until Idle
    client1.connect(broker,port)                        #re-establish connection
    ret= client1.publish("lights","idle")               #publish Idle
    client1.disconnect()                                #disconnect until next cycle
    time.sleep(18)                                      #sleep until next command
    client1.connect(broker,port)                        #establish connection
    ret= client1.publish("lights","zero")               #publish
    client1.disconnect()                                #disconnect until idle
    time.sleep(18)                                      #pause until Idle
    client1.connect(broker,port)                        #re-establish connection
    ret= client1.publish("lights","idle")               #publish Idle
    client1.disconnect()                                #disconnect until next cycle
    time.sleep(18)                                      #sleep until next command
    client1.connect(broker,port)                        #establish connection
    ret= client1.publish("lights","1000ad")             #publish
    client1.disconnect()                                #disconnect until idle
    time.sleep(18)                                      #pause until Idle
    client1.connect(broker,port)                        #re-establish connection
    ret= client1.publish("lights","idle")               #publish Idle
    client1.disconnect()                                #disconnect until next cycle
    time.sleep(18)                                      #sleep until next command
    client1.connect(broker,port)                        #establish connection
    ret= client1.publish("lights","2000ad")             #publish
    client1.disconnect()                                #disconnect until idle
    time.sleep(18)                                      #pause until Idle
    client1.connect(broker,port)                        #re-establish connection
    ret= client1.publish("lights","idle")               #publish Idle
    client1.disconnect()                                #disconnect until next cycle
    time.sleep(18)                                      #sleep until next command
