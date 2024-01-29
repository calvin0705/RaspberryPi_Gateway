import paho.mqtt.client as mqtt
from lib.Topic2TJC.MQTT_Init import float_reduce_str
from lib.Topic2TJC.MQTT_Init import serial_init
from lib.Topic2TJC.MQTT_Init import on_connect
from lib.Topic2TJC.MQTT_Init import on_disconnect

print("SN.PY ------------------------------------ 222222 ")
serial_init()

# ############################################
# MQTT initial
# ############################################
client_sn2 = mqtt.Client("rpi_client_sn2") #this should be a unique name
flag_connected = 0
client_sn2.on_connect = on_connect
client_sn2.on_disconnect = on_disconnect

# "clinet" device name define
def client_subscriptions(client_sn2):
    client_sn2.subscribe("cvilux/2/#")

# "訊息分類/序列/感測器類型/第幾顆"
# "cvilux/1/pm1_0/1"
###############################################
# SN2-1
###############################################
def callback_esp32_1_co(client_sn2, userdata, msg):
    ESP_co = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co,2,"t41.txt")
client_sn2.message_callback_add('cvilux/2/co/1', callback_esp32_1_co)

###############################################
# SN2-2
###############################################
def callback_esp32_2_co(client_sn2, userdata, msg):
    ESP_co = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co,2,"t42.txt")
client_sn2.message_callback_add('cvilux/2/co/2', callback_esp32_2_co)

###############################################
# SN2-3
###############################################
def callback_esp32_3_co(client_sn2, userdata, msg):
    ESP_co = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co,2,"t43.txt")
client_sn2.message_callback_add('cvilux/2/co/3', callback_esp32_3_co)

###############################################
# SN2-4
###############################################
def callback_esp32_4_co(client_sn2, userdata, msg):
    ESP_co = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co,2,"t44.txt")
client_sn2.message_callback_add('cvilux/2/co/4', callback_esp32_4_co)

###############################################
# SN2-5
###############################################
def callback_esp32_5_co(client_sn2, userdata, msg):
    ESP_co = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co,2,"t45.txt")
client_sn2.message_callback_add('cvilux/2/co/5', callback_esp32_5_co)

###############################################
# SN2-6
###############################################
def callback_esp32_6_co(client_sn2, userdata, msg):
    ESP_co = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co,2,"t46.txt")
client_sn2.message_callback_add('cvilux/2/co/6', callback_esp32_6_co)

###############################################
# SN2-7
###############################################
def callback_esp32_7_co(client_sn2, userdata, msg):
    ESP_co = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co,2,"t47.txt")
client_sn2.message_callback_add('cvilux/2/co/7', callback_esp32_7_co)

###############################################
# SN2-8
###############################################
def callback_esp32_8_co(client_sn2, userdata, msg):
    ESP_co = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co,2,"t48.txt")
client_sn2.message_callback_add('cvilux/2/co/8', callback_esp32_8_co)

###############################################
# SN2-9
###############################################
def callback_esp32_9_co(client_sn2, userdata, msg):
    ESP_co = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co,2,"t49.txt")
client_sn2.message_callback_add('cvilux/2/co/9', callback_esp32_9_co)

###############################################
# SN2-10
###############################################
def callback_esp32_10_co(client_sn2, userdata, msg):
    ESP_co = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co,2,"t50.txt")
client_sn2.message_callback_add('cvilux/2/co/10', callback_esp32_10_co)

# ############################################
# Client to connecct MQTT server
# ############################################
client_sn2.connect('127.0.0.1',1883)
client_sn2.loop_start() # start a new thread
client_subscriptions(client_sn2)
print("......client_sn2 setup complete............")
# MQTT initial END
# ############################################