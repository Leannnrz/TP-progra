
import login

def test_cargar_usuarios(tmp_path, monkeypatch):
    # Utilizamos un archivo temporal para no modificar usuarios.txt.
    archivo = tmp_path / "usuarios.txt"
    archivo.write_text("ana,1234,Cliente\njuan,5678,Cliente\n", encoding="UTF-8")

    monkeypatch.setattr(login, "archivo_usuarios", str(archivo))

    usuarios = login.cargar_usuarios()

    assert usuarios == [
        ["ana", "1234", "Cliente"],
        ["juan", "5678", "Cliente"]
    ]


def test_cargar_usuarios_sin_archivo(tmp_path, monkeypatch):
    # Si el archivo no existe, se crea con el usuario predeterminado.
    archivo = tmp_path / "usuarios.txt"
    monkeypatch.setattr(login, "archivo_usuarios", str(archivo))

    usuarios = login.cargar_usuarios()

    assert usuarios == [["cliente", "4321", "Cliente"]]
    assert archivo.exists()


def test_registrar_usuario(monkeypatch, tmp_path):
    # Probamos registrar un usuario nuevo.
    archivo = tmp_path / "usuarios.txt"
    archivo.write_text("cliente,4321,Cliente\n", encoding="UTF-8")
    monkeypatch.setattr(login, "archivo_usuarios", str(archivo))

    entradas = iter(["ana", "1234"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    login.registrar_usuario()

    usuarios = login.cargar_usuarios()

    assert ["ana", "1234", "Cliente"] in usuarios


def test_registrar_usuario_existente(monkeypatch, tmp_path):
    # No debe permitir registrar un usuario que ya existe.
    archivo = tmp_path / "usuarios.txt"
    archivo.write_text("ana,1234,Cliente\n", encoding="UTF-8")
    monkeypatch.setattr(login, "archivo_usuarios", str(archivo))

    entradas = iter(["ana", "5678"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    login.registrar_usuario()

    usuarios = login.cargar_usuarios()

    assert usuarios == [["ana", "1234", "Cliente"]]


def test_registrar_usuario_campos_vacios(monkeypatch, tmp_path):
    # No se permite registrar usuarios con campos vacíos.
    archivo = tmp_path / "usuarios.txt"
    archivo.write_text("cliente,4321,Cliente\n", encoding="UTF-8")
    monkeypatch.setattr(login, "archivo_usuarios", str(archivo))

    entradas = iter(["", "1234"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    login.registrar_usuario()

    usuarios = login.cargar_usuarios()

    assert usuarios == [["cliente", "4321", "Cliente"]]


def test_registrar_usuario_con_coma(monkeypatch, tmp_path):
    # No se permite utilizar comas en el nombre o la contraseña.
    archivo = tmp_path / "usuarios.txt"
    archivo.write_text("cliente,4321,Cliente\n", encoding="UTF-8")
    monkeypatch.setattr(login, "archivo_usuarios", str(archivo))

    entradas = iter(["ana,juan", "1234"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    login.registrar_usuario()

    usuarios = login.cargar_usuarios()

    assert usuarios == [["cliente", "4321", "Cliente"]]


def test_iniciar_sesion_cliente(monkeypatch, tmp_path):
    # Probamos el inicio de sesión de un cliente.
    archivo = tmp_path / "usuarios.txt"
    archivo.write_text("ana,1234,Cliente\n", encoding="UTF-8")
    monkeypatch.setattr(login, "archivo_usuarios", str(archivo))

    entradas = iter(["ana", "1234"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    assert login.iniciar_sesion() == "Cliente"


def test_iniciar_sesion_administrador(monkeypatch, tmp_path):
    # Probamos el inicio de sesión del administrador.
    archivo = tmp_path / "usuarios.txt"
    archivo.write_text("cliente,4321,Cliente\n", encoding="UTF-8")
    monkeypatch.setattr(login, "archivo_usuarios", str(archivo))

    entradas = iter(["admin", "1234"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    assert login.iniciar_sesion() == "Administrador"


def test_iniciar_sesion_datos_incorrectos(monkeypatch, tmp_path):
    # Si los datos son incorrectos, permite tres intentos y devuelve None.
    archivo = tmp_path / "usuarios.txt"
    archivo.write_text("cliente,4321,Cliente\n", encoding="UTF-8")
    monkeypatch.setattr(login, "archivo_usuarios", str(archivo))

    entradas = iter([
        "ana", "1111",
        "juan", "2222",
        "pedro", "3333"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    assert login.iniciar_sesion() == None
