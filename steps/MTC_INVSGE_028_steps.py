import time

from Config.config import images, login_data


def MTC_INVSGE_028_steps(sge_funct, img_inicioFactura):
    # -------------------------------------------------------------------------4
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
    print("17 Posicionarse en Columna Linea y presionar la combinacion de teclas ctrl + E")
    sge_funct.press_hotkeys('ctrl+e')
    print("18 Ingresar la línea del producto")
    sge_funct.send_text('49')
    print("19 Teclear input")
    sge_funct.press_enter()
    print("20 Escribimos el codigo CKOR92106")
    sge_funct.send_text('CKOR92106')
    print("21 Teclear input")
    sge_funct.press_enter()
    print("22 Presionamos Enter hasta posicionarnos en la columna cantidad y capturamos N unidades.")
    sge_funct.press_enter()
    print("23 Teclear input")
    sge_funct.press_enter()
    print("24 Teclear input")
    sge_funct.press_enter()
    print("25 Ingresar la cantidad de producto")
    sge_funct.send_text('2')
    print("26 Teclear input")
    sge_funct.press_enter()
    print("27 Teclear input")
    sge_funct.press_enter()
    print("28 Presionamos ctrl + W para facturar lo capturado en la ventada del detalle esperar 5 segundos")
    sge_funct.press_hotkeys('ctrl+w')
    print("29 Presionamos ctrl + W para Continuar")
    sge_funct.press_hotkeys('ctrl+w')
    print(
        "30 Posicionados en la columna Forma de Pago presionamos 4 veces la flecha abajo para posicionarse en tarjeta debito")
    sge_funct.flecha_abajo()
    sge_funct.flecha_abajo()
    sge_funct.flecha_abajo()
    sge_funct.flecha_abajo()
    print("31 Capturar el total a liquidar")
    sge_funct.send_text('69.99')
    print("32 Seleccionar el banco de la primera opcion con enter")
    sge_funct.press_enter()
    print("33 Teclear input")
    sge_funct.press_enter()
    print("34 Capturar los ultimos cuatro digitos de la tarjeta 3452")
    sge_funct.send_text('3452')
    print("35 Presionamos ctrl + W para grabar (generar factura)")
    sge_funct.press_hotkeys('ctrl+w')
    print("36 Presiona Enter para confirmar que si esta correcto ")
    sge_funct.press_enter()
    sge_funct.segundos_de_espera(5)
    print("37 Presionamos Enter para continuar ")
    sge_funct.press_enter()
    # print("38 Presionamos Enter para continuar ")
    # sge_funct.press_enter()

    num_factura = sge_funct.doubleclick_axis_x(img_inicioFactura, 10)
    print(f"Factura Generada: {num_factura}")
    assert num_factura is not None
    sge_funct.close_sge_session()
    # -------------------------------------------------------------------------4
    print("------------------------------------------------------------------------ inicia TC 28")
    print("Trying to Connect...")
    sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
    print("Validating connection...")
    assert sge_funct.validate_adm_sge_connection(
        images.img_sge_adm_pantalla_inicial), "Error Found, SGE Connection Failed!!"

    # num_factura = "12B3048916"
    print("2 Ingresar en el teclado el <<Numero de sucursal>>")
    sge_funct.send_text('12')
    sge_funct.validar_sucursal_12_seleccionada()
    print("3 Teclear input")
    sge_funct.press_enter()
    print("4 Teclear input")
    sge_funct.send_text('4')
    print("5 Teclear input")
    sge_funct.press_enter()
    print("6 Capturamos la opción 13")
    sge_funct.send_text('13')
    print("7 Teclear input")
    sge_funct.press_enter()
    print("8 Capturamos la opción 1 devoluciones")
    sge_funct.send_text('1')
    print("9 Teclear input")
    sge_funct.press_enter()
    print("10 En el campo factura pegar el numero de la factura con clic derecho")
    sge_funct.send_text(num_factura)
    print("11 Teclear input")
    sge_funct.press_enter()
    sge_funct.segundos_de_espera(3)
    print("12 Posicionarnos en la opción Dev. Cambio Medida de Producto")
    sge_funct.send_text('Flecha abajo 5 veces')
    for i in range(5):
        sge_funct.flecha_abajo()
    print("13 Teclear input")
    sge_funct.press_enter()
    print("14 Capturar bodega/almacen")
    sge_funct.send_text('01')
    print("15 Capturar ctrl+v para cargar la información")
    sge_funct.press_hotkeys('ctrl+v')
    print("16 Teclear enter para seleccionar el primer articulo")
    sge_funct.press_enter()
    print("17 Capturar la cantidad a devolver")
    sge_funct.send_text('1')
    print("18 Teclear input")
    sge_funct.press_enter()
    print("19 Capturar ctrl+w")
    sge_funct.press_hotkeys('ctrl+w')
    print("20 Teclear input")
    sge_funct.press_enter()
    print("21 Teclear input")
    sge_funct.press_enter()
    print("22 Teclear input")
    sge_funct.press_enter()
    print("23 Capturar ctrl+w")
    sge_funct.press_hotkeys('ctrl+w')
    print("24 Capturar si")
    sge_funct.send_text('s')
    print("25 Teclear input")
    sge_funct.press_enter()
    sge_funct.segundos_de_espera(5)
