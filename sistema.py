from estrutura.cliente import Cliente
from estrutura.conta import *

# Criando clientes:
cliente1 = Cliente('Lucas Carvalho', '123.456.789-10', '(00)99999-9999')
cliente2 = Cliente('Karine Lopes', '111.222.333-44', '(00)00000-0000')

# Criando contas:
conta1 = Conta('12345', '1234', 1000, cliente1)
conta2 = Conta('678910', '5678', 500, cliente2)

# Adicionando contas aos clientes:
cliente1.adicionar_conta(conta1)
cliente2.adicionar_conta(conta2)

# Operações bancárias:
conta1.depositar(500)
conta1.sacar(100)
conta1.transferir(conta2, 300)

# Listando contas dos clientes:
cliente1.listar_contas()
cliente2.listar_contas()
