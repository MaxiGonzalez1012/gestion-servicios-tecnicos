# Sistema de Gestión de Servicios Técnicos

Trabajo Práctico Integrador desarrollado en Python. El sistema permite administrar clientes, técnicos, trabajos, cobros y generar reportes mediante una aplicación de consola.

---

# Cómo ejecutar el sistema

## Requisitos

- Python 3.x

## Ejecución

Desde la carpeta del proyecto ejecutar:

```bash
python main.py
```

o, en Linux:

```bash
python3 main.py
```

Al iniciar, el sistema carga automáticamente los datos almacenados en la carpeta `data`.

---

# Descripción de los módulos

## main.py

Contiene el menú principal del sistema y coordina el acceso a todos los módulos.

## clientes.py

Permite administrar clientes:

- Agregar
- Listar
- Editar
- Eliminar

## tecnicos.py

Permite administrar los técnicos:

- Agregar
- Listar
- Editar
- Eliminar

## trabajos.py

Gestiona los trabajos realizados por la empresa.

Permite:

- Registrar nuevos trabajos
- Asignar técnicos
- Modificar estados
- Eliminar trabajos

## cobros.py

Administra la parte económica del sistema.

Permite:

- Registrar importes
- Registrar pagos
- Consultar liquidaciones por empresa

## reportes.py

Genera distintos reportes del sistema:

- Trabajos pendientes
- Trabajos realizados
- Trabajos incompletos
- Trabajos reprogramados
- Cobros pendientes

## utilidades.py

Contiene funciones auxiliares utilizadas por todos los módulos, como:

- Validación de entradas
- Búsqueda por ID
- Limpieza de consola
- Menús
- Impresión con efecto de escritura

## data/database.py

Se encarga de la persistencia de datos.

Funciones principales:

- Cargar datos desde archivos
- Guardar datos
- Generar IDs
- Mantener las listas compartidas del sistema

---

# Librerías utilizadas

El proyecto utiliza únicamente librerías estándar de Python:

- `os`
- `time`

No es necesario instalar dependencias adicionales.

---

# Limitaciones conocidas

- Los datos se almacenan en archivos de texto (`.txt`) separados por `;`.
- No existe autenticación de usuarios.
- Toda la información se mantiene en memoria durante la ejecución y se guarda al finalizar cada modificación.
- Las fechas y horarios son ingresados como texto y no poseen validación de formato.

---

Trabajo Práctico Integrador: https://drive.google.com/drive/folders/1IgjL9gWmO1XnpmjiymEY58GOvFcJ8Z6a?usp=sharing