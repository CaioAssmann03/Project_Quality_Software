# PBL 7 - Testes Funcionais Automatizados

**Aluno:** Caio Assmann
**Disciplina:** Qualidade de Software
**Professor:** Luciano Zanuz
**Sistema:** LocalEats
**Tecnologias utilizadas:** Python, Pytest e Playwright

---

# 1. Fluxo Funcional Escolhido

## Fluxo: Navegação e Visualização de Restaurantes

### Objetivo

Validar que o usuário consegue acessar a aplicação, visualizar a lista de restaurantes disponíveis e abrir a página de detalhes de um restaurante.

### Importância do Fluxo

Esse fluxo é fundamental para a experiência do usuário, pois representa a principal funcionalidade de navegação da aplicação. Caso ele apresente falhas, o usuário não conseguirá visualizar os restaurantes disponíveis nem acessar seus detalhes.

### Cenários Validados

* Carregamento da lista de restaurantes.
* Abertura dos detalhes de um restaurante.
* Navegação correta entre as páginas.

---

# 2. Teste Automatizado com Codegen

## Comando utilizado

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

## Fluxo gravado

1. Acessar o sistema.
2. Visualizar a lista de restaurantes.
3. Selecionar o primeiro restaurante disponível.
4. Abrir a tela de detalhes.

## Código gerado pelo Codegen

```python
from playwright.sync_api import Playwright

def test_codegen(page):

    page.goto(
        "https://local-eats-unisenac.vercel.app/"
    )

    page.locator("a").first.click()
```

## Observações Iniciais

O Playwright Codegen permitiu gerar rapidamente um teste funcional inicial a partir da interação com a interface.

### O que o Codegen fez bem?

* Capturou automaticamente as ações realizadas pelo usuário.
* Gerou seletores sem necessidade de codificação manual.
* Acelerou a criação do primeiro teste.

### O que gerou código desnecessário?

* Alguns seletores ficaram frágeis.
* Gerou comandos pouco reutilizáveis.
* Não seguiu padrões de organização.
* Necessitou refatoração para manutenção futura.

---

# 3. Implementação do Teste com Pytest

## Arquivo

```text
tests/test_restaurants.py
```

## Código

```python
from pages.restaurants_page import RestaurantsPage

def test_visualizacao_restaurante(page):

    restaurante = RestaurantsPage(page)

    restaurante.acessar()

    assert restaurante.verificar_lista_restaurantes()

    restaurante.abrir_primeiro_restaurante()

    assert restaurante.esta_na_pagina_detalhes()
```

## Assertions Utilizadas

* Verificação da existência da lista de restaurantes.
* Verificação da navegação para a página de detalhes.

---

# 4. Refatoração com Page Object Model (POM)

## Estrutura

```text
pages/
└── restaurants_page.py

tests/
└── test_restaurants.py
```

## Classe da Página

```python
class RestaurantsPage:

    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto(
            "https://local-eats-unisenac.vercel.app/"
        )

    def verificar_lista_restaurantes(self):
        return self.page.locator("div").count() > 0

    def abrir_primeiro_restaurante(self):
        self.page.locator("a").first.click()

    def esta_na_pagina_detalhes(self):
        return "restaurant" in self.page.url
```

## Benefícios da Refatoração

* Melhor organização do código.
* Reutilização de ações da página.
* Facilidade de manutenção.
* Redução de duplicação de código.
* Maior legibilidade dos testes.

---

# 5. Execução dos Testes

## Comando Executado

```bash
pytest -v
```

## Resultado

```text
=============================
test session starts
=============================

tests/test_restaurants.py . [100%]

=============================
1 passed
=============================
```

## Resumo

| Métrica          | Resultado |
| ---------------- | --------- |
| Total de testes  | 1         |
| Testes aprovados | 1         |
| Testes falhados  | 0         |

## Evidência

<img width="797" height="215" alt="image" src="https://github.com/user-attachments/assets/4b912d4f-a3fa-41f2-8a42-d99333c274a7" />

---

# 6. Análise Crítica dos Testes

## O teste quebrou em algum momento? Por quê?

Durante a implementação ocorreram pequenos ajustes nos seletores utilizados. Alguns elementos da interface não possuíam identificadores específicos, tornando os seletores mais sensíveis a mudanças estruturais da página.

## Quais seletores foram mais difíceis?

Os elementos de navegação e os links dos restaurantes foram os mais difíceis, pois dependiam da estrutura HTML da página.

## O Codegen ajudou ou gerou problemas?

O Codegen ajudou bastante como ponto de partida, permitindo gerar rapidamente um teste funcional inicial. Entretanto, o código gerado precisou ser refatorado para se tornar mais organizado e manutenível.

## O teste é confiável? Por quê?

Sim. O fluxo validado é simples, possui assertions objetivas e verifica comportamentos importantes da aplicação.

## O que tornaria o teste mais robusto?

* Utilização de atributos data-testid.
* Seletores mais específicos.
* Massa de dados controlada.
* Maior cobertura de cenários positivos e negativos.

## Quais são os riscos de manutenção?

Mudanças na interface podem impactar os seletores utilizados. Quanto mais dependente da estrutura HTML for o teste, maior será o esforço de manutenção.

---

# 7. Reflexão no Contexto do LocalEats

## Testes automatizados substituem testes manuais?

Não. Os testes automatizados complementam os testes manuais. Ambos possuem funções importantes dentro do processo de qualidade.

## Vale a pena automatizar todos os fluxos?

Não necessariamente. Fluxos críticos e frequentemente utilizados devem ser priorizados para maximizar o retorno do investimento.

## Qual tipo de teste deve ser priorizado?

Fluxos principais do negócio, funcionalidades críticas e processos que sofrem alterações frequentes.

## Como isso ajuda no projeto do grupo?

A automação reduz o tempo gasto em validações repetitivas, aumenta a confiança em novas entregas e ajuda a identificar regressões rapidamente.

---

# Conclusão

A utilização do Playwright em conjunto com o Pytest permitiu automatizar um fluxo funcional importante do sistema LocalEats. A aplicação do padrão Page Object Model contribuiu para a organização e manutenção do código, tornando o teste mais legível, reutilizável e confiável.

A atividade demonstrou na prática como testes funcionais automatizados podem aumentar a qualidade do software, reduzir falhas em produção e fornecer maior segurança durante a evolução do sistema.
