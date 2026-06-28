# PBL 10 – Modelos de Maturidade

**Disciplina:** Qualidade de Software

**Projeto:** LocalEats

**Aluno:** Caio Assmann

---

# Objetivo

Esta atividade tem como objetivo avaliar o nível de maturidade do processo de desenvolvimento utilizado pela equipe do projeto **LocalEats**, utilizando como referência os conceitos apresentados pelos modelos **CMMI** e **MPS.BR**.

A análise busca identificar pontos fortes, lacunas existentes e oportunidades de melhoria para aumentar a qualidade do processo de desenvolvimento do software.

---

# 1. Diagnóstico de Maturidade

## Avaliação do Processo

| Critério                                                                             | Sim | Parcial | Não |
| ------------------------------------------------------------------------------------ | :-: | :-----: | :-: |
| Os requisitos são documentados?                                                      |  ✅  |         |     |
| Existe controle de mudanças?                                                         |  ✅  |         |     |
| Há atividades de teste definidas?                                                    |  ✅  |         |     |
| Os defeitos são registrados?                                                         |     |    ✅    |     |
| O processo de desenvolvimento é conhecido por toda a equipe?                         |  ✅  |         |     |
| As tarefas são planejadas e acompanhadas regularmente?                               |     |    ✅    |     |
| Existe padronização para implementação de funcionalidades?                           |  ✅  |         |     |
| Os testes são executados antes da entrega das funcionalidades?                       |  ✅  |         |     |
| Há revisão de código ou validação por outro integrante da equipe?                    |     |    ✅    |     |
| A equipe utiliza ferramentas para gerenciamento das atividades?                      |  ✅  |         |     |
| Os artefatos do projeto (requisitos, testes e código) são organizados e versionados? |  ✅  |         |     |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas?             |     |    ✅    |     |
| A equipe realiza reuniões ou retrospectivas para identificar melhorias?              |     |    ✅    |     |
| Existem indicadores ou métricas para acompanhar a qualidade do projeto?              |     |         |  ❌  |

---

## Classificação do Processo

### Nível de Maturidade

**Definido**

### Justificativa

O processo de desenvolvimento do LocalEats apresenta características de um processo definido, pois existe um fluxo conhecido pela equipe, utilização de controle de versão, documentação das atividades, planejamento das funcionalidades e execução de testes durante o desenvolvimento.

Além disso, foram adotadas práticas como TDD, BDD, testes funcionais automatizados e documentação das PBLs, demonstrando padronização na execução das atividades.

Entretanto, ainda não são utilizadas métricas quantitativas, indicadores de desempenho, integração contínua (CI/CD) ou um processo formal de melhoria contínua, impedindo que o projeto seja classificado em níveis superiores de maturidade.

---

# 2. Lacunas Identificadas

| Lacuna                                                     | Impacto                                                                           |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Ausência de métricas de qualidade                          | Dificulta acompanhar a evolução do projeto e identificar tendências de qualidade. |
| Revisão de código realizada de forma informal              | Aumenta a possibilidade de defeitos chegarem ao repositório principal.            |
| Falta de integração contínua (CI/CD)                       | Os testes dependem da execução manual antes da entrega.                           |
| Rastreabilidade parcial entre requisitos e funcionalidades | Torna mais difícil identificar o impacto de mudanças futuras.                     |
| Pouca utilização de indicadores de desempenho              | Limita a avaliação objetiva da qualidade do processo.                             |

---

# 3. Propostas de Melhoria

| Melhoria                                                                                        | Benefício                                                                          |
| ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Implantar GitHub Actions para execução automática dos testes                                    | Garantia de que novas alterações não quebrem funcionalidades existentes.           |
| Formalizar o processo de Code Review utilizando Pull Requests                                   | Maior qualidade do código e compartilhamento de conhecimento entre os integrantes. |
| Definir indicadores de qualidade (cobertura de testes, defeitos encontrados, tempo de correção) | Permite acompanhar a evolução do processo de forma objetiva.                       |
| Melhorar a rastreabilidade entre requisitos, testes e funcionalidades                           | Facilita manutenção e futuras evoluções do sistema.                                |
| Realizar retrospectivas ao final de cada ciclo de desenvolvimento                               | Promove melhoria contínua do processo de trabalho.                                 |

---

# Relação com os Modelos de Maturidade

Durante o desenvolvimento do LocalEats foram aplicadas diversas práticas relacionadas à qualidade de software, como documentação, testes unitários, testes funcionais automatizados, TDD, BDD e utilização de controle de versão.

Essas práticas demonstram aderência aos princípios presentes nos modelos CMMI e MPS.BR, especialmente no que se refere à padronização dos processos e à preocupação com a qualidade do produto.

No entanto, ainda existem oportunidades de evolução relacionadas ao monitoramento do processo por meio de métricas, automação completa do pipeline de desenvolvimento e institucionalização da melhoria contínua.

---

# Conclusão

A avaliação realizada indica que o processo de desenvolvimento do LocalEats encontra-se em um nível **Definido** de maturidade.

O projeto possui um fluxo organizado, utiliza boas práticas de desenvolvimento e qualidade, além de empregar ferramentas de versionamento e diferentes tipos de testes para validação das funcionalidades.

Apesar disso, ainda há espaço para evolução, principalmente na utilização de métricas, integração contínua, revisões formais de código e acompanhamento sistemático da qualidade do processo.

A adoção dessas melhorias permitirá aumentar a maturidade organizacional da equipe, reduzindo retrabalho, melhorando a confiabilidade do software e tornando o desenvolvimento mais eficiente.
