PERMISOS_ROL = {

    "Administrador": [
        "USUARIOS_CONSULTAR",
        "USUARIOS_CREAR",
        "USUARIOS_EDITAR",
        "USUARIOS_ELIMINAR",

        "INVENTARIO_CONSULTAR",
        "INVENTARIO_ENTRADA",
        "INVENTARIO_SALIDA",

        "COMPRAS_CONSULTAR",
        "COMPRAS_CREAR",

        "VENTAS_CONSULTAR",
        "VENTAS_CREAR"
    ],

    "Inventarios": [
        "INVENTARIO_CONSULTAR",
        "INVENTARIO_ENTRADA",
        "INVENTARIO_SALIDA"
    ],

    "Compras": [
        "COMPRAS_CONSULTAR",
        "COMPRAS_CREAR"
    ],

    "Ventas": [
        "VENTAS_CONSULTAR",
        "VENTAS_CREAR"
    ]
}


def obtener_permisos(nom_rol: str):

    return PERMISOS_ROL.get(
        nom_rol,
        []
    )