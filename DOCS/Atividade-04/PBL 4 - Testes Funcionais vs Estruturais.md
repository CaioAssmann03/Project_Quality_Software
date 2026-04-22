# 🧪 Aula 5 – Testes Funcionais vs Estruturais  
**LocalEats**

## 👥 Nome: Caio Assmann    

## 🎯 1. Funcionalidade escolhida  

**Funcionalidade selecionada:**  
Busca de restaurantes  

**Descrição da funcionalidade:**  
Permite que o usuário pesquise restaurantes por nome, tipo de culinária, localização ou faixa de preço, retornando uma lista de resultados relevantes.

**O que o usuário espera:**  
- Encontrar rapidamente restaurantes relacionados à busca  
- Ver resultados corretos e atualizados  
- Aplicar filtros corretamente  
- Não receber erros ou resultados irrelevantes  

---

## 🔍 2. Testes Caixa-Preta (Visão do Usuário)  

**Quais testes vocês fariam sem conhecer o código?**

### 🔹 Cenários de teste  

**Cenário 1:**  
Buscar por nome de restaurante existente  
→ Esperado: restaurante aparece na lista  

**Cenário 2:**  
Buscar por tipo de culinária (ex: “italiana”)  
→ Esperado: lista com restaurantes desse tipo  

**Cenário 3:**  
Buscar com campo vazio  
→ Esperado: mensagem de erro ou lista padrão  

**Cenário 4:**  
Buscar por algo inexistente  
→ Esperado: mensagem “nenhum resultado encontrado”  

---

### 🔹 Possíveis erros identificados  
- Resultados não relacionados à busca  
- Busca não retorna resultados existentes  
- Filtros não funcionam corretamente  
- Sistema não trata buscas vazias  
- Lentidão ou travamento  

---

## 🔧 3. Testes Caixa-Branca (Visão do Sistema)  

**Como essa funcionalidade poderia estar implementada internamente?**

### 🔹 Lógica hipotética (pseudo-código ou descrição)  
