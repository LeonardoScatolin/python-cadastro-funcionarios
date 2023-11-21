from Pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome, idade, endereco, telefone, cargo, salario):
        super().__init__(nome, idade, endereco, telefone)
        self.__cargo = cargo
        self.__salario = salario

    @property
    def cargo(self):
        return self.__cargo

    @property
    def salario(self):
        return self.__salario

    @cargo.setter
    def cargo(self, novo_cargo):
        self.__cargo = novo_cargo

    @salario.setter
    def salario(self, novo_salario):
        self.__salario = novo_salario
