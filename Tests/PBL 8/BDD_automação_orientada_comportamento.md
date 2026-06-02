# Aula 12 – BDD e Automação Orientada a Comportamento

**Disciplina:** Qualidade de Software
**Professor:** Luciano Zanuz
**Sistema:** LocalEats
**Aluno:** Caio Assmann

---

# 1. Fluxo Escolhido

## Visualização de Restaurantes

### Descrição

O fluxo de visualização de restaurantes permite que o usuário visualize os restaurantes disponíveis na plataforma LocalEats e acesse os detalhes de um restaurante específico.

### Importância

Este fluxo é a base da experiência do usuário dentro do sistema, pois é através dele que os usuários descobrem os restaurantes disponíveis e iniciam sua jornada de compra.

### Problema que resolve

Permite que os usuários encontrem restaurantes disponíveis de forma rápida e intuitiva.

### Regras de comportamento esperadas

* Os restaurantes devem ser exibidos na página inicial.
* A lista de restaurantes deve ser carregada corretamente.
* O usuário deve conseguir acessar os detalhes de um restaurante.
* A navegação deve ocorrer sem erros.

---

# 2. Escrita dos Cenários BDD

## Feature

```gherkin
Feature: Visualização de restaurantes

  Como usuário do LocalEats
  Quero visualizar os restaurantes disponíveis
  Para escolher onde realizar um pedido
```

---

## Cenário 1 – Visualizar lista de restaurantes

```gherkin
Scenario: Visualizar lista de restaurantes

  Given que o usuário acessa a página inicial do LocalEats

  When visualizar os restaurantes disponíveis

  Then a lista de restaurantes deve ser exibida
```

### Objetivo

Validar que a aplicação exibe corretamente os restaurantes disponíveis para o usuário.

---

## Cenário 2 – Acessar detalhes de um restaurante

```gherkin
Scenario: Acessar detalhes de um restaurante

  Given que o usuário acessa a página inicial do LocalEats

  When selecionar um restaurante

  Then os detalhes do restaurante devem ser exibidos
```

### Objetivo

Validar que o usuário consegue acessar a página de detalhes de um restaurante.

---

# 3. Implementação da Automação com pytest-bdd

## Estrutura do Projeto

```text
projeto/
│
├── features/
│   └── visualizacao_restaurantes.feature
│
├── tests/
│   └── test_visualizacao_restaurantes_bdd.py
│
├── pages/
│   └── restaurants_page.py
│
└── evidencias/
```

---

## Arquivo Feature

### visualizacao_restaurantes.feature

```gherkin
Feature: Visualização de restaurantes

  Como usuário do LocalEats
  Quero visualizar os restaurantes disponíveis
  Para escolher onde realizar um pedido

  Scenario: Visualizar lista de restaurantes

    Given que o usuário acessa a página inicial do LocalEats

    When visualizar os restaurantes disponíveis

    Then a lista de restaurantes deve ser exibida

  Scenario: Acessar detalhes de um restaurante

    Given que o usuário acessa a página inicial do LocalEats

    When selecionar um restaurante

    Then os detalhes do restaurante devem ser exibidos
```

---

## Arquivo de Teste

### test_visualizacao_restaurantes_bdd.py

```python
from pytest_bdd import scenarios, given, when, then

from pages.restaurants_page import RestaurantsPage

scenarios("../features/visualizacao_restaurantes.feature")


@given("que o usuário acessa a página inicial do LocalEats")
def acessar_home(page):

    restaurante = RestaurantsPage(page)

    restaurante.acessar()

    page.wait_for_load_state("networkidle")

    return restaurante


@when("visualizar os restaurantes disponíveis")
def visualizar_restaurantes():
    pass


@then("a lista de restaurantes deve ser exibida")
def validar_lista(acessar_home):

    assert acessar_home.verificar_lista_restaurantes()


@when("selecionar um restaurante")
def selecionar_restaurante(acessar_home):

    acessar_home.abrir_primeiro_restaurante()


@then("os detalhes do restaurante devem ser exibidos")
def validar_detalhes(acessar_home):

    assert acessar_home.esta_na_pagina_detalhes()
```

---

# 4. Organização do Projeto

A automação foi organizada utilizando o padrão Page Object Model (POM), já existente no projeto.

### Benefícios

* Separação entre comportamento e implementação.
* Melhor manutenção dos testes.
* Reaproveitamento de código.
* Maior legibilidade.
* Menor acoplamento com a interface.

A estrutura atende às recomendações de organização apresentadas na atividade.

---

# 5. Execução dos Testes

## Comando Executado

```bash
pytest -v
```

## Resultado Obtido

| Métrica           | Quantidade |
| ----------------- | ---------- |
| Total de Cenários | 2          |
| Passaram          | 2          |
| Falharam          | 0          |

### Evidência


<img width="854" height="315" alt="image" src="https://github.com/user-attachments/assets/3b022827-9524-4263-bc5b-d60cd81f53dc" />



---

# 6. Análise Crítica

## O cenário escrito ficou compreensível?

Sim. Os cenários utilizam linguagem próxima ao negócio e podem ser compreendidos por pessoas técnicas e não técnicas.

---

## O teste automatizado ficou legível?

Sim. A estrutura Given-When-Then facilita a leitura e o entendimento do comportamento esperado.

---

## O BDD ajudou a entender o comportamento?

Sim. O foco passou a ser o comportamento esperado pelo usuário e não os detalhes técnicos da implementação.

---

## Quais dificuldades surgiram?

A principal dificuldade foi identificar seletores estáveis para garantir que a automação continue funcionando mesmo após alterações na interface.

---

## Os seletores foram frágeis?

Alguns seletores podem ser impactados por alterações visuais futuras. O uso do padrão Page Object reduz esse problema.

---

## O teste ficou dependente da interface?

Sim. Como se trata de um teste funcional automatizado, existe dependência dos elementos visuais da aplicação.

---

## O cenário representa realmente uma regra de negócio?

Sim. A visualização de restaurantes é um dos principais fluxos de negócio do sistema LocalEats.

---

## O que tornaria o teste mais robusto?

* Utilizar atributos específicos para automação.
* Criar identificadores exclusivos para elementos importantes.
* Adicionar validações adicionais sobre conteúdo exibido.

---

# 7. Reflexão no Contexto do LocalEats

## BDD melhora a comunicação entre a equipe?

Sim. O BDD cria uma linguagem comum entre negócio, desenvolvimento e qualidade.

---

## Todo teste deve ser escrito em BDD?

Não. O BDD é mais indicado para comportamentos importantes de negócio e fluxos relevantes para o usuário.

---

## Quando vale a pena usar BDD?

Quando é necessário alinhar entendimento entre diferentes áreas e documentar comportamentos de forma clara e executável.

---

## O comportamento ficou mais claro?

Sim. A escrita em Gherkin tornou explícito o que o sistema deve fazer sob a perspectiva do usuário.

---

## Como isso ajuda no projeto do grupo?

Ajuda a reduzir ambiguidades, melhora a comunicação da equipe, cria documentação viva e facilita a manutenção dos testes automatizados.

---

# Conclusão

A aplicação do BDD no LocalEats permitiu transformar comportamentos importantes do sistema em cenários compreensíveis e automatizáveis. A integração entre pytest-bdd, Playwright e o padrão Page Object possibilitou a construção de testes organizados, reutilizáveis e alinhados às necessidades do negócio.

Além de validar funcionalidades importantes da aplicação, o BDD contribui para uma melhor comunicação entre todos os envolvidos no desenvolvimento do sistema, tornando os requisitos mais claros e reduzindo riscos de interpretação incorreta.
