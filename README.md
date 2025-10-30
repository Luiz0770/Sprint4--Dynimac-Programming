# ⚙️ SmartStock PD - Otimização do Consumo de Insumos com Programação Dinâmica

O **SmartStock PD** é uma extensão do projeto *SmartStock*, desenvolvida com foco em **modelagem matemática e otimização via Programação Dinâmica (PD)**.  
O sistema busca aprimorar o **controle de consumo de insumos em unidades de diagnóstico**, garantindo **previsão eficiente de reposição**, **redução de desperdícios** e **melhor visibilidade do uso de reagentes e descartáveis**.

---

## ✅ Objetivo

Modelar e resolver o problema do consumo diário de insumos utilizando **Programação Dinâmica**, com três abordagens distintas:

- 🧩 **Versão Recursiva**  
- 💾 **Versão com Memorização (Top-Down)**  
- 📊 **Versão Iterativa (Bottom-Up)**  

Todas as versões garantem **os mesmos resultados**, demonstrando a equivalência das abordagens e permitindo comparar **eficiência e desempenho**.

---

## 🧱 Estrutura do Problema

Cada insumo é representado por sua **quantidade disponível**, **consumo médio diário** e **estoque ideal desejado**.  
O objetivo é determinar o **consumo ótimo diário**, evitando falta ou excesso de produtos.

```python
estoque = {
    "Reagente A": {"estoque_atual": 50, "consumo_medio": 5, "estoque_ideal": 60},
    "Reagente B": {"estoque_atual": 20, "consumo_medio": 4, "estoque_ideal": 25},
    "Descartável C": {"estoque_atual": 15, "consumo_medio": 2, "estoque_ideal": 20}
}
```

---

## 📌 Formulação do Problema

### 🔹 Estados
O **estado** é definido pelo **dia** e pela **quantidade restante** de cada insumo:  
`estado = (dia, quantidade_restante)`

### 🔹 Decisões
A **decisão** consiste em **quanto consumir** de um insumo no dia.  
`decisao = consumo_dia`

### 🔹 Função de Transição
Após cada decisão, o sistema atualiza o estado:
```
quantidade_restante' = quantidade_restante - consumo_dia
```

### 🔹 Função Objetivo
Minimizar o **custo total** (diferença entre estoque real e ideal), evitando desperdícios e rupturas:
```
Custo total = |estoque_final - estoque_ideal|
```

---

## 💡 Estruturas e Algoritmos Aplicados

| Conceito / Estrutura                 | Aplicação no Contexto do Problema                                                                 |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| **Programação Dinâmica**            | Modela o problema de decisão diária de consumo, otimizando o custo final                           |
| **Versão Recursiva**                | Resolve o problema dividindo em subproblemas menores, explorando todas as combinações possíveis     |
| **Versão com Memorização (Top-Down)**| Armazena resultados já calculados para evitar recomputações redundantes                             |
| **Versão Iterativa (Bottom-Up)**    | Constrói a solução do zero até o resultado final utilizando tabela de resultados parciais           |
| **Função de Custo Dinâmico**        | Calcula a diferença entre consumo real e estoque ideal, penalizando decisões ineficientes           |
| **Comparação de Resultados**        | Garante que as três versões retornem o mesmo resultado ótimo                                        |
| **Visualização via Print/Loop**     | Mostra o custo ótimo e os estados percorridos                                                      |

---

## 🔁 Funcionamento das Versões

### 🧩 1. Versão Recursiva
Implementa a lógica clássica de PD:
- Define o problema de forma recursiva.
- Chama a si mesma para subproblemas menores.
- Possui maior custo computacional.

📘 *Uso*: ideal para entender a estrutura conceitual do problema.

---

### 💾 2. Versão com Memorização (Top-Down)
Aproveita a versão recursiva, mas adiciona um **cache (`memo`)**:
- Armazena resultados já resolvidos.
- Evita cálculos repetidos.
- Reduz exponencialmente o tempo de execução.

📘 *Uso*: melhora a eficiência mantendo a clareza da recursão.

---

### 📊 3. Versão Iterativa (Bottom-Up)
Usa **tabelas** para resolver o problema do menor caso ao maior:
- Itera sobre dias e quantidades.
- Constrói progressivamente o resultado final.
- É a forma **mais eficiente** em tempo e memória.

📘 *Uso*: ideal para grandes volumes de dados e aplicações reais.

---

## 🧠 Exemplo de Resultado

Ao simular o consumo diário de insumos, o sistema calcula o **custo mínimo total** e **determina a política ótima de consumo**:

```
=== Consumo ótimo ===
Custo mínimo: 10 unidades
Estratégia ótima: consumir 5 unidades/dia de Reagente A, 2 unidades/dia de Descartável C
```

E as três abordagens (recursiva, top-down e bottom-up) retornam o mesmo resultado, garantindo consistência do modelo.

---

## 🧮 Comparação de Desempenho

| Versão | Tipo de Execução | Tempo de Execução | Uso de Memória | Facilidade de Entendimento |
|--------|------------------|-------------------|----------------|-----------------------------|
| Recursiva | Top-Down (sem cache) | ❌ Alta | ⚙️ Baixo | ✅ Alta |
| Memorização | Top-Down (com cache) | ⚡ Média | 💾 Média | ✅ Alta |
| Iterativa | Bottom-Up | 🚀 Baixa | 💽 Alta | ⚙️ Média |

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- Estruturas nativas (`dict`, `list`)
- Nenhuma biblioteca externa
- Execução via terminal

---

## 📄 Boas Práticas Aplicadas

- Código limpo, modular e comentado  
- Nomes claros para funções e variáveis  
- Separação entre **modelo matemático** e **execução**  
- Garantia de **resultados equivalentes** entre versões  
- Uso de **tipagem e retornos consistentes**

---

## 🧪 Como Executar

1. Certifique-se de ter o Python 3.x instalado:
   ```bash
   python --version
   ```

2. Execute o script:
   ```bash
   python smartstock_pd.py
   ```

3. Observe o resultado no terminal:
   - Consumo ótimo por insumo  
   - Custo total mínimo  
   - Comparação entre versões recursiva, memorizada e iterativa  

---

## 📌 Observações Finais

O projeto **SmartStock PD** demonstra o uso prático da **Programação Dinâmica** em um **problema real de gestão de estoque**, unindo **conceitos matemáticos e implementação em Python**.  

O modelo pode ser expandido para:
- Incluir múltiplos períodos (dias, semanas)
- Inserir custos de pedido e transporte
- Utilizar heurísticas de previsão de demanda
- Integrar com o sistema SmartStock original

---

> Desenvolvido com 💡 por:  
- **Luiz Felipe Coelho Ramos** | RM: 5550774  
- **Vitor Musolino Teixeira** | RM: 555012  
- **Fernando Gonzales Alexandre** | RM: 555045  
- **Lucas Catroppa Piratininga Dias** | RM: 555450  
- **Gabriel Guerreiro Escobosa Vallejo** | RM: 554973  
