import paho.mqtt.client as mqtt
import serial


def add123():
    print("1+1=2")

def serial_tjc():
    end = [0xff, 0xff, 0xff]
    port_lcd = serial.Serial(port='/dev/ttyAMA1', baudrate=115200, parity='N', stopbits=1, bytesize=8, timeout=1.0)
    ary_end = bytearray(end)

def on_connect(client, userdata, flags, rc):
   global flag_connected
   flag_connected = 1
   client_subscriptions(client)
   print("Connected to MQTT server")

def on_disconnect(client, userdata, rc):
   global flag_connected
   flag_connected = 0
   print("Disconnected from MQTT server")

def client_subscriptions(client):
    client.subscribe("cvilux/#")


# ############################################
# Set at SN py
# ############################################
# client = mqtt.Client("rpi_client1") #this should be a unique name
# flag_connected = 0
# client.on_connect = on_connect
# client.on_disconnect = on_disconnect

# ############################################

# client.connect('127.0.0.1',1883)

# client.loop_start() # start a new thread
# client_subscriptions(client)
# print("......client setup complete............")

# MQTT initial END
# ############################################
    
