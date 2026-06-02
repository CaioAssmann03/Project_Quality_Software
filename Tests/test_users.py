import pytest
from unittest.mock import MagicMock

from fastapi import HTTPException

from routers.users import login
from schemas import UserLogin


class FakeUser:
    def __init__(self, user_id, name, email, password):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password


def test_deve_realizar_login_com_credenciais_validas():
    """
    Cenário:
    Usuário existe no banco e senha está correta.

    Resultado esperado:
    Retornar id e nome do usuário.
    """

    usuario_mock = FakeUser(
        user_id=1,
        name="João",
        email="joao@email.com",
        password="123456"
    )

    db = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = usuario_mock

    resultado = login(
        UserLogin(
            email="joao@email.com",
            password="123456"
        ),
        db
    )

    assert resultado["user_id"] == 1
    assert resultado["name"] == "João"


def test_deve_retornar_dados_corretos_do_usuario_autenticado():
    """
    Cenário:
    Usuário Maria realiza login.

    Resultado esperado:
    Retornar os dados corretos.
    """

    usuario_mock = FakeUser(
        user_id=2,
        name="Maria",
        email="maria@email.com",
        password="senha123"
    )

    db = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = usuario_mock

    resultado = login(
        UserLogin(
            email="maria@email.com",
            password="senha123"
        ),
        db
    )

    assert resultado == {
        "user_id": 2,
        "name": "Maria"
    }


def test_deve_gerar_erro_quando_credenciais_foreem_invalidas():
    """
    Cenário:
    Usuário não encontrado.

    Resultado esperado:
    HTTPException 401.
    """

    db = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = None

    with pytest.raises(HTTPException) as erro:

        login(
            UserLogin(
                email="invalido@email.com",
                password="senha_errada"
            ),
            db
        )

    assert erro.value.status_code == 401
    assert erro.value.detail == "Invalid credentials"