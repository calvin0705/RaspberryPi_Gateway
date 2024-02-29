import paho.mqtt.client as mqtt
from lib.Topic2TJC.MQTT_Init import display_tjc
from lib.Topic2TJC.MQTT_Init import float_reduce_str
from lib.Topic2TJC.MQTT_Init import serial_init
from lib.Topic2TJC.MQTT_Init import on_connect
from lib.Topic2TJC.MQTT_Init import on_disconnect

print("SN.PY ------------------------------------ 999999 ")
serial_init()

# ############################################
# MQTT initial
# ############################################
client_sn9 = mqtt.Client("rpi_client_sn9") #this should be a unique name
flag_connected = 0
client_sn9.on_connect = on_connect
client_sn9.on_disconnect = on_disconnect

# "clinet" device name define
def client_subscriptions(client_sn9):
    client_sn9.subscribe("cvilux/9/#")
    client_sn9.subscribe("warn/9/#")

###############################################
# SN8 Warning define
###############################################
global warning_over
warning_over = 0

global warning_clear
warning_clear = 0

def callback_esp32_9_temp_warn(client_sn9, userdata, msg):
    global warning_over
    global warning_clear

    temp_warn_9 = msg.payload.decode('utf-8')
    
    if(temp_warn_9 == "over"):
        # warning_over = warning_over + 1
        # print("warning_over  ++++++++++++++++++++++++++++++++++++>> ", warning_over)
        display_tjc("Warning","b9.txt")

    # if(temp_warn_9 == "clear"):
    #     warning_clear = warning_clear + 1
    #     print("warning_clear  -------------------------------------->> ", warning_clear)

client_sn9.message_callback_add('warn/9/#', callback_esp32_9_temp_warn)

# "訊息分類/序列/感測器類型/第幾顆"
# "cvilux/1/pm1_0/1"
###############################################
# SN9-1
###############################################
def callback_esp32_1_pm2_5(client_sn9, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t370.txt")
client_sn9.message_callback_add('cvilux/9/pm2_5/1', callback_esp32_1_pm2_5)

def callback_esp32_1_pm10(client_sn9, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t371.txt")
client_sn9.message_callback_add('cvilux/9/pm10/1', callback_esp32_1_pm10)

def callback_esp32_1_pm1_0(client_sn9, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t372.txt")
client_sn9.message_callback_add('cvilux/9/pm1_0/1', callback_esp32_1_pm1_0)

def callback_esp32_1_temp(client_sn9, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t373.txt")
client_sn9.message_callback_add('cvilux/9/temp/1', callback_esp32_1_temp)

def callback_esp32_1_humi(client_sn9, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t374.txt")
client_sn9.message_callback_add('cvilux/9/humi/1', callback_esp32_1_humi)

###############################################
# SN9-2
###############################################
def callback_esp32_2_pm2_5(client_sn9, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t375.txt")
client_sn9.message_callback_add('cvilux/9/pm2_5/2', callback_esp32_2_pm2_5)

def callback_esp32_2_pm10(client_sn9, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t376.txt")
client_sn9.message_callback_add('cvilux/9/pm10/2', callback_esp32_2_pm10)

def callback_esp32_2_pm1_0(client_sn9, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t377.txt")
client_sn9.message_callback_add('cvilux/9/pm1_0/2', callback_esp32_2_pm1_0)

def callback_esp32_2_temp(client_sn9, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t378.txt")
client_sn9.message_callback_add('cvilux/9/temp/2', callback_esp32_2_temp)

def callback_esp32_2_humi(client_sn9, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t379.txt")
client_sn9.message_callback_add('cvilux/9/humi/2', callback_esp32_2_humi)

###############################################
# SN9-3
###############################################
def callback_esp32_3_pm2_5(client_sn9, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t380.txt")
client_sn9.message_callback_add('cvilux/9/pm2_5/3', callback_esp32_3_pm2_5)

def callback_esp32_3_pm10(client_sn9, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t381.txt")
client_sn9.message_callback_add('cvilux/9/pm10/3', callback_esp32_3_pm10)

def callback_esp32_3_pm1_0(client_sn9, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t382.txt")
client_sn9.message_callback_add('cvilux/9/pm1_0/3', callback_esp32_3_pm1_0)

def callback_esp32_3_temp(client_sn9, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t383.txt")
client_sn9.message_callback_add('cvilux/9/temp/3', callback_esp32_3_temp)

def callback_esp32_3_humi(client_sn9, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t384.txt")
client_sn9.message_callback_add('cvilux/9/humi/3', callback_esp32_3_humi)

###############################################
# SN9-4
###############################################
def callback_esp32_4_pm2_5(client_sn9, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t385.txt")
client_sn9.message_callback_add('cvilux/9/pm2_5/4', callback_esp32_4_pm2_5)

def callback_esp32_4_pm10(client_sn9, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t386.txt")
client_sn9.message_callback_add('cvilux/9/pm10/4', callback_esp32_4_pm10)

def callback_esp32_4_pm1_0(client_sn9, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t387.txt")
client_sn9.message_callback_add('cvilux/9/pm1_0/4', callback_esp32_4_pm1_0)

def callback_esp32_4_temp(client_sn9, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t388.txt")
client_sn9.message_callback_add('cvilux/9/temp/4', callback_esp32_4_temp)

def callback_esp32_4_humi(client_sn9, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t389.txt")
client_sn9.message_callback_add('cvilux/9/humi/4', callback_esp32_4_humi)

###############################################
# SN9-5
###############################################
def callback_esp32_5_pm2_5(client_sn9, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t390.txt")
client_sn9.message_callback_add('cvilux/9/pm2_5/5', callback_esp32_5_pm2_5)

def callback_esp32_5_pm10(client_sn9, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t391.txt")
client_sn9.message_callback_add('cvilux/9/pm10/5', callback_esp32_5_pm10)

def callback_esp32_5_pm1_0(client_sn9, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t392.txt")
client_sn9.message_callback_add('cvilux/9/pm1_0/5', callback_esp32_5_pm1_0)

def callback_esp32_5_temp(client_sn9, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t393.txt")
client_sn9.message_callback_add('cvilux/9/temp/5', callback_esp32_5_temp)

def callback_esp32_5_humi(client_sn9, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t394.txt")
client_sn9.message_callback_add('cvilux/9/humi/5', callback_esp32_5_humi)

###############################################
# SN9-6
###############################################
def callback_esp32_6_pm2_5(client_sn9, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t395.txt")
client_sn9.message_callback_add('cvilux/9/pm2_5/6', callback_esp32_6_pm2_5)

def callback_esp32_6_pm10(client_sn9, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t396.txt")
client_sn9.message_callback_add('cvilux/9/pm10/6', callback_esp32_6_pm10)

def callback_esp32_6_pm1_0(client_sn9, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t397.txt")
client_sn9.message_callback_add('cvilux/9/pm1_0/6', callback_esp32_6_pm1_0)

def callback_esp32_6_temp(client_sn9, userdata, msg):
    ESP_temp1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_temp1,2,"t398.txt")
client_sn9.message_callback_add('cvilux/9/temp/6', callback_esp32_6_temp)

def callback_esp32_6_humi(client_sn9, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t399.txt")
client_sn9.message_callback_add('cvilux/9/humi/6', callback_esp32_6_humi)

# ############################################
# Client to connecct MQTT server
# ############################################
client_sn9.connect('127.0.0.1',1883)
client_sn9.loop_start() # start a new thread
client_subscriptions(client_sn9)
print("......client_sn9 setup complete............")
# MQTT initial END
# ############################################