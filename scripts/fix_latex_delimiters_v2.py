import os
import re
from pathlib import Path

def fix_latex_delimiters(filepath):
    """
    Convierte delimitadores LaTeX inline de $ a $$ para compatibilidad con Kramdown.
    Con math_engine: mathjax, Kramdown usa $$ tanto para inline como display math.
    La diferencia está en el contexto (inline vs en su propia línea).
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

    # Primero, proteger los display math que ya usan $$...$$
    # Usamos un patrón más robusto que captura $$...$$ incluso multilínea
    display_math_pattern = r'\$\$(.*?)\$\$'
    display_matches = []

    def save_display_math(match):
        placeholder = f"<<<DISPLAY_MATH_{len(display_matches)}>>>"
        display_matches.append(match.group(0))  # Guardar con los $$
        return placeholder

    body = re.sub(display_math_pattern, save_display_math, body, flags=re.DOTALL)

    # Ahora convertir inline math $...$ a $$...$$
    # Patrón: $ que no sea parte de $$ seguido de contenido, seguido de $ que no sea parte de $$
    inline_pattern = r'(?<!\$)\$(?!\$)([^\$\n]+?)\$(?!\$)'

    def replace_inline(match):
        math_content = match.group(1)
        # Verificar que no sea un placeholder
        if '<<<' not in math_content and '>>>' not in math_content:
            return f'$${math_content}$$'
        return match.group(0)

    body = re.sub(inline_pattern, replace_inline, body)

    # Restaurar display math (ya tienen $$)
    for i, original in enumerate(display_matches):
        placeholder = f"<<<DISPLAY_MATH_{i}>>>"
        body = body.replace(placeholder, original)

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

    print("=== CONVERSIÓN DE DELIMITADORES LaTeX (v2) ===\n")
    print("Convirtiendo $...$ a $$...$$ para compatibilidad con Kramdown\n")
    print("Con math_engine: mathjax, Kramdown usa $$ para inline y display.")
    print("La diferencia está en el contexto (inline con texto vs línea propia)\n")

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

    print("\nNOTA: Todos los delimitadores ahora usan $$...$$")
    print("Kramdown distingue inline vs display por contexto.")

if __name__ == '__main__':
    main()
