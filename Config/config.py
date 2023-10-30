"""
pip install pytest-html
pip install ansi2html
pip install ddt
"""
import os


class login_data:
    # uat02
    apuntando_A = "surplus"
    ambiente = "UAT02"
    linux_username = "itmx12"
    password = "sgem5986"
    ip = "192.168.1.3"
    usuario_de_compras = "sfabian"


class csv_files_path:
    main_dir = "Config/TestDataSet/"
    file_name = "tmpmasivo.txt"
    txt_file = main_dir + file_name
    csv_invoice_mostrador_simple_order = "Config/TestDataSet/invoice_mostrador_simple.csv"
    csv_invoice_credit_simple_order = "Config/TestDataSet/invoice_credit_simple_order.csv"
    csv_invoice_credit_massive_order = "Config/TestDataSet/invoiceCreditMassiveOrder.csv"


class txt_files_path:
    main_dir = "Config/TestDataSet/"
    file_name = "tmpmasivo.txt"
    txt_file = main_dir + file_name
    carga_masiva_txt = "Config/TestDataSet/tmpmasivo.txt"
    carga_masiva_20_txt = "Config/TestDataSet/tmpmasivo20.txt"
    carga_masiva_50_txt = "Config/TestDataSet/tmpmasivo50.txt"


class images:
    """images location"""
    ROOT = os.path.abspath(os.path.join(".", os.pardir))
    img_pantalla_inicial = f"image_files/pantallaInicial.png"
    img_error_connection = f"image_files/errorConexion2.png"
    img_error_atraso_importante = f"image_files/Error atraso importante.png"
    img_error_cedi_preferente = f"image_files/error_cedi_preferente.png"
    img_invoice_created_correctly = f"image_files/folioGeneradoValidacion.png"
    img_rclick_carga_masiva = f"image_files/rclick_carga_masiva.png"
    img_promociones = f"image_files/promociones.png"
    img_promociones2 = f"image_files/promociones2.png"
    img_inicio_orden_de_compra = "image_files/inicioOrdenCompra.png"
    img_consulta_orde_de_compra = "image_files/consulta_oc.png"
    img_confirmacion_colocada = "image_files/confirmacionColocada.png"
    img_header_orden_de_compra = "image_files/header_orden_de_compra.png"
    img_sge_adm_pantalla_inicial = f"image_files/sge_adm_pantalla_inicial.png"
    img_folio_generado_validacion = f"image_files/folioGeneradoValidacion.png"
    img_allure_screenshot_name = "my_allure_screenshot.png"
    img_allure_screenshot_path = "/Screenshots/my_allure_screenshot.png"
    img_seleccion_sucursal_12 = "image_files/seleccion_sucursal_12.png"
    img_inicio_factura = "image_files/inicioFactura.png"
    img_validacion_devolucion_total = "image_files/devolucion_factura_credito_total.png"
    img_pantalla_mod02 = "image_files/pantalla_mod02.png"
    img_pantalla_modificacion_datos_f2_f00 = "image_files/pantalla_modificacion_de_datos_del_f2_f00.png"
    img_sucursal_12_selec_mods = "image_files/sucursal_12_selec_mods.png"
    img_costo_adquisicion = "image_files/costo_adquision_vigente.png"
    img_utilerias_menu = "image_files/utilerias_homescreen.png"
    img_utilerias_mod_rfc = "image_files/utilerias_rfc_screen.png"
    img_invoice_created_correctly_20 = "image_files/folioGeneradoValidacion_20.png"
    img_invoice_created_correctly_50 = "image_files/folioGeneradoValidacion_50.png"

class files:
    directory_tmp_file = "tmp_file/"
    inv_base_txt_file = "Config/TestDataSet/INV-012M0021200190RD.txt"
    screenshot_folder = "Screenshots/"
    change_rfc_date = "Config/TestDataSet/change_rfc_date.json"
    importe_venta_menor_al_costo = "Config/TestDataSet/importe_venta_menor_al_costo2.json"
    entry_to_articles = "Config/TestDataSet/Entry_to_Articles2.json"


class commons_cmds:
    ctrle = "ctrl+e"
    ctrlo = "ctrl+o"
    ctrlw = "ctrl+w"
    ctrlk = "ctrl+k"
    ctrla = "ctrl+a"
    ctrlr = "ctrl+r"
    rclick = 'rclick'
    arrow_down = 'down'
    tab = "tab"
    doubleClick = 'doubleclick'
    bk_space = 'backspace'
    space = 'space'
    tiempo_fuera_2 = '2 segundos'
    tiempo_fuera_3 = '3 segundos'
    tiempo_fuera_5 = '5 segundos'
    tiempo_fuera_10 = '10 segundos'
    promociones = 'promociones'
    leer_archivo = 'leer_archivo'
    enter = 'enter'
    validar_cdi = "validar_cdi"


class image_root:
    ROOT = os.path.abspath(os.path.join(".", os.pardir))
