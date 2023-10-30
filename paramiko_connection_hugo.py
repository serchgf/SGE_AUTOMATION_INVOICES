import time

import subprocess
import datetime
import paramiko

import threading


# Define una función que será ejecutada por un hilo
def imprimir_hola(username: str):
    #print("ini ,"+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M:%S.%f")+", allSession")
    for _ in range(1):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #print("start process")
        print("start process"+','+ ""+str(time.time()) +',' + f"test{str(int(username)+_)}")
        #print(f"test{str(80+_)}")
        if (int(username)+_) > 120:
            client.connect("192.168.1.30", username=f"test{str(int(username)+_)}", password="abc123")
        else:
            client.connect("192.168.1.30", username=f"test{str(int(username)+_)}", password="123abc")
        
        shell = client.invoke_shell()
        
        shell.close()
        client.close()
        #print(f"test{str(80 + _)}")
        print("end process"+','+ ""+str(time.time())  +','+ f"test{str(int(username)+_)}")
        #print("end process")

# Crea un objeto Thread y pasa la función como argumento
hilo1 = threading.Thread(target=imprimir_hola, args=("80",))
hilo2 = threading.Thread(target=imprimir_hola, args=("90",))
hilo3 = threading.Thread(target=imprimir_hola, args=("100",))
hilo4 = threading.Thread(target=imprimir_hola, args=("110",))
hilo5 = threading.Thread(target=imprimir_hola, args=("120",))
hilo6 = threading.Thread(target=imprimir_hola, args=("130",))
hilo7 = threading.Thread(target=imprimir_hola, args=("140",))
hilo8 = threading.Thread(target=imprimir_hola, args=("150",))
hilo9 = threading.Thread(target=imprimir_hola, args=("160",))
hilo10 = threading.Thread(target=imprimir_hola, args=("170",))
hilo11 = threading.Thread(target=imprimir_hola, args=("180",))
hilo12 = threading.Thread(target=imprimir_hola, args=("190",))

hilos = [hilo1, hilo2, hilo3, hilo4, hilo5, hilo6, hilo7, hilo8, hilo9, hilo10, hilo11, hilo12]
# Inicia la ejecución del hilo
for hilo in hilos:
    #print(threading.enumerate())
    hilo.start()

# El hilo principal continúa ejecutándose mientras el hilo secundario se ejecuta en paralelo



