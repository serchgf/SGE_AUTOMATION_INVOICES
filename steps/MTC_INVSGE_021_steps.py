from Config.config import images


def MTC_INVSGE_021_steps(sge_funct, archivo_productos):
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
    print("8 Posicionarse en campo cuenta y capturar la cuenta 45828833")
    sge_funct.send_text('45828833')
    print("9 Presionamos ctrl + O para más opciones")
    sge_funct.press_hotkeys('ctrl+o')
    print("10 Presionar Letra M Importa pedido masivo")
    sge_funct.send_text('m')
    print("11 Presionamos Enter para continuar ")
    sge_funct.press_enter()
    print("12 Oprimir click derecho del mouse para Pegar los datos de los articulos a facturar tmpmasivo.txt")
    sge_funct.leer_archivo_productos(archivo_productos)
    sge_funct.segundos_de_espera(5)
    print("13 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("14 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("15 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("17 Presionarmos Enter Para seleccionar al cliente de mostrador")
    sge_funct.press_enter()
    sge_funct.segundos_de_espera(1)
    print("18 Teclear input")
    sge_funct.press_tab()
    sge_funct.segundos_de_espera(1)
    print("19 Teclear input")
    sge_funct.press_tab()
    sge_funct.segundos_de_espera(1)
    print("20  y capturamos la cuenta  0274890 (el primer carácter es espacios)")
    sge_funct.send_text(' 0274890')
    sge_funct.segundos_de_espera(3)
    print("21 Teclear input")
    sge_funct.press_enter()
    print("22 Capturamos clave del agente 06")
    sge_funct.send_text('06')
    print("23 Teclear input")
    sge_funct.press_enter()
    print("24 Presionamos Enter sin capturar nada sobre el campo referencia")
    sge_funct.press_enter()
    print("25 Presionamos Enter sin capturar nada sobre el campo Regimen Fiscal")
    sge_funct.press_enter()
    print("26 Presionamos Enter sin capturar nada sobre el campo Uso del CFDI")
    sge_funct.press_enter()
    print("27 Presionamos Enter sin capturar nada sobre el campo Medio de entrega/embarque")
    sge_funct.press_enter()
    print("28 Presionamos ctrl + W para regresar a la ventana del Detalle")
    sge_funct.press_hotkeys('ctrl+w')
    print("29 Presionamos ctrl + W para Facturar")
    sge_funct.press_hotkeys('ctrl+w')
    print("30 Presionamos ctrl + W para Continuar")
    sge_funct.press_hotkeys('ctrl+w')
    print("31 Posicionados en la columna Forma de Pago presionamos ctrl + R aplicar adeudo")
    sge_funct.press_hotkeys('ctrl+r')
    print("32 Presionamos ctrl + W para grabar (generar factura)")
    sge_funct.press_hotkeys('ctrl+w')
    print("33 Presiona Enter para confirmar que si esta correcto ")
    sge_funct.press_enter()
    sge_funct.segundos_de_espera(7)
    print("34 Presionamos Enter para continuar ")
    sge_funct.press_enter()



