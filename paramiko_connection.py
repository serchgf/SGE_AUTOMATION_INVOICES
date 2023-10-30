
import datetime
import paramiko

import threading


# Define una función que será ejecutada por un hilo
def imprimir_hola(username: str):
    print("ini")
    print(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M:%S.%f/"))
    for _ in range(9):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #print("start process")
        print("start process"+','+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M:%S.%f/" + ',' + f"test{str(int(username)+_)},"))
        #print(f"test{str(80+_)}")
        client.connect("192.168.1.30", username=f"test{str(int(username)+_)}", password="123abc")
        shell = client.invoke_shell()
        shell.close()
        client.close()
        #print(f"test{str(80 + _)}")
        print("end process"+','+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M:%S.%f/") + ',' + f"test{str(int(username)+_)},")
        #print("end process")

# Crea un objeto Thread y pasa la función como argumento
hilo1 = threading.Thread(target=imprimir_hola, args=("80",))
hilo2 = threading.Thread(target=imprimir_hola, args=("90",))
hilo3 = threading.Thread(target=imprimir_hola, args=("100",))
hilo4 = threading.Thread(target=imprimir_hola, args=("110",))


hilos = [hilo1, hilo2, hilo3, hilo4]
# Inicia la ejecución del hilo
for hilo in hilos:
    print(threading.enumerate())
    hilo.start()

# El hilo principal continúa ejecutándose mientras el hilo secundario se ejecuta en paralelo

# Puedes hacer que el hilo principal espere a que el hilo secundario termine usando el método join()
# hilo.join()
# print("Fin del programa")
# print(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M:%S.%f/"))

