import paho.mqtt.client as mqtt
from lib.Topic2TJC.MQTT_Init import display_tjc
from lib.Topic2TJC.MQTT_Init import float_reduce_str
from lib.Topic2TJC.MQTT_Init import serial_init
from lib.Topic2TJC.MQTT_Init import on_connect
from lib.Topic2TJC.MQTT_Init import on_disconnect

print("SN.PY ------------------------------------ 666666 ")
serial_init()

# ############################################
# MQTT initial
# ############################################
client_sn6 = mqtt.Client("rpi_client_sn6") #this should be a unique name
flag_connected = 0
client_sn6.on_connect = on_connect
client_sn6.on_disconnect = on_disconnect

# "clinet" device name define
def client_subscriptions(client_sn6):
    client_sn6.subscribe("cvilux/6/#")
    client_sn6.subscribe("warn/6/#")

###############################################
# SN6 Warning define
###############################################
global warning_over
warning_over = 0

global warning_clear
warning_clear = 0

def callback_esp32_6_temp_warn(client_sn6, userdata, msg):
    global warning_over
    global warning_clear

    temp_warn_6 = msg.payload.decode('utf-8')
    
    if(temp_warn_6 == "over"):
        # warning_over = warning_over + 1
        # print("warning_over  ++++++++++++++++++++++++++++++++++++>> ", warning_over)
        display_tjc("Warning","b6.txt")

    # if(temp_warn_6 == "clear"):
    #     warning_clear = warning_clear + 1
    #     print("warning_clear  -------------------------------------->> ", warning_clear)

client_sn6.message_callback_add('warn/6/#', callback_esp32_6_temp_warn)

# "訊息分類/序列/感測器類型/第幾顆"
# "cvilux/1/pm1_0/1"
###############################################
# SN6-1
###############################################
def callback_esp32_1_co(client_sn6, userdata, msg):
    ESP_co = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co,2,"t220.txt")
client_sn6.message_callback_add('cvilux/6/co/1', callback_esp32_1_co)

def callback_esp32_1_temp(client_sn6, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t221.txt")
client_sn6.message_callback_add('cvilux/6/temp/1', callback_esp32_1_temp)

def callback_esp32_1_humi(client_sn6, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t222.txt")
client_sn6.message_callback_add('cvilux/6/humi/1', callback_esp32_1_humi)

###############################################
# SN6-2
###############################################
def callback_esp32_2_co(client_sn6, userdata, msg):
    ESP_co = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co,2,"t223.txt")
client_sn6.message_callback_add('cvilux/6/co/2', callback_esp32_2_co)

def callback_esp32_2_temp(client_sn6, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t224.txt")
client_sn6.message_callback_add('cvilux/6/temp/2', callback_esp32_2_temp)

def callback_esp32_2_humi(client_sn6, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t225.txt")
client_sn6.message_callback_add('cvilux/6/humi/2', callback_esp32_2_humi)

###############################################
# SN6-3
###############################################
def callback_esp32_3_co(client_sn6, userdata, msg):
    ESP_co = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co,2,"t226.txt")
client_sn6.message_callback_add('cvilux/6/co/3', callback_esp32_3_co)

def callback_esp32_3_temp(client_sn6, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t227.txt")
client_sn6.message_callback_add('cvilux/6/temp/3', callback_esp32_3_temp)

def callback_esp32_3_humi(client_sn6, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t228.txt")
client_sn6.message_callback_add('cvilux/6/humi/3', callback_esp32_3_humi)

###############################################
# SN6-4
###############################################
def callback_esp32_4_co(client_sn6, userdata, msg):
    ESP_co = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co,2,"t229.txt")
client_sn6.message_callback_add('cvilux/6/co/4', callback_esp32_4_co)

def callback_esp32_4_temp(client_sn6, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t230.txt")
client_sn6.message_callback_add('cvilux/6/temp/4', callback_esp32_4_temp)

def callback_esp32_4_humi(client_sn6, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t231.txt")
client_sn6.message_callback_add('cvilux/6/humi/4', callback_esp32_4_humi)

###############################################
# SN6-5
###############################################
def callback_esp32_5_co(client_sn6, userdata, msg):
    ESP_co = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co,2,"t232.txt")
client_sn6.message_callback_add('cvilux/6/co/5', callback_esp32_5_co)

def callback_esp32_5_temp(client_sn6, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t233.txt")
client_sn6.message_callback_add('cvilux/6/temp/5', callback_esp32_5_temp)

def callback_esp32_5_humi(client_sn6, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t234.txt")
client_sn6.message_callback_add('cvilux/6/humi/5', callback_esp32_5_humi)

###############################################
# SN6-6
###############################################
def callback_esp32_6_co(client_sn6, userdata, msg):
    ESP_co = msg.payload.decode('utf-8')
    float_reduce_str(ESP_co,2,"t235.txt")
client_sn6.message_callback_add('cvilux/6/co/6', callback_esp32_6_co)

def callback_esp32_6_temp(client_sn6, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t236.txt")
client_sn6.message_callback_add('cvilux/6/temp/6', callback_esp32_6_temp)

def callback_esp32_6_humi(client_sn6, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t237.txt")
client_sn6.message_callback_add('cvilux/6/humi/6', callback_esp32_6_humi)

# ############################################
# Client to connecct MQTT server
# ############################################
client_sn6.connect('127.0.0.1',1883)
client_sn6.loop_start() # start a new thread
client_subscriptions(client_sn6)
print("......client_sn6 setup complete............")
# MQTT initial END
# ############################################