from modelos import Producto, OrdenCompra, TarjetaCredito, Queja

def test_final():
    print("\n--- Prueba Bloque 3: Flujo Completo ---")
    # 1. Preparar datos
    p1 = Producto("B02", "Teclado RGB", 150.0, 20)
    visa = TarjetaCredito()
    orden = OrdenCompra("Sebastian Gutierrez")
    
    # 2. Proceso de compra
    orden.agregar_item(p1, 2)
    total = sum(i["producto"].precio * i["cantidad"] for i in orden.items)
    visa.procesar_pago(total)
    
    # 3. Soporte (Quejas) [cite: 25]
    reclamo = Queja("Sebastian", "Demora en entrega")
    reclamo.remitir_a_gerencia()

if __name__ == "__main__":
    test_final()