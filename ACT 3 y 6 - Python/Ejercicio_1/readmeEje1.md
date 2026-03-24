# Ejercicio 1: Sistema TeleVentas

## Metodología de Desarrollo Paso a Paso

1. **Análisis de Requisitos:** Se identificaron los actores (Cliente, Agente de Depósito, Logística y Gerente) y sus responsabilidades.
2. **Abstracción de Datos:** Definición de la clase `Producto` con gestión de stock integrada.
3. **Aplicación de Principios SOLID:** - Se implementó la clase abstracta `MetodoPago` (Inversión de Dependencia) para permitir que el sistema escale a nuevos medios de pago sin modificar la lógica de la orden.
4. **Lógica de Negocio:** Desarrollo de `OrdenCompra` con validaciones de disponibilidad en tiempo real.
5. **Flujo de Proceso:** Integración del empaquetado en depósito y la delegación a empresas de logística externas.
6. **Gestión de Soporte:** Canalización directa de quejas hacia la gerencia de relaciones.