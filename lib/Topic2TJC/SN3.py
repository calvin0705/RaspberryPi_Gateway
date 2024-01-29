import paho.mqtt.client as mqtt
from lib.Topic2TJC.MQTT_Init import float_reduce_str
from lib.Topic2TJC.MQTT_Init import serial_init
from lib.Topic2TJC.MQTT_Init import on_connect
from lib.Topic2TJC.MQTT_Init import on_disconnect

print("SN.PY ------------------------------------ 333333 ")
serial_init()

# ############################################
# MQTT initial
# ############################################
client_sn3 = mqtt.Client("rpi_client_sn3") #this should be a unique name
flag_connected = 0
client_sn3.on_connect = on_connect
client_sn3.on_disconnect = on_disconnect

# "clinet" device name define
def client_subscriptions(client_sn3):
    client_sn3.subscribe("cvilux/3/#")

# "訊息分類/序列/感測器類型/第幾顆"
# "cvilux/1/pm1_0/1"
###############################################
# SN3-1
###############################################
def callback_esp32_1_co2(client_sn3, userdata, msg):
    ESP_co2 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co2,2,"t61.txt")
client_sn3.message_callback_add('cvilux/3/co2/1', callback_esp32_1_co2)

###############################################
# SN3-2
###############################################
def callback_esp32_2_co2(client_sn3, userdata, msg):
    ESP_co2 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co2,2,"t62.txt")
client_sn3.message_callback_add('cvilux/3/co2/2', callback_esp32_2_co2)

###############################################
# SN3-3
###############################################
def callback_esp32_3_co2(client_sn3, userdata, msg):
    ESP_co2 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co2,2,"t63.txt")
client_sn3.message_callback_add('cvilux/3/co2/3', callback_esp32_3_co2)

###############################################
# SN3-4
###############################################
def callback_esp32_4_co2(client_sn3, userdata, msg):
    ESP_co2 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co2,2,"t64.txt")
client_sn3.message_callback_add('cvilux/3/co2/4', callback_esp32_4_co2)

###############################################
# SN3-5
###############################################
def callback_esp32_5_co2(client_sn3, userdata, msg):
    ESP_co2 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co2,2,"t65.txt")
client_sn3.message_callback_add('cvilux/3/co2/5', callback_esp32_5_co2)

###############################################
# SN3-6
###############################################
def callback_esp32_6_co2(client_sn3, userdata, msg):
    ESP_co2 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co2,2,"t66.txt")
client_sn3.message_callback_add('cvilux/3/co2/6', callback_esp32_6_co2)

###############################################
# SN3-7
###############################################
def callback_esp32_7_co2(client_sn3, userdata, msg):
    ESP_co2 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co2,2,"t67.txt")
client_sn3.message_callback_add('cvilux/3/co2/7', callback_esp32_7_co2)

###############################################
# SN3-8
###############################################
def callback_esp32_8_co2(client_sn3, userdata, msg):
    ESP_co2 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co2,2,"t68.txt")
client_sn3.message_callback_add('cvilux/3/co2/8', callback_esp32_8_co2)

###############################################
# SN3-9
###############################################
def callback_esp32_9_co2(client_sn3, userdata, msg):
    ESP_co2 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co2,2,"t69.txt")
client_sn3.message_callback_add('cvilux/3/co2/9', callback_esp32_9_co2)

###############################################
# SN3-10
###############################################
def callback_esp32_10_co2(client_sn3, userdata, msg):
    ESP_co2 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co2,2,"t70.txt")
client_sn3.message_callback_add('cvilux/3/co2/10', callback_esp32_10_co2)

# ############################################
# Client to connecct MQTT server
# ############################################
client_sn3.connect('127.0.0.1',1883)
client_sn3.loop_start() # start a new thread
client_subscriptions(client_sn3)
print("......client_sn3 setup complete............")
# MQTT initial END
# ############################################