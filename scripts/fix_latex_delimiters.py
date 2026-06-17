import os
import re
from pathlib import Path

def fix_latex_delimiters(filepath):
    """
    Convierte delimitadores LaTeX inline de $ a \\( \\) para compatibilidad con Kramdown.
    Kramdown reconoce \\( \\) pero no $ $.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error leyendo {filepath}: {e}")
        return False

    original_content = content

    # Separar el front matter del contenido
    parts = content.split('---', 2)
    if len(parts) >= 3:
        front_matter = parts[1]
        body = parts[2]
    else:
        print(f"Warning: No front matter en {filepath}")
        return False

    # Patrón para encontrar matemáticas inline con $...$
    # Debe evitar $$...$$ (display math) y ser cuidadoso con casos edge

    # Primero, proteger temporalmente los display math $$...$$
    display_math_pattern = r'\$\$(.*?)\$\$'
    display_matches = re.findall(display_math_pattern, body, re.DOTALL)

    # Reemplazar display math con placeholders
    placeholders_display = []
    for i, match in enumerate(display_matches):
        placeholder = f"<<<DISPLAY_MATH_{i}>>>"
        placeholders_display.append(match)
        body = body.replace(f'$${match}$$', placeholder, 1)

    # Ahora convertir inline math $...$ a \\(...\\)
    # Este patrón busca $ que no sea parte de $$
    inline_pattern = r'(?<!\$)\$(?!\$)([^\$\n]+?)\$(?!\$)'

    def replace_inline(match):
        math_content = match.group(1)
        # Verificar que no sea un placeholder
        if '<<<' not in math_content and '>>>' not in math_content:
            return f'\\\\({math_content}\\\\)'
        return match.group(0)

    body = re.sub(inline_pattern, replace_inline, body)

    # Restaurar display math con delimitadores correctos (mantener $$)
    for i, match in enumerate(placeholders_display):
        placeholder = f"<<<DISPLAY_MATH_{i}>>>"
        body = body.replace(placeholder, f'$${match}$$')

    # Reconstruir el archivo
    new_content = f"---{front_matter}---{body}"

    if new_content != original_content:
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

    print("=== CONVERSIÓN DE DELIMITADORES LaTeX ===\n")
    print("Convirtiendo $...$ a \\(...\\) para compatibilidad con Kramdown\n")

    updated_count = 0
    skipped_count = 0
    total_count = 0

    files = [f for f in os.listdir(posts_dir) if f.endswith('.md')]
    print(f"Total de posts a procesar: {len(files)}\n")

    for filename in files:
        filepath = os.path.join(posts_dir, filename)
        total_count += 1

        if fix_latex_delimiters(filepath):
            print(f"OK Actualizado: {filename}")
            updated_count += 1
        else:
            skipped_count += 1

    print(f"\n=== RESUMEN ===")
    print(f"Posts actualizados: {updated_count}")
    print(f"Posts sin cambios: {skipped_count}")
    print(f"Total procesados: {total_count}")

    print("\nNOTA: Los delimitadores display math ($$...$$) se mantienen igual.")
    print("Los delimitadores inline ($...$) ahora son \\(...\\)")

if __name__ == '__main__':
    main()
