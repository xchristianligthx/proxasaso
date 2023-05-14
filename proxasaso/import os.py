import os
import shutil

# Ruta de la carpeta de origen
from_dir = "Descargas"

# Ruta de la carpeta de destino
to_dir = "Documentos"

# Verificar si la carpeta de destino existe, de lo contrario, crearla
if not os.path.exists(to_dir):
    os.makedirs(to_dir)

# Obtener la lista de archivos en la carpeta de origen
files = os.listdir(from_dir)

# Iterar sobre los archivos y mover los archivos PDF a la carpeta de destino
for file_name in files:
    # Obtener la ruta completa del archivo
    file_path = os.path.join(from_dir, file_name)
    
    # Verificar si el archivo es un PDF
    if file_name.endswith(".pdf"):
        # Crear las rutas de origen y destino
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Document_Files")
        path3 = os.path.join(path2, file_name)
        
        # Verificar si la carpeta de destino existe, de lo contrario, crearla
        if not os.path.exists(path2):
            os.makedirs(path2)
        
        # Mover el archivo a la carpeta de destino
        shutil.move(path1, path3)
        
        print("Moviendo", file_name, ".....")

