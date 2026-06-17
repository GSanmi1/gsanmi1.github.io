import shutil
import os
from pathlib import Path

source = r"C:\Users\sanmi\Documents\DocumentosDeGerman\GitRepos\gsanmi1.github.io\assets\img"
dest = r"C:\Users\sanmi\Documents\DocumentosDeGerman\GitRepos\WebTests\assets\images\past-blogs"

print(f"Copiando de: {source}")
print(f"Copiando a: {dest}")
print("Esto puede tomar varios minutos...")

try:
    # Copiar todo el directorio recursivamente
    shutil.copytree(source, dest, dirs_exist_ok=True)
    print("\nCopia completada exitosamente!")

    # Contar archivos copiados
    file_count = sum(1 for _ in Path(dest).rglob('*') if _.is_file())
    print(f"Total de archivos copiados: {file_count}")

except Exception as e:
    print(f"Error: {e}")
