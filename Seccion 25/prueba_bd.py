import psycopg2

conexion =  psycopg2.connect(
    user='postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona where id_persona = %s'
            id_persona = int(input('Proporciona el valor id_persona: '))
            cursor.execute(sentencia, (id_persona,))
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
