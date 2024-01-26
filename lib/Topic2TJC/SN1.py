import paho.mqtt.client as mqtt
from lib.Topic2TJC.MQTT_Init import float_reduce_str
from lib.Topic2TJC.MQTT_Init import serial_init
from lib.Topic2TJC.MQTT_Init import on_connect
from lib.Topic2TJC.MQTT_Init import on_disconnect

print("SN.PY ------------------------------------ 111111")
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
    float_reduce_str(ESP_temp1,2,"t271.txt")
client_sn1.message_callback_add('cvilux/1/temp/1', callback_esp32_1_temp)

def callback_esp32_1_humi(client_sn1, userdata, msg):
    ESP_humi1 = msg.payload.decode('utf-8')
    float_reduce_str(ESP_humi1,2,"t272.txt")
client_sn1.message_callback_add('cvilux/1/humi/1', callback_esp32_1_humi)


# ############################################
# Client to connecct MQTT server
# ############################################
client_sn1.connect('127.0.0.1',1883)
client_sn1.loop_start() # start a new thread
client_subscriptions(client_sn1)
print("......client_sn1 setup complete............")
# MQTT initial END
# ############################################