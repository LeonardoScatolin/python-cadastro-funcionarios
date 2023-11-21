class Pessoa:
    def __init__(self, nome, idade, endereco, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__endereco = endereco
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def endereco(self):
        return self.__endereco

    @property
    def telefone(self):
        return self.__telefone

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade

    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    @telefone.setter
    def telefone(self, novo_telefone):
        self.__telefone = novo_telefone

