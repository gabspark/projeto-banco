from dataclasses import dataclass, field
from transacao import Transacao


@dataclass
class ContaBancaria:
    titular: str
    saldo: float = 0.0
    historico: list = field(default_factory=list)

    def deposito(self, valor: float):
        if valor > 0:
            self.saldo += valor
            transacao = Transacao("Depósito", valor)
            self.historico.append(transacao)
        else:
            print("Valor inválido. Por favor, selecione um valor acima de 0")
    
    def saque(self, valor: float):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            transacao = Transacao("Saque", valor)
            self.historico.append(transacao)
        else:
            print("Verifique se há saldo suficiente para realizar esta operação.")

    def extrato(self):
        print(f"Extrato bancário da conta: {self.titular}")
        for transacao in self.historico:
            print(transacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
