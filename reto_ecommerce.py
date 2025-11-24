

productos = [
    {"id": 1, "nombre": "Laptop Pro 14", "categoria": "Computo", "precio": 25000, "descuento": 0.10, "stock": 5},
    {"id": 2, "nombre": "Mouse Gamer X", "categoria": "Accesorios", "precio": 1200, "descuento": 0.15, "stock": 20},
    {"id": 3, "nombre": "Teclado Mecánico K1", "categoria": "Accesorios", "precio": 2200, "descuento": 0.05, "stock": 10},
    {"id": 4, "nombre": "Monitor 27'' 4K", "categoria": "Computo", "precio": 8000, "descuento": 0.20, "stock": 7},
    {"id": 5, "nombre": "Audífonos Bluetooth Z", "categoria": "Audio", "precio": 1500, "descuento": 0.0, "stock": 15},
]

ventas = [
    {"venta_id": 101, "producto_id": 1, "cantidad": 1, "cliente": "Ana"},
    {"venta_id": 102, "producto_id": 2, "cantidad": 2, "cliente": "Luis"},
    {"venta_id": 103, "producto_id": 4, "cantidad": 1, "cliente": "Sofía"},
    {"venta_id": 104, "producto_id": 2, "cantidad": 1, "cliente": "Carlos"},
    {"venta_id": 105, "producto_id": 5, "cantidad": 3, "cliente": "Ana"},
]

tienda_info = ("TechieStore", "Santiago", 2025)

"""1. Mensaje de bienvenida"""

nombre_tienda = tienda_info[0]
ubicacion = tienda_info[1]
anio = tienda_info[2]

print(f"Bienvenido a {nombre_tienda} en {ubicacion} ({anio})")

"""2. Mostrar cuántos productos existen"""

total = len(productos)
print(f"Total de productos: {total}")

"""3. Precio final con descuento (sin loops)"""

precio_mouse = 1200.0
descuento_mouse = 0.15  # El porcentage de descuento del mouse es 15%

precio_final_mouse = precio_mouse - (precio_mouse * descuento_mouse)

print(f"Mouse Gamer X → ${precio_final_mouse}")


"""4. Total de cada venta (sin loops)"""

comprador_101 = "Ana"
producto_101 = "Laptop Pro 14"
cantidad_101 = 1
precio_final_laptop = 22500.0

total_pagado_101 = precio_final_laptop * cantidad_101

print(f"Venta 101: {comprador_101} compró {cantidad_101} {producto_101} y pagó {total_pagado_101}")

"""5. Ingreso total de la tienda"""

total_venta_101 = 22500.0
total_venta_102 = 2040.0

ingreso_total = total_venta_101 + total_venta_102

print(f"Ingreso total: {ingreso_total}")
