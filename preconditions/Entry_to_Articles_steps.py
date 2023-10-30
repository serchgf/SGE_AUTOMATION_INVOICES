from Config.config import images

#producto de testcase 2
#precio unitario 1716.00
#linea 01 parte 615 075 precio de venta 925.06
#costo adquirido 698.24

def pre_Entry_to_Articles(sge_funct, data):
    print("2 Ingresar en el teclado el <<Numero de sucursal>>")
    sge_funct.send_text(data["sucursal"])
    sge_funct.segundos_de_espera(1)
    sge_funct.validar_sucursal_12_seleccionada()
    #CONOCER EL CONTROL DE INVENTARIO DEL ARTICULO
    print("3 Teclear input Enter")
    sge_funct.press_enter()
    print("4 Teclear input 2")
    sge_funct.send_text('2')
    print("5 Teclear input Enter")
    sge_funct.press_enter()
    print("6 Teclear input 2")
    sge_funct.send_text('2')
    print("7 Teclear input Enter")
    sge_funct.press_enter()
    print("4 Teclear input 1")
    sge_funct.send_text('1')
    print("5 Teclear input Enter")
    sge_funct.press_enter()
    print("Consultamos el producto")
    sge_funct.send_text("c")
    print("Seleccionamos la Linea 01")
    sge_funct.send_text(data["linea"])
    print("5 Teclear input Enter")
    sge_funct.press_enter()
    print("Seleccionamos la Parte 1408")
    sge_funct.send_text(data["codigo"])
    print("5 Teclear input Enter")
    sge_funct.press_enter()
    print("Seleccionamos la Bodega R. Michel 01")
    sge_funct.send_text(data["almacen"])
    print("5 Teclear input Enter")
    sge_funct.press_enter()
    sge_funct.segundos_de_espera(5)


def calculate_and_entry_articles(sge_funct, costo_adquisicion:str , cantidad:int, data):
    #costo de adquisicion * cantiadad a ingresar = importe
    #1.00*999999999
    #
    #CALCULO PARA LA PARTE 615 075 DE 10 PIEZAS
    costo_adquisicion=costo_adquisicion.replace(".00","")
    calculate =int(costo_adquisicion) * cantidad
    print("Ingresar en el teclado el <<Numero de sucursal>>")
    sge_funct.send_text(data["sucursal"])
    sge_funct.segundos_de_espera(1)
    sge_funct.validar_sucursal_12_seleccionada()
    #ENTRAR A LA CAPTURA DE MOVIMIENTOS
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Teclear input 2")
    sge_funct.send_text('2')
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Teclear input 4")
    sge_funct.send_text('4')
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Teclear input 2")
    sge_funct.send_text('2')
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("seleccionar la opcion c")
    sge_funct.send_text("c")
    print("Introducir la Referencia")
    sge_funct.send_text(data["referencia"])
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Introducir el Importe")
    sge_funct.send_text(str(calculate))
    print("Presionamos ctrl +w")
    sge_funct.press_hotkeys('ctrl+w')
    print("Introducimos el Almacen 01")
    sge_funct.send_text(data["almacen"])
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Introducimos la linea 31")
    sge_funct.send_text(data["linea"])
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Introducimos el codigo o parte 1408")
    sge_funct.send_text(data["codigo"])
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Introducimos la cantidad a ingresar en inventario")
    sge_funct.send_text(str(cantidad))
    print("Teclear input Enter")
    sge_funct.press_enter()
    #este enter se da por que ya esta en automatico el precio
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Presionamos ctrl +w")
    sge_funct.press_hotkeys('ctrl+w')
    #pretendo poner una espera por que cuando se pidan
    #cantidades grandes podria tardar en procesarlo
    sge_funct.segundos_de_espera(5)
    print("Teclear input Enter")
    sge_funct.press_enter()
    sge_funct.segundos_de_espera(5)



