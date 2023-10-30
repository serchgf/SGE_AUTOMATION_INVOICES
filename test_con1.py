import time

from Config.config import login_data
import subprocess
import datetime

def connection(username, ip, password):
    try:
        connect = 'putty.exe -ssh {}@{} -pw {}'.format(username, ip, password)

        subprocess.Popen(connect, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    except:
        print("Connection Failed...\nCheck your credentials access...")

# connection super user
#connection(login_data.linux_username, login_data.ip, login_data.password)

# connection test user
for i in range(10):

    print(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M:%S.%f/"))
    #connection(login_data.linux_username, login_data.ip, login_data.password)
    #connection("itmx16", login_data.ip, "sgeg4913")
    #connection("itmx16", login_data.ip, "sgeg4913")
    #connection("itmx17", login_data.ip, "java135")
    #connection("test18", login_data.ip, "123abc")
    connection("test80", "192.168.1.30", "123abc")
    #connection(login_data.linux_username, login_data.ip, login_data.password)
    #time.sleep(2)
print(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M:%S.%f/"))

