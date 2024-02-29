import paho.mqtt.client as mqtt
from lib.Topic2TJC.MQTT_Init import display_tjc
from lib.Topic2TJC.MQTT_Init import float_reduce_str
from lib.Topic2TJC.MQTT_Init import serial_init
from lib.Topic2TJC.MQTT_Init import on_connect
from lib.Topic2TJC.MQTT_Init import on_disconnect

print("SN.PY ------------------------------------ 555555 ")
serial_init()

# ############################################
# MQTT initial
# ############################################
client_sn5 = mqtt.Client("rpi_client_sn5") #this should be a unique name
flag_connected = 0
client_sn5.on_connect = on_connect
client_sn5.on_disconnect = on_disconnect

# "clinet" device name define
def client_subscriptions(client_sn5):
    client_sn5.subscribe("cvilux/5/#")
    client_sn5.subscribe("warn/5/#")

###############################################
# SN5 Warning define
###############################################
global warning_over
warning_over = 0

global warning_clear
warning_clear = 0

def callback_esp32_5_temp_warn(client_sn5, userdata, msg):
    global warning_over
    global warning_clear

    temp_warn_5 = msg.payload.decode('utf-8')
    
    if(temp_warn_5 == "over"):
        # warning_over = warning_over + 1
        # print("warning_over  ++++++++++++++++++++++++++++++++++++>> ", warning_over)
        display_tjc("Warning","b5.txt")

    # if(temp_warn_5 == "clear"):
    #     warning_clear = warning_clear + 1
    #     print("warning_clear  -------------------------------------->> ", warning_clear)

client_sn5.message_callback_add('warn/5/#', callback_esp32_5_temp_warn)

# "訊息分類/序列/感測器類型/第幾顆"
# "cvilux/1/pm1_0/1"
###############################################
# SN5-1
###############################################
def callback_esp32_1_pm2_5(client_sn5, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t101.txt")
client_sn5.message_callback_add('cvilux/5/pm2_5/1', callback_esp32_1_pm2_5)

def callback_esp32_1_pm10(client_sn5, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t102.txt")
client_sn5.message_callback_add('cvilux/5/pm10/1', callback_esp32_1_pm10)

def callback_esp32_1_pm1_0(client_sn5, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t103.txt")
client_sn5.message_callback_add('cvilux/5/pm1_0/1', callback_esp32_1_pm1_0)

###############################################
# SN5-2
###############################################
def callback_esp32_2_pm2_5(client_sn5, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t104.txt")
client_sn5.message_callback_add('cvilux/5/pm2_5/2', callback_esp32_2_pm2_5)

def callback_esp32_2_pm10(client_sn5, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t105.txt")
client_sn5.message_callback_add('cvilux/5/pm10/2', callback_esp32_2_pm10)

def callback_esp32_2_pm1_0(client_sn5, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t106.txt")
client_sn5.message_callback_add('cvilux/5/pm1_0/2', callback_esp32_2_pm1_0)

###############################################
# SN5-3
###############################################
def callback_esp32_3_pm2_5(client_sn5, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t107.txt")
client_sn5.message_callback_add('cvilux/5/pm2_5/3', callback_esp32_3_pm2_5)

def callback_esp32_3_pm10(client_sn5, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t108.txt")
client_sn5.message_callback_add('cvilux/5/pm10/3', callback_esp32_3_pm10)

def callback_esp32_3_pm1_0(client_sn5, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t109.txt")
client_sn5.message_callback_add('cvilux/5/pm1_0/3', callback_esp32_3_pm1_0)

###############################################
# SN5-4
###############################################
def callback_esp32_4_pm2_5(client_sn5, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t110.txt")
client_sn5.message_callback_add('cvilux/5/pm2_5/4', callback_esp32_4_pm2_5)

def callback_esp32_4_pm10(client_sn5, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t111.txt")
client_sn5.message_callback_add('cvilux/5/pm10/4', callback_esp32_4_pm10)

def callback_esp32_4_pm1_0(client_sn5, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t112.txt")
client_sn5.message_callback_add('cvilux/5/pm1_0/4', callback_esp32_4_pm1_0)

###############################################
# SN5-5
###############################################
def callback_esp32_5_pm2_5(client_sn5, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t113.txt")
client_sn5.message_callback_add('cvilux/5/pm2_5/5', callback_esp32_5_pm2_5)

def callback_esp32_5_pm10(client_sn5, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t114.txt")
client_sn5.message_callback_add('cvilux/5/pm10/5', callback_esp32_5_pm10)

def callback_esp32_5_pm1_0(client_sn5, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t115.txt")
client_sn5.message_callback_add('cvilux/5/pm1_0/5', callback_esp32_5_pm1_0)

###############################################
# SN5-6
###############################################
def callback_esp32_6_pm2_5(client_sn5, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t116.txt")
client_sn5.message_callback_add('cvilux/5/pm2_5/6', callback_esp32_6_pm2_5)

def callback_esp32_6_pm10(client_sn5, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t117.txt")
client_sn5.message_callback_add('cvilux/5/pm10/6', callback_esp32_6_pm10)

def callback_esp32_6_pm1_0(client_sn5, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t118.txt")
client_sn5.message_callback_add('cvilux/5/pm1_0/6', callback_esp32_6_pm1_0)

###############################################
# SN5-7
###############################################
def callback_esp32_7_pm2_5(client_sn5, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t119.txt")
client_sn5.message_callback_add('cvilux/5/pm2_5/7', callback_esp32_7_pm2_5)

def callback_esp32_7_pm10(client_sn5, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t120.txt")
client_sn5.message_callback_add('cvilux/5/pm10/7', callback_esp32_7_pm10)

def callback_esp32_7_pm1_0(client_sn5, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t121.txt")
client_sn5.message_callback_add('cvilux/5/pm1_0/7', callback_esp32_7_pm1_0)

###############################################
# SN5-8
###############################################
def callback_esp32_8_pm2_5(client_sn5, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t122.txt")
client_sn5.message_callback_add('cvilux/5/pm2_5/8', callback_esp32_8_pm2_5)

def callback_esp32_8_pm10(client_sn5, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t123.txt")
client_sn5.message_callback_add('cvilux/5/pm10/8', callback_esp32_8_pm10)

def callback_esp32_8_pm1_0(client_sn5, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t124.txt")
client_sn5.message_callback_add('cvilux/5/pm1_0/8', callback_esp32_8_pm1_0)

# ############################################
# Client to connecct MQTT server
# ############################################
client_sn5.connect('127.0.0.1',1883)
client_sn5.loop_start() # start a new thread
client_subscriptions(client_sn5)
print("......client_sn5 setup complete............")
# MQTT initial END
# ############################################