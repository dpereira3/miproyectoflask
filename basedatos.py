import pymysql 

def dame_conexion():
    return pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        db = 'bdflask'
        )

def dame_conexion_remota():
    return pymysql.connect(
        host = 'sql10.freesqldatabase.com',
        user = 'sql10549750',
        password = 'NldJytlJZC',
        db = 'sql10549750'
    )

def insertar_articulo(nombre, precio):
    try:
        conexion = dame_conexion_remota()
    except Exception as e:
        print(f"Error de conexion: {e}")
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO articulos(id, nombre, precio) VALUES (NULL, %s, %s)", (nombre, precio))
        conexion.commit()
        conexion.close()

def listar_articulos():
    try:
        conexion = dame_conexion_remota()
    except Exception as e:
        print(f"Error de conexion: {e}")
    articulos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, precio FROM articulos")
        articulos = cursor.fetchall()
        conexion.close()
        return articulos

def eliminar_articulo(id):
    try:
        conexion = dame_conexion_remota()
    except Exception as e:
        print(f"Error de conexion: {e}")
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM articulos WHERE id = %s", (id))
        conexion.commit()
        conexion.close()

def obtener_articulo(id):
    try:
        conexion = dame_conexion_remota()
    except Exception as e:
        print(f"Error de conexion: {e}")
    articulo = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, precio FROM articulos WHERE id = %s",(id))
        articulo = cursor.fetchone()
        conexion.close()
        return articulo

def actualizar_articulo(id, nombre, precio):
    try:
        conexion = dame_conexion_remota()
    except Exception as e:
        print(f"Error de conexion: {e}")
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE articulos SET nombre = %s, precio = %s WHERE id = %s", (nombre, precio, id))
        conexion.commit()
        conexion.close()

def alta_usuario(email, clave):
    try:
        conexion = dame_conexion_remota()
    except Exception as e:
        print(f"Error de conexion: {e}")
    with conexion.cursor() as cursor:
        cursor.execute(
            "INSERT INTO usuarios(id, email, clave) VALUES (NULL, %s, %s)", (email, clave)
        )
    conexion.commit()
    conexion.close()

def obtener_usuario(email):
    try:
        conexion = dame_conexion_remota()
    except Exception as e:
        print(f"Error de conexion: {e}")
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT email, clave FROM usuarios WHERE email = %s", (email)
        )
    usuario = cursor.fetchone()
    conexion.close()
    return usuario

#if __name__ == '__main__':
    #articulos = listar_articulos()
    #print(articulos)
    #alta_usuario('lala', '1234')