from gpiozero import CPUTemperature
from time import sleep
import RPi.GPIO as GPIO
import logging
import re
import time
import os, datetime


PIN  = 24

######################################
############ Init Service ############
def Gpio_Init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)

def Debug_Setting():
    format = '%(asctime)s - [%(filename)s][line:%(lineno)d][%(funcName)s()] - %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.INFO,format=format,filename=time.strftime('/home/pi/esg/log/boot/%Y%m%d_%H%M%S.bootlog'),filemode='w')

def Fan_Init():
    for x in range(600):
        Fan_Run(100)
        
def ntp_service():
    ntp_return1 = "0"
    ntp_return2 = "0"
    ntp_return3 = "0"
    
    cmd1 = "sudo ntpdate -u time.windows.com"
    cmd2 = "sudo ntpdate -u time1.cloud.tencent.com"
    cmd3 = "sudo ntpdate -u ntp.aliyun.com"
    
    ntp_return1 = str(os.system(cmd1))
    print("[ntp_return1] ntp_return111 cmd return : " + ntp_return1)
    
    while ((ntp_return1 != "0") or (ntp_return2 != "0") or (ntp_return3 != "0")):
        ntp_return1 = str(os.system(cmd1))
        print("[ntp_return1] ntp_return1 cmd return : " + ntp_return1)
        ntp_return2 = str(os.system(cmd2))
        print("[ntp_return2] ntp_return2 cmd return : " + ntp_return2)
        ntp_return3 = str(os.system(cmd3))
        print("[ntp_return3] ntp_return3 cmd return : " + ntp_return3)
        time.sleep(0.5)
        if (ntp_return1 == "0") or (ntp_return2 == "0") or (ntp_return3 == "0"):
            break
    

######################################
############ Fan_Service #############
def Fan_Run(duty):
    GPIO.output(PIN,0)
    sleep((101-duty)*0.0001)
    GPIO.output(PIN,1)
    sleep(duty*0.0001)
    
def Get_Tamp():
    cpu = CPUTemperature()
    #logging.info(cpu)
    m = re.search('(?<==)\w+',format(cpu))
    logging.info(m.group(0))
    tamp = m.group(0)
    
    return int(tamp)

def Fan_Pwm():
    tamp = Get_Tamp()
    if (tamp < 60):
       Pwm = 0
    if (tamp >= 60):
       Pwm = 60
       
    return Pwm
    
def Fan_Service():
    Pwm = Fan_Pwm()
    
    Fan_Init()
    
    for x in range(16000):
        Fan_Run(Pwm)


######################################
############ Delete_Log_Service ######
def Delete_BootLog_Service():
    dirToBeEmptied = '/home/pi/esg/log/boot'
    ds = list(os.walk(dirToBeEmptied)) #獲得所有資料夾的資訊列表
    delta = datetime.timedelta(days=30) # Only days, seconds, and microseconds remain
    now = datetime.datetime.now() #獲取當前時間

    for d in ds: #遍歷該列表
        os.chdir(d[0]) #進入本級路徑，防止找不到檔案而報錯
        
        if d[2] != []: #如果該路徑下有檔案
            for x in d[2]: #遍歷這些檔案
                ctime = datetime.datetime.fromtimestamp(os.path.getctime(x)) #獲取檔案建立時間
                
                if ctime < (now-delta): #若建立於delta天前
                    os.remove(x) #則刪掉

def Delete_C20Log_Service():
    dirToBeEmptied = '/home/pi/esg/log/c20'
    ds = list(os.walk(dirToBeEmptied)) #獲得所有資料夾的資訊列表
    delta = datetime.timedelta(days=30) # Only days, seconds, and microseconds remain
    now = datetime.datetime.now() #獲取當前時間

    for d in ds: #遍歷該列表
        os.chdir(d[0]) #進入本級路徑，防止找不到檔案而報錯
        
        if d[2] != []: #如果該路徑下有檔案
            for x in d[2]: #遍歷這些檔案
                ctime = datetime.datetime.fromtimestamp(os.path.getctime(x)) #獲取檔案建立時間
                
                if ctime < (now-delta): #若建立於delta天前
                    os.remove(x) #則刪掉

def Delete_Log_Service():
    Delete_BootLog_Service()
    Delete_C20Log_Service()
                    

######################################
############ Run Code ################
def Init_App():
    ntp_service()
    Gpio_Init()
    Fan_Init()
    Debug_Setting()
    Delete_Log_Service()

def main():

    Init_App()

    while True:
        Fan_Service()
        
if __name__ == '__main__':
    main()
