import mysql.connector

print("INICIANDO PROGRAMA...")

try:
    # Conexión a la base de datos
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="BTStuspatrones", 
        database="escuela",
        port=3307
    )

    print("Conexión exitosa a MySQL")

    cursor = conexion.cursor()

    # Obtener datos
    cursor.execute("SELECT * FROM Persona")
    personas = cursor.fetchall()

    # Verificar si hay datos
    if len(personas) > 0:

        print("\nTABLA DE PERSONAS:\n")
        print("ID | Nombre | Apellido | Cédula | Edad")
        print("----------------------------------------")

        for p in personas:
            print(f"{p[0]} | {p[1]} | {p[2]} | {p[3]} | {p[4]}")

        # Promedio de edad (lambda)
        edades = list(map(lambda x: x[4], personas))
        promedio = sum(edades) / len(edades)
        print("\nPromedio de edad:", promedio)

        # Persona con menor edad (lambda)
        menor = min(personas, key=lambda x: x[4])
        print("Persona con menor edad:", menor[1])

    else:
        print("No hay datos en la tabla Persona")

    conexion.close()

except Exception as e:
    print("Error:", e)

input("\nPresiona Enter para salir...")