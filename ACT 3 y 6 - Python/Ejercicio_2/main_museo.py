from modelos_museo import ObraDeArte, Cuadro, Escultura, Usuario
from typing import List

def probar_gestion_director():
    print("\n" + "="*45)
    print("      MÓDULO DE DIRECCIÓN Y SEGURIDAD")
    print("="*45)

    # 1. Seguridad
    director = Usuario("admin", "lasalle123", "Director")
    print("[Login] Intentando acceder como Director...")
    
    if director.autenticar("admin", "lasalle123"):
        print("[OK] Autenticación exitosa. Bienvenido, Director.")
        
        # 2. Inventario para valoración
        obra1 = Cuadro("La Noche Estrellada", "Van Gogh", "Post", 100000000, "1889", "Imp", "Óleo")
        obra2 = Escultura("El Pensador", "Rodin", "Moderna", 50000000, "1904", "Real", "Bronce")
        inventario: List[ObraDeArte] = [obra1, obra2]

        # 3. Requisito: Suma total de valoraciones
        total_museo = sum(obra.valor for obra in inventario)
        print(f"\n[REPORTE] Valoración total del patrimonio: ${total_museo}")

        # 4. Gestión de Cesiones
        obra1.ceder_a_museo("Museo del Louvre", 15000000)
        # Intentar ceder la misma obra a otro (debe quedar en espera)
        obra1.ceder_a_museo("Museo Prado", 12000000)

if __name__ == "__main__":
    # Mantén tu función anterior si quieres, o solo llama a la nueva
    probar_gestion_director()