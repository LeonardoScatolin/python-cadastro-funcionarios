from Funcionario import Funcionario


def novo_funcionario():
    nome = input("Digite o nome do funcionário: ")
    idade = int(input("Digite a idade do funcionário: "))
    endereco = input("Digite o endereço do funcionário: ")
    telefone = input("Digite o telefone do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    salario = float(input("Digite o salário do funcioário: "))

    return Funcionario(nome, idade, endereco, telefone, cargo, salario)


def exibir_lista_funcionarios(resultados):
    if resultados:
        print("Lista de Funcionários:")
        print("-" * 150)

        for result in resultados:
            id, nome, idade, endereco, telefone, cargo, salario = result
            salario_formatado = "{:.2f}".format(salario)
            print(
                f"ID - {id} | NOME - {nome} | IDADE - {idade} | ENDERECO - {endereco} | TELEFONE - {telefone} | CARGO - {cargo} | SALÁRIO - R$ {salario_formatado}")
        print("-" * 150)
    else:
        print("Nenhum funcionário cadastrado.")
