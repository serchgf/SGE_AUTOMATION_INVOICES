""" COMANDOS PARA FACTURA CREDITO PEDIDO MASIVO """


class invoice_commands:
    opc_sistema_comercial = "3"
    opc_mayoreo_de_autopartes = "3"
    no_sucursal = "12"
    opc_pedidos_facturacion = "4"
    opc_ventas_directas = "10"
    ingresar_cuenta = "45820263"
    read_file = 'leer_archivo'
    ctrlw = hk_carga = hk_guardar = hk_facturar = hk_grabar = hk_continuar = ("ctrl", "w")
    ctrle = hk_buscar = ("ctrl", "e")
    ctrlo = hk_opciones = ("ctrl", "o")
    ctrla = hk_salir = ("ctrl", "a")
    doubleclick = 'doubleclick'
    arrow_down = "down"
    rclick = 'rclick'
    ctrlk = ("ctrl", "k")
    ingresar_linea = "99"
    ingresar_codigo = "3013M"
    n_unidades = "2"
    tiempo_fuera_5 = '5 segundos'
    tiempo_fuera_2 = '2 segundos'
    tiempo_fuera_3 = '3 segundos'
    promociones = 'promociones'
    #
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
    #     # # step 7 presionar 3 veces enter para posicionarse en Domicilio de entrega
    #     '\n',
    #     '\n',
    #     '\n',
    #     # # step 8 presionar enter por cuarta vez para seleccionar primer domicilio
    #     '\n',
    #     # # step 9 presionar ctrl+w para continuar y abrir detalle del pedido
    #     hk_continuar,
    #     tiempo_fuera_2,
    #     # paso verificacion de promociones
    #     promociones,
    #     # # step 10 presionar ctrl+o para ver la lista de opciones
    #     hk_opciones,
    #     # # step 11 ´presionar letra 'M' hasta encontrar la opcion ctrl+u Importa pedido masivo
    #     'm',
    #     # #step 12 presionar 'Enter'
    #     '\n',
    #     # # step 13 leer archivo para copiar y escribir los datos de archivo tmpmasivo.txt (esto sustituye el clic derecho
    #     read_file,
    #     # # presionar 'Enter' para que muestre la ultima linea bien
    #     '\n',
    #     #rclick,
    #     # # step 14P resionamos "ctrl + W" 2 veces para continuar y pasar al detalle de facturacion
    #     hk_continuar,
    #     # # step presionar ctrl+w para grabar lo capturado en la ventana
    #     hk_grabar,
    #     # # step 15 presionar ctrl+w para facturar
    #     hk_facturar,
    #     # # esperar 2 o 3 segundos
    #     tiempo_fuera_5,
    #     # # step 16 presionar 'Enter' para continuar
    #     '\n'
    #     # # validar imagen Folio Generado Enter Continuar
    # ]


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
        "tiempo_fuera_2": tiempo_fuera_2,
        "verificacion de promociones": promociones,
        "step 10 presionar ctrl+o para ver la lista de opciones" :hk_opciones,
        "step 11 ´presionar letra 'M' hasta encontrar la opcion ctrl+u Importar pedido masivo": 'm',
        "step 12 presionar 'Enter'":'\n',
        "step 13 leer archivo para copiar y escribir los datos de archivo tmpmasivo.txt (esto sustituye el clic derecho": read_file,
        "presionar 'Enter' para que muestre la ultima linea bien":'\n',
        "step 14 Presionamos 'ctrl + W' 2 veces para continuar y pasar al detalle de facturacion": hk_continuar,
        "step presionar ctrl+w para grabar lo capturado en la ventana": hk_grabar,
        "step 15 presionar ctrl+w para facturar": hk_facturar,
        "tiempo_fuera_5": tiempo_fuera_5,
        "step 16 presionar 'Enter' para continuar":'\n'
        # # validar imagen Folio Generado Enter Continuar
    }


    # with open("C:\\Users\\m1sgarciaf\\Desktop\\invoice mostrador simple order.csv", 'r') as file:
    #     for line in file:
    #         print(line)
    #