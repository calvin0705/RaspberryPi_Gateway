import serial
import os
import threading
import time

end = [0xff, 0xff, 0xff]
port_lcd = serial.Serial(port='/dev/ttyAMA1', baudrate=115200, parity='N', stopbits=1, bytesize=8, timeout=1.0)
ary_end = bytearray(end)
global recv_buffer_no
global update_wifi_no
global update_wifi_counter
global update_wifi_chk
global sys1_99
global stop_counter
recv_buffer_no = 1
update_wifi_no = 0
update_wifi_counter = 10
update_wifi_chk = 0
sys1_99 = 0
stop_counter = 0

def change_static_ip(ip_address, routers, dns):
    conf_file = '/etc/dhcpcd.conf'
    try:            
        # Sanitize/validate params above
        with open(conf_file, 'r') as file:
            data = file.readlines()
            print(data)
        # Find if config exists
        ethFound = next((x for x in data if 'interface wlan0' in x), None)

        if ethFound:
            ethIndex = data.index(ethFound)
            if data[ethIndex].startswith('#'):
                data[ethIndex].replace('#', '') # commented out by default, make active
        # If config is found, use index to edit the lines you need ( the next 3)
        if ethIndex:
            data[ethIndex+1] = f'static ip_address={ip_address}/24\n'
            data[ethIndex+2] = f'static routers={routers}\n'
            data[ethIndex+3] = f'static domain_name_servers={dns}\n'
        with open(conf_file, 'w') as file:
            file.writelines( data )
    except Exception as ex:
        print("IP changing error: %s", ex)
    finally:
        pass

def set_wifi_ssid_psk(ssid, psk):
    
  os.system('sudo wpa_cli -i wlan0 set_network 0 ssid ' + '\'"' + ssid + '"\'')
  os.system('sudo wpa_cli -i wlan0 set_network 0 psk ' + '\'"' + psk + '"\'')
  os.system('sudo wpa_cli -i wlan0 select_network 0')
  os.system('sudo wpa_cli -i wlan0 enable_network 0')
  os.system('sudo wpa_cli -i wlan0 save_config')
  os.system('sudo ip link set wlan0 down')
  os.system('sudo ip link set wlan0 up')


def read_tjc_wifi_page():
    global update_wifi_chk
    global update_wifi_no
    global update_wifi_counter
    global recv_buffer_no
    global sys1_99
    global stop_counter
    print("**********************")
    try:
        time.sleep(0.1)
        port_lcd.write("get sys1".encode())
        port_lcd.write(ary_end)
        chk_sys1=list(port_lcd.read(200))
        print(99 in chk_sys1)
        
        if (update_wifi_chk == 1 and stop_counter<10):
            txt=" Wait ... " + str(update_wifi_counter)
            txt='\"' + txt + '\"'
            msg= "t999.txt=" + str(txt)
            port_lcd.write(msg.encode())
            port_lcd.write(ary_end)
            update_wifi_counter = update_wifi_counter - 1
            update_wifi_no = update_wifi_no + 1
            print(update_wifi_counter)
            print(update_wifi_chk)
            
        if (update_wifi_chk == 1 and update_wifi_no == 10):
            print("-------------------------------------------------")
            if "192" in (os.popen('sudo ifconfig | grep 192').read()):
                msg="t999.txt=\" *** Wifi Connection *** \""
                port_lcd.write(msg.encode())
                port_lcd.write(ary_end)
                update_wifi_chk = 0
                update_wifi_no = 0
                stop_counter=0
            else:
                msg="t999.txt=\" *** Wifi Disconnection ***\""
                port_lcd.write(msg.encode())
                port_lcd.write(ary_end)
                update_wifi_chk = 0
                update_wifi_no = 0
                stop_counter=0
                
        if (99 in chk_sys1 and update_wifi_chk ==0 and sys1_99 == 0):
            msg="t999.txt=\" Start update WiFi Setting ~~~ \""
            port_lcd.write(msg.encode())
            port_lcd.write(ary_end)
            sys1_99=99
            print("start update wifi .....")
            
        if (sys1_99 == 99):
            wifi_data=str(port_lcd.read(600))
#            print(wifi_data)
            data_count=wifi_data.count('+')
#            print("+  =",data_count)
            stop_counter=stop_counter+1
            if(stop_counter==10):
                update_wifi_chk = 1
                update_wifi_no = 10
                sys1_99=0
            
        if (data_count == 6 and sys1_99 == 99):
            wifi_data_n=wifi_data.find('+')
            wifi_data1=wifi_data[wifi_data_n+1:]

            wifi_data_n=wifi_data1.find('+')
            wifi_ssid=wifi_data1[0:wifi_data_n]
            print(wifi_ssid)
            wifi_data2=wifi_data1[wifi_data_n+1:]

            wifi_data_n=wifi_data2.find('+')
            wifi_password=wifi_data2[0:wifi_data_n]
            print(wifi_password)
            wifi_data3=wifi_data2[wifi_data_n+1:]
                
            wifi_data_n=wifi_data3.find('+')
            wifi_ip=wifi_data3[0:wifi_data_n]
            print(wifi_ip)
            wifi_data4=wifi_data3[wifi_data_n+1:]
                
            wifi_data_n=wifi_data4.find('+')
            wifi_routers=wifi_data4[0:wifi_data_n]
            print(wifi_routers)
            wifi_data5=wifi_data4[wifi_data_n+1:]
                
            wifi_data_n=wifi_data5.find('+')
            wifi_dns=wifi_data5[0:wifi_data_n]
            print(wifi_dns)
            port_lcd.write("sys1=0".encode())
            port_lcd.write(ary_end)
            update_wifi_counter=10
            sys1_99=0
                
            change_static_ip(wifi_ip,wifi_routers,wifi_dns)
            set_wifi_ssid_psk(wifi_ssid,wifi_password)
            update_wifi_no = 0
            update_wifi_chk = 1
            print("update wifi")
    except:
        print("wait wifi seting")
    
    threading.Timer(1, read_tjc_wifi_page).start()

if __name__ == '__main__':
    read_tjc_wifi_page()
    
    
