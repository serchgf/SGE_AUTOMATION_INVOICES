from Config.config import images


def MTC_INVSGE_024_steps(sge_funct, archivo_productos):
    # esta funcion recibe como parametro una instancia de la clase SGE functions y un archivo co los productos
    print("2 Ingresar numero de sucursal ")
    sge_funct.send_text('12')
    sge_funct.segundos_de_espera(1)
    sge_funct.validar_sucursal_12_seleccionada()
    print("3 Press Enter")
    sge_funct.press_enter()
    print("4 Ingresar opcion de 'pedidos facturacion' ")
    sge_funct.send_text('4')
    print("5 Press Enter")
    sge_funct.press_enter()
    print("6 Ingresar opcion de 'ventas directas' ")
    sge_funct.send_text('10')
    print("7 Press Enter")
    sge_funct.press_enter()
    print("8 Posicionarse en campo cuenta y capturar la cuenta 03016701")
    sge_funct.send_text('03016701')
    print("9 Capturar la letra s")
    sge_funct.send_text('s')
    print("10 Teclear input")
    sge_funct.press_enter()
    print("11 Teclear input")
    sge_funct.press_enter()
    print("12 Presionamos ctrl+e")
    sge_funct.press_hotkeys('ctrl+e')
    print("13 Teclear input")
    sge_funct.press_tab()
    print("14 Capturar 02")
    sge_funct.send_text('02')
    print("15 Teclear input")
    sge_funct.press_enter()
    print("16 Teclear input")
    sge_funct.press_enter()
    print("17 Presionamos ctrl +w")
    sge_funct.press_hotkeys('ctrl+w')
    print("18 Se visualizan promociones o advertencias")
    while sge_funct.promociones_y_atrasos():
        sge_funct.press_hotkeys('ctrl+a')
    print("19 Posicionarse en Columna Linea y presionar la combinacion de teclas ctrl + o")
    sge_funct.press_hotkeys('ctrl+o')
    print("20 Presionar Letra M Importa pedido masivo")
    sge_funct.send_text('m')
    print("21 Presionamos Enter para continuar ")
    sge_funct.press_enter()
    print("22 Oprimir click derecho del mouse para Pegar los datos de los articulos a facturar tmpmasivo.txt")
    sge_funct.leer_archivo_productos(archivo_productos)
    print("23 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("24 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("25 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    sge_funct.segundos_de_espera(40)
    print("26 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("27 Capturar s")
    sge_funct.send_text("s")
    sge_funct.segundos_de_espera(110)
    print("27 Presionamos Enter para continuar ")
    sge_funct.press_enter()
