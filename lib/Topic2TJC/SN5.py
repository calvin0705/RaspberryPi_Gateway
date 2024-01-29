import paho.mqtt.client as mqtt
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
    float_reduce_str(ESP_pm2_5,2,"t101.txt")
client_sn5.message_callback_add('cvilux/5/pm2_5/2', callback_esp32_2_pm2_5)

def callback_esp32_2_pm10(client_sn5, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t102.txt")
client_sn5.message_callback_add('cvilux/5/pm10/2', callback_esp32_2_pm10)

def callback_esp32_2_pm1_0(client_sn5, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t103.txt")
client_sn5.message_callback_add('cvilux/5/pm1_0/2', callback_esp32_2_pm1_0)

###############################################
# SN5-3
###############################################
def callback_esp32_3_pm2_5(client_sn5, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t101.txt")
client_sn5.message_callback_add('cvilux/5/pm2_5/3', callback_esp32_3_pm2_5)

def callback_esp32_3_pm10(client_sn5, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t102.txt")
client_sn5.message_callback_add('cvilux/5/pm10/3', callback_esp32_3_pm10)

def callback_esp32_3_pm1_0(client_sn5, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t103.txt")
client_sn5.message_callback_add('cvilux/5/pm1_0/3', callback_esp32_3_pm1_0)

###############################################
# SN5-4
###############################################
def callback_esp32_4_pm2_5(client_sn5, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t101.txt")
client_sn5.message_callback_add('cvilux/5/pm2_5/4', callback_esp32_4_pm2_5)

def callback_esp32_4_pm10(client_sn5, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t102.txt")
client_sn5.message_callback_add('cvilux/5/pm10/4', callback_esp32_4_pm10)

def callback_esp32_4_pm1_0(client_sn5, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t103.txt")
client_sn5.message_callback_add('cvilux/5/pm1_0/4', callback_esp32_4_pm1_0)

###############################################
# SN5-5
###############################################
def callback_esp32_5_pm2_5(client_sn5, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t101.txt")
client_sn5.message_callback_add('cvilux/5/pm2_5/5', callback_esp32_5_pm2_5)

def callback_esp32_5_pm10(client_sn5, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t102.txt")
client_sn5.message_callback_add('cvilux/5/pm10/5', callback_esp32_5_pm10)

def callback_esp32_5_pm1_0(client_sn5, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t103.txt")
client_sn5.message_callback_add('cvilux/5/pm1_0/5', callback_esp32_5_pm1_0)

###############################################
# SN5-6
###############################################
def callback_esp32_6_pm2_5(client_sn5, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t101.txt")
client_sn5.message_callback_add('cvilux/5/pm2_5/6', callback_esp32_6_pm2_5)

def callback_esp32_6_pm10(client_sn5, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t102.txt")
client_sn5.message_callback_add('cvilux/5/pm10/6', callback_esp32_6_pm10)

def callback_esp32_6_pm1_0(client_sn5, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t103.txt")
client_sn5.message_callback_add('cvilux/5/pm1_0/6', callback_esp32_6_pm1_0)

###############################################
# SN5-7
###############################################
def callback_esp32_7_pm2_5(client_sn5, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t101.txt")
client_sn5.message_callback_add('cvilux/5/pm2_5/7', callback_esp32_7_pm2_5)

def callback_esp32_7_pm10(client_sn5, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t102.txt")
client_sn5.message_callback_add('cvilux/5/pm10/7', callback_esp32_7_pm10)

def callback_esp32_7_pm1_0(client_sn5, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t103.txt")
client_sn5.message_callback_add('cvilux/5/pm1_0/7', callback_esp32_7_pm1_0)

###############################################
# SN5-8
###############################################
def callback_esp32_8_pm2_5(client_sn5, userdata, msg):
    ESP_pm2_5 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm2_5,2,"t101.txt")
client_sn5.message_callback_add('cvilux/5/pm2_5/8', callback_esp32_8_pm2_5)

def callback_esp32_8_pm10(client_sn5, userdata, msg):
    ESP_pm10 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm10,2,"t102.txt")
client_sn5.message_callback_add('cvilux/5/pm10/8', callback_esp32_8_pm10)

def callback_esp32_8_pm1_0(client_sn5, userdata, msg):
    ESP_pm1_0 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_pm1_0,2,"t103.txt")
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