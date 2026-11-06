import login


def test_cargar_usuarios():
    # Creamos un archivo con dos usuarios.
    archivo = open(login.archivo_usuarios, "w", encoding="UTF-8")
    archivo.write("ana,1234,Cliente\n")
    archivo.write("juan,5678,Cliente\n")
    archivo.close()

    usuarios = login.cargar_usuarios()

    assert usuarios == [
        ["ana", "1234", "Cliente"],
        ["juan", "5678", "Cliente"]
    ]


def test_cargar_usuarios_sin_archivo():
    # Eliminamos el archivo para comprobar qué sucede.
    import os

    if os.path.exists(login.archivo_usuarios):
        os.remove(login.archivo_usuarios)

    usuarios = login.cargar_usuarios()

    assert usuarios == [["cliente", "4321", "Cliente"]]


def test_registrar_usuario():
    # Preparamos un archivo con un usuario.
    archivo = open(login.archivo_usuarios, "w", encoding="UTF-8")
    archivo.write("cliente,4321,Cliente\n")
    archivo.close()

    # Registramos un usuario nuevo.
    login.input = lambda mensaje: "ana" if "nombre" in mensaje else "1234"

    login.registrar_usuario()

    usuarios = login.cargar_usuarios()

    assert ["ana", "1234", "Cliente"] in usuarios


def test_registrar_usuario_existente():
    # Preparamos un usuario que ya existe.
    archivo = open(login.archivo_usuarios, "w", encoding="UTF-8")
    archivo.write("ana,1234,Cliente\n")
    archivo.close()

    login.input = lambda mensaje: "ana" if "nombre" in mensaje else "5678"

    login.registrar_usuario()

    usuarios = login.cargar_usuarios()

    assert usuarios == [["ana", "1234", "Cliente"]]


def test_registrar_usuario_campos_vacios():
    # Preparamos el archivo inicial.
    archivo = open(login.archivo_usuarios, "w", encoding="UTF-8")
    archivo.write("cliente,4321,Cliente\n")
    archivo.close()

    login.input = lambda mensaje: "" if "nombre" in mensaje else "1234"

    login.registrar_usuario()

    usuarios = login.cargar_usuarios()

    assert usuarios == [["cliente", "4321", "Cliente"]]


def test_registrar_usuario_con_coma():
    # Preparamos el archivo inicial.
    archivo = open(login.archivo_usuarios, "w", encoding="UTF-8")
    archivo.write("cliente,4321,Cliente\n")
    archivo.close()

    login.input = lambda mensaje: "ana,juan" if "nombre" in mensaje else "1234"

    login.registrar_usuario()

    usuarios = login.cargar_usuarios()

    assert usuarios == [["cliente", "4321", "Cliente"]]


def test_iniciar_sesion_cliente():
    # Preparamos los datos del cliente.
    archivo = open(login.archivo_usuarios, "w", encoding="UTF-8")
    archivo.write("ana,1234,Cliente\n")
    archivo.close()

    datos = ["ana", "1234"]
    login.input = lambda mensaje: datos.pop(0)

    assert login.iniciar_sesion() == "Cliente"


def test_iniciar_sesion_administrador():
    # Preparamos los datos del administrador.
    archivo = open(login.archivo_usuarios, "w", encoding="UTF-8")
    archivo.write("cliente,4321,Cliente\n")
    archivo.close()

    datos = ["admin", "1234"]
    login.input = lambda mensaje: datos.pop(0)

    assert login.iniciar_sesion() == "Administrador"


def test_iniciar_sesion_datos_incorrectos():
    # Preparamos los datos iniciales.
    archivo = open(login.archivo_usuarios, "w", encoding="UTF-8")
    archivo.write("cliente,4321,Cliente\n")
    archivo.close()

    datos = [
        "ana", "1111",
        "juan", "2222",
        "pedro", "3333"
    ]
    login.input = lambda mensaje: datos.pop(0)

    assert login.iniciar_sesion() == None
