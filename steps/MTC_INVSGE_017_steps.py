def MTC_INVSGE_017_steps(sge_funct):

    print("2 Ingresar en el teclado el <<Numero de sucursal>>")
    sge_funct.send_text('12')
    sge_funct.validar_sucursal_12_seleccionada()
    print("3 Teclear input")
    sge_funct.press_enter()
    print("4 Teclear input")
    sge_funct.send_text('4')
    print("5 Teclear input")
    sge_funct.press_enter()
    print("6 Teclear input")
    sge_funct.send_text('10')
    print("7 Teclear input")
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
    # agregar la validacion del rfc? o correr precondiciones antes?
    sge_funct.segundos_de_espera(2)
    print("18 Se visualizan promociones o advertencias")
    while sge_funct.promociones_y_atrasos():
        sge_funct.press_hotkeys('ctrl+a')
    print("19 Posicionarse en Columna Linea y presionar la combinacion de teclas ctrl + o")
    sge_funct.press_hotkeys('ctrl+o')
    print("20 Presionamos ->ctrl + i<- presionar k")   # workaround presionar k para seleccionar kits
    # sge_funct.send_text('ctrl+i')
    sge_funct.send_text('k')
    sge_funct.segundos_de_espera(2)
    print("21 Capturar el código del kit AM 206 CC,XS T 1.6 ")# 'AM 206 CC,XS T 1.6 04-7' se quito el 04-7 porque excede caracteres de captura
    sge_funct.send_text('AM 206 CC')
    print("22 Teclear input")
    sge_funct.press_enter()
    print("23 Teclear input")
    sge_funct.press_enter()
    print("24 Teclear input")
    sge_funct.press_enter()
    print("25 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("26 Presionamos ctrl + W para facturar lo capturado en la ventana del detalle")
    sge_funct.press_hotkeys('ctrl+w')
    sge_funct.segundos_de_espera(5)
    print("27 Capturar la letra s")
    sge_funct.send_text('s')
    print("28 Presionamos Enter para continuar ")
    sge_funct.press_enter()
    sge_funct.segundos_de_espera(2)
    print("29 Presionamos Enter para continuar ")
    sge_funct.press_enter()
    sge_funct.segundos_de_espera(2)


