from Config.config import images


def MTC_INVSGE_009_steps(sge_funct):
    print("***MTC_ASGE_009-Facturacion_sencilla_contado_plaza_equivalente***")
    print("2 Ingresar en el teclado el <<Numero de sucursal>>")
    sge_funct.send_text('12')
    sge_funct.segundos_de_espera(1)
    sge_funct.validar_sucursal_12_seleccionada()
    print("3 Teclear input Enter")
    sge_funct.press_enter()
    print("4 Teclear input 4")
    sge_funct.send_text('4')
    print("5 Teclear input Enter")
    sge_funct.press_enter()
    print("6 Teclear input 10")
    sge_funct.send_text('10')
    print("7 Teclear input Enter")
    sge_funct.press_enter()
    print("8 Posicionarse en campo cuenta y capturar la cuenta 45820006")
    sge_funct.send_text('45820006')
    print("9 Teclear input Enter")
    sge_funct.press_enter()
    print("10 Teclear input Enter")
    sge_funct.press_enter()
    print("11 Presionar enter por cuarta vez para seleccionar primer domicilio")
    sge_funct.press_enter()
    print("12 Buscar el medio de entrega/embarque")
    sge_funct.press_hotkeys('ctrl+e')
    print("13 Capturar la paquetería DHL")
    sge_funct.send_text('DHL')
    print("14 Teclear input Enter")
    sge_funct.press_enter()
    print("15 Teclear input Enter")
    sge_funct.press_enter()
    print("16 Presionar ctrl + W para pasar al detalle del pedido")
    sge_funct.press_hotkeys('ctrl+w')
    sge_funct.segundos_de_espera(5)
    # validar error al comunicarse al sat
    print("17 Posicionarse en Columna Linea y presionar la combinacion de teclas ctrl + E")
    sge_funct.press_hotkeys('ctrl+e')
    print("18 Ingresar la línea del producto")
    sge_funct.send_text('31')
    print("19 Teclear input Enter")
    sge_funct.press_enter()
    print("20 Escribimos el codigo 1408")
    sge_funct.send_text('1408')
    print("21 Teclear input Enter")
    sge_funct.press_enter()
    print("22 Presionamos ctrl+l para ver los articulos equivalentes")
    sge_funct.press_hotkeys('ctrl+l')
    sge_funct.flecha_abajo()
    #sge_funct.flecha_abajo()
    print("23 Posicionarnos en el articulo 01  30    173596 e ingresamos 1")
    sge_funct.send_text('1')
    print("24 Teclear input Enter")
    sge_funct.press_enter()
    print("25 Presionamos ctrl+w para grabar")
    sge_funct.press_hotkeys('ctrl+w')
    print("26 Teclear input Enter")
    sge_funct.press_enter()

    print("27 Presionamos ctrl + W para facturar lo capturado en la ventada del detalle esperar 5 segundos")
    sge_funct.press_hotkeys('ctrl+w')
    print("28 Presionamos ctrl + W para Continuar")
    sge_funct.press_hotkeys('ctrl+w')
    print("29 Posicionados en la columna Forma de Pago presionamos 4 veces la flecha abajo para posicionarse en tarjeta debito")
    sge_funct.flecha_abajo()
    sge_funct.flecha_abajo()
    sge_funct.flecha_abajo()
    sge_funct.flecha_abajo()
    print("30 Capturar el total a liquidar")
    sge_funct.send_text('349')
    print("31 Seleccionar el banco de la primera opcion con enter")
    sge_funct.press_enter()
    print("32 Teclear input Enter")
    sge_funct.press_enter()
    print("33 Capturar los ultimos cuatro digitos de la tarjeta 3452")
    sge_funct.send_text('3452')
    print("34 Presionamos ctrl + W para grabar (generar factura)")
    sge_funct.press_hotkeys('ctrl+w')
    print("35 Presiona Enter para confirmar que si esta correcto ")
    sge_funct.press_enter()
    print("36 Presionamos Enter para continuar ")
    sge_funct.press_enter()
    sge_funct.segundos_de_espera(5)
    print("37 Presionamos Enter para continuar ")
    sge_funct.press_enter()
