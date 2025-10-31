# ⚙️ SmartStock - Controle de Estoque de Insumos

O **SmartStock ** é um sistema de **controle de consumo de insumos** desenvolvido com o objetivo de **otimizar o consumo diário**, evitando **faltas e excessos**, garantindo **custo mínimo total** para insumos como reagentes e materiais descartáveis.

---

## ✅ Objetivo

Determinar a **política ótima de consumo diário** para um insumo, considerando:

- Estoque inicial disponível  
- Estoque ideal desejado  
- Consumo diário médio  

O sistema utiliza três abordagens:

- 🧩 **Versão Recursiva (Top-Down)**  
- 💾 **Versão Recursiva com Memoização (Top-Down com cache)**  
- 📊 **Versão Iterativa (Bottom-Up)**  

Todas as versões retornam **o mesmo resultado**, garantindo **consistência do modelo**.

---

## 🧱 Estrutura do Problema

Cada insumo é descrito por:

```python
insumo = {
    "nome": "Luvas descartaveis",
    "estoque_inicial": 10,
    "estoque_ideal": 10,
    "consumo_diario": 3,
    "dias_planejados": 7
}
```

O modelo avalia **quantos itens consumir por dia** para minimizar o custo de falta ou excesso.

---

## 📌 Formulação do Problema

### 🔹 Estados
O **estado** é definido pelo **dia atual** e pelo **estoque restante**:

```
estado = (dia, estoque_atual)
```

### 🔹 Decisões
A **decisão** consiste em **quanto consumir** do insumo no dia, escolhendo entre:

```
decisoes(consumo_ideal) = [consumo_ideal-1, consumo_ideal, consumo_ideal+1]
```

- Garante decisões realistas e não negativas.
- Permite flexibilidade no consumo diário.

### 🔹 Função de Transição
Atualiza o estado após cada decisão:

```
estoque_proximo = estoque_atual - consumo_dia
```

### 🔹 Função Objetivo
Minimizar o **custo total acumulado**, definido como:

- **Custo por falta**: quantidade negativa × 8  
- **Custo por excesso**: quantidade acima do ideal × 2  

```
Custo total = Σ custo_diario
```

---

## 💡 Estruturas e Algoritmos Aplicados

| Conceito / Estrutura                 | Aplicação no Contexto do Problema                                                                 |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| **Programação Dinâmica**            | Otimiza o consumo diário, considerando todas as combinações possíveis de decisões                   |
| **Versão Recursiva (Top-Down)**     | Resolve o problema recursivamente, explorando todas as decisões possíveis                          |
| **Versão Recursiva com Memoização** | Usa `lru_cache` para armazenar subproblemas já resolvidos, evitando recomputações                  |
| **Versão Iterativa (Bottom-Up)**    | Constrói tabela `dp[dia][estoque]` do menor para o maior caso, garantindo maior eficiência         |
| **Função de Custo Dinâmico**        | Penaliza faltas e excessos com valores fixos, calculando o custo diário total                      |
| **Comparação de Resultados**        | Verifica consistência entre as três abordagens                                                   |
| **Execução via Loop/Print**         | Permite simular a política ótima e visualizar o custo mínimo                                       |

---

## 🔁 Funcionamento das Versões

### 🧩 1. Versão Recursiva
- Define o problema de forma recursiva.  
- Explora todas as combinações de decisões para cada dia.  
- Retorna o **custo mínimo total**.

📘 *Uso*: mais simples, porem menos eficiente.

---

### 💾 2. Versão Recursiva com Memoização
- Igual à versão recursiva, mas armazena subproblemas já resolvidos com `@lru_cache`.  
- Evita recalcular estados repetidos, **reduzindo tempo de execução**.

📘 *Uso*: mantém clareza recursiva, mas mais eficiente.

---

### 📊 3. Versão Iterativa (Bottom-Up)
- Cria tabela `dp[dia][estoque]` com todos os custos possíveis.  
- Preenche a tabela do **último dia para o primeiro**.  
- Retorna o **menor custo total** para o estoque inicial.

📘 *Uso*: mais eficiente em tempo e memória, ideal para volumes maiores.

---

## 🧠 Exemplo de Resultado

Simulação de consumo diário:

```text
Insumo: Luvas descartaveis
Estoque inicial: 10 | Consumo diário ideal: 3

Recursiva: 0
Recursiva memoizada: 0
Iterativa (Bottom-Up): 0

Todas as versões deram o mesmo resultado
```

- Indica **política ótima encontrada**.  
- Todas as versões retornam o **mesmo custo mínimo**, garantindo consistência.

---

## 🧮 Comparação de Desempenho

| Versão | Tipo de Execução | Tempo de Execução | Uso de Memória | Facilidade de Entendimento |
|--------|------------------|-----------------|----------------|-----------------------------|
| Recursiva | Top-Down (sem cache) | ❌ Alto | ⚙️ Baixo | ✅ Alta |
| Memoização | Top-Down (com cache) | ⚡ Médio | 💾 Médio | ✅ Alta |
| Iterativa | Bottom-Up | 🚀 Baixo | 💽 Alto | ⚙️ Média |

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**  
- Estruturas nativas (`list`, `dict`)  
- Biblioteca **functools** para `lru_cache`  
- Execução via terminal  

---

## 📄 Boas Práticas Aplicadas

- Código modular e comentado  
- Nomes claros para funções e variáveis  
- Separação entre **modelo matemático** e **execução**  
- Garantia de **resultados equivalentes** entre versões  
- Uso de **valores constantes para custos**, mantendo consistência

---

## 🧪 Como Executar

1. Certifique-se de ter Python 3.x instalado:
```bash
python --version
```

2. Execute o script:
```bash
python smartstock.py
```

3. Observe os resultados no terminal:
- Custo mínimo total  
- Comparação entre recursiva, memoizada e iterativa  

---

> Desenvolvido com 💡 por:  
- **Luiz Felipe Coelho Ramos** | RM: 5550774  
- **Vitor Musolino Teixeira** | RM: 555012  
- **Fernando Gonzales Alexandre** | RM: 555045  
- **Lucas Catroppa Piratininga Dias** | RM: 555450  
- **Gabriel Guerreiro Escobosa Vallejo** | RM: 554973  

