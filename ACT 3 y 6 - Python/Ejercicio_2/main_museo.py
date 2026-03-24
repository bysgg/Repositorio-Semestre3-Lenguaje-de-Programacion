from modelos_museo import Cuadro, Escultura

def probar_inventario():
    print("="*40)
    print("      MUSEO LA SALLE: INVENTARIO")
    print("="*40)
    
    obra1 = Cuadro("La Noche Estrellada", "Van Gogh", "Postimpresionismo", 100000000, "1889", "Impresionista", "Óleo")
    obra2 = Escultura("El Pensador", "Rodin", "Moderna", 50000000, "1904", "Realismo", "Bronce")
    
    print(f"{obra1} -> {obra1.mostrar_detalle()}")
    print(f"{obra2} -> {obra2.mostrar_detalle()}")
    print("="*40)

if __name__ == "__main__":
    probar_inventario()