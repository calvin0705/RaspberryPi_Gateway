import paho.mqtt.client as mqtt
from lib.Topic2TJC.MQTT_Init import float_reduce_str
from lib.Topic2TJC.MQTT_Init import serial_init
from lib.Topic2TJC.MQTT_Init import on_connect
from lib.Topic2TJC.MQTT_Init import on_disconnect

print("SN.PY ------------------------------------ 111111 ")
serial_init()

# ############################################
# MQTT initial
# ############################################
client_sn1 = mqtt.Client("rpi_client_sn1") #this should be a unique name
flag_connected = 0
client_sn1.on_connect = on_connect
client_sn1.on_disconnect = on_disconnect

# "clinet" device name define
def client_subscriptions(client_sn1):
    client_sn1.subscribe("cvilux/1/#")

# "訊息分類/序列/感測器類型/第幾顆"
# "cvilux/1/pm1_0/1"
###############################################
# SN1-1
###############################################
def callback_esp32_1_temp(client_sn1, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t1.txt")
client_sn1.message_callback_add('cvilux/1/temp/1', callback_esp32_1_temp)

def callback_esp32_1_humi(client_sn1, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t2.txt")
client_sn1.message_callback_add('cvilux/1/humi/1', callback_esp32_1_humi)

###############################################
# SN1-2
###############################################
def callback_esp32_2_temp(client_sn1, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t3.txt")
client_sn1.message_callback_add('cvilux/1/temp/2', callback_esp32_2_temp)

def callback_esp32_2_humi(client_sn1, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t4.txt")
client_sn1.message_callback_add('cvilux/1/humi/2', callback_esp32_2_humi)

###############################################
# SN1-3
###############################################
def callback_esp32_3_temp(client_sn1, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t5.txt")
client_sn1.message_callback_add('cvilux/1/temp/3', callback_esp32_3_temp)

def callback_esp32_3_humi(client_sn1, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t6.txt")
client_sn1.message_callback_add('cvilux/1/humi/3', callback_esp32_3_humi)

###############################################
# SN1-4
###############################################
def callback_esp32_4_temp(client_sn1, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t7.txt")
client_sn1.message_callback_add('cvilux/1/temp/4', callback_esp32_4_temp)

def callback_esp32_4_humi(client_sn1, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t8.txt")
client_sn1.message_callback_add('cvilux/1/humi/4', callback_esp32_4_humi)

###############################################
# SN1-5
###############################################
def callback_esp32_5_temp(client_sn1, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t9.txt")
client_sn1.message_callback_add('cvilux/1/temp/5', callback_esp32_5_temp)

def callback_esp32_5_humi(client_sn1, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t10.txt")
client_sn1.message_callback_add('cvilux/1/humi/5', callback_esp32_5_humi)

###############################################
# SN1-6
###############################################
def callback_esp32_6_temp(client_sn1, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t11.txt")
client_sn1.message_callback_add('cvilux/1/temp/6', callback_esp32_6_temp)

def callback_esp32_6_humi(client_sn1, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t12.txt")
client_sn1.message_callback_add('cvilux/1/humi/6', callback_esp32_6_humi)

###############################################
# SN1-7
###############################################
def callback_esp32_7_temp(client_sn1, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t13.txt")
client_sn1.message_callback_add('cvilux/1/temp/7', callback_esp32_7_temp)

def callback_esp32_7_humi(client_sn1, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t14.txt")
client_sn1.message_callback_add('cvilux/1/humi/7', callback_esp32_7_humi)

###############################################
# SN1-8
###############################################
def callback_esp32_8_temp(client_sn1, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t15.txt")
client_sn1.message_callback_add('cvilux/1/temp/8', callback_esp32_8_temp)

def callback_esp32_8_humi(client_sn1, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t16.txt")
client_sn1.message_callback_add('cvilux/1/humi/8', callback_esp32_8_humi)

###############################################
# SN1-9
###############################################
def callback_esp32_9_temp(client_sn1, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t17.txt")
client_sn1.message_callback_add('cvilux/1/temp/9', callback_esp32_9_temp)

def callback_esp32_9_humi(client_sn1, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t18.txt")
client_sn1.message_callback_add('cvilux/1/humi/9', callback_esp32_9_humi)

###############################################
# SN1-10
###############################################
def callback_esp32_10_temp(client_sn1, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t21.txt")
client_sn1.message_callback_add('cvilux/1/temp/10', callback_esp32_10_temp)

def callback_esp32_10_humi(client_sn1, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t20.txt")
client_sn1.message_callback_add('cvilux/1/humi/10', callback_esp32_10_humi)

# ############################################
# Client to connecct MQTT server
# ############################################
client_sn1.connect('127.0.0.1',1883)
client_sn1.loop_start() # start a new thread
client_subscriptions(client_sn1)
print("......client_sn1 setup complete............")
# MQTT initial END
# ############################################