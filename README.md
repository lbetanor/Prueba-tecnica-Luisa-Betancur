# Nombre: Luisa Fernanda Betancur Orrego
# Fecha entrega: 29-06-2025

## Sección 1: Excel Avanzado
### Versión: Microsoft 365 de 64 bits.

### ⚠️ Consideraciones importantes
- Este archivo fue desarrollado y probado **exclusivamente en Windows**. Podría presentar incompatibilidades si se abre en **macOS**.
- Al abrir el archivo `Data_Cuentas.xlsm`, es posible que las macros se bloqueen por configuración de seguridad de Windows.  
  Puedes seguir estas [instrucciones oficiales para habilitarlas](https://support.microsoft.com/es-es/topic/se-ha-bloqueado-una-macro-potencialmente-peligrosa-0952faa0-37e7-4316-b61d-5b5ed6024216).
- **Contraseña de apertura del archivo:** `1234`
- Los archivos generados _(`logs` y `cuentas_reportables.txt`)_ se almacenan en el mismo directorio donde esté el archivo `Data_Cuentas.xlsm`.
- El control de cambios solicitado se implementó dentro de logs. 
- Para los cálculos con UVR se tuvo en cuenta el valor reportado por el Banco de la República para el 27-06-2025.

### 🧠 Descripción técnica
El proyecto se desarrolla en el archivo `Data_Cuentas.xlsm`, donde se implementa la lógica de negocio solicitada en la prueba, utilizando **programación orientada a objetos (POO)** en VBA.

Dentro del entorno de desarrollo de **Visual Basic for Applications (VBA)**, se incluyen los siguientes componentes:

- **Módulo estándar (`Módulo1`)**: contiene todas las subrutinas principales.
- **Formulario de usuario (`frmProcesador`)**: interfaz que permite al usuario ejecutar las acciones del sistema.
- **Módulo de clases**: define dos clases clave:
  - `Cuenta`
  - `Procesador_Icetex`
- **ThisWorkbook**: contiene subrutinas que se ejecutan automáticamente al abrir el archivo, utilizando el evento `Workbook_Open`.

Todo el código se encuentra comentado para facilitar su comprensión y mantenimiento.


### 🧩 Usabilidad
Sigue estos pasos para utilizar correctamente el archivo `Data_Cuentas.xlsm`:

1. **Abrir el archivo** `Data_Cuentas.xlsm`.
2. **Ingresar la contraseña:** `1234`.
3. Automáticamente se abrirá un **formulario interactivo (UserForm)** que permite ejecutar tres acciones:
    - Procesar cuentas
        - Actualiza todos los cálculos de la hoja **"Base"**.
    - Exportar TXT
        - Actualiza los cálculos de la hoja **"Base"**.
        - Genera el archivo **`cuentas_reportables.txt`** en el mismo directorio.
    - Crear resumen
        - Genera una **tabla dinámica** en la hoja **"Resumen"** que incluye: Cantidad y porcentaje de cuentas **reportables** +  Totales por **tipo de cuenta** + Un **gráfico de columnas** asociado.
        - Al finalizar, se redirige automáticamente a la hoja **"Resumen"**.

✅ Cada acción notifica si se ha procesado correctamente y guarda un **registro de actividad (log)** con nombre: `logs_YYYY-MM-DD HH-MM-SS.log`, que incluye información sobre el éxito o errores ocurridos durante la ejecución.



## Sección 2: Power BI
### Versión: 2.144.878.0 64-bit 

### ⚠️ Consideraciones importantes
- Para los cálculos con UVR se tuvo en cuenta el valor reportado por el Banco de la República para el 27-06-2025.
- Los filtros generales del informe no afectan el gráfico de linea de tiempo. Este se desarrolló en una tabla independiente ya que requería recalcular la base mensual y por temas de tiempo no se hizo relación con la tabla principal.
- Para el cálculo de las cuentas intactivas se toman 180 días después del la fecha del último movimiento. (Ya que no se indicaba en el documento, se toma de la web, donde indican que una cuenta de ahorros se considera inactiva si no tiene movimientos (depósitos o retiros) durante 180 días).


### 🧠 Descripción técnica

Se desarrolla proyecto en el archivo `prueba_Luisa_Betancur.pbix` con una estructura organizada y visualizaciones dinámicas. Se aplicaron transformaciones en **Power Query** y se implementaron cálculos con **DAX** para resolver la lógica de negocio solicitada en la prueba, incluyendo:

- Normalización de columnas
- Creación de campos adicionales en la tabla **mock_data** requeridos para el ejercicio:
    - dias_inactividad
    - saldo_uvr
    - cuenta_inactiva
    - reportable
    - fecha_estimada_inactivacion
- Creación de parámetro con la UVR del día
- Creación de tabla en **DAX** donde se recalcula la base de activos mensual, para obtener la **tasa_inactivacion** para desarrollar gráfico linea de tiempo solicitado.
- Creación de medidas en **DAX**, necesarias para análisis y cálculo de indicadores solicitados:
    -  %_cuentas_reportables
    - marcación: cuentas_inactivas
    - promedio_saldo_pesos
    - promedio_saldo_uvr
    - tasa_inactivacion_mensual
    - total_cuentas
    - total_uvr

### 🧩 Usabilidad
- Abre el archivo `prueba_Luisa_Betancur.pbix`.
- Manipula los filtros según tu necesidad
- El PDF y capturas solicitadas se encuentran en la **img** que está dentro del proyecto.




## Sección 3: Python
### Versión: 3.11.4


### 🧠 Descripción técnica

Se creó un proyecto modular en Python, el cual es ejecutado desde el archivo principal `Python/codigo/main.py`.  
En este proyecto se implementa la lógica de negocio solicitada en la prueba, utilizando **programación orientada a objetos (POO)**.

**Estructura del proyecto**
```text
Python/
│
├── codigo/
│ ├── main.py # Módulo principal que orquesta todo el proceso
│ ├── clase.py # Define la clase Cuenta
│ ├── gestor_cuentas.py # Define la clase GestorCuentas
│ ├── logger.py # Manejo de logs de ejecución
│ ├── utils.py # Funciones auxiliares
│ ├── visualizador.py # Generación de gráficos y PDF
│ └── requirements.txt # Librerías necesarias para ejecutar el proyecto
│
├── data/
│ ├── mock_data.csv # Datos fuente de prueba
│ └── UVR.csv # Tabla de valores UVR del día
│
├── output/
│ ├── cuentas_reportables.csv # Resultado con cuentas filtradas
│ ├── hist_saldos.png # Histograma de saldos en UVR
│ └── hist_saldos.pdf # Reporte en PDF con gráfico
```

### 🧩 Usabilidad
Para ejecutar el proyecto correctamente, seguir estos pasos:

1. Crear un ambiente virtual (se recomienda usar Python **3.11.4**):
   ```bash
   python -m venv venv
   ```

2. Activar el ambiente virtual (según sistema operativo):
    - En Windows 
    ```bash
    venv\Scripts\activate
    ```
    - En macOS/Linux 
    ```bash
    source venv/bin/activate
    ```

3. Instalar las dependencias
    ```bash 
    pip install -r Python/requirements.txt`
    ```

4. Ejecutar el proyecto
    ```bash 
    python Python/main.py
    ```

