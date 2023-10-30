""" COMANDOS PARA FACTURA MOSTRADOR PEDIDO SIMPLE """


class invoice_commands:
    opc_sistema_comercial = "3"
    opc_mayoreo_de_autopartes = "3"
    no_sucursal = "12"
    opc_pedidos_facturacion = "4"
    opc_ventas_directas = "10"
    ingresar_cuenta = "45828833"
    ctrlw = hk_carga = hk_guardar = hk_facturar = hk_grabar = hk_continuar = ("ctrl", "w")
    ctrle = hk_buscar = ("ctrl", "e")
    ctrla = hk_salir = ("ctrl", "a")
    ctrlr = ("ctrl", "r")
    ingresar_linea = "31"
    ingresar_codigo = "1408"
    ingresar_cuenta_mostrador = " 0274890"
    clave_agente = "06"
    n_unidades = "2"
    tiempo_fuera = '5 segundos'
    tab = "tab"
    tiempo_fuera_5 = '5 segundos'
    tiempo_fuera_2 = '2 segundos'
    tiempo_fuera_3 = '3 segundos'
    promociones ='promociones'

    cmds = {
        "step 1 Ingresar al 'sistema comercial": opc_sistema_comercial,
        "Press Enter0": '\n',
        "step 2 Ingresar a 'Mayoreo de Autopartes'":opc_mayoreo_de_autopartes,
        "Press Enter1": '\n',
        "step 3 ingresar numero de sucursal": no_sucursal,
        "Press Enter2": '\n',
        "step 4 ingresar opcion de 'pedidos facturacion'": opc_pedidos_facturacion,
        "Press Enter3": '\n',
        "step 5 ingresar opcion de 'ventas directas'": opc_ventas_directas,
        "Press Enter4": '\n',
        "step 6 ingresar cuenta": ingresar_cuenta,
        "verificacion de promociones": promociones,
        "step 7 presionar 'crtl + e' para abrir busqueda de linea": ctrle,
        "step 7.1 ingresar numero de linea": ingresar_linea,
        "Press Enter5": '\n',
        "step 8 ingresar codigo y presionar 'Enter'": ingresar_codigo,
        "Press Enter6": '\n',
        "step 9 presionar 3 veces enter para posicionarse en columna 'cantidad'": '\n',
        "Press Enter7": '\n',
        "Press Enter8": '\n',
        "step 9.1 capturar 'cantidad' y presionar 'Enter'": n_unidades,
        "Press Enter9": '\n',
        "step 10 presionar enter SIN EDITAR columna importe": '\n',
        "step 11 presionar ctrl+w para facturar lo capturado en ventana del detalle": hk_facturar,
        "Press Enter10": '\n',
        "step 12 presionar 'Tab' dos veces": tab,
        "Press Tab": tab,
        "step 12.1 ingresar cuenta mostrador": ingresar_cuenta_mostrador,
        # "Press Enter11": '\n',  verificar si este enter va o no va
        "step 13 presionar 'Enter' para seleccionar cliente buscado": '\n',
        "step 14 ingresar clave de agente y presionar 'Enter'": clave_agente,
        "Press Enter12": '\n',
        "step 15 presionar 'Enter' en campo 'referencia' sin capturar nada": '\n',
        "step 16 presionar 'Enter' en campo 'regimen fiscal' sin capturar nada": '\n',
        "step 17 presionar 'Enter' en campo 'Uso del CFDI' sin capturar nada":'\n',
        "step 18 presionar 'Enter' en campo 'Medio de entrega/enbarque' sin capturar nada": '\n',
        "step 19 presionar 'crtl + w' para regresar a la ventana del detalle": ctrlw,
        "step 20 presionar 'crtl + w' para facturar": hk_facturar,
        "step 21 presionar 'crtl + w' para continuar": hk_continuar,
        "step 22 presionar 'crtl + r' para aplicar adeudo": ctrlr,
        "step 23 presionar 'crtl + w' para grabar(generar factura)": hk_grabar,
        "step 24 presionar 'Enter' para confirmar si es correcto": '\n',
        "tiempo_fuera_3": tiempo_fuera_3,
        "step 25 presionar 'Enter' para continuar": '\n'
    }

    # cmds = [
    #     # step 1 ingresar al "sistema comercial"
    #     opc_sistema_comercial,
    #     '\n',
    #     # step 2 ingresara a "Mayoreo de Autopartes"
    #     opc_mayoreo_de_autopartes,
    #     '\n',
    #     # step 3 ingresar numero de sucursal
    #     no_sucursal,
    #     '\n',
    #     # step 4 ingresar opcion de "pedidos facturacion"
    #     opc_pedidos_facturacion,
    #     '\n',
    #     # step 5 ingresar opcion de "ventas directas"
    #     opc_ventas_directas,
    #     '\n',
    #     # step 6 ingresar cuenta
    #     ingresar_cuenta,
    #     # paso verificacion de promociones
    #     promociones,
    #     # step 7 presionar 'crtl + e' para abrir busqueda de linea
    #     ctrle,
    #     # # step 7.1 ingresar numero de linea y presionar 'Enter'
    #     ingresar_linea,
    #     '\n',
    #     # # step 8 ingresar codigo y presionar 'Enter'
    #     ingresar_codigo,
    #     '\n',
    #     # # step 9 presionar 3 veces enter para posicionarse en columna 'cantidad'
    #     '\n',
    #     '\n',
    #     '\n',
    #     # # step 9.1 capturar 'cantidad' y presionar 'Enter'
    #     n_unidades,
    #     '\n',
    #     # # step 10 presionar enter SIN EDITAR columna importe
    #     '\n',
    #     # # step 11 presionar ctrl+w para facturar lo capturado en ventana del detalle
    #     hk_facturar,
    #     # # step 12 presionar 'Enter' para seleccionar cliente de mostrador
    #     '\n',
    #     # # step 13 presionar 'Tab' dos veces
    #     tab,
    #     tab,
    #     # # step 13.1 ingresar cuenta mostrador
    #     ingresar_cuenta_mostrador,
    #     # # step 14 presionar 'Enter' para seleccionar cliente buscado
    #     '\n',
    #     # # step 15 ingresar clave de agente y presionar 'Enter'
    #     clave_agente,
    #     '\n',
    #     # # step 16 presionar 'Enter' en campo 'referencia' sin capturar nada
    #     '\n',
    #     # # step 17 presionar 'Enter' en campo 'regimen fiscal' sin capturar nada
    #     '\n',
    #     # # step 18 presionar 'Enter' en campo 'Uso del CFDI' sin capturar nada
    #     '\n',
    #     # # step 19 presionar 'Enter' en campo 'Medio de entrega/enbarque' sin capturar nada
    #     '\n',
    #     # # step 20 presionar 'crtl + w' para regresar a la ventana del detalle
    #     ctrlw,
    #     # # step 21 presionar 'crtl + w' para facturar
    #     hk_facturar,
    #     # # step 22 presionar 'crtl + w' para continuar
    #     hk_continuar,
    #     # # step 23 presionar 'crtl + r' para aplicar adeudo
    #     ctrlr,
    #     # # step 24 presionar 'crtl + w' para grabar (generar factura)
    #     hk_grabar,
    #     # # step 25 presionar 'Enter' para confirmar si es correcto
    #     '\n',
    #     tiempo_fuera_3,
    #     # # step 26 presionar 'Enter' para continuar
    #     '\n'
    #     # # # validar imagen Folio Generado Enter Continuar
    # ]
