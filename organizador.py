import os
import shutil

# Carpeta a organizar
carpeta = r"C:\Users\omarg\Escuela\COBA"

# Clasificación por tipo
extensiones = {
    "PDFs": [".pdf"],
    "Word": [".docx"],
    "Excel": [".xlsx"],
    "PowerPoint": [".pptx"],
    "Imágenes": [".png", ".jpg", ".jpeg"],
    "Codigo": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "Apps_Kodular": [".aia"],
    "Blender": [".blend"],
    "Unity": [".unity", ".prefab", ".anim"],
    "Scripts_CSharp": [".cs"],
    "Otros": []
}
def mover_con_renombre(origen, destino):
    base, extension = os.path.splitext(destino)
    contador = 1

    while os.path.exists(destino):
        destino = f"{base}_{contador}{extension}"
        contador += 1

    shutil.move(origen, destino)
for raiz, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta_archivo = os.path.join(raiz, archivo)

        movido = False
        for carpeta_destino, tipos in extensiones.items():
            if any(archivo.lower().endswith(ext) for ext in tipos):
                ruta_carpeta = os.path.join(carpeta, carpeta_destino)
                os.makedirs(ruta_carpeta, exist_ok=True)
                destino_final = os.path.join(ruta_carpeta, archivo)

                if ruta_archivo != destino_final:
                    mover_con_renombre(ruta_archivo, destino_final)
                    print(f"Movido: {archivo} → {carpeta_destino}")

                movido = True
                break

        if not movido:
            ruta_carpeta = os.path.join(carpeta, "Otros")
            os.makedirs(ruta_carpeta, exist_ok=True)
            destino_final = os.path.join(ruta_carpeta, archivo)

            if ruta_archivo != destino_final:
                mover_con_renombre(ruta_archivo, destino_final)
                print(f"Movido: {archivo} → Otros")
print("Listo chabal")