import sqlite3

db_file = 'DB/productos.db'

def crear_tabla_productos():
    conn = sqlite3.connect(database=db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                        nombre TEXT,
                        cantidad REAL,
                        unidad TEXT
                    )''')
    conn.commit()
    conn.close()

def insertar_producto(nombre, cantidad, unidad):
    conn = sqlite3.connect(database=db_file)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO productos VALUES (?,?,?)', (nombre, cantidad, unidad))
    conn.commit()
    conn.close()

def leer_productos():
    conn = sqlite3.connect(database=db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    rows = cursor.fetchall()
    conn.close()
    return rows


def main():
    # Crear la tabla si no existe
    crear_tabla_productos()

# Leer y mostrar los datos
productos = leer_productos()
for producto in productos:
    print(producto)

if __name__=='__main__':
    main()
