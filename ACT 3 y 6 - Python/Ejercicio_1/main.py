from modelos import Producto

def test_inicial():
    # Prueba de creación de producto según requerimientos (código, descripción, precio, etc.) [cite: 22]
    p1 = Producto("A01", "Laptop Oficina", 2500.0, 10)
    print("--- Prueba Bloque 1 ---")
    print(p1)

if __name__ == "__main__":
    test_inicial()