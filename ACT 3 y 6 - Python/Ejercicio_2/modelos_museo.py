from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional

class ObraDeArte(ABC):
    def __init__(self, titulo: str, autor: str, periodo: str, valor: float, fecha_creacion: str):
        self.titulo: str = titulo
        self.autor: str = autor
        self.periodo: str = periodo
        self.valor: float = valor
        self.fecha_creacion: str = fecha_creacion
        self.fecha_entrada_museo: datetime = datetime.now()
        self.estado: str = "Expuesta"  # Expuesta, Restauración, Cedida
        
        # AQUÍ USAMOS OPTIONAL: El próximo museo puede ser un texto o None
        self.proximo_museo: Optional[str] = None 
        
        # Historial de restauraciones
        self.historial_restauraciones: List[str] = []

    @abstractmethod
    def mostrar_detalle(self) -> str:
        pass

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] {self.titulo} - {self.autor} (${self.valor})"

class Cuadro(ObraDeArte):
    def __init__(self, titulo: str, autor: str, periodo: str, valor: float, fecha_creacion: str, estilo: str, tecnica: str):
        super().__init__(titulo, autor, periodo, valor, fecha_creacion)
        self.estilo: str = estilo
        self.tecnica: str = tecnica

    def mostrar_detalle(self) -> str:
        return f"Cuadro ({self.estilo}) - Técnica: {self.tecnica}"

class Escultura(ObraDeArte):
    def __init__(self, titulo: str, autor: str, periodo: str, valor: float, fecha_creacion: str, estilo: str, material: str):
        super().__init__(titulo, autor, periodo, valor, fecha_creacion)
        self.estilo: str = estilo
        self.material: str = material

    def mostrar_detalle(self) -> str:
        return f"Escultura ({self.estilo}) - Material: {self.material}"