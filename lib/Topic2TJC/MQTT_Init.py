import paho.mqtt.client as mqtt
import serial

end = [0xff, 0xff, 0xff]
port_lcd = serial.Serial(port='/dev/ttyAMA1', baudrate=115200, parity='N', stopbits=1, bytesize=8, timeout=1.0)
ary_end = bytearray(end)

def float_reduce_str(sen_payload,float_num,txt_num):

    sen_payload = float(sen_payload)
    sen_payload = round(sen_payload, float_num)
    ESP_temp1_tjc = str(sen_payload)
    print("ESP_temp1_tjc : ", ESP_temp1_tjc)

    try:
        recv_buffer = '\"' + ESP_temp1_tjc + '\"'
        txt_num = txt_num + '='
        TJC_LCD2 = txt_num + recv_buffer
        port_lcd.write(TJC_LCD2.encode())
        port_lcd.write(ary_end)
        
        recv_buffer = b''
        data = None
        
    except:
        print("float_reduce_str fail => ", txt_num)
    