from Config.config import images


def MTC_INVSGE_013_steps(sge_funct):
    print("PASO")
    print("2 Ingresar en el teclado el <<Numero de sucursal>>")
    sge_funct.send_text('12')
    sge_funct.segundos_de_espera(1)
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
    print("8 Posicionarse en campo cuenta y capturar la cuenta 45828833")
    sge_funct.send_text('45828833')
    print("9 Posicionarse en Columna Linea y presionar la combinacion de teclas")
    sge_funct.press_hotkeys('ctrl+e')
    print("10 Ingresar la línea del producto")
    sge_funct.send_text('4x')
    print("11 Teclear input")
    sge_funct.press_enter()
    print("12 Escribimos el codigo")
    sge_funct.send_text('AMP-24-675')
    print("13 Teclear input")
    sge_funct.press_enter()
    print("14 Desde la línea del articulo obligado teclear flecha arriba")
    sge_funct.flecha_arriba()#coment
    print("15 Teclear input")
    sge_funct.press_enter()
    print("16 Teclear input")
    sge_funct.press_enter()
    print("17 Presionamos Enter hasta posicionarnos en la columna cantidad")
    sge_funct.press_enter()
    print("18 Capturamos N unidades")
    sge_funct.send_text('2')
    print("19 Teclear input")
    sge_funct.press_enter()
    print("20 Teclear input")
    sge_funct.press_enter()
    print("21 Presionamos ctrl + W para facturar lo capturado en la ventana del detalle")
    sge_funct.press_hotkeys('ctrl+w')
    print("22 Presionarmos Enter Para seleccionar al cliente de mostrador")
    sge_funct.press_enter()
    print("23 Teclear input")
    sge_funct.press_tab()
    print("24 Teclear input")
    sge_funct.press_tab()
    print("25  y capturamos la cuenta  0274890 (el primer carácter es espacios)")
    sge_funct.send_text(' 0274890')
    print("26 Teclear input")
    sge_funct.press_enter()
    print("27 Capturamos clave del agente 06")
    sge_funct.send_text('06')
    print("28 Teclear input")
    sge_funct.press_enter()
    print("29 Presionamos Enter sin capturar nada sobre el campo referencia")
    sge_funct.press_enter()
    print("30 Presionamos Enter sin capturar nada sobre el campo Regimen Fiscal")
    sge_funct.press_enter()
    print("31 Presionamos Enter sin capturar nada sobre el campo Uso del CFDI")
    sge_funct.press_enter()
    print("32 Presionamos Enter sin capturar nada sobre el campo Medio de entrega/embarque")
    sge_funct.press_enter()
    print("33 Presionamos ctrl + W para regresar a la ventana del Detalle")
    sge_funct.press_hotkeys('ctrl+w')
    print("34 Presionamos ctrl + W para Facturar")
    sge_funct.press_hotkeys('ctrl+w')
    print("35 Presionamos ctrl + W para Continuar")
    sge_funct.press_hotkeys('ctrl+w')
    print("36 Posicionados en la columna Forma de Pago presionamos ctrl + R aplicar adeudo")
    sge_funct.press_hotkeys('ctrl+r')
    print("37 Presionamos ctrl + W para facturar lo capturado en la ventada del detalle esperar 5 segundos")
    sge_funct.press_hotkeys('ctrl+w')
    sge_funct.segundos_de_espera(5)
    print("38 Presionamos Enter para continuar ")
    sge_funct.press_enter()
    sge_funct.segundos_de_espera(3)
    print("39 Presionamos Enter para continuar ")
    sge_funct.press_enter()