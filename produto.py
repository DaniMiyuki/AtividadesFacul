from dataclasses import dataclass

@dataclass
class Produto:
    id: int
    codigo: int 
    marca: str 
    quantidade: int 
    preco_unitario: float
