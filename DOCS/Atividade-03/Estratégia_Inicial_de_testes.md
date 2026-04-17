# Estratégia Inicial de Testes – LocalEats

## 1. Funcionalidades
- Login
- Busquem restaurantes por tipo de culinária, localização e faixa de preço
- Visualizem cardápios, fotos e avaliações
- Salvem locais favoritos
- Recebam recomendações personalizadas
- Compartilhem experiências


---

## 2. Níveis de Teste

### Funcionalidade: Login
- Unitário: validar senha e campos obrigatórios
- Integração: verificar comunicação com banco
- Sistema: usuário faz login completo
- Aceitação: usuário entra no sistema sem erro

### Funcionalidade: Campo de Busca 
- Unitário: Testar se o campo de busca retorna resultados corretos ao inserir um termo específico
- Integração: Verificar se o campo de busca se comunica corretamente com o banco de dados e retorna os restaurantes conforme filtros aplicados (tipo, localização e preço)
- Sistema: Testar o funcionamento completo da busca dentro da aplicação, incluindo exibição de resultados, navegação e performance
- Aceitação: Validar se a busca atende às expectativas do usuário, retornando resultados relevantes de forma rápida e fácil de usar

Funcionalidade: Visualizar cardápios, fotos e avaliações
- Unitário: Testar se os dados (cardápio, fotos e avaliações) são exibidos corretamente na interface
- Integração: Verificar se as informações são carregadas corretamente do banco de dados ou API
- Sistema: Testar o fluxo completo de visualização, desde a seleção do restaurante até a exibição dos detalhes
- Aceitação: Validar se o usuário consegue visualizar facilmente as informações e se elas são claras e completas

Funcionalidade: Salvar locais favoritos
- Unitário: Testar se os locais selecionados como favorito ficam salvos
- Integração: Verificar se as informações dos favoritos estão carregando corretamente no banco de dados
- Sistema: Testar o fluxo completo de favoritar e desfavoritar um local e verificar se aparece na aba de favoritos
- Aceitação: Validar se o usuário consegue visualizar facilmente as informações e se elas são claras e completas

Funcionalidade: Receber recomendações personalizadas
- Unitário: Testar se o sistema gera recomendações com base em critérios definidos
- Integração: Verificar se o sistema utiliza corretamente os dados do usuário (histórico, preferências)
- Sistema: Testar o funcionamento completo das recomendações dentro da aplicação
- Aceitação: Validar se as recomendações são relevantes e úteis para o usuário

Funcionalidade: Compartilhar experiências
- Unitário: Testar se o usuário consegue escrever e enviar uma avaliação
- Integração: Verificar se a avaliação é salva corretamente no sistema
- Sistema: Testar o fluxo completo de envio e exibição das avaliações
- Aceitação: Validar se o processo de compartilhamento é simples e se as avaliações aparecem corretamente para outros usuários


---

## 3. Prioridades e Riscos

Alta prioridade:
- Login -> sem login o usuário não usa o sistema
- Busca -> Sem o funcionamento de busca os clientes não encontram os restaurantes que preferem
- Visualização -> Visualizar os cardapios é de extrema importância para o cliente

Justificativa:
Sem essas 3 prioridades o sistema não fornece o minímo para o cliente se interessar na plataforma

Baixa prioridade: 
- Favoritos -> não impede uso
- Compartilhar -> Não compartilhar as expêriencias não atrapalha o uso dos clientes
- Recomendação -> É importante a recomendação, mas de baixa prioridade no momento

Justificativa:
Os itens em baixa prioridade são ótimos benefícios, mas não são obrigatórios para o funcionamento da plataforma.

---

## 4. Pirâmide de Testes

- Maior foco: Login , Busca e visualização
- Médio foco: Recomendação,  Compartilhar
- Menor foco: Favoritos

Justificativa:
O critério de prioridade se baseia no quanto a funcionalidade é importante para o funcionamento da plataforma.

---
## 5. Testes em Produção

- Uso de monitoramento para identificar erros em tempo real (logs e métricas)
- Aplicar testes A/B para validar melhorias e novas funcionalidades

Justificativa:
Os testes em produção são importantes para identificar problemas reais que não aparecem em ambiente de desenvolvimento.
O monitoramento permite detectar falhas rapidamente, enquanto os testes A/B ajudam a avaliar mudanças com base no comportamento dos usuários, garantindo melhorias contínuas na qualidade do sistema.


## 6. Melhoria
- Garantir compatibilidade entre dispositivos
- Padronizar comportamento entre web e mobile
