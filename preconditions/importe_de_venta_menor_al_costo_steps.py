from Config.config import images


def pre_importe_de_venta_menor_al_costo(sge_funct, data):
    print("1 press 'MM'")
    print(data["sucursal"])
    #sge_funct.send_text('mm')
    sge_funct.activar_menu_mods()
    sge_funct.segundos_de_espera(1)
    # validar pantalla menu mods
    assert sge_funct.validate_image_x(images.img_utilerias_menu), "No se ingreso en pantalla de MOD's"
    print("2 Ingresar opcion mod 02 ")
    sge_funct.send_text('02')
    print("3 Press Enter")
    sge_funct.press_enter()
    # validar pantalla mod02
    assert sge_funct.validate_image_x(images.img_pantalla_mod02), "No se ingreso al MOD 02"
    print("Ingresar en el teclado el <<Numero de sucursal>>")
    sge_funct.send_text(data["sucursal"])
    sge_funct.validar_sucursal_12_seleccionada()
    sge_funct.press_enter()
    # validar pantalla de modificacion F2-F00
    assert sge_funct.validate_image_x(images.img_pantalla_modificacion_datos_f2_f00), "No se ingreso a la pantalla correcta"
    print("4 presionar b para buscar el producto ")
    sge_funct.send_text('b')
    print("4 presionar enter para posicionarse en ALM ")
    sge_funct.press_enter()
    print("4 ingresar almacen ")
    sge_funct.send_text(data["almacen"])
    sge_funct.press_enter()
    print("4 ingresar linea ")
    sge_funct.send_text(data["linea"])
    sge_funct.press_enter()
    print("4 ingresar codigo")
    sge_funct.clean_field()
    sge_funct.send_text(data["codigo"])
    sge_funct.press_enter()
    print("4 presionar m ")
    sge_funct.send_text('m')
    print("5 escribir D03")
    sge_funct.send_text('D03')
    print("6 escribir 0")
    sge_funct.clean_field()
    sge_funct.send_text('0')
    print("7 Press Enter")
    sge_funct.press_enter()
    print("8 escribir D04")
    sge_funct.send_text('D04')
    print("9 escribir 0")
    sge_funct.clean_field()
    sge_funct.send_text("0")
    print("10 Press Enter")
    sge_funct.press_enter()
    print("8 escribir D07")
    sge_funct.send_text('D07')
    sge_funct.clean_field()
    print("9 escribir 1")
    sge_funct.send_text(data["ultimo_costo"])
    print("10 Press Enter")
    sge_funct.press_enter()
    print("11 grabar los cambios ")
    sge_funct.send_text('99')
    print("12 Press Enter")
    sge_funct.press_enter()
    sge_funct.take_screenshot("ex_D03_D04_modificado")
    print("13 presionar T para terminar")
    sge_funct.send_text('t')
    sge_funct.segundos_de_espera(1)
    print("14 Presionar ctrl+a ")
    sge_funct.press_hotkeys('ctrl+a')
    print("15 Presionar ctrl+a ")
    sge_funct.press_hotkeys('ctrl+a')
    print("16 Presionar ctrl+a ")
    sge_funct.press_hotkeys('ctrl+a')