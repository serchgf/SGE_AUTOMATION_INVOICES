from Config.config import images


def MTC_INVSGE_025_steps(sge_funct, archivo_productos):
    # esta funcion recibe como parametro una instancia de la clase SGE functions y un archivo co los productos
    print("2 Ingresar numero de sucursal ")
    sge_funct.send_text('12')
    sge_funct.segundos_de_espera(1)
    sge_funct.validar_sucursal_12_seleccionada()
    print("3 Press Enter")
    sge_funct.press_enter()
    print("4 Teclear input")
    sge_funct.send_text('4')
    print("5 Teclear input")
    sge_funct.press_enter()
    print("6 Teclear input")
    sge_funct.send_text('10')
    print("7 Teclear input")
    sge_funct.press_enter()
    print("8 Posicionarse en campo cuenta y capturar la cuenta 45820006")
    sge_funct.send_text('45820006')
    print("9 Teclear input")
    sge_funct.press_enter()
    print("10 Teclear input")
    sge_funct.press_enter()
    print("11 Teclear input")
    sge_funct.press_enter()
    print("12 Buscar el medio de entrega/embarque")
    sge_funct.press_hotkeys('ctrl+e')
    print("13 Capturar la paquetería DHL")
    sge_funct.send_text('DHL')
    print("14 Teclear input")
    sge_funct.press_enter()
    print("15 Teclear input")
    sge_funct.press_enter()
    print("16 Presionar ctrl + W para pasar al detalle del pedido")
    sge_funct.press_hotkeys('ctrl+w')
    print("17 Presionamos ctrl + O para más opciones")
    sge_funct.press_hotkeys('ctrl+o')
    print("18 Presionar Letra M Importa pedido masivo")
    sge_funct.send_text('m')
    print("19 Presionamos Enter para continuar ")
    sge_funct.press_enter()
    print("20 Oprimir click derecho del mouse para Pegar los datos de los articulos a facturar tmpmasivo.txt")
    sge_funct.leer_archivo_productos(archivo_productos)
    sge_funct.segundos_de_espera(5)
    print("21 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("22 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("23 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("24 Presionamos ctrl + W para facturar lo capturado en la ventada del detalle")
    sge_funct.press_hotkeys('ctrl+w')
    #print("25 Presionamos ctrl + W")
    #sge_funct.press_hotkeys('ctrl+w')
    print("26 Posicionados en la columna Forma de Pago presionamos 4 veces la flecha abajo para posicionarse en tarjeta debito")
    sge_funct.flecha_abajo()
    sge_funct.flecha_abajo()
    sge_funct.flecha_abajo()
    sge_funct.flecha_abajo()
    print("27 Posicionados en la columna Forma de Pago presionamos ctrl + R aplicar adeudo")
    sge_funct.press_hotkeys('ctrl+r')
    sge_funct.press_enter()
    print("28 Capturar los ultimos cuatro digitos de la tarjeta 3452")
    sge_funct.send_text('3452')
    sge_funct.press_hotkeys('ctrl+w')
    print("29 Presiona Enter para confirmar que si esta correcto ")
    sge_funct.press_enter()
    sge_funct.segundos_de_espera(5)
    print("30 Presionamos Enter para continuar ")
    sge_funct.press_enter()





