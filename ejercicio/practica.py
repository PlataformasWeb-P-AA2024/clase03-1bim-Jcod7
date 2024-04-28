import csv

plantilla_html = """
        <!DOCTYPE html>
            <html lang="en" dir="ltr">
            <head>
                <meta charset = "utf-8">
                <title>Información de Institución</title>
            </head>
            <body>
                <h1>Información de la Institución</h1>
                <p><strong>Código AMIE:</strong> {codigo_amie}</p>
                <p><strong>Nombre de la Institución Educativa:</strong> {nombre}</p>
                <p><strong>Provincia:</strong> {provincia}</p>
                <p><strong>Cantón:</strong> {canton}</p>
                <p><strong>Parroquia:</strong> {parroquia}</p>
                <p><strong>Zona Administrativa:</strong> {zona}</p>
                <p><strong>Código de Distrito:</strong> {codigo_distrito}</p>
                <p><strong>Sostenimiento:</strong> {sostenimiento}</p>
                <p><strong>Régimen Escolar:</strong> {regimen}</p>
                <p><strong>Modalidad:</strong> {modalidad}</p>
                <p><strong>Jornada:</strong> {jornada}</p>
                <p><strong>Nivel:</strong> {nivel}</p>
                <p><strong>Etnia:</strong> {etnia}</p>
                <p><strong>Número de estudiantes:</strong> {num_estudiantes}</p>
                <p><strong>Número de docentes:</strong> {num_docentes}</p>
                <p><strong>Estado:</strong> {estado}</p>
            </body>
        </html>
            """

archivo_csv = 'data/Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv'

with open (archivo_csv, newline='', encoding='utf-8') as csvFile :
    lector_csv = csv.reader(csvFile, delimiter='|')

    next(lector_csv)


    for linea in lector_csv:
        codigo_amie, nombre, provincia, canton, parroquia, zona, codigo_distrito, sostenimiento, regimen, modalidad, jornada, nivel, etnia, num_estudiantes, num_docentes, estado = linea

        contenido_html = plantilla_html.format(
            codigo_amie=codigo_amie,
            nombre=nombre,
            provincia=provincia,
            canton=canton,
            parroquia=parroquia,
            zona=zona,
            codigo_distrito=codigo_distrito,
            sostenimiento=sostenimiento,
            regimen=regimen,
            modalidad=modalidad,
            jornada=jornada,
            nivel=nivel,
            etnia=etnia,
            num_estudiantes=num_estudiantes,
            num_docentes=num_docentes,
            estado=estado
        )

        with open(f'{codigo_amie}.html', 'w', encoding='utf-8') as archivo_html:
                archivo_html.write(contenido_html)

print("Archivo HTML creado")