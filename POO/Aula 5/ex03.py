class conta_bancaria:
    """
    documentação em breve
    """
    def __init__(self, id, nome, saldo):
        self.id = id
        self.nome = nome
        self.saldo = saldo

    def __str__(self):
        return f"O id é {self.id}, conta: {self.nome} e saldo: {self.saldo:,.2f}"

    def deposito(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        if valor < self.saldo:
            self.saldo -= valor
        else:
            return f"Solicitação de {valor} não autorizada. Valor insuficiente"
        return self.saldo

c1 = conta_bancaria(1, "Weslley", 3000)
c1D = c1.deposito(3000)
c1S = c1.sacar(2000)
print(c1S)

print(c1)