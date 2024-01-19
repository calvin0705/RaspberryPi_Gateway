import serial
import os
import threading

end = [0xff, 0xff, 0xff]
port_lcd = serial.Serial(port='/dev/ttyAMA1', baudrate=9600, parity='N', stopbits=1, bytesize=8, timeout=1.0)
ary_end = bytearray(end)
global recv_buffer_no
global update_wifi_no
global update_wifi_counter
global update_wifi_chk
recv_buffer_no = 1
update_wifi_no = 0
update_wifi_counter = 10
update_wifi_chk = 0

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
    print("**********************")
    try:
        port_lcd.write("get sys0".encode())
        port_lcd.write(ary_end)
        page_sys0=list(port_lcd.readline())
        port_lcd.write("get sys1".encode())
        port_lcd.write(ary_end)
        page_sys1=list(port_lcd.readline())
        print(page_sys0[1])
        print(page_sys1[1])
        if (page_sys0[1] == 99 and page_sys1[1] == 99):
            msg="t999.txt=\" Start update WiFi Setting ~~~ \""
            port_lcd.write(msg.encode())
            port_lcd.write(ary_end)
            update_wifi_counter=10
            port_lcd.write("get WIFI.t1171.txt".encode())
            port_lcd.write(ary_end)
            wifi_ssid=list(port_lcd.readlines())
            a=wifi_ssid[0]
            wifi_ssid=a[1:len(a)-3].decode()
            print(wifi_ssid)
            port_lcd.write("get WIFI.t1174.txt".encode())
            port_lcd.write(ary_end)
            wifi_password=list(port_lcd.readlines())
            a=wifi_password[0]
            wifi_password=a[1:len(a)-3].decode()
            print(wifi_password)
            port_lcd.write("get WIFI.t1176.txt".encode())
            port_lcd.write(ary_end)
            wifi_ip=list(port_lcd.readlines())
            a=wifi_ip[0]
            wifi_ip=a[1:len(a)-3].decode()
            print(wifi_ip)
            port_lcd.write("get WIFI.t1177.txt".encode())
            port_lcd.write(ary_end)
            wifi_routers=list(port_lcd.readlines())
            a=wifi_routers[0]
            wifi_routers=a[1:len(a)-3].decode()
            print(wifi_routers)
            port_lcd.write("get WIFI.t1178.txt".encode())
            port_lcd.write(ary_end)
            wifi_dns=list(port_lcd.readlines())
            a=wifi_dns[0]
            wifi_dns=a[1:len(a)-3].decode()
            print(wifi_dns)
        
            change_static_ip(wifi_ip,wifi_routers,wifi_dns)
            set_wifi_ssid_psk(wifi_ssid,wifi_password)
            port_lcd.write("sys1=0".encode())
            port_lcd.write(ary_end)
            update_wifi_no = 0
            update_wifi_chk = 1
            print("update wifi")
        if (update_wifi_chk == 1 and update_wifi_no == 10):
            print("-------------------------------------------------")
            if "192" in (os.popen('sudo ifconfig | grep 192').read()):
                msg="t999.txt=\" *** Wifi Connection *** \""
                port_lcd.write(msg.encode())
                port_lcd.write(ary_end)
                update_wifi_chk = 0
            else:
                msg="t999.txt=\" *** Wifi Disconnection ***\""
                port_lcd.write(msg.encode())
                port_lcd.write(ary_end)
                update_wifi_chk = 0
    
        if (update_wifi_chk == 1):
            txt=" Wait ... " + str(update_wifi_counter)
            txt='\"' + txt + '\"'
            msg= "t999.txt=" + str(txt)
            port_lcd.write(msg.encode())
            port_lcd.write(ary_end)
            update_wifi_counter = update_wifi_counter -1
            update_wifi_no = update_wifi_no +1
            print(update_wifi_no)
        if (page_sys0[1] != 99):
            update_wifi_chk = 0
            update_wifi_no = 0
            print("back page")
    except:
        print("wait wifi seting")
    threading.Timer(1, read_tjc_wifi_page).start()

if __name__ == '__main__':
    read_tjc_wifi_page()
    
    
