def calcular_media_notas(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

nome_aluno = input("informe o nome do aluno: ")
notas = []
while len(notas) < 5:
    try:
        nota = float(input(f"informe a {len(notas)+1}° nota: "))
        notas.append(nota)
    except ValueError:
        print("insira um número válido.")
media = calcular_media_notas(notas)
print(f"a média das notas de {nome_aluno} é: {media:.2f}")
if media >= 7:      
    print(f"{nome_aluno} foi aprovado.")    
else:
    print(f"{nome_aluno} foi reprovado.")

