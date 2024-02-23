import paho.mqtt.client as mqtt
from lib.Topic2TJC.MQTT_Init import display_tjc
from lib.Topic2TJC.MQTT_Init import float_reduce_str
from lib.Topic2TJC.MQTT_Init import serial_init
from lib.Topic2TJC.MQTT_Init import on_connect
from lib.Topic2TJC.MQTT_Init import on_disconnect

print("SN.PY ------------------------------------ 777777 ")
serial_init()

# ############################################
# MQTT initial
# ############################################
client_sn7 = mqtt.Client("rpi_client_sn7") #this should be a unique name
flag_connected = 0
client_sn7.on_connect = on_connect
client_sn7.on_disconnect = on_disconnect

# "clinet" device name define
def client_subscriptions(client_sn7):
    client_sn7.subscribe("cvilux/7/#")
    client_sn7.subscribe("warn/7/#")

###############################################
# SN7 Warning define
###############################################
global warning_over
warning_over = 0

global warning_clear
warning_clear = 0

def callback_esp32_7_temp_warn(client_sn7, userdata, msg):
    global warning_over
    global warning_clear

    temp_warn_7 = msg.payload.decode('utf-8')
    
    if(temp_warn_7 == "over"):
        warning_over = warning_over + 1
        print("warning_over  ++++++++++++++++++++++++++++++++++++>> ", warning_over)
        display_tjc("Warning","b7.txt")

    # if(temp_warn_7 == "clear"):
    #     warning_clear = warning_clear + 1
    #     print("warning_clear  -------------------------------------->> ", warning_clear)

client_sn7.message_callback_add('warn/7/#', callback_esp32_7_temp_warn)

# "訊息分類/序列/感測器類型/第幾顆"
# "cvilux/1/pm1_0/1"
###############################################
# SN7-1
###############################################
def callback_esp32_1_co2(client_sn7, userdata, msg):
    ESP_co2 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co2,2,"t270.txt")
client_sn7.message_callback_add('cvilux/7/co2/1', callback_esp32_1_co2)

def callback_esp32_1_temp(client_sn7, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t271.txt")
client_sn7.message_callback_add('cvilux/7/temp/1', callback_esp32_1_temp)

def callback_esp32_1_humi(client_sn7, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t272.txt")
client_sn7.message_callback_add('cvilux/7/humi/1', callback_esp32_1_humi)

###############################################
# SN7-2
###############################################
def callback_esp32_2_co2(client_sn7, userdata, msg):
    ESP_co2 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co2,2,"t273.txt")
client_sn7.message_callback_add('cvilux/7/co2/2', callback_esp32_2_co2)

def callback_esp32_2_temp(client_sn7, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t274.txt")
client_sn7.message_callback_add('cvilux/7/temp/2', callback_esp32_2_temp)

def callback_esp32_2_humi(client_sn7, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t275.txt")
client_sn7.message_callback_add('cvilux/7/humi/2', callback_esp32_2_humi)

###############################################
# SN7-3
###############################################
def callback_esp32_3_co2(client_sn7, userdata, msg):
    ESP_co2 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co2,2,"t276.txt")
client_sn7.message_callback_add('cvilux/7/co2/3', callback_esp32_3_co2)

def callback_esp32_3_temp(client_sn7, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t277.txt")
client_sn7.message_callback_add('cvilux/7/temp/3', callback_esp32_3_temp)

def callback_esp32_3_humi(client_sn7, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t278.txt")
client_sn7.message_callback_add('cvilux/7/humi/3', callback_esp32_3_humi)

###############################################
# SN7-4
###############################################
def callback_esp32_4_co2(client_sn7, userdata, msg):
    ESP_co2 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co2,2,"t279.txt")
client_sn7.message_callback_add('cvilux/7/co2/4', callback_esp32_4_co2)

def callback_esp32_4_temp(client_sn7, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t280.txt")
client_sn7.message_callback_add('cvilux/7/temp/4', callback_esp32_4_temp)

def callback_esp32_4_humi(client_sn7, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t281.txt")
client_sn7.message_callback_add('cvilux/7/humi/4', callback_esp32_4_humi)

###############################################
# SN7-5
###############################################
def callback_esp32_5_co2(client_sn7, userdata, msg):
    ESP_co2 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co2,2,"t282.txt")
client_sn7.message_callback_add('cvilux/7/co2/5', callback_esp32_5_co2)

def callback_esp32_5_temp(client_sn7, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t283.txt")
client_sn7.message_callback_add('cvilux/7/temp/5', callback_esp32_5_temp)

def callback_esp32_5_humi(client_sn7, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t284.txt")
client_sn7.message_callback_add('cvilux/7/humi/5', callback_esp32_5_humi)

###############################################
# SN7-6
###############################################
def callback_esp32_6_co2(client_sn7, userdata, msg):
    ESP_co2 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co2,2,"t285.txt")
client_sn7.message_callback_add('cvilux/7/co2/6', callback_esp32_6_co2)

def callback_esp32_6_temp(client_sn7, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t286.txt")
client_sn7.message_callback_add('cvilux/7/temp/6', callback_esp32_6_temp)

def callback_esp32_6_humi(client_sn7, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t287.txt")
client_sn7.message_callback_add('cvilux/7/humi/6', callback_esp32_6_humi)

# ############################################
# Client to connecct MQTT server
# ############################################
client_sn7.connect('127.0.0.1',1883)
client_sn7.loop_start() # start a new thread
client_subscriptions(client_sn7)
print("......client_sn7 setup complete............")
# MQTT initial END
# ############################################