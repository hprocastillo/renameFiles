import os

def renombrar_pdfs(directorio):
    # Obtener todos los archivos .pdf en la carpeta
    archivos = [f for f in os.listdir(directorio) if f.lower().endswith('.pdf')]

    # Ordenar los archivos alfabéticamente
    archivos.sort()

    # Renombrar con nombres correlativos
    for i, archivo in enumerate(archivos, start=1):
        nuevo_nombre = f"scan{str(i).zfill(5)}.pdf"  # Formato: scan00001.pdf
        ruta_actual = os.path.join(directorio, archivo)
        nueva_ruta = os.path.join(directorio, nuevo_nombre)

        # Evitar colisión de nombres
        if ruta_actual != nueva_ruta:
            os.rename(ruta_actual, nueva_ruta)
            print(f'Renombrado: {archivo} -> {nuevo_nombre}')
        else:
            print(f'Se mantiene: {archivo}')


# Ruta de la carpeta donde están los PDFs (cambiar por la ruta real)
carpeta = r"C:\escaneos"
renombrar_pdfs(carpeta)
