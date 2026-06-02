# Aula 09 – Testes Unitários Automatizados e TDD

## Integrante

Caio Assmann

## Sistema

LocalEats

## 1. Funcionalidade Escolhida

### Validação de Login

Funcionalidade existente no backend do LocalEats:

```python
@router.post("/login")
def login(user_data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.email == user_data.email,
        models.User.password == user_data.password
    ).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"user_id": user.id, "name": user.name}
```

### O que faz

Valida as credenciais do usuário para permitir acesso ao sistema.

### Regras de negócio

* Email deve existir no banco de dados
* Senha deve corresponder ao usuário
* Credenciais inválidas devem retornar erro
* Login válido deve retornar os dados do usuário

### Importância

Essa funcionalidade é responsável pelo controle de acesso ao sistema e proteção dos dados dos usuários.

---

# 2. Testes Unitários

## Teste 1

### Nome descritivo

Deve realizar login com credenciais válidas

### Cenário testado

Valida se um usuário existente consegue autenticar corretamente.

### Dados de entrada

```python
email = "joao@email.com"
senha = "123456"
```

### Resultado esperado

```python
{
    "user_id": 1,
    "name": "João"
}
```

### Código do teste

```python
def test_login_com_credenciais_validas():

    usuario_mock = User(
        id=1,
        name="João",
        email="joao@email.com",
        password="123456"
    )

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
```

---

## Teste 2

### Nome descritivo

Deve retornar os dados corretos do usuário autenticado

### Cenário testado

Verifica se o retorno contém as informações corretas após autenticação.

### Dados de entrada

```python
email = "maria@email.com"
senha = "senha123"
```

### Resultado esperado

```python
{
    "user_id": 2,
    "name": "Maria"
}
```

### Código do teste

```python
def test_retorna_dados_corretos_do_usuario():

    usuario_mock = User(
        id=2,
        name="Maria",
        email="maria@email.com",
        password="senha123"
    )

    db.query.return_value.filter.return_value.first.return_value = usuario_mock

    resultado = login(
        UserLogin(
            email="maria@email.com",
            password="senha123"
        ),
        db
    )

    assert resultado["user_id"] == 2
    assert resultado["name"] == "Maria"
```

---

## Teste 3

### Nome descritivo

Deve gerar erro quando as credenciais forem inválidas

### Cenário testado

Valida se o sistema bloqueia login com usuário ou senha incorretos.

### Dados de entrada

```python
email = "teste@email.com"
senha = "errada"
```

### Resultado esperado

Exceção HTTP 401.

### Código do teste

```python
import pytest
from fastapi import HTTPException

def test_login_com_credenciais_invalidas():

    db.query.return_value.filter.return_value.first.return_value = None

    with pytest.raises(HTTPException) as erro:

        login(
            UserLogin(
                email="teste@email.com",
                password="errada"
            ),
            db
        )

    assert erro.value.status_code == 401
```

---

# 3. Aplicação do TDD

## RED

Primeiramente foi criado o teste:

```python
def test_login_com_credenciais_invalidas():
```

Ao executar:

```bash
pytest
```

O teste falhou porque a funcionalidade ainda não estava implementada.

Resultado:

```text
FAILED
```

---

## GREEN

Foi implementada a lógica mínima:

```python
if not user:
    raise HTTPException(
        status_code=401,
        detail="Invalid credentials"
    )
```

Após a implementação:

```bash
pytest
```

Resultado:

```text
3 passed
```

---

## REFACTOR

### Antes

```python
if not user:
    raise HTTPException(
        status_code=401,
        detail="Invalid credentials"
    )

return {
    "user_id": user.id,
    "name": user.name
}
```

### Depois

```python
return {
    "user_id": user.id,
    "name": user.name
}
```

Mantendo a validação em bloco separado e melhorando a legibilidade.

### Melhorias realizadas

* Código mais organizado
* Melhor leitura
* Separação clara entre validação e retorno
* Facilidade para manutenção futura

---

# 4. Refatoração

Foram identificados alguns problemas no código:

### Problema 1

Senhas armazenadas em texto puro.

### Problema 2

Comparação direta da senha.

### Problema 3

Ausência de hash de senha.

### Sugestão

Utilizar:

```python
bcrypt
```

para armazenamento seguro das credenciais.

---

# 5. Execução dos Testes

### Comando

```bash
pytest
```

### Resultado

| Métrica         | Valor |
| --------------- | ----- |
| Total de testes | 3     |
| Passaram        | 3     |
| Falharam        | 0     |

### Evidência

<img width="1020" height="200" alt="WhatsApp Image 2026-06-02 at 14 34 13" src="https://github.com/user-attachments/assets/54071164-c287-4c26-90ac-a8df688e1651" />


---

# 6. Reflexão

### Foi difícil escrever testes antes do código?

Não. Os testes ajudaram a definir claramente o comportamento esperado da funcionalidade.

### O TDD ajudou no desenvolvimento?

Sim. O desenvolvimento foi guiado pelos requisitos da regra de negócio, reduzindo retrabalho.

### Os testes aumentaram a confiança no código?

Sim. Qualquer alteração futura poderá ser validada automaticamente pelos testes.

### O que melhorariam?

Adicionar testes para campos vazios, e-mails inválidos e integração com autenticação real utilizando hash de senha.

### Como isso ajuda no projeto do grupo?

Os testes automatizados reduzem regressões, aumentam a qualidade do software e tornam a manutenção do sistema LocalEats mais segura e previsível.
