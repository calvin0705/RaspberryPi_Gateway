import paho.mqtt.client as mqtt
from lib.Topic2TJC.MQTT_Init import float_reduce_str
from lib.Topic2TJC.MQTT_Init import serial_init
from lib.Topic2TJC.MQTT_Init import on_connect
from lib.Topic2TJC.MQTT_Init import on_disconnect

print("SN.PY ------------------------------------ 888888 ")
serial_init()

# ############################################
# MQTT initial
# ############################################
client_sn8 = mqtt.Client("rpi_client_sn8") #this should be a unique name
flag_connected = 0
client_sn8.on_connect = on_connect
client_sn8.on_disconnect = on_disconnect

# "clinet" device name define
def client_subscriptions(client_sn8):
    client_sn8.subscribe("cvilux/8/#")

# "訊息分類/序列/感測器類型/第幾顆"
# "cvilux/1/pm1_0/1"
###############################################
# SN8-1
###############################################
def callback_esp32_1_ch2o(client_sn8, userdata, msg):
    ESP_ch2o = msg.payload.decode('utf-8')
    float_reduce_str(ESP_ch2o,3,"t320.txt")
client_sn8.message_callback_add('cvilux/8/ch2o/1', callback_esp32_1_ch2o)

def callback_esp32_1_temp(client_sn8, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t321.txt")
client_sn8.message_callback_add('cvilux/8/temp/1', callback_esp32_1_temp)

def callback_esp32_1_humi(client_sn8, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t322.txt")
client_sn8.message_callback_add('cvilux/8/humi/1', callback_esp32_1_humi)

###############################################
# SN8-2
###############################################
def callback_esp32_2_ch2o(client_sn8, userdata, msg):
    ESP_ch2o = msg.payload.decode('utf-8')
    float_reduce_str(ESP_ch2o,2,"t323.txt")
client_sn8.message_callback_add('cvilux/8/ch2o/2', callback_esp32_2_ch2o)

def callback_esp32_2_temp(client_sn8, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t324.txt")
client_sn8.message_callback_add('cvilux/8/temp/2', callback_esp32_2_temp)

def callback_esp32_2_humi(client_sn8, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t325.txt")
client_sn8.message_callback_add('cvilux/8/humi/2', callback_esp32_2_humi)

###############################################
# SN8-3
###############################################
def callback_esp32_3_ch2o(client_sn8, userdata, msg):
    ESP_ch2o = msg.payload.decode('utf-8')
    float_reduce_str(ESP_ch2o,2,"t326.txt")
client_sn8.message_callback_add('cvilux/8/ch2o/3', callback_esp32_3_ch2o)

def callback_esp32_3_temp(client_sn8, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t327.txt")
client_sn8.message_callback_add('cvilux/8/temp/3', callback_esp32_3_temp)

def callback_esp32_3_humi(client_sn8, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t328.txt")
client_sn8.message_callback_add('cvilux/8/humi/3', callback_esp32_3_humi)

###############################################
# SN8-4
###############################################
def callback_esp32_4_ch2o(client_sn8, userdata, msg):
    ESP_ch2o = msg.payload.decode('utf-8')
    float_reduce_str(ESP_ch2o,2,"t329.txt")
client_sn8.message_callback_add('cvilux/8/ch2o/4', callback_esp32_4_ch2o)

def callback_esp32_4_temp(client_sn8, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t330.txt")
client_sn8.message_callback_add('cvilux/8/temp/4', callback_esp32_4_temp)

def callback_esp32_4_humi(client_sn8, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t331.txt")
client_sn8.message_callback_add('cvilux/8/humi/4', callback_esp32_4_humi)

###############################################
# SN8-5
###############################################
def callback_esp32_5_ch2o(client_sn8, userdata, msg):
    ESP_ch2o = msg.payload.decode('utf-8')
    float_reduce_str(ESP_ch2o,2,"t332.txt")
client_sn8.message_callback_add('cvilux/8/ch2o/5', callback_esp32_5_ch2o)

def callback_esp32_5_temp(client_sn8, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t333.txt")
client_sn8.message_callback_add('cvilux/8/temp/5', callback_esp32_5_temp)

def callback_esp32_5_humi(client_sn8, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t334.txt")
client_sn8.message_callback_add('cvilux/8/humi/5', callback_esp32_5_humi)

###############################################
# SN8-6
###############################################
def callback_esp32_6_ch2o(client_sn8, userdata, msg):
    ESP_ch2o = msg.payload.decode('utf-8')
    float_reduce_str(ESP_ch2o,2,"t335.txt")
client_sn8.message_callback_add('cvilux/8/ch2o/6', callback_esp32_6_ch2o)

def callback_esp32_6_temp(client_sn8, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t336.txt")
client_sn8.message_callback_add('cvilux/8/temp/6', callback_esp32_6_temp)

def callback_esp32_6_humi(client_sn8, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t337.txt")
client_sn8.message_callback_add('cvilux/8/humi/6', callback_esp32_6_humi)

# ############################################
# Client to connecct MQTT server
# ############################################
client_sn8.connect('127.0.0.1',1883)
client_sn8.loop_start() # start a new thread
client_subscriptions(client_sn8)
print("......client_sn8 setup complete............")
# MQTT initial END
# ############################################