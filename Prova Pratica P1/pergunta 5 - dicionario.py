funcionarios = {}

def cadastrar_funcionario():   
    nome = input("digite o nome do funcionário: ").strip().title()
    if nome in funcionarios:
        print(f"\no funcionário '{nome}' já está cadastrado.")
        return

    while True:
        try:
            salario_str = input("digite o salário: ").replace(',', '.')
            salario = float(salario_str)
            if salario < 0:
                raise ValueError
            break
        except ValueError:
            print("digite um valor numérico positivo para o salário.")
            
    cargo = input("digite o cargo do funcionário: ").strip().title()

    funcionarios[nome] = {
        'salario': salario,
        'cargo': cargo
    }
    print(f"\nfuncionário '{nome}' cadastrado com sucesso!")
    input("\n[ P R E S S  E N T E R ]")

def consultar_funcionario():
    nome_consulta = input("digite o nome do funcionário que deseja consultar: ").strip().title()

    if nome_consulta in funcionarios:
        dados = funcionarios[nome_consulta]
        salario_formatado = f"R$ {dados['salario']:,.2f}".replace(',', '_').replace('.', ',').replace('_', '.')
        
        print(f"\ninformações de {nome_consulta}:")
        print(f"  cargo: {dados['cargo']}")
        print(f"  salário: {salario_formatado}")
        input("\n[ P R E S S  E N T E R ]")
    else:
        print(f"\nfuncionário '{nome_consulta}' não encontrado no cadastro.")
        input("\n[ P R E S S  E N T E R ]")

def listar_funcionarios():
    if not funcionarios:
        print("nenhum funcionário cadastrado.")
        return
    for nome, dados in funcionarios.items():
        salario_formatado = f"R$ {dados['salario']:,.2f}".replace(',', '_').replace('.', ',').replace('_', '.')
        print(f"\nNome: {nome} | Cargo: {dados['cargo']} | Salário: {salario_formatado}")
        input("\n[ P R E S S  E N T E R ]")

def menu_principal():

    while True:
        print("\n" + "="*40)
        print("gerenciamento de funcionarios")
        print("="*40)
        print("1 - cadastrar novo funcionário")
        print("2 - consultar funcionário por nome")
        print("3 - listar todos os funcionários")
        print("4 - sair")
        
        opcao = input("escolha uma opção: ")

        if opcao == '1':
            cadastrar_funcionario()
        elif opcao == '2':
            consultar_funcionario()
        elif opcao == '3':
            listar_funcionarios()
        elif opcao == '4':
            print("\nencerrando o programa.")
            input("\n[ P R E S S  E N T E R ]")
            break
        else:
            print("\nopção inválida. tente novamente.")
            input("\n[ P R E S S  E N T E R ]")


menu_principal()