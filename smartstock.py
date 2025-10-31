from functools import lru_cache

# Função: calcular custo diário
def calcular_custo(estoque, ideal):
    # Define os custos extras (valores fictícios para o exemplo)
    custo_falta = 8   
    custo_excesso = 2  
    
    if estoque < 0:
        return (-estoque) * custo_falta 
    elif estoque > ideal:
        return (estoque - ideal) * custo_excesso
    return 0  # estoque ideal

# Função: gera decisões possíveis de consumo
def decisoes(consumo_ideal):
    consumir_menos = consumo_ideal - 1
    if consumir_menos < 0:
        consumir_menos = 0 
    consumir_ideal = consumo_ideal
    consumir_mais = consumo_ideal + 1
    lista_decisoes = [consumir_menos, consumir_ideal, consumir_mais]
    return lista_decisoes

# VERSÃO: Recursiva simples
def versao_recursiva(dia, estoque, dias_totais, consumo_ideal, ideal):
    if dia == dias_totais:
        return 0
    # float('inf') representa um valor maior que qualquer outro
    melhor = float('inf')
    for decisao in decisoes(consumo_ideal):
        prox_estoque = estoque - decisao
        custo = calcular_custo(prox_estoque, ideal) + versao_recursiva(dia + 1, prox_estoque, dias_totais, consumo_ideal, ideal)
        if custo < melhor:
            melhor = custo
    return melhor

# VERSÃO: Recursiva com memoização
@lru_cache(maxsize=None)
def versao_memorizada(dia, estoque, dias_totais, consumo_ideal, ideal):
    if dia == dias_totais:
        return 0
    # float('inf') representa um valor maior que qualquer outro
    melhor = float('inf')
    for dec in decisoes(consumo_ideal):
        prox_estoque = estoque - dec
        custo = calcular_custo(prox_estoque, ideal) + versao_memorizada(dia + 1, prox_estoque, dias_totais, consumo_ideal, ideal)
        if custo < melhor:
            melhor = custo
    return melhor

# VERSÃO: Iterativa (Bottom-Up)
def versao_iterativa(estoque_inicial, dias_totais, consumo_ideal, ideal):
    limite_neg = -ideal * 2
    limite_pos = ideal * 2
    tamanho = limite_pos - limite_neg + 1
    dp = []
    for dia in range(dias_totais + 1):
        linha = []
        for estoque_index in range(tamanho):
            # float('inf') representa um valor maior que qualquer outro
            linha.append(float('inf'))
        dp.append(linha)
    
    # Último dia, custo zero
    for i in range(tamanho):
        dp[dias_totais][i] = 0
    for dia in range(dias_totais - 1, -1, -1):
        for estoque_index in range(tamanho):
            estoque = estoque_index + limite_neg
            for dec in decisoes(consumo_ideal):
                prox_estoque = estoque - dec
                custo_dia = calcular_custo(prox_estoque, ideal)
                prox_index = prox_estoque - limite_neg
                if 0 <= prox_index < tamanho:
                    total = custo_dia + dp[dia + 1][prox_index]
                    if total < dp[dia][estoque_index]:
                        dp[dia][estoque_index] = total
    return dp[0][estoque_inicial - limite_neg]


# EXECUÇÃO
while True:
    # Valores de exemplo
    insumo = "Luvas descartaveis"
    estoque_inicial = 10
    estoque_ideal = 10
    consumo_diario = 3
    dias_planejados = 7
    
    print(f"\nInsumo: {insumo}")
    print(f"Estoque inicial: {estoque_inicial} | Consumo diário ideal: {consumo_diario}\n")

    recursiva = versao_recursiva(0, estoque_inicial, dias_planejados, consumo_diario, estoque_ideal)
    memorizada = versao_memorizada(0, estoque_inicial, dias_planejados, consumo_diario, estoque_ideal)
    iterativa = versao_iterativa(estoque_inicial, dias_planejados, consumo_diario, estoque_ideal)

    print(f"Recursiva: {recursiva}")
    print(f"Recursiva memoizada: {memorizada}")
    print(f"Iterativa (Bottom-Up): {iterativa}")

    if recursiva == memorizada == iterativa:
        print("\nTodas as versões deram o mesmo resultado")
    else:
        print("\nAs versões nao deram o mesmo resultado")
    break
