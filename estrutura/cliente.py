class Cliente:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_contas(self):
        for conta in self.contas:
            return conta

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Telefone: {self.telefone}"
