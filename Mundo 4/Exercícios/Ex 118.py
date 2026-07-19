class ContaBancaria:

    """
    Cria uma conta bancária que permite fazer saques e depósitos.
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"A conta R${self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."

    def deposito(self, valor):
        self.saldo += valor
        print(f"Deposito de valor R${valor:,.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"> Saque NEGADO no valor de R${valor:,.2f} paara a conta {self.id}: SALDO INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"> Saque de R${valor:,.2f} AUTORIZADO na conta {self.id}")


c1 = ContaBancaria(666, "Igor", 3000)
c1.deposito(500)
c1.sacar(2000000)
print(c1)
