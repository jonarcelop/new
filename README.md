# 🌱 Proyecto: Sistema para la Administración de Viveros

## 📌 Descripción
Este proyecto es un sistema de administración de viveros que permite gestionar **Productores, Fincas, Viveros y Labores** realizadas en cada uno de ellos. También maneja el uso de **Productos de Control** para plagas, fertilizantes y hongos.

## 📋 Requisitos del Proyecto
- **Modelo de Dominio**: Implementado con Django ORM.
- **Diagrama de Clases**: Se ha creado un modelo de datos en Django basado en el diagrama de clases definido.
- **Pruebas Unitarias**: Mínimo 3 pruebas unitarias por entidad, validando relaciones y restricciones.
- **Repositorio en GitHub**: El código se mantiene bajo control de versiones en GitHub.

## 🔧 Desarrollo de la Actividad
### 1️⃣ Modelo con Entidades y ORM
Se ha creado un **Diagrama de Clases** que representa el modelo de dominio del sistema. Este modelo ha sido implementado con **Django ORM**, asegurando una correspondencia exacta entre las entidades y la base de datos.

### 2️⃣ Pruebas Unitarias
Se han desarrollado un mínimo de **3 pruebas unitarias por entidad**, enfocadas en validar:
- **Requerimientos Funcionales**: Comprobación de que cada entidad se crea y se relaciona correctamente.
- **Requerimientos No Funcionales**: Validación de restricciones y comportamientos esperados.

### 3️⃣ Campos Obligatorios
Todos los atributos de las entidades son **obligatorios**. Se han definido restricciones en los modelos para asegurar que ningún campo quede vacío.

### 4️⃣ Verificación de Relaciones entre Entidades
Las pruebas unitarias incluyen validaciones de las **relaciones entre Productores, Fincas, Viveros y Labores**, asegurando que los datos sean consistentes y respeten la lógica del sistema.

### 5️⃣ Control de Versiones con GitHub
El proyecto ha sido subido a **GitHub** para su gestión y control de versiones, permitiendo futuras colaboraciones y mejoras.

## ⚙️ Instalación y Configuración
### 1️⃣ Clonar el Repositorio
```bash
git clone https://github.com/jonarcelop/new.git
cd new
```

### 2️⃣ Crear y Activar un Entorno Virtual
```bash
python -m venv venv  # Crear el entorno virtual
source venv/bin/activate  # Para Mac/Linux
venv\Scripts\activate  # Para Windows
```

### 3️⃣ Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar Migraciones y Crear Superusuario
```bash
python manage.py migrate
python manage.py createsuperuser  # Crear un usuario para acceder al admin
```

### 5️⃣ Ejecutar el Servidor
```bash
python manage.py runserver
```
Luego, accede en el navegador a `http://127.0.0.1:8000/admin/` e inicia sesión.

## ✅ Pruebas Unitarias
Para ejecutar las pruebas unitarias y verificar que el sistema funciona correctamente, usa:
```bash
python manage.py test gestion
```

## 📄 Licencia
Este proyecto es de código abierto y está disponible bajo la licencia MIT.

🚀 **¡Listo para usar y mejorar!**
