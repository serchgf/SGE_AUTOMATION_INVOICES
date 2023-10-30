""" COMANDOS PARA FACTURA CREDITO PEDIDO SIMPLE """


class invoice_commands:
    opc_sistema_comercial = "3"
    opc_mayoreo_de_autopartes = "3"
    no_sucursal = "12"
    opc_pedidos_facturacion = "4"
    opc_ventas_directas = "10"
    ingresar_cuenta = "45820263"
    ctrlw = hk_carga = hk_guardar = hk_facturar = hk_grabar = hk_continuar = ("ctrl", "w")
    ctrle = hk_buscar = ("ctrl", "e")
    ctrla = hk_salir = ("ctrl", "a")
    ingresar_linea = "99"
    ingresar_codigo = "3013M"
    n_unidades = "2"
    tiempo_fuera_5 = '5 segundos'
    tiempo_fuera_2 = '2 segundos'
    tiempo_fuera_3 = '3 segundos'
    promociones = "promociones"

    cmds = {
        "step 1 Ingresar al 'sistema comercial": opc_sistema_comercial,
        "Press Enter0": '\n',
        "step 2 Ingresar a 'Mayoreo de Autopartes'": opc_mayoreo_de_autopartes,
        "Press Enter1": '\n',
        "step 3 ingresar numero de sucursal": no_sucursal,
        "Press Enter2": '\n',
        "step 4 ingresar opcion de 'pedidos facturacion'": opc_pedidos_facturacion,
        "Press Enter3": '\n',
        "step 5 ingresar opcion de 'ventas directas'": opc_ventas_directas,
        "Press Enter4": '\n',
        "step 6 ingresar cuenta": ingresar_cuenta,
        "step 7 presionar 3 veces enter para posicionarse en Domicilio de entrega": '\n',
        "Press Enter5": '\n',
        "Press Enter6": '\n',
        "step 8 presionar enter por cuarta vez para seleccionar primer domicilio": '\n',
        "step 9 presionar ctrl+w para continuar y abrir detalle del pedido": hk_continuar,
        # "tiempo_fuera_2": tiempo_fuera_2,
        "verificacion de promociones": promociones,
        "step 10 presionar ctrl+e para buscar lineas de producto de inventario": hk_buscar,
        "step 11 step 11 ingresar numero de linea": ingresar_linea,
        "Press Enter7": '\n',
        "step 12 ingresar codigo": ingresar_codigo,
        "Press Enter8": '\n',
        "step 13 presionar 3 veces enter para posicionarse en columna 'Cantidad'": '\n',
        "Press Enter9": '\n',
        "Press Enter10": '\n',
        "ingresar n cantidad de unidade": n_unidades,
        "Press Enter11": '\n',
        "step 14 seleccionar opcion facturar con ctrl+w para facturar lo capturado en la ventana de detalle": hk_facturar,
        "tiempo_fuera_5": tiempo_fuera_5,
        "step presionar ctrl+w para grabar lo capturado en la ventana": hk_grabar,
        "step 15 presionar 'Enter' para continuar": '\n'
    }


    # cmds = [
    #     # step 1 ingresar al "sistema comercial"
    #     opc_sistema_comercial,
    #     '\n',
    #     # step 2 ingresar a "Mayoreo de Autopartes"
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
    #     # step 6 ingresar ingresar cuenta
    #     ingresar_cuenta,
    #     # # step 7 presionar 3 veces enter para posicionarse en 'Domicilio de entrega'
    #     '\n',
    #     '\n',
    #     '\n',
    #     # step 8 presionar enter por cuarta vez para seleccionar primer domicilio
    #     '\n',
    #     # step 9 presionar ctrl+w para continuar y abrir detalle del pedido
    #     hk_continuar,
    #     promociones,
    #     # step 10 presionar ctrl+e para buscar lineas de producto de inventario
    #     hk_buscar,
    #     # step 11 ingresar numero de linea
    #     ingresar_linea,
    #     '\n',
    #     # step 12 ingresar codigo
    #     ingresar_codigo,
    #     '\n',
    #     # step 13 presionar 3 veces enter para posicionarse en columna 'Cantidad'
    #     '\n',
    #     '\n',
    #     '\n',
    #     # ingresar n cantidad de unidades
    #     n_unidades,
    #     '\n',
    #     # step 14 seleccionar opcion facturar con ctrl+w para facturar lo capturado en la ventana de detalle
    #     hk_facturar,
    #     tiempo_fuera_5,
    #     # validar la imagen de referencia ok
    #     # step 15 presionar 'Enter' para continuar
    #     '\n'
    #     # validar imagen Folio Generado Enter Continuar
    # ]

