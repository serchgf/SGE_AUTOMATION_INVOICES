def MTC_INVSGE_003_steps(sge_funct):
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
    print("8 Posicionarse en campo cuenta y capturar la cuenta 45820263")
    sge_funct.send_text('45820263')
    print("9 Teclear input")
    sge_funct.press_enter()
    print("10 Teclear input")
    sge_funct.press_enter()
    print("11 Teclear input")
    sge_funct.press_enter()
    print("12 Teclear input")
    sge_funct.press_enter()
    print("13 Presionar ctrl + W para pasar al detalle del pedido")
    sge_funct.press_hotkeys('ctrl+w')
    sge_funct.segundos_de_espera(2)
    print("14 Aparece mensaje de promociones o advertencias de la cuenta")
    while sge_funct.promociones_y_atrasos():
        sge_funct.press_hotkeys('ctrl+a')
    print("15 Posicionarse en Columna Linea y presionar la combinacion de teclas ctrl + E")
    sge_funct.press_hotkeys('ctrl+e')
    print("16 Ingresar la línea del producto")
    sge_funct.send_text('99')
    print("17 Teclear input")
    sge_funct.press_enter()
    print("18 Escribimos el codigo 3013M")
    sge_funct.send_text('3013M')
    print("19 Teclear input")
    sge_funct.press_enter()
    print("20 Presionamos Enter hasta posicionarnos en la columna cantidad y capturamos N unidades.")
    sge_funct.press_enter()
    print("21 Teclear input")
    sge_funct.press_enter()
    print("22 Teclear input")
    sge_funct.press_enter()
    print("23 Ingresar la cantidad de producto")
    sge_funct.send_text('2')
    print("24 Teclear input")
    sge_funct.press_enter()
    print("25 Presionamos ctrl + W para facturar lo capturado en la ventada del detalle esperar 5 segundos")
    sge_funct.press_hotkeys('ctrl+w')
    sge_funct.segundos_de_espera(5)
    print("26 Presionamos Enter para continuar ")
    sge_funct.press_enter()
