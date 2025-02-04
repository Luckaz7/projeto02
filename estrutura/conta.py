class Conta:
    def __init__(self, numero, agencia, saldo, cliente):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo
        self.cliente = cliente

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R$ {valor} efetuado com sucesso.')
        else:
            print('Saldo insuficiente')

    def transferir(self, conta_destino, valor):
        if valor <= self.saldo:
            self.sacar(valor)
            conta_destino.depositar(valor)
            print(f'Transferencia de R$ {valor} para a conta {
                  conta_destino} efetuada com sucesso.')
        else:
            print('Saldo insuficiente para transferência.')

    def __str__(self):
        return f'Número: {self.numero}, Agência: {self.agencia}, Saldo: {self.saldo}'
