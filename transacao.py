from dataclasses import dataclass
from datetime import datetime

@dataclass
class Transacao:
    tipo: str
    valor: float
    data: datetime = datetime.now()

    def __str__(self):
        return f"{self.tipo}: R$ {self.valor:.2f} - {self.data.strftime('%Y-%m-%d %H:%M:%S')}"
