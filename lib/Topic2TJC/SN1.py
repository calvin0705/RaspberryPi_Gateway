import paho.mqtt.client as mqtt
import serial
from lib.Topic2TJC.MQTT_Init import float_reduce_str

print("SN.PY ------------------------------------ 111111")

end = [0xff, 0xff, 0xff]
port_lcd = serial.Serial(port='/dev/ttyAMA1', baudrate=115200, parity='N', stopbits=1, bytesize=8, timeout=1.0)
ary_end = bytearray(end)

# ############################################
# MQTT initial
# ############################################
def on_connect(client_sn1, userdata, flags, rc):
   global flag_connected
   flag_connected = 1
   client_subscriptions(client_sn1)
   print("Connected to MQTT server")

def on_disconnect(client_sn1, userdata, rc):
   global flag_connected
   flag_connected = 0
   print("Disconnected from MQTT server")

client_sn1 = mqtt.Client("rpi_client_sn1") #this should be a unique name
flag_connected = 0
client_sn1.on_connect = on_connect
client_sn1.on_disconnect = on_disconnect

# "clinet" device name define
def client_subscriptions(client_sn1):
    client_sn1.subscribe("cvilux/1/#")

# ############################################
# Sub Function
# ############################################
# def float_reduce_str(sen_payload,float_num,txt_num):

#     sen_payload = float(sen_payload)
#     sen_payload = round(sen_payload, float_num)
#     ESP_temp1_tjc = str(sen_payload)
#     print("ESP_temp1_tjc : ", ESP_temp1_tjc)

#     try:
#         recv_buffer = '\"' + ESP_temp1_tjc + '\"'
#         txt_num = txt_num + '='
#         TJC_LCD2 = txt_num + recv_buffer
#         port_lcd.write(TJC_LCD2.encode())
#         port_lcd.write(ary_end)
        
#         recv_buffer = b''
#         data = None
        
#     except:
#         print("float_reduce_str fail => ", txt_num)

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
    float_reduce_str(ESP_humi1,2,"t271.txt")
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