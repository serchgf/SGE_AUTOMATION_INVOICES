from Config.config import images


def pre_change_rfc_date(sge_funct, rfc: str):
    print("1 press 'MM'")
    sge_funct.send_text('mm')
    sge_funct.segundos_de_espera(1)
    assert sge_funct.validate_image_x(images.img_utilerias_menu), "No se ingreso en pantalla de MOD's"
    #sge_funct.stop_pyautogui()
    print("2 Ingresar opcion mod rfc ")
    sge_funct.send_text('79')
    print("3 Press Enter")
    sge_funct.press_enter()
    # validar imagen utilerias rfc
    assert sge_funct.validate_image_x(images.img_utilerias_mod_rfc), "No se ingreso al MOD rfc"
    print("4 presionar b ")
    sge_funct.send_text('b')
    print("5 escribir rfc a modificar")
    sge_funct.send_text(rfc)
    print("6 Press Enter")
    sge_funct.press_enter()
    print("7 elegir opcion para modificar ")
    sge_funct.send_text('m')
    print("8 elegir opcion para modificar fecha ")
    sge_funct.send_text('d05')
    print("9 ingresar fecha actual formato yyyymmdd ")
    fecha= sge_funct.fecha_yyyymmdd()
    sge_funct.send_text(fecha)
    print("10 grabar los cambios ")
    sge_funct.send_text('99')
    print("11 Press Enter")
    sge_funct.press_enter()
    sge_funct.take_screenshot("cambio_fecha_rfc")
    print("presionar T para terminar")
    sge_funct.send_text('t')
    assert sge_funct.validate_image_x(images.img_utilerias_menu), "No se ingreso en pantalla de MOD's"
    print("16 Presionar ctrl+a ")
    sge_funct.press_hotkeys('ctrl+a')
    print("16 Presionar ctrl+a ")
    sge_funct.press_hotkeys('ctrl+a')
