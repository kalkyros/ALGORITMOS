def calcular_aumento_salarial(salario_atual: float) -> tuple[float, float]:
    if salario_atual <= 2800.00:
        percentual_aumento = 0.20
    elif salario_atual <= 7000.00:
        percentual_aumento = 0.15
    elif salario_atual <= 15000.00:
        percentual_aumento = 0.10
    else:
        percentual_aumento = 0.05
    valor_do_aumento = salario_atual * percentual_aumento
    novo_salario = salario_atual + valor_do_aumento
    return valor_do_aumento, novo_salario, percentual_aumento

try:   
    salario_str = input("digite o salário atual do programador: ")
    salario_atual = float(salario_str.replace(',', '.'))
    if salario_atual < 0:
        print("o salário deve ter um valor positivo.")
    else:
        valor_do_aumento, novo_salario, percentual_aumento = calcular_aumento_salarial(salario_atual)
        print(f"salário atual: R$ {salario_atual:,.2f}".replace(',', '_').replace('.', ',').replace('_', '.'))
        print(f"percentual de aumento: {percentual_aumento * 100:.0f}%")
        print(f"valor do aumento: R$ {valor_do_aumento:,.2f}".replace(',', '_').replace('.', ',').replace('_', '.'))
        print(f"novo salário: R$ {novo_salario:,.2f}".replace(',', '_').replace('.', ',').replace('_', '.'))

except ValueError:
    print("\ninsira um valor numérico válido para o salário.")
except Exception as e:
    print(f"\nocorreu um erro inesperado: {e}")