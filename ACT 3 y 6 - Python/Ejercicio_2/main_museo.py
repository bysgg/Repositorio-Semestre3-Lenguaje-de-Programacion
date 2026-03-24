from modelos_museo import Cuadro, Escultura
from datetime import datetime, timedelta

def probar_museo():
    print("="*45)
    print("      SISTEMA DE GESTIÓN MURAL - LA SALLE")
    print("="*45)
    
    # 1. Registro de Obras
    obra1 = Cuadro("La Noche Estrellada", "Van Gogh", "Postimpresionismo", 100000000, "1889", "Impresionista", "Óleo")
    obra2 = Escultura("El Pensador", "Rodin", "Moderna", 50000000, "1904", "Realismo", "Bronce")
    
    # 2. Simulación de Tiempo (Forzamos que la escultura necesite restauración de 5 años)
    obra2.ultima_restauracion = datetime.now() - timedelta(days=6*365)
    
    inventario = [obra1, obra2]
    
    for obra in inventario:
        print(f"\n[*] Analizando: {obra}")
        print(f"    Detalles: {obra.mostrar_detalle()}")
        
        # Ejecutar chequeo diario automático
        obra.chequear_mantenimiento_automatico()
        
    print("\n" + "="*45)
    print("      REPORTE DE RESTAURACIONES")
    print("="*45)
    for obra in inventario:
        if obra.historial_restauraciones:
            print(f"Obra: {obra.titulo}")
            for res in obra.historial_restauraciones:
                print(f"  - {res}")

if __name__ == "__main__":
    probar_museo()