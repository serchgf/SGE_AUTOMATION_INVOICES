import time

from Config.config import images, login_data


def MTC_INVSGE_027_steps(sge_funct, img_inicioFactura):
    # -------------------------------------------------------------------------3
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
    sge_funct.segundos_de_espera(1)
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
    num_factura = sge_funct.doubleclick_axis_x(img_inicioFactura, 10)
    print(f"Factura Generada: {num_factura}")
    assert num_factura is not None
    sge_funct.close_sge_session()
    # -------------------------------------------------------------------------3
    #num_factura = "12B3048904"
    print("------------------------------------------------------------------------ inicia TC 27")
    print("Trying to Connect...")
    sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
    print("Validating connection...")
    assert sge_funct.validate_adm_sge_connection(
        images.img_sge_adm_pantalla_inicial), "Error Found, SGE Connection Failed!!"

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
    sge_funct.flecha_abajo()
    sge_funct.flecha_abajo()
    sge_funct.flecha_abajo()
    sge_funct.flecha_abajo()
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
    sge_funct.segundos_de_espera(5)










