# SISTEMA DE GESTION DE UNA CHURRASQUERIA

Este proyecto fue hecho por los estudiantes de ANALISIS Y DISENO DE SISTEMAS
NOMBRES:
	Apaza Guzmán Juan Agustin
	Miguel Angel Cazón Huanca 
	Kevin Jose Ollisco Claure 
	Soledad Cerezo Guzmán
	Mauricio Joel Flores Garzofino
 
### Pre-Requisites
`Python 3.7`
`BD Browser SQLite

![El Corral 6_15_2023 1_57_08 AM](https://github.com/JuanApazaG/ChurrasqueriaUltimo/assets/111205513/00125d08-360c-4047-a351-82f3dd4d72d7)
![Modo_ ADMIN 6_14_2023 9_35_07 PM](https://github.com/JuanApazaG/ChurrasqueriaUltimo/assets/111205513/3145fcd6-4e79-4f6f-bd5b-7348c1eae78d)
![Billing System 6_14_2023 9_34_25 PM](https://github.com/JuanApazaG/ChurrasqueriaUltimo/assets/111205513/433f937c-6312-42bb-b453-0722a4a22a3e)

## Quick Start

- **Run:** From the project root run:

```bash
python main.py
```

- **Database file:** [Database/store.db](Database/store.db)

## Credenciales de ejemplo que ya funcionan

- **Admin (UI login):**
	- Usuario (emp_id): `EMP0000`
	- Contraseña: `admin`

- **Empleado (UI login):**
	- Usuario (emp_id): `E27`
	- Contraseña: `emp`

Nota: estos usuarios existen en la tabla `employee` de la base de datos. Para cambiar, añadir o gestionar usuarios abre `Database/store.db` con DB Browser for SQLite o ejecuta scripts SQL.

## Si quieres que añada/cree otras credenciales

- Puedo generar nuevos usuarios y establecer contraseñas seguras y luego actualizar la base de datos por ti.

## Descripción

Este proyecto es un sistema de gestión para una churrasquería. Permite:

- Administrar cuentas de empleados y administradores.
- Generar y gestionar facturas (crear, buscar y registrar ventas).
- Mantener un inventario de productos y categorías.
- Registrar datos de clientes y realizar operaciones de facturación desde una interfaz gráfica.

Está pensado para facilitar la administración diaria del negocio y llevar un registro histórico de facturas e inventario.

## Tecnologías usadas

- **Python** (3.7+): lenguaje principal del proyecto.
- **Tkinter**: biblioteca para la interfaz gráfica (UI).
- **SQLite**: base de datos ligera (archivo `Database/store.db`).
- **Módulos estándar**: `sqlite3`, `os`, `re`, `random`, `string`, `datetime`, etc.
- **Recursos locales**: imágenes dentro de `images/` y fuentes en `fonts/`.

Recomendación: usa DB Browser for SQLite para abrir y editar `Database/store.db` si necesitas gestionar usuarios o datos directamente.
