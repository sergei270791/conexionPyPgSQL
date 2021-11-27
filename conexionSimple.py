import psycopg2

conexion1 = psycopg2.connect(database="dupont", user="postgres", password="slobodan123")
cursor1=conexion1.cursor()
sql="insert into cargos(cargo_id,cargo_titulo,sueldo_min,sueldo_max) values (%s,%s,%s,%s)"
datos=("FR_DEV", "Front-end Developer",4500,9000)
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close() 