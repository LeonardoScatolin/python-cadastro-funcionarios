import mysql.connector

import Utils
from Utils import novo_funcionario
from decimal import Decimal

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="funcionarios"
)

mycursor = mydb.cursor()

while True:
    print("""
==================================
--- CADASTRAR NOVO FUNCIONÁRIO ---
0 - ENCERRAR
1 - CADASTRAR FUNCIONÁRIO
2 - AUMENTAR SALÁRIO DE UM FUNCIONÁRIO
3 - EXIBIR TODOS OS FUNCIONÁRIOS
4 - EXCLUIR FUNCIONÁRIO
==================================
    """)
    opc = int(input("Selecione sua opção: "))

    if opc == 0:
        break

    elif opc == 1:
        funcionario = novo_funcionario()

        sql = "INSERT INTO funcionarios (nome, idade, endereco, telefone, cargo, salario) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (funcionario.nome, funcionario.idade, funcionario.endereco, funcionario.telefone, funcionario.cargo, funcionario.salario)
        mycursor.execute(sql, val)

        mydb.commit()

        print(f"O novo funcionário {funcionario.nome} foi cadastrado com SUCESSO!")

    elif opc == 2:
        mycursor.execute("SELECT * FROM funcionarios")
        myresult = mycursor.fetchall()

        if myresult:
            Utils.exibir_lista_funcionarios(myresult)

            id = int(input("Digite o ID do funcionário: "))
            mycursor.execute(f"SELECT * FROM funcionarios WHERE id = {id}")
            result = mycursor.fetchone()

            if result:
                mycursor.execute(f"SELECT salario FROM funcionarios WHERE id = {id}")
                salario_atual = mycursor.fetchone()

                if salario_atual:
                    aumento = Decimal(input("Qual a porcentagem salarial deseja aumentar? "))
                    novo_salario = salario_atual[0] * (1 + aumento / 100)

                    sql = f"UPDATE funcionarios SET salario = {novo_salario} WHERE id = {id}"
                    mycursor.execute(sql)
                    mydb.commit()

                    print(f"Salário atualizado com sucesso para o funcionário ID {id}. novo salário de: R$ {novo_salario}")
                else:
                    print(f"Funcionário com ID {id} não encontrado.")
            else:
                print(f"Funcionário com ID {id} não encontrado.")
        else:
            print("Nenhum funcionário cadastrado.")

    elif opc == 3:
        mycursor.execute("SELECT * FROM funcionarios")
        myresult = mycursor.fetchall()
        Utils.exibir_lista_funcionarios(myresult)

    elif opc == 4:
        mycursor.execute("SELECT * FROM funcionarios")
        myresult = mycursor.fetchall()

        if myresult:
            Utils.exibir_lista_funcionarios(myresult)

            id = int(input("Digite o ID do funcionário: "))
            mycursor.execute(f"SELECT * FROM funcionarios WHERE id = {id}")
            result = mycursor.fetchone()

            if result:
                sql = f"DELETE FROM funcionarios WHERE id = {id}"
                mycursor.execute(sql)
                mydb.commit()
                print("Funcionário deletado com SUCESSO.")
            else:
                print(f"Funcionário com ID {id} não encontrado.")
        else:
            print("Nenhum funcionário cadastrado.")


