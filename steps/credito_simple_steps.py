from Config.config import images


def crear_credito_simple_invoice(sge_funct):
    print("5 Ingresar numero de sucursal ")
    sge_funct.send_text('12')
    sge_funct.segundos_de_espera(1)
    sge_funct.validar_sucursal_12_seleccionada()
    print("6 Press Enter")
    sge_funct.press_enter()
    print("7 Ingresar opcion de 'pedidos facturacion' ")
    sge_funct.send_text('4')
    print("8 Press Enter")
    sge_funct.press_enter()
    print("9 Ingresar opcion de 'ventas directas' ")
    sge_funct.send_text('10')
    print("10 Press Enter")
    sge_funct.press_enter()
    print("11 Ingresar cuenta ")
    sge_funct.send_text('45820263')
    print("12 Presionar 3 veces enter para posicionarse en Domicilio de entrega")
    sge_funct.press_enter()
    print("13 Press Enter")
    sge_funct.press_enter()
    print("14 Press Enter")
    sge_funct.press_enter()
    print("15 Presionar enter por cuarta vez para seleccionar primer domicilio") #MOTO
    sge_funct.press_enter()
    print("16 Presionar ctrl+w para continuar y abrir detalle del pedido")
    sge_funct.press_hotkeys('ctrl+w')
    print("17 Verificacion de promociones y atrasos")
    while sge_funct.promociones_y_atrasos():
        sge_funct.press_hotkeys('ctrl+a')
    print("18 Presionar ctrl+e para buscar lineas de producto de inventario")
    sge_funct.press_hotkeys('ctrl+e')
    print("19 Ingresar numero de linea")
    sge_funct.send_text('99')
    print("20 Press Enter")
    sge_funct.press_enter()
    print("21 Ingresar codigo")
    sge_funct.send_text('3013M')
    print("22 Press Enter")
    sge_funct.press_enter()
    print("23 presionar 3 veces enter para posicionarse en columna 'Cantidad'")
    sge_funct.press_enter()
    print("24 Press Enter")
    sge_funct.press_enter()
    print("25 Press Enter")
    sge_funct.press_enter()
    print("26 Ingresar n cantidad de unidades")
    sge_funct.send_text('2')
    print("27 Press Enter")
    sge_funct.press_enter()
    print("28 Seleccionar opcion facturar con ctrl+w para facturar lo capturado en la ventana de detalle")
    sge_funct.press_hotkeys('ctrl+w')
    sge_funct.segundos_de_espera(5)
    sge_funct.send_text('5 segundos')
    print("30 Presionar ctrl+w para grabar lo capturado en la ventana")
    sge_funct.press_hotkeys('ctrl+w')
    sge_funct.segundos_de_espera(3)
    print("32 Presionar 'Enter' para continuar")
    sge_funct.press_enter()
