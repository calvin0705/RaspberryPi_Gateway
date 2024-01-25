#!/usr/bin/python3
#for git
import paho.mqtt.client as mqtt
import time

import serial
import re
import os
import logging
import threading
import math
import RPi.GPIO as GPIO
import sys
import socket
import struct
import numpy as np
import csv

import lib.callback

end = [0xff, 0xff, 0xff]
port_lcd = serial.Serial(port='/dev/ttyAMA1', baudrate=115200, parity='N', stopbits=1, bytesize=8, timeout=1.0)
ary_end = bytearray(end)

global ESP_1_temp
global ESP_1_humi
global ESP_2_temp
global ESP_2_humi
global ESP_3_temp
global ESP_3_humi
global ESP_CO
global ESP_CO2
global ESP_CH2O
global ESP_PM1_0
global ESP_PM2_5
global ESP_PM10

ESP_temp1 = 0
ESP_humi1 = 0
ESP_temp2 = 0
ESP_humi2 = 0
ESP_temp3 = 0
ESP_humi3 = 0
ESP_CO    = 0
ESP_CO2   = 0
ESP_CH2O  = 0
ESP_PM1_0 = 0
ESP_PM2_5 = 0
ESP_PM10  = 0


global temp_offset_1
global humi_offset_1
global temp_offset_2
global humi_offset_2
global temp_offset_3
global humi_offset_3
global Write_tjc_button

temp_offset_1 = 0
humi_offset_1 = 0
temp_offset_2 = 0
humi_offset_2 = 0
temp_offset_3 = 0
humi_offset_3 = 0

# ############################################
# temp/humi offset initial
# ############################################
def read_offset_1():
    global temp_offset_1
    global humi_offset_1

    print("read_offset_1()")
    f1 = open('/home/pi/esg/offset/offset1.txt','rb')
    time.sleep(0.1)
    data1 = f1.read()
    
    try:
        sonsor_num  = data1[0]
        temp_offset_1 = data1[1]
        humi_offset_1 = data1[2]

        print(sonsor_num)
        print(temp_offset_1)
        print(humi_offset_1)
        
        if(temp_offset_1 > 150):
            temp_offset_1 = temp_offset_1 - 256

        if(humi_offset_1 > 150):
            humi_offset_1 = humi_offset_1 - 256

        temp_1 = temp_offset_1
        humi_1 = humi_offset_1

        for i in range(3):
            print("i ==========>>> ",i)
            recv_buffer1 = temp_1
            TJC_LCD2 = "n1.val=" + str(recv_buffer1)
            port_lcd.write(TJC_LCD2.encode())
            port_lcd.write(ary_end)
            time.sleep(0.1)

            recv_buffer1 = humi_1
            TJC_LCD2 = "n2.val=" + str(recv_buffer1)
            port_lcd.write(TJC_LCD2.encode())
            port_lcd.write(ary_end)
            time.sleep(0.1)
    except:
        print("no offset data in offset1.txt.")

def read_offset_2():
    global temp_offset_2
    global humi_offset_2

    print("read_offset_2()")
    f2 = open('/home/pi/esg/offset/offset2.txt','rb')
    time.sleep(0.1)
    data2 = f2.read()
    
    try:
        sonsor_num  = data2[0]
        temp_offset_2 = data2[1]
        humi_offset_2 = data2[2]

        print(sonsor_num)
        print(temp_offset_2)
        print(humi_offset_2)
        
        if(temp_offset_2 > 150):
            temp_offset_2 = temp_offset_2 - 256

        if(humi_offset_2 > 150):
            humi_offset_2 = humi_offset_2 - 256

        temp_2 = temp_offset_2
        humi_2 = humi_offset_2

        for i in range(3):
            recv_buffer2 = temp_2
            TJC_LCD2 = "n3.val=" + str(recv_buffer2)
            port_lcd.write(TJC_LCD2.encode())
            port_lcd.write(ary_end)
            time.sleep(0.1)

            recv_buffer2 = humi_2
            TJC_LCD2 = "n4.val=" + str(recv_buffer2)
            port_lcd.write(TJC_LCD2.encode())
            port_lcd.write(ary_end)
            time.sleep(0.1)
    except:
        print("no offset data in offset2.txt.")

def read_offset_3():
    global temp_offset_3
    global humi_offset_3

    print("read_offset_3()")
    f3 = open('/home/pi/esg/offset/offset3.txt','rb')
    time.sleep(0.1)
    data3 = f3.read()

    try:
        sonsor_num  = data3[0]
        temp_offset_3 = data3[1]
        humi_offset_3 = data3[2]

        print(sonsor_num)
        print(temp_offset_3)
        print(humi_offset_3)
        
        if(temp_offset_3 > 150):
            temp_offset_3 = temp_offset_3 - 256

        if(humi_offset_3 > 150):
            humi_offset_3 = humi_offset_3 - 256

        temp_3 = temp_offset_3
        humi_3 = humi_offset_3

        for i in range(3):
            recv_buffer3 = temp_3
            TJC_LCD2 = "n5.val=" + str(recv_buffer3)
            port_lcd.write(TJC_LCD2.encode())
            port_lcd.write(ary_end)
            time.sleep(0.1)

            recv_buffer3 = humi_3
            TJC_LCD2 = "n6.val=" + str(recv_buffer3)
            port_lcd.write(TJC_LCD2.encode())
            port_lcd.write(ary_end)
            time.sleep(0.1)
    except:
        print("no offset data in offset3.txt.")
    
def write_offset_1():
    global Write_tjc_button
    global temp_offset_1
    global humi_offset_1
    
    print("write_offset_1()write_offset_1()")
    f = open('/home/pi/offset/offset1.txt','wb')
    f.write(Write_tjc_button)
    time.sleep(0.1)
    f.close()
    data = Write_tjc_button

    sonsor_num  = data[0]
    temp_offset_1 = data[1]
    humi_offset_1 = data[2]

    if(temp_offset_1 > 150):
        temp_offset_1 = temp_offset_1 - 256

    if(humi_offset_1 > 150):
        humi_offset_1 = humi_offset_1 - 256
    print(sonsor_num)
    #print(temp_offset_1)
    print("temp_offset_1====>>>>>", temp_offset_1)
    print(humi_offset_1)

def write_offset_2():
    global Write_tjc_button
    global temp_offset_2
    global humi_offset_2
    
    print("write_offset_2()write_offset_2()")
    f = open('/home/pi/offset/offset2.txt','wb')
    f.write(Write_tjc_button)
    time.sleep(0.1)
    f.close()
    data = Write_tjc_button

    sonsor_num  = data[0]
    temp_offset_2 = data[1]
    humi_offset_2 = data[2]

    if(temp_offset_2 > 150):
        temp_offset_2 = temp_offset_2 - 256

    if(humi_offset_2 > 150):
        humi_offset_2 = humi_offset_2 - 256
    print(sonsor_num)
    print(temp_offset_2)
    print(humi_offset_2)

def write_offset_3():
    global Write_tjc_button
    global temp_offset_3
    global humi_offset_3
    
    print("write_offset_3()write_offset_3()")
    f = open('/home/pi/offset/offset3.txt','wb')
    f.write(Write_tjc_button)
    time.sleep(0.1)
    f.close()
    data = Write_tjc_button

    sonsor_num  = data[0]
    temp_offset_3 = data[1]
    humi_offset_3= data[2]

    if(temp_offset_3 > 150):
        temp_offset_3 = temp_offset_3 - 256

    if(humi_offset_3 > 150):
        humi_offset_3 = humi_offset_3 - 256
    print(sonsor_num)
    print(temp_offset_3)
    print(humi_offset_3)

read_offset_1()
read_offset_2()
read_offset_3()

# ############################################
# MQTT initial
# ############################################
def on_connect(client, userdata, flags, rc):
   global flag_connected
   flag_connected = 1
   client_subscriptions(client)
   print("Connected to MQTT server")

def on_disconnect(client, userdata, rc):
   global flag_connected
   flag_connected = 0
   print("Disconnected from MQTT server")

client = mqtt.Client("rpi_client1") #this should be a unique name
flag_connected = 0
# client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_connect = on_connect

# "clinet" device name define
def client_subscriptions(client):
    # client.subscribe("cvilux/#")
    client.subscribe("cvilux/6/temp/4")
###############################################
# Define esp32_1_temp loop in callback function
# Define esp32_1_humi loop in callback function
###############################################
def callback_esp32_1_temp(client, userdata, msg):
    global ESP_temp1
    ESP_temp1 = msg.payload.decode('utf-8')
client.message_callback_add('cvilux/temp-1', callback_esp32_1_temp)

def callback_esp32_1_humi(client, userdata, msg):
    global ESP_humi1
    ESP_humi1 = msg.payload.decode('utf-8')
client.message_callback_add('cvilux/humi-1', callback_esp32_1_humi)

###############################################
# Define esp32_2_temp loop in callback function
# Define esp32_2_humi loop in callback function
###############################################
def callback_esp32_2_temp(client, userdata, msg):
    global ESP_temp2
    ESP_temp2 = msg.payload.decode('utf-8')
client.message_callback_add('cvilux/temp-2', callback_esp32_2_temp)

def callback_esp32_2_humi(client, userdata, msg):
    global ESP_humi2
    ESP_humi2 = msg.payload.decode('utf-8')
client.message_callback_add('cvilux/humi-2', callback_esp32_2_humi)

###############################################
# Define esp32_3_temp loop in callback function
# Define esp32_3_humi loop in callback function
###############################################
def callback_esp32_3_temp(client, userdata, msg):
    global ESP_temp3
    ESP_temp3 = msg.payload.decode('utf-8')
client.message_callback_add('cvilux/temp-3', callback_esp32_3_temp)

def callback_esp32_3_humi(client, userdata, msg):
    global ESP_humi3
    ESP_humi3 = msg.payload.decode('utf-8')
client.message_callback_add('cvilux/humi-3', callback_esp32_3_humi)

###############################################
# Define esp32_CO loop in callback function
###############################################
def callback_esp32_CO(client, userdata, msg):
    global ESP_CO
    ESP_CO = msg.payload.decode('utf-8')
client.message_callback_add('cvilux/CO-1', callback_esp32_CO)

###############################################
# Define esp32_CO2 loop in callback function
###############################################
def callback_esp32_CO2(client, userdata, msg):
    global ESP_CO2
    ESP_CO2 = msg.payload.decode('utf-8')
client.message_callback_add('cvilux/CO2-1', callback_esp32_CO2)

###############################################
# Define esp32_CO2 loop in callback function
###############################################
def callback_esp32_CH2O(client, userdata, msg):
    global ESP_CH2O
    ESP_CH2O = msg.payload.decode('utf-8')
client.message_callback_add('cvilux/CH2O-1', callback_esp32_CH2O)

###############################################
# Define PM1.0
###############################################
def callback_esp32_PM1_0(client, userdata, msg):
    global ESP_PM1_0
    ESP_PM1_0 = msg.payload.decode('utf-8')
client.message_callback_add('cvilux/PM1_0-1', callback_esp32_PM1_0)

###############################################
# Define PM2.5
###############################################
def callback_esp32_PM2_5(client, userdata, msg):
    global ESP_PM2_5
    ESP_PM2_5 = msg.payload.decode('utf-8')
client.message_callback_add('cvilux/PM2_5-1', callback_esp32_PM2_5)

###############################################
# Define PM10
###############################################
def callback_esp32_PM10(client, userdata, msg):
    global ESP_PM10
    ESP_PM10 = msg.payload.decode('utf-8')
client.message_callback_add('cvilux/PM10-1', callback_esp32_PM10)

######### define callback initial end ########
###############################################

# client.connect('127.0.0.1',1883)

# client.loop_start() # start a new thread
# client_subscriptions(client)
# print("......client setup complete............")
# MQTT initial END
# ############################################

def task1(): # MQTT flag
    print("q123.............. ", lib.callback.q123())
    if (flag_connected != 1):
        print("task1..")
        # client.on_connect = on_connect
        
    threading.Timer(10, task1).start()

def task2(): # ESP32_1
    global ESP_temp1
    global ESP_humi1
    global temp_offset_1
    global humi_offset_1
    global ESP_temp1_tjc
    global ESP_humi1_tjc
    
    ESP_temp1 = float(ESP_temp1)
    ESP_humi1 = float(ESP_humi1)

    ESP_temp1 = round(ESP_temp1, 2)
    ESP_humi1 = round(ESP_humi1, 2)

    ESP_temp1_tjc = ESP_temp1 + temp_offset_1
    ESP_humi1_tjc = ESP_humi1 + humi_offset_1

    #print("ESP_temp1 ===>>> ",ESP_temp1_tjc)
    #print("temp_offset_1 ===>>> ",temp_offset_1)

    ESP_temp1_tjc = str(ESP_temp1_tjc)
    ESP_humi1_tjc = str(ESP_humi1_tjc)

    # print("ESP_temp1_tjc .................................. " ,ESP_temp1_tjc)

    #print("ESP_temp1 : ", ESP_temp1)
    #print("ESP_humi1 : ", ESP_humi1)
    #print("")

    try:
        recv_buffer = '\"' + ESP_temp1_tjc + '\"'
        TJC_LCD2 = "t1.txt=" + str(recv_buffer)
        port_lcd.write(TJC_LCD2.encode())
        port_lcd.write(ary_end)
        
        recv_buffer = '\"' + ESP_humi1_tjc + '\"'
        TJC_LCD2 = "t2.txt=" + str(recv_buffer)
        port_lcd.write(TJC_LCD2.encode())
        port_lcd.write(ary_end)
        
        recv_buffer = b''
        data = None
    except:
        print("wait data to tjc lcd (task2)")

    threading.Timer(1, task2).start()

def task3(): # ESP32_2
    global ESP_temp2
    global ESP_humi2
    global temp_offset_2
    global humi_offset_2
    global ESP_temp2_tjc
    global ESP_humi2_tjc
    
    ESP_temp2 = float(ESP_temp2)
    ESP_humi2 = float(ESP_humi2)

    ESP_temp2 = round(ESP_temp2, 2)
    ESP_humi2 = round(ESP_humi2, 2)

    ESP_temp2_tjc = ESP_temp2 + temp_offset_2
    ESP_humi2_tjc = ESP_humi2 + humi_offset_2

    ESP_temp2_tjc = str(ESP_temp2_tjc)
    ESP_humi2_tjc = str(ESP_humi2_tjc)

    #print("ESP_temp2 : ", ESP_temp2)
    #print("ESP_humi2 : ", ESP_humi2)
    #print("")

    try:
        recv_buffer = '\"' + ESP_temp2_tjc + '\"'
        TJC_LCD2 = "t3.txt=" + str(recv_buffer)
        port_lcd.write(TJC_LCD2.encode())
        port_lcd.write(ary_end)
        
        recv_buffer = '\"' + ESP_humi2_tjc + '\"'
        TJC_LCD2 = "t4.txt=" + str(recv_buffer)
        port_lcd.write(TJC_LCD2.encode())
        port_lcd.write(ary_end)
        
        recv_buffer = b''
        data = None
    except:
        print("wait data to tjc lcd (task3)")

    threading.Timer(1, task3).start()

def task4(): # ESP32_3
    global ESP_temp3
    global ESP_humi3
    global temp_offset_3
    global humi_offset_3
    global ESP_temp3_tjc
    global ESP_humi3_tjc
    
    ESP_temp3 = float(ESP_temp3)
    ESP_humi3 = float(ESP_humi3)

    ESP_temp3 = round(ESP_temp3, 2)
    ESP_humi3 = round(ESP_humi3, 2)

    ESP_temp3_tjc = ESP_temp3 + temp_offset_3
    ESP_humi3_tjc = ESP_humi3 + humi_offset_3

    ESP_temp3_tjc = str(ESP_temp3_tjc)
    ESP_humi3_tjc = str(ESP_humi3_tjc)

    #print("ESP_temp3 : ", ESP_temp3)
    #print("ESP_humi3 : ", ESP_humi3)
    #print("")

    try:
        recv_buffer = '\"' + ESP_temp3_tjc + '\"'
        TJC_LCD2 = "t5.txt=" + str(recv_buffer)
        port_lcd.write(TJC_LCD2.encode())
        port_lcd.write(ary_end)
        
        recv_buffer = '\"' + ESP_humi3_tjc + '\"'
        TJC_LCD2 = "t6.txt=" + str(recv_buffer)
        port_lcd.write(TJC_LCD2.encode())
        port_lcd.write(ary_end)
        
        recv_buffer = b''
        data = None
    except:
        print("wait data to tjc lcd (task4)")

    threading.Timer(1, task4).start()

def task5(): # offset
    global Write_tjc_button

    Write_tjc_button = port_lcd.read_all()

    if(Write_tjc_button):

        byte1 = Write_tjc_button[0]
        #print("byte1 ---> ",byte1)
        
        if(byte1 != 26):
            if(byte1 == 161):
                read_offset_1()
            if(byte1 == 162):
                read_offset_2()
            if(byte1 == 163):
                read_offset_3()
            
            if(byte1 == 1):
                write_offset_1()
            if(byte1 == 2):
                write_offset_2()
            if(byte1 == 3):
                write_offset_3()
    
    threading.Timer(0.3, task5).start()
    

def task6(): # CO
    global ESP_CO
    
    ESP_CO = format(float(ESP_CO), '.2f')
    ESP_CO = str(ESP_CO)
    
    #print("ESP_CO ==> ", ESP_CO)

    try:
        recv_buffer = '\"' + ESP_CO + '\"'
        TJC_LCD2 = "t13.txt=" + str(recv_buffer)
        port_lcd.write(TJC_LCD2.encode())
        port_lcd.write(ary_end)
        
        recv_buffer = b''
        data = None
    except:
        print("wait data to tjc lcd (task2)")

    threading.Timer(1, task6).start()
    
def task7(): # CO2
    global ESP_CO2
    
    ESP_CO2 = float(ESP_CO2)
    ESP_CO2 = round(ESP_CO2, 2)
    ESP_CO2 = str(ESP_CO2)

    try:
        recv_buffer = '\"' + ESP_CO2 + '\"'
        TJC_LCD2 = "t16.txt=" + str(recv_buffer)
        port_lcd.write(TJC_LCD2.encode())
        port_lcd.write(ary_end)
        
        recv_buffer = b''
        data = None
    except:
        print("wait data to tjc lcd (task2)")

    threading.Timer(1, task7).start()
    
def task8(): # CH2O
    global ESP_CH2O
    
    ESP_CH2O = format(float(ESP_CH2O), '.3f')
    ESP_CH2O = str(ESP_CH2O)

    try:
        recv_buffer = '\"' + ESP_CH2O + '\"'
        TJC_LCD2 = "t19.txt=" + str(recv_buffer)
        port_lcd.write(TJC_LCD2.encode())
        port_lcd.write(ary_end)
        
        recv_buffer = b''
        data = None
    except:
        print("wait data to tjc lcd (task2)")

    threading.Timer(1, task8).start()
    
# ############################################
# PM2.5
# ############################################
def task9(): # PM1.0
    global ESP_PM1_0
    
    ESP_PM1_0 = format(float(ESP_PM1_0), '.1f')
    ESP_PM1_0 = str(ESP_PM1_0)
    
    # print("ESP_PM1_0 ===>>> ",ESP_PM1_0)

    try:
        recv_buffer = '\"' + ESP_PM1_0 + '\"'
        TJC_LCD2 = "t22.txt=" + str(recv_buffer)
        port_lcd.write(TJC_LCD2.encode())
        port_lcd.write(ary_end)
        
        recv_buffer = b''
        data = None
    except:
        print("wait data to tjc lcd (task2)")

    threading.Timer(1, task9).start()
    
def task10(): # PM2.5
    global ESP_PM2_5
    
    ESP_PM2_5 = format(float(ESP_PM2_5), '.1f')
    ESP_PM2_5 = str(ESP_PM2_5)

    try:
        recv_buffer = '\"' + ESP_PM2_5 + '\"'
        TJC_LCD2 = "t12.txt=" + str(recv_buffer)
        port_lcd.write(TJC_LCD2.encode())
        port_lcd.write(ary_end)
        
        recv_buffer = b''
        data = None
    except:
        print("wait data to tjc lcd (task2)")

    threading.Timer(1, task10).start()
    
def task11(): # PM10
    global ESP_PM10
    
    ESP_PM10 = format(float(ESP_PM10), '.1f')
    ESP_PM10 = str(ESP_PM10)

    try:
        recv_buffer = '\"' + ESP_PM10 + '\"'
        TJC_LCD2 = "t18.txt=" + str(recv_buffer)
        port_lcd.write(TJC_LCD2.encode())
        port_lcd.write(ary_end)
        
        recv_buffer = b''
        data = None
    except:
        print("wait data to tjc lcd (task2)")

    threading.Timer(1, task11).start()


if __name__ == '__main__':
    task1()  # MQTT flag
    # task2()  # ESP32_1 temp/humi
    task3()  # ESP32_2 temp/humi
    task4()  # ESP32_3 temp/humi
    # task5()  # offset
    task6()  # CO
    task7()  # CO2
    task8()  # CH2O
    task9()  # PM1.0
    task10() # PM2.5
    task11() # PM10
