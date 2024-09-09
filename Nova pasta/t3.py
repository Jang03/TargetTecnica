import json

def carregar_faturamento(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados["faturamento_diario"]

def calcular_faturamento(faturamento_diario):
    valores = [dia["valor"] for dia in faturamento_diario if dia["valor"] > 0]

    if not valores:
        print("Não há faturamentos disponíveis.")
        return
    
    menor_faturamento = min(valores)

    maior_faturamento = max(valores)

    media_mensal = sum(valores) / len(valores)

    dias_acima_da_media = len([valor for valor in valores if valor > media_mensal])

    print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
    print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

caminho_arquivo = 'faturamento.json'

faturamento_diario = carregar_faturamento(caminho_arquivo)

calcular_faturamento(faturamento_diario)
