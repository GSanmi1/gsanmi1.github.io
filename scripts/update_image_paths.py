import os
import re
from pathlib import Path

def update_image_paths(filepath):
    """Actualiza rutas de imágenes en un post"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error leyendo {filepath}: {e}")
        return False

    # Patrón: {{ 'assets/img/...' | relative_url }}
    # Reemplazo: {{ '/assets/images/past-blogs/...' | relative_url }}
    pattern = r"{{\s*'assets/img/([^']+)'\s*\|\s*relative_url\s*}}"
    replacement = r"{{ '/assets/images/past-blogs/\1' | relative_url }}"

    new_content = re.sub(pattern, replacement, content)

    if new_content != content:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        except Exception as e:
            print(f"Error escribiendo {filepath}: {e}")
            return False
    return False

def main():
    posts_dir = r"C:\Users\sanmi\Documents\DocumentosDeGerman\GitRepos\WebTests\_posts"

    print("=== ACTUALIZACIÓN DE RUTAS DE IMÁGENES ===\n")

    updated_count = 0
    skipped_count = 0
    total_count = 0

    files = [f for f in os.listdir(posts_dir) if f.endswith('.md')]
    print(f"Total de posts a procesar: {len(files)}\n")

    for filename in files:
        filepath = os.path.join(posts_dir, filename)
        total_count += 1

        if update_image_paths(filepath):
            print(f"OK Actualizado: {filename}")
            updated_count += 1
        else:
            skipped_count += 1

    print(f"\n=== RESUMEN ===")
    print(f"Posts actualizados: {updated_count}")
    print(f"Posts sin cambios: {skipped_count}")
    print(f"Total procesados: {total_count}")

if __name__ == '__main__':
    main()
