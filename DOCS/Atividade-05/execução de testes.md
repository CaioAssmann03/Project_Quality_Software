# Aula 6 – Planejamento e Execução de Testes

> Disciplina: Qualidade de Software  
> Projeto: LocalEats  
> Nome: Caio Assmann
---

# 1. Plano de Testes

## 1.1 Objetivo
Validar as principais funcionalidades do sistema LocalEats, garantindo que apresentem comportamento correto, consistente e sem falhas em cenários comuns de uso.

---

## 1.2 Escopo

### O que será testado
- Login/Cadastro
- Busca de restaurantes
- Avaliação de restaurantes

### O que NÃO será testado
- Integração com sistemas externos
- Performance em larga escala
- Segurança avançada (ex: ataques)

---

## 1.3 Funcionalidades selecionadas

- Login/Cadastro
- Busca de restaurantes
- Avaliação

---

## 1.4 Estratégia de Testes

Descreva como os testes serão realizados.

- Tipos de teste:
  - (X) Funcional
  - (X) Usabilidade
  - ( ) Outros: _______

- Abordagem:
  Testes manuais baseados em cenários previamente definidos, simulando o comportamento real do usuário.

---

## 1.5 Responsáveis

| Nome | Responsabilidade |
|------|----------------|
| Caio Assmann | Planejamento e execução dos testes |
| QA 2| Criação dos casos de teste |
| Dev pleno | Execução e registro de evidências |
| QA | Análise dos resultados |

---

# 2. Casos de Teste

---

## CT-01 – Login com sucesso

**Pré-condição:**  
Usuário cadastrado no sistema

**Passos:**  
1. Acessar a página de login  
2. Informar email e senha válidos  
3. Clicar em entrar  

**Dados de entrada:**  
Email válido e senha correta  

**Resultado esperado:**  
Usuário é redirecionado para a página inicial logado  

---

## CT-02 – Login com senha incorreta

**Pré-condição:**  
Usuário cadastrado

**Passos:**  
1. Acessar a página de login  
2. Informar email válido  
3. Informar senha incorreta  
4. Clicar em entrar  

**Dados de entrada:**  
Email válido e senha errada  

**Resultado esperado:**  
Sistema exibe mensagem de erro e não realiza login  

---

## CT-03 – Busca de restaurante existente

**Pré-condição:**  
Sistema com restaurantes cadastrados

**Passos:**  
1. Acessar a busca  
2. Digitar nome de restaurante existente  
3. Confirmar busca  

**Dados de entrada:**  
Nome válido  

**Resultado esperado:**  
Lista de restaurantes correspondente à busca  

---

## CT-04 – Busca sem resultados

**Pré-condição:**  
Sistema ativo

**Passos:**  
1. Acessar a busca  
2. Digitar termo inexistente  
3. Confirmar busca  

**Dados de entrada:**  
Texto inexistente  

**Resultado esperado:**  
Sistema exibe mensagem “nenhum resultado encontrado”  

---

## CT-05 – Avaliação de restaurante com sucesso

**Pré-condição:**  
Usuário logado

**Passos:**  
1. Acessar um restaurante  
2. Selecionar nota  
3. Enviar avaliação  

**Dados de entrada:**  
Nota e comentário  

**Resultado esperado:**  
Avaliação registrada com sucesso  

---

# 3. Execução dos Testes

| ID     | Resultado (Passou/Falhou) | Evidência (descrição ou print) |
|--------|--------------------------|--------------------------------|
| CT-01  | Passou                   | Login realizado com sucesso     |
| CT-02  | Passou                   | Mensagem de erro exibida        |
| CT-03  | Falhou                   | Resultados incorretos           |
| CT-04  | Passou                   | Mensagem exibida corretamente   |
| CT-05  | Falhou                   | Avaliação não foi salva         |

---

# 4. Análise dos Resultados

- Quantidade de testes executados: 5  
- Quantidade de testes que passaram: 3  
- Quantidade de testes que falharam: 2  

## Principais problemas encontrados
- Busca retornando resultados incorretos  
- Falha ao salvar avaliação  
- Inconsistência em algumas funcionalidades  

---

# 5. Reflexão

- O plano de testes ajudou a organizar melhor o processo? Por quê?  
Sim, pois permitiu estruturar os testes de forma clara, definindo o que testar, como testar e quem seria responsável por cada etapa.

- Algum problema só foi identificado durante a execução? Explique.  
Sim, o erro na avaliação só foi percebido durante a execução prática, pois não era evidente apenas na análise teórica.

- O que o grupo melhoraria no processo de testes?  
Melhor definição de cenários, inclusão de mais casos de erro e uso de testes automatizados no futuro.

---

## Conclusão

O comportamento das funcionalidades foi parcialmente aceitável, pois algumas funcionaram corretamente, mas erros críticos foram identificados, especialmente na busca e avaliação.

---

# 6. Conclusão Geral

- Qualidade geral do sistema testado: Regular  
- Principais pontos positivos:
  - Login funcional  
  - Mensagens de erro bem definidas  

- Principais problemas identificados:
  - Falhas na busca  
  - Problemas ao salvar avaliação  

- Impressão geral sobre o processo de testes:
O processo foi essencial para identificar falhas reais do sistema e demonstrou a importância de testes bem planejados e executados.
