# 🛒 Manual de Programación: Sistema TeleVentas La Salle

## 1. Descripción General
Este software es una solución integral para la gestión de ventas a distancia. El sistema permite automatizar el flujo completo desde la consulta de productos en un catálogo hasta la entrega logística, pasando por pasarelas de pago y soporte post-venta.

---

## 2. Arquitectura del Sistema
El proyecto sigue un patrón de diseño modular para separar la lógica de negocio de la interfaz de ejecución, facilitando el mantenimiento:

- **modelos.py**: Contiene la definición de clases, tipos de datos (`typing`) y las reglas de negocio.  
- **main.py**: Script principal que orquesta la simulación y valida la interacción entre los objetos del sistema.  
- **Televentas Diagrama UML.jpeg**: Representación gráfica de la jerarquía y relaciones de clases.  

---

## 3. Implementación de Conceptos POO

### A. Abstracción y Herencia
Se implementó una Clase Base Abstracta (ABC) para la gestión de pagos, siguiendo el principio SOLID de Abierto/Cerrado:

- **Clase `MetodoPago`**: Define el contrato obligatorio `procesar(monto) -> bool`.  
- **Clase `TarjetaCredito`**: Implementación concreta que hereda de la base.  

Esta arquitectura permite extender el sistema a nuevos métodos (PSE, Efectivo, Cripto) sin alterar la lógica de la orden de compra.

---

### B. Encapsulamiento y Máquina de Estados
La clase `OrdenCompra` gestiona el ciclo de vida del pedido mediante una máquina de estados para garantizar la integridad del proceso:

- **PENDIENTE**: Estado inicial donde se permite la reserva de stock.  
- **PAGADA**: Se alcanza tras una transacción exitosa. Es requisito para el despacho.  
- **ARMADA**: El Agente de Depósito ha confirmado el empaque físico.  
- **ENVIADA**: Estado final tras la delegación a la empresa de logística.  
- **CANCELADA**: Revierte la operación y devuelve automáticamente las existencias al inventario de productos.  

---

### C. Tipado Estricto y Composición

- **`Dict[str, Any]`**: Se utilizó tipado avanzado para los ítems de la orden, asegurando que Pylance identifique correctamente la relación entre objetos `Producto` y cantidades enteras.  
- **Métodos Estáticos**: La clase `Logistica` utiliza `@staticmethod` para servicios de despacho que no requieren instanciación de estado, optimizando el uso de memoria.  

---

## 4. Manual de Pruebas Funcionales (Escenarios)

| Funcionalidad         | Clase / Método      | Resultado Validado |
|----------------------|--------------------|-------------------|
| Control de Stock     | `agregar_producto()` | El inventario se reduce automáticamente al añadir ítems a la orden. |
| Validación de Pago   | `TarjetaCredito`     | Retorna un booleano que dispara el cambio de estado a PAGADA. |
| Flujo de Depósito    | `AgenteDeposito`     | Solo permite armar pedidos que tengan el estado de pago verificado. |
| Soporte Post-Venta   | `Queja.remitir()`    | Despliega una alerta inmediata dirigida a la Gerencia de Relaciones. |

---

## 5. Instrucciones de Ejecución

Para iniciar la simulación y observar la trazabilidad de procesos en la terminal, ejecute:

```bash
python main.py