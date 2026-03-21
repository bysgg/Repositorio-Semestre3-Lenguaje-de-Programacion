from abc import ABC, abstractmethod

class Producto:
    def __init__(self, codigo: str, descripcion: str, precio: float, cantidad: int):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad # Cantidad disponible en stock

    def __str__(self) -> str:
        return f"Producto: {self.descripcion} | Precio: ${self.precio} | Stock: {self.cantidad}"

class MetodoPago(ABC):
    @abstractmethod
    def procesar(self, monto: float) -> None:
        pass