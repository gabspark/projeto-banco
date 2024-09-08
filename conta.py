from dataclasses import dataclass, field
from transacao import Transacao
from datetime import datetime


@dataclass
class ContaBancaria:
    titular: str
    saldo: float = 0.0
    historico: list = field(default_factory=list)
    saques_diarios: int = 0
    ultimo_saque: datetime = None

    def deposito(self, valor: float):
        if valor > 0:
            self.saldo += valor
            transacao = Transacao("Depósito", valor)
            self.historico.append(transacao)
        else:
            print("Valor inválido. Por favor, selecione um valor acima de 0")
    
    def saque(self, valor: float):

        hoje = datetime.now().date()

        if self.ultimo_saque is None or self.ultimo_saque.date() != hoje:
            self.saques_diarios = 0
        
        if self.saques_diarios >= 3:
            print("Limite de saques atingido. Tente novamente amanhã!")
            return
        
        if valor > 500:
            print("O valor máximo para saque é de R$ 500.00!")
            return
        
        if valor > self.saldo:
            print("Saldo Insuficiente.")
            return
        
        self.saldo -= valor
        self.saques_diarios += 1
        self.ultimo_saque = datetime.now()
        transacao = Transacao("Saque", valor)
        self.historico.append(transacao)
        print(f"Saque de {valor:.2f} autorizado.")


    def extrato(self):
        print(f"Extrato bancário da conta: {self.titular}")
        for transacao in self.historico:
            print(transacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
