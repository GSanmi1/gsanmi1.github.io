import os
import re
from pathlib import Path

# Mapeo de tags a categorías
TAG_MAPPING = {
    'burp': (['Past Blogs', 'Web Security'], ['burp-suite', 'web-attacks']),
    'pen': (['Past Blogs', 'Pentesting'], ['penetration-testing', 'security']),
    'thm': (['Past Blogs', 'CTF'], ['tryhackme', 'challenges']),
    'csoft': (['Past Blogs', 'Binary Exploitation'], ['memory-corruption', 'exploits']),
    'C': (['Past Blogs', 'Programming'], ['c-language', 'systems']),
    'redteam': (['Past Blogs', 'Red Team'], ['offensive-security', 'tactics']),
    'assem': (['Past Blogs', 'Assembly'], ['x86', 'reverse-engineering']),
    'redes': (['Past Blogs', 'Networks'], ['networking', 'protocols']),
    'hack': (['Past Blogs', 'Hacking'], ['hacking', 'techniques']),
    'blueteam': (['Past Blogs', 'Blue Team'], ['defensive-security', 'hardening']),
    'otw': (['Past Blogs', 'Wargames'], ['overthewire', 'wargames']),
    'wargame': (['Past Blogs', 'Wargames'], ['challenges', 'ctf']),
    'math': (['Maths'], ['mathematics', 'theory']),
    'matemáticas': (['Maths'], ['mathematics', 'theory']),
    'fuzz': (['Past Blogs', 'Fuzzing'], ['fuzzing', 'testing']),
    'DHA': (['Past Blogs', 'Programming'], ['dharma', 'projects'])
}

def extract_date_from_filename(filename):
    """Extrae YYYY-MM-DD del nombre del archivo"""
    match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
    return match.group(1) if match else '2024-01-01'

def convert_post(filepath, dest_dir):
    """Convierte un post del formato antiguo al nuevo"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error leyendo {filepath}: {e}")
        return False

    # Extraer front matter antiguo
    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not fm_match:
        print(f"Warning: No front matter en {filepath}")
        return False

    old_fm, body = fm_match.groups()

    # Parsear campos
    title_match = re.search(r'title:\s*(.+)', old_fm)
    subtitle_match = re.search(r'subtitle:\s*(.+)', old_fm)
    tags_match = re.search(r'tags:\s*\[(.+?)\]', old_fm)

    # Determinar categorías y tags nuevos
    old_tag = tags_match.group(1).strip() if tags_match else 'pen'
    categories, new_tags = TAG_MAPPING.get(old_tag, (['Past Blogs'], [old_tag]))

    # Inferir fecha del nombre del archivo
    filename = os.path.basename(filepath)
    date = extract_date_from_filename(filename)

    # Extraer título sin comillas extras
    title_text = title_match.group(1).strip() if title_match else 'Untitled'
    # Remover comillas si ya las tiene
    title_text = title_text.strip('"').strip("'")

    # Construir nuevo front matter
    subtitle_line = f'subtitle: "{subtitle_match.group(1).strip()}"\n' if subtitle_match else ''

    new_fm = f"""---
layout: post
title: "{title_text}"
{subtitle_line}date: {date} 09:00:00 +0000
categories: {categories}
tags: {new_tags}
author: German Sanmi
---"""

    # Reconstruir archivo
    new_content = f"{new_fm}\n\n{body}"

    # Escribir en destino
    dest_path = Path(dest_dir) / filename
    try:
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"OK Convertido: {filename:<50} [{old_tag:>12}] -> {categories}")
        return True
    except Exception as e:
        print(f"Error escribiendo {dest_path}: {e}")
        return False

def main():
    source_dir = r"C:\Users\sanmi\Documents\DocumentosDeGerman\GitRepos\gsanmi1.github.io\_posts"
    dest_dir = r"C:\Users\sanmi\Documents\DocumentosDeGerman\GitRepos\WebTests\_posts"

    print("=== MIGRACIÓN DE POSTS ===\n")
    print(f"Origen: {source_dir}")
    print(f"Destino: {dest_dir}\n")

    success_count = 0
    fail_count = 0

    files = [f for f in os.listdir(source_dir) if f.endswith('.md')]
    total_files = len(files)

    print(f"Total de posts a migrar: {total_files}\n")

    for i, filename in enumerate(files, 1):
        filepath = os.path.join(source_dir, filename)
        print(f"[{i}/{total_files}] ", end='')
        if convert_post(filepath, dest_dir):
            success_count += 1
        else:
            fail_count += 1

    print(f"\n=== RESUMEN ===")
    print(f"Exitosos: {success_count}")
    print(f"Fallidos: {fail_count}")
    print(f"Total: {total_files}")

if __name__ == '__main__':
    main()
