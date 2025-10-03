def calcula_imposto_renda(salario: float) -> float:
    if salario <= 2112.00:
        aliquota = 0.00
        deducao = 0.00
    elif salario <= 2826.65:
        aliquota = 0.075  
        deducao = 158.40
    elif salario <= 3751.05:
        aliquota = 0.15   
        deducao = 370.40
    elif salario <= 4664.68:
        aliquota = 0.225 
        deducao = 651.73
    else: 
        aliquota = 0.275
        deducao = 884.96
    imposto_devido = (salario * aliquota) - deducao    
    return max(0.00, imposto_devido)

try:
    salario_bruto_str = input("digite o valor do salário bruto: ")
    salario_bruto = float(salario_bruto_str.replace(',', '.'))
    imposto = calcula_imposto_renda(salario_bruto)
    print(f"salário bruto: R$ {salario_bruto:.2f}")
    print(f"Imposto de renda devido: R$ {imposto:.2f}")

except ValueError:
    print("\ninsira um valor numérico válido para o salário.")
except Exception as e:
    print(f"\nocorreu um erro: {e}")
