import pyautogui as pa
import subprocess
import time
from Config.config import images
from Config.config import files
import csv
import datetime
import shutil
from Config.config import txt_files_path
from Config.config import commons_cmds
from Config.invoice_credit_simple_order_cmds import invoice_commands


class Pasos_prueba:

    def __init__(self, step_index: str, action: str, step_input: str, expected_result: str):
        #self.__Index = Index
        self.__step_index = step_index
        self.__action = action
        self.__step_input = step_input
        self.__expected_result = expected_result

    def obtener_step_index(self):
        return self.__step_index

    def obtener_action(self):
        return self.__action

    def obtener_step_input(self):
        return self.__step_input

    def obtener_expected_result(self):
        return self.__expected_result

    def actualizar_step_index(self, step_index: str):
        self.__step_index = step_index

    def actualizar_action(self, action: str):
        self.__action = action

    def actualizar_step_input(self, step_input: str):
        self.__step_input  = step_input

    def actualizar_expected_result(self, expected_result: str):
        self.__expected_result = expected_result

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"step_index={self.__step_index}, action={self.__action}, step_input={self.__step_input}, expected_result={self.__expected_result}"

class SgeFunctions:

    img_pantalla_inicial = images.img_pantalla_inicial
    img_error_connection = images.img_error_connection
    img_invoice_created_correctly = images.img_invoice_created_correctly
    img_promociones = images.img_promociones
    img_promociones2 = images.img_promociones2
    img_atraso = images.img_error_atraso_importante
    img_error_cedi_preferente = images.img_error_cedi_preferente
    # img_rclick_carga_masiva = images.img_rclick_carga_masiva


    img_inicio_orden_de_compra = images.img_inicio_orden_de_compra
    img_consulta_orde_de_compra = images.img_consulta_orde_de_compra
    img_confirmacion_colocada = images.img_confirmacion_colocada
    img_header_orden_de_compra = images.img_header_orden_de_compra
    #inv_base_text_file = files.inv_base_txt_file

    close_as = ""
    route_image = ""
    titulo_del_reporte = ""

    def create_report_directory(self):
        main_report_dir = 'Reports/SGE_invoice_Test_report_' + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M/")
        return main_report_dir

    def connection(self, username, ip, password):
        try:
            connect = 'putty.exe -ssh {}@{} -pw {}'.format(username, ip, password)
            subprocess.Popen(connect, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            time.sleep(3)
        except:
            print("Connection Failed...\nCheck your credentials access...")

    def validate_connection(self):
        s = pa.locateOnScreen(self.img_pantalla_inicial)
        e = pa.locateOnScreen(self.img_error_connection)
        if s is not None:
           # print("Connection Successful!!")
            return True

        elif e is not None:
            time.sleep(1)
            message = "Connection Failed"
            self.take_screenshot(message)
            #print("Error Found, Connection Failed!!")
            return False, "Error Found, Connection Failed"
        else:
            assert False, "Error connection no defined"

    def crear_objeto(self, line: list):
        # Line[0] = index. Line[1] = Action. Line[2] = input. Line[3] = expected_result
        my_step = Pasos_prueba(line[0], line[1], line[2], line[3])
        return my_step

    def crear_lista_objetos(self, csv_file):
        lista_objetos = []
        # Line[0] = index. Line[1] = Action. Line[2] = input.
        with open(csv_file, newline='') as file:
            file_reader = csv.reader(file)
            next(file_reader)
            for line in file_reader:
                my_step = self.crear_objeto(line)
                my_step.actualizar_step_input(self.clean_input_text(my_step.obtener_step_input()))
                lista_objetos.append(my_step)
        return lista_objetos

    def clean_input_text(self, step_input):
        if '"' in step_input:
            cleaned_input = step_input.replace('"', "")
            #print(cleaned_input)
            return str(cleaned_input)
        #print(step_input)
        return step_input

    def press_hotkeys(self, cmd):
        pa.hotkey(str(cmd))

    def take_screenshot(self, message):
        print("taking screenshot " + message)
        img_name = "my_screenshot.png"
        pa.screenshot(f"Screenshots/{img_name}")
        # return self.route_image

    def close_sge_session(self, close_as):
        pa.press('enter')
        pa.hotkey('alt', 'f4')
        if close_as != 0:
            pa.press('enter')
        else:
            pass

    def close_invoice_session(self):
        print("Test Finished")
        pa.press('enter')
        pa.hotkey('alt', 'f4')
        pa.press('enter')
        print("Session Terminated")

    def obtener_fecha(self):
        fecha = str(datetime.datetime.now())
        fecha = fecha.split(".")
        final = ""
        if ":" in fecha[0]:
            nueva = fecha[0].replace(":", "h_", 1)
            semi = nueva.replace(":", "min_", 2)
            final = semi + "s_"
            final = final.replace(" ", "_")
        return final

    def error_screenshot(self):
        message = "connection_error"
        self.take_screenshot(message)

    def move_to_report_dir(self, img_to_move, path_to_move):
        # obtain name of directory
        report_directory = self.create_report_directory()
        #print("------")
        #print(f"Images saved in the following Directory: \n{report_directory}{img_to_move}")
        #print("------")
        shutil.move(f"Screenshots/my_screenshot.png", f"{path_to_move}/{img_to_move}")
        return f"images_report/{img_to_move}"

    def validating_invoice(self):
        coord_xy = pa.locateOnScreen(self.img_invoice_created_correctly)

        if coord_xy == None or coord_xy == "":
            print("An error has Occurred during Invoice creation")
            message = "Error_during_invoice_creation"
            self.take_screenshot(message)
            assert False
        else:
            print("Invoice created succesfully")
            message = "Invoice created succesfully"
            self.take_screenshot(message)

    def create_general_invoice(self, object_list_to_process, img_r_Click: None, img_doubleClick: None):
        print("Creating general invoice")
        try:
            self.read_general_commands(object_list_to_process, img_r_Click, img_doubleClick)
        except:
            print("An error has occurred, During Invoice creation")
            message = "Error_during_Invoice_Creation"
            time.sleep(1)
            self.take_screenshot(message)
            assert False, "An error has occurred, A command has not been processed correctly"

    def read_general_commands(self, object_list, img_r_Click: None, img_doubleClick: None):

        for obj in object_list:
            print(obj.obtener_action())
            self.press_general_commands(obj.obtener_step_input(), img_r_Click, img_doubleClick)
        # for cmd in command_list:
        #     self.press_general_comma.nds(cmd, img_r_Click, img_doubleClick)

    def press_general_commands(self, cmd, img_r_Click: None, img_doubleClick: None):
        # if '"' in cmd: cmd.replace('"', '')

        if cmd == commons_cmds.ctrle:
            pa.hotkey('ctrl', 'e')

        elif cmd == commons_cmds.ctrlw:
            pa.hotkey('ctrl', 'w')

        elif cmd == commons_cmds.ctrlr:
            pa.hotkey('ctrl', 'r')

        elif cmd == commons_cmds.ctrlo:
            pa.hotkey('ctrl', 'o')

        elif cmd == commons_cmds.arrow_down:
            pa.press('down')

        elif cmd == commons_cmds.ctrla:
            pa.hotkey('ctrl', 'a')

        elif cmd == commons_cmds.promociones:
            # pass
            while self.promociones_y_atrasos():
                pa.hotkey('ctrl', 'a')

        elif cmd == commons_cmds.validar_cdi:
            self.sugerencia_CEDI()

        elif cmd == commons_cmds.tab:
            #pa.press('tab')
            pa.hotkey(commons_cmds.tab)

        elif cmd == commons_cmds.space:
            pa.press('space')

        elif cmd == "leer_archivo":
            pa.press('tab')
            with open(txt_files_path.txt_file, 'r') as f1:
                for line in f1:
                    print(line)
                    pa.typewrite(line)
                    pa.press('tab')

        elif cmd == commons_cmds.rclick:
            coordinates_rclick = pa.locateCenterOnScreen(img_r_Click)
            pa.click(coordinates_rclick, button="right")

        elif cmd == commons_cmds.enter:
            pa.press('enter')
            time.sleep(1)

        elif cmd == commons_cmds.tiempo_fuera_2:
            time.sleep(2)

        elif cmd == commons_cmds.tiempo_fuera_3:
            time.sleep(3)

        elif cmd == commons_cmds.tiempo_fuera_5:
            time.sleep(5)

        elif cmd == commons_cmds.tiempo_fuera_10:
            time.sleep(10)

        else:
            self.type_cmds(cmd)

    def type_cmds(self, cmd):
        try:
            pa.typewrite(cmd)
            time.sleep(1)
        except TypeError:
            self.type_cmds(cmd)


########################################################################################################################

    def promociones_y_atrasos(self):
        gdl = pa.locateOnScreen(self.img_error_cedi_preferente)
        atraso = pa.locateOnScreen(self.img_atraso)
        p2 = pa.locateOnScreen(self.img_promociones2)
        p = pa.locateOnScreen(self.img_promociones)
        if atraso is not None or p is not None or p2 is not None or gdl is not None:
            return True
        else:
            return False

    def sugerencia_CEDI(self):
        time.sleep(2)
        gdl = pa.locateOnScreen(self.img_error_cedi_preferente)
        if gdl is not None:
            pa.press('s')


