#!/usr/bin/python
import socket
import time
#from builtins import str
import binascii
import re
import os
import serial
import threading
import RPi.GPIO as GPIO

end = [0xff, 0xff, 0xff]
port_lcd = serial.Serial(port='/dev/ttyAMA1', baudrate=9600, parity='N', stopbits=1, bytesize=8, timeout=1.0)
ary_end = bytearray(end)

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup(38)
GPIO.setup(38, GPIO.OUT, initial=1)

port = 1
read_tjc_button = b''

serverMACAddress1 = '84:cc:a8:2c:70:ee'
cmd = "sudo bluetoothctl disconnect 84:cc:a8:2c:70:ee"
os.system(cmd)
time.sleep(0.1)
s1 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s1.connect((serverMACAddress1,port))
time.sleep(0.1)

recv_buffer1 = b''
recv_buffer2 = b''
recv_buffer3 = b''

print("start")

def read_tjc():
    global read_tjc_button
    global port_lcd
    global s1, s2, s3
    
    try:
        global s1, s2, s3
        
        read_tjc_button = port_lcd.read_all()
        print("read_tjc_button == >> ", read_tjc_button)
        
        uart = read_tjc_button
        
        if(uart == b'\x01\x00'):
            data_pi = "BT-1-OFF";
            s1.send(data_pi.encode());
        if(uart == b'\x01\x01'):
            data_pi = "BT-1-ON";
            s1.send(data_pi.encode());
            
        if(uart == b'\x02\x00'):
            data_pi = "BT-2-OFF";
            s2.send(data_pi.encode());
        if(uart == b'\x02\x01'):
            data_pi = "BT-2-ON";
            s2.send(data_pi.encode());
        
        if(uart == b'\x03\x00'):
            data_pi = "BT-3-OFF";
            s3.send(data_pi.encode());
        if(uart == b'\x03\x01'):
            data_pi = "BT-3-ON";
            s3.send(data_pi.encode());
    except:
        print("read_tjc_button fail ~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("read_tjc_button fail ~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
    print("executed read_tjc_button")
    threading.Timer(0.3, read_tjc).start()

def task2(): # Read BT form esp32 read plc
    global s1
    global recv_buffer1
    try:
        data = s1.recv(1024)
        #data = data.decode("utf-8")
        
        recv_buffer1 += data 
        
        print(data)
        
        data = str(data)
        m = re.search(r';', data)
        
        data = data.replace(";","")
        
        if (m != None):
            recv_buffer1 = recv_buffer1.decode("utf-8")
            recv_buffer1 = recv_buffer1.replace(";","")
            recv_buffer1 = '\"' + recv_buffer1 + '\"'
            TJC_LCD2 = "t1.txt=" + str(recv_buffer1)
            #TJC_LCD2 = str('t1.txt="Touch PASS"')
            #print("TJC_LCD1 ==>>>   ", TJC_LCD2)
            port_lcd.write(TJC_LCD2.encode())
            port_lcd.write(ary_end)
            
            recv_buffer1 = b''
            data = None
        
    except:
        cmd = "sudo bluetoothctl disconnect 84:cc:a8:2c:70:ee"
        os.system(cmd)
        time.sleep(0.1)
        s1 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s1.connect((serverMACAddress1,port))
        time.sleep(0.1)
        data = None
        recv_buffer1 = b''
    
    #print("executed task2")
    threading.Timer(0.01, task2).start()

def task4(): # Read BT form esp32 read plc
    global s2
    global recv_buffer2
    try:
        data = s2.recv(1024)
        recv_buffer2 += data 
        
        sdata2 = str(recv_buffer2)
        
        m = re.search(r';', sdata2)
        
        if (m != None):
            msg2 = re.findall(r"[0-9]+", recv_buffer2.decode('utf8'))
            
            TJC_LCD2 = "n1.val=" + str(msg2[0])
            print("TJC_LCD2 ==>>>   ", TJC_LCD2)
            
            port_lcd.write(TJC_LCD2.encode())
            port_lcd.write(ary_end)
            
            recv_buffer2 = b''
            data = None
        
    except:
        cmd = "sudo bluetoothctl disconnect 9c:9c:1f:cb:13:1a"
        os.system(cmd)
        time.sleep(0.1)
        s2 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s2.connect((serverMACAddress2,port))
        time.sleep(0.1)
        data = None
        recv_buffer = b''
    
    print("executed task4")
    threading.Timer(1, task4).start()

def task6(): # Read BT form esp32 read plc
    global s3
    global recv_buffer3
    try:
        data = s3.recv(1024)
        
        msg2 = re.findall(r"[0-9]+", data.decode('utf8'))
        
        TJC_LCD2 = "n2.val=" + str(msg2[0])
        print("TJC_LCD3 ==>>>   ", TJC_LCD2)
        
        port_lcd.write(TJC_LCD2.encode())
        port_lcd.write(ary_end)
        
        recv_buffer3 = b''
        data = None
        
    except:
        cmd = "sudo bluetoothctl disconnect 9c:9c:1f:c9:fd:d2"
        os.system(cmd)
        time.sleep(0.1)
        s3 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s3.connect((serverMACAddress3,port))
        time.sleep(0.1)
        data = None
        recv_buffer3 = b''
    
    print("executed task6")
    threading.Timer(0.2, task6).start()


if __name__ == '__main__':
    #read_tjc()
    task2()
    #task4()
    #task6()