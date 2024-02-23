import paho.mqtt.client as mqtt
from lib.Topic2TJC.MQTT_Init import display_tjc
from lib.Topic2TJC.MQTT_Init import float_reduce_str
from lib.Topic2TJC.MQTT_Init import serial_init
from lib.Topic2TJC.MQTT_Init import on_connect
from lib.Topic2TJC.MQTT_Init import on_disconnect

print("SN.PY ------------------------------------ 444444 ")
serial_init()

# ############################################
# MQTT initial
# ############################################
client_sn4 = mqtt.Client("rpi_client_sn4") #this should be a unique name
flag_connected = 0
client_sn4.on_connect = on_connect
client_sn4.on_disconnect = on_disconnect

# "clinet" device name define
def client_subscriptions(client_sn4):
    client_sn4.subscribe("cvilux/4/#")
    client_sn4.subscribe("warn/4/#")

###############################################
# SN4 Warning define
###############################################
global warning_over
warning_over = 0

global warning_clear
warning_clear = 0

def callback_esp32_4_temp_warn(client_sn4, userdata, msg):
    global warning_over
    global warning_clear

    temp_warn_4 = msg.payload.decode('utf-8')
    
    if(temp_warn_4 == "over"):
        warning_over = warning_over + 1
        print("warning_over  ++++++++++++++++++++++++++++++++++++>> ", warning_over)
        display_tjc("Warning","b4.txt")

    # if(temp_warn_4 == "clear"):
    #     warning_clear = warning_clear + 1
    #     print("warning_clear  -------------------------------------->> ", warning_clear)

client_sn4.message_callback_add('warn/4/#', callback_esp32_4_temp_warn)

# "訊息分類/序列/感測器類型/第幾顆"
# "cvilux/1/pm1_0/1"
###############################################
# SN4-1
###############################################
def callback_esp32_1_ch2o(client_sn4, userdata, msg):
    ESP_ch2o = msg.payload.decode('utf-8')
    float_reduce_str(ESP_ch2o,2,"t81.txt")
client_sn4.message_callback_add('cvilux/4/ch2o/1', callback_esp32_1_ch2o)

###############################################
# SN4-2
###############################################
def callback_esp32_2_ch2o(client_sn4, userdata, msg):
    ESP_ch2o = msg.payload.decode('utf-8')
    float_reduce_str(ESP_ch2o,2,"t82.txt")
client_sn4.message_callback_add('cvilux/4/ch2o/2', callback_esp32_2_ch2o)

###############################################
# SN4-3
###############################################
def callback_esp32_3_ch2o(client_sn4, userdata, msg):
    ESP_ch2o = msg.payload.decode('utf-8')
    float_reduce_str(ESP_ch2o,2,"t83.txt")
client_sn4.message_callback_add('cvilux/4/ch2o/3', callback_esp32_3_ch2o)

###############################################
# SN4-4
###############################################
def callback_esp32_4_ch2o(client_sn4, userdata, msg):
    ESP_ch2o = msg.payload.decode('utf-8')
    float_reduce_str(ESP_ch2o,2,"t84.txt")
client_sn4.message_callback_add('cvilux/4/ch2o/4', callback_esp32_4_ch2o)

###############################################
# SN4-5
###############################################
def callback_esp32_5_ch2o(client_sn4, userdata, msg):
    ESP_ch2o = msg.payload.decode('utf-8')
    float_reduce_str(ESP_ch2o,2,"t85.txt")
client_sn4.message_callback_add('cvilux/4/ch2o/5', callback_esp32_5_ch2o)

###############################################
# SN4-6
###############################################
def callback_esp32_6_ch2o(client_sn4, userdata, msg):
    ESP_ch2o = msg.payload.decode('utf-8')
    float_reduce_str(ESP_ch2o,2,"t86.txt")
client_sn4.message_callback_add('cvilux/4/ch2o/6', callback_esp32_6_ch2o)

###############################################
# SN4-7
###############################################
def callback_esp32_7_ch2o(client_sn4, userdata, msg):
    ESP_ch2o = msg.payload.decode('utf-8')
    float_reduce_str(ESP_ch2o,2,"t87.txt")
client_sn4.message_callback_add('cvilux/4/ch2o/7', callback_esp32_7_ch2o)

###############################################
# SN4-8
###############################################
def callback_esp32_8_ch2o(client_sn4, userdata, msg):
    ESP_ch2o = msg.payload.decode('utf-8')
    float_reduce_str(ESP_ch2o,2,"t88.txt")
client_sn4.message_callback_add('cvilux/4/ch2o/8', callback_esp32_8_ch2o)

###############################################
# SN4-9
###############################################
def callback_esp32_9_ch2o(client_sn4, userdata, msg):
    ESP_ch2o = msg.payload.decode('utf-8')
    float_reduce_str(ESP_ch2o,2,"t89.txt")
client_sn4.message_callback_add('cvilux/4/ch2o/9', callback_esp32_9_ch2o)

###############################################
# SN4-10
###############################################
def callback_esp32_10_ch2o(client_sn4, userdata, msg):
    ESP_ch2o = msg.payload.decode('utf-8')
    float_reduce_str(ESP_ch2o,2,"t90.txt")
client_sn4.message_callback_add('cvilux/4/ch2o/10', callback_esp32_10_ch2o)

# ############################################
# Client to connecct MQTT server
# ############################################
client_sn4.connect('127.0.0.1',1883)
client_sn4.loop_start() # start a new thread
client_subscriptions(client_sn4)
print("......client_sn4 setup complete............")
# MQTT initial END
# ############################################