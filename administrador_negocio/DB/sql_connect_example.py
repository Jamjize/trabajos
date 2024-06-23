import sqlite3

def crear_tabla_productos():
    conn = sqlite3.connect('productos.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                        nombre TEXT,
                        cantidad REAL,
                        unidad TEXT
                    )''')
    conn.commit()
    conn.close()

def insertar_producto(nombre, cantidad, unidad):
    conn = sqlite3.connect('productos.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO productos VALUES (?,?,?)', (nombre, cantidad, unidad))
    conn.commit()
    conn.close()

def leer_productos():
    conn = sqlite3.connect('productos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Crear la tabla si no existe
crear_tabla_productos()

# Insertar valores de ejemplo
insertar_producto("pizza", 30, "u")
insertar_producto("Manaos cola", 20, "Ltrs")

# Leer y mostrar los datos
productos = leer_productos()
for producto in productos:
    print(producto)
