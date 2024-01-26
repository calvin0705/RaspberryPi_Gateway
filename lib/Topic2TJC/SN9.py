import paho.mqtt.client as mqtt
import serial

print("SN.PY ------------------------------------ 999999999999999999999999999999999999")

end = [0xff, 0xff, 0xff]
port_lcd = serial.Serial(port='/dev/ttyAMA1', baudrate=115200, parity='N', stopbits=1, bytesize=8, timeout=1.0)
ary_end = bytearray(end)

def serial_tjc():
    end = [0xff, 0xff, 0xff]
    port_lcd = serial.Serial(port='/dev/ttyAMA1', baudrate=115200, parity='N', stopbits=1, bytesize=8, timeout=1.0)
    ary_end = bytearray(end)

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

client = mqtt.Client("rpi_client1_sn9") #this should be a unique name
flag_connected = 0
client.on_connect = on_connect
client.on_disconnect = on_disconnect

# "clinet" device name define
def client_subscriptions(client):
    client.subscribe("cvilux/9/#")

# "訊息分類/序列/感測器類型/第幾顆"
# "cvilux/9/pm1_0/1"
###############################################
# MQTT Revice Test
###############################################
def MQTT_Revice_Test(client, userdata, msg):
    global cvilux_all
    cvilux_all = msg.payload.decode('utf-8')

    print("MQTT_Revice_Test(cvilux_all) ------------------------------------ 999999999999999999999999 ", cvilux_all)

client.message_callback_add('cvilux/#', MQTT_Revice_Test)
###############################################
# Define esp32_1_temp loop in callback function
# Define esp32_1_humi loop in callback function
###############################################
def q123():
    return 20

def callback_esp32_1_temp(client, userdata, msg):
    global ESP_temp1
    ESP_temp1 = msg.payload.decode('utf-8')

    print("ESP_temp1 000=====================================================>>>>> ", ESP_temp1)

    ESP_temp1 = float(ESP_temp1)

    ESP_temp1 = round(ESP_temp1, 2)

    ESP_temp1_tjc = ESP_temp1

    ESP_temp1_tjc = str(ESP_temp1_tjc)

    print("ESP_temp1 : ", ESP_temp1)

    try:
        recv_buffer = '\"' + ESP_temp1_tjc + '\"'
        TJC_LCD2 = "t271.txt=" + str(recv_buffer)
        port_lcd.write(TJC_LCD2.encode())
        port_lcd.write(ary_end)
        
        recv_buffer = b''
        data = None
        
    except:
        print("wait data to tjc lcd (task2)")

client.message_callback_add('cvilux/1/temp/1', callback_esp32_1_temp)

def callback_esp32_1_humi(client, userdata, msg):
    global ESP_humi1
    ESP_humi1 = msg.payload.decode('utf-8')
client.message_callback_add('cvilux/1/humi/1', callback_esp32_1_humi)

###############################################
# Define esp32_2_temp loop in callback function
# Define esp32_2_humi loop in callback functionz
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

    ESP_CO2 = float(ESP_CO2)

    ESP_CO2 = round(ESP_CO2, 2)

    ESP_CO2_tjc = ESP_CO2

    ESP_CO2_tjc = str(ESP_CO2_tjc)

    print("ESP_CO2 : ", ESP_CO2)

    try:
        recv_buffer = '\"' + ESP_CO2_tjc + '\"'
        TJC_LCD2 = "t270.txt=" + str(recv_buffer)
        port_lcd.write(TJC_LCD2.encode())
        port_lcd.write(ary_end)
        
        recv_buffer = b''
        data = None
        
    except:
        print("wait data to tjc lcd (task2)")
client.message_callback_add('cvilux/1/co2/1', callback_esp32_CO2)

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


client.connect('127.0.0.1',1883)

client.loop_start() # start a new thread
client_subscriptions(client)
print("......client setup complete............")
# MQTT initial END
# ############################################