# 🏛️ Manual de Programación: Sistema de Gestión de Museos (MURAL)

## 1. Descripción General
El sistema **MURAL** (Management & Unified Restoration Art Ledger) es una solución integral diseñada para automatizar la administración de catálogos artísticos, procesos de restauración por ciclo de vida y la gestión de cesiones internacionales entre instituciones culturales.

---

## 2. Arquitectura del Proyecto
El software implementa una arquitectura modular y desacoplada para garantizar la escalabilidad:

- **modelos_museo.py**: Motor lógico que contiene la jerarquía de clases de las obras, la gestión de usuarios y el registro detallado de restauraciones.  
- **main_museo.py**: Punto de entrada que orquesta el flujo de trabajo diario de los tres roles principales (Encargado, Restaurador Jefe y Director).  
- **Diagrama_UML_Museo.png**: Documentación gráfica de la estructura de clases y sus relaciones de composición.  

---

## 3. Implementación de Conceptos POO Avanzados

### A. Herencia y Polimorfismo
Se utiliza una estructura de herencia para especializar los objetos del museo:

- **Clase Base `ObraDeArte`**: Clase abstracta (ABC) que centraliza atributos comunes como `autor`, `periodo`, `valor` y `estilo`. No permite instanciación directa.  
- **Especialización**: Las clases `Cuadro` y `Escultura` extienden la base añadiendo atributos técnicos específicos (`tecnica` y `material`).  
- **Polimorfismo**: El método `@abstractmethod def mostrar_detalle()` obliga a las subclases a implementar su propia lógica de visualización, permitiendo un tratamiento uniforme de la colección.  

---

### B. Composición y Gestión de Historial
Para cumplir con el requisito de auditoría del Restaurador Jefe, se implementó:

- **Clase `Restauracion`**: Objeto independiente que almacena fechas de inicio/fin y tipo de intervención.  
- **Relación de Composición**: Cada `ObraDeArte` posee una lista de objetos `Restauracion`, permitiendo reconstruir cronológicamente el historial de mantenimiento de cada pieza ordenado por antigüedad.  

---

### C. Lógica de Disponibilidad (Lista de Espera)
El sistema gestiona la concurrencia de préstamos mediante un control de estados estricto:

- **Bloqueo de Cesión**: Una obra solo puede ser cedida si su estado es `Expuesta`.  
- **Estado Diferido**: Si la obra está en `Restauración`, el sistema utiliza el atributo `museo_en_espera` (tipo `Optional`) para encolar solicitudes futuras, garantizando que el Director mantenga el control de la demanda externa.  

---

## 4. Seguridad y Roles
El acceso a las funciones críticas está protegido mediante la clase `Usuario`, que valida permisos según el cargo:

- **Encargado**: Responsable de la carga inicial del catálogo y metadatos.  
- **Restaurador Jefe**: Supervisa el mantenimiento quinquenal y consulta historiales.  
- **Director**: Autoriza cesiones económicas y genera reportes de valoración patrimonial (`$`).  

---

## 5. Manual de Pruebas Funcionales (Escenarios)

| Caso de Prueba            | Funcionalidad                  | Resultado Validado |
|--------------------------|--------------------------------|-------------------|
| Seguridad                | `Usuario.autenticar()`         | Deniega el acceso ante credenciales inválidas. |
| Mantenimiento Quinquenal | `timedelta(days=5*365)`        | Identifica obras con >5 años sin revisión y cambia su estado automáticamente. |
| Daño Accidental          | `enviar_a_restauracion()`      | Permite el ingreso inmediato a taller, sobrescribiendo el estado de exposición. |
| Valoración Total         | `sum(o.valor)`                 | Calcula dinámicamente el valor total de la colección para activos financieros. |
| Gestión de Espera        | `museo_en_espera`              | Registra automáticamente el interés de un museo si la obra no está disponible. |

---

## 6. Ejecución del Sistema
Para iniciar la simulación integral que recorre los módulos de seguridad, restauración y dirección, ejecute:

```bash
python main_museo.py