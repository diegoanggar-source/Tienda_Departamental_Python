# # Tienda Departamental - Sistema de Gestión en Python

Sistema de punto de venta (POS) y gestión integral para tienda departamental desarrollado en Python. Simula el funcionamiento real de una tienda como Liverpool / Sears / Suburbia con múltiples departamentos, inventario, clientes, carrito y facturación.

## 📖 Descripción

El programa permite administrar una tienda departamental desde consola o interfaz Tkinter, gestionando productos por departamentos (Ropa, Electrónica, Hogar, Juguetería, Cosméticos), control de empleados, clientes con tarjeta departamental y generación de tickets.

Proyecto desarrollado con Programación Orientada a Objetos (POO).

## 🏬 Módulos Principales

**1. Gestión de Departamentos:**
- Ropa y Calzado
- Electrónica y Línea Blanca
- Hogar y Muebles
- Belleza y Perfumería
- Juguetería y Deportes

**2. Funcionalidades CRUD:**
- Alta, baja y modificación de productos
- Control de tallas, colores y existencias por sucursal
- Búsqueda por SKU, departamento o marca

**3. Sistema de Ventas:**
- Carrito de compras
- Aplicación de descuentos y promociones por departamento
- Cliente con tarjeta departamental (10% descuento)
- Generación de ticket en PDF con `reportlab`
- Métodos de pago: efectivo, tarjeta, meses sin intereses

**4. Administración:**
- Login con roles: Administrador, Cajero, Vendedor
- Corte de caja diario
- Reporte de ventas por departamento
- Alerta de inventario bajo

## 🛠️ Stack Tecnológico

- **Lenguaje:** Python 3.11+
- **Paradigma:** POO (Programación Orientada a Objetos)
- **Base de Datos (opcional):** SQLite3 / MySQL / JSON como almacenamiento local
- **Librerías:**
