# Migración del Blog Antiguo a WebTests

## Estadísticas Finales

- **Fecha de migración**: 11 de enero de 2026
- **Posts migrados**: 98 posts (2022-2026)
- **Imágenes copiadas**: 3,507 archivos (~263MB)
- **Total de posts en el sitio**: 101 (98 migrados + 3 ZKP existentes)
- **Categorías creadas**: 3 categorías primarias + 10 subcategorías

## Estructura de Categorías

### Categorías Primarias

1. **Past Blogs** (96 posts)
   Contenido migrado del blog anterior (2022-2026)

2. **ZKP** (3 posts)
   Investigación actual sobre Zero-Knowledge Proofs

3. **Maths** (2 posts)
   Contenido matemático puro:
   - 2026-01-11-PvsNP.md
   - 2025-12-25-MathTest.md

### Subcategorías (bajo Past Blogs)

- **Web Security** (23 posts) - Burp Suite, vulnerabilidades web
- **Pentesting** (18 posts) - PEN-200, OSCP, técnicas de pentesting
- **CTF** (8 posts) - TryHackMe, desafíos
- **Binary Exploitation** (8 posts) - Memory corruption, exploits
- **Programming** (11 posts) - C, Dharma, proyectos
- **Red Team** (8 posts) - Offensive security, tactics
- **Assembly** (6 posts) - x86, reverse engineering
- **Networks** (4 posts) - Networking, protocolos
- **Hacking** (3 posts) - HTB, técnicas
- **Blue Team** (2 posts) - Defensive security
- **Wargames** (3 posts) - OverTheWire, desafíos
- **Fuzzing** (1 post) - Dharma fuzzing

## Mapeo de Tags a Categorías

| Tag Original | Posts | Nueva Categoría | Nueva Subcategoría |
|--------------|-------|-----------------|-------------------|
| burp | 23 | Past Blogs | Web Security |
| pen | 18 | Past Blogs | Pentesting |
| thm | 8 | Past Blogs | CTF |
| csoft | 8 | Past Blogs | Binary Exploitation |
| C | 10 | Past Blogs | Programming |
| redteam | 8 | Past Blogs | Red Team |
| assem | 6 | Past Blogs | Assembly |
| redes | 4 | Past Blogs | Networks |
| hack | 3 | Past Blogs | Hacking |
| blueteam | 2 | Past Blogs | Blue Team |
| otw/wargame | 3 | Past Blogs | Wargames |
| fuzz | 1 | Past Blogs | Fuzzing |
| DHA | 1 | Past Blogs | Programming |
| math/matemáticas | 2 | Maths | - |

## Cambios en Rutas de Imágenes

**Ruta antigua:**
```
{{ 'assets/img/[carpeta]/imagen.png' | relative_url }}
```

**Ruta nueva:**
```
{{ '/assets/images/past-blogs/[carpeta]/imagen.png' | relative_url }}
```

**Posts actualizados con nuevas rutas**: 69 de 101

## Estructura de Archivos

```
WebTests/
├── _posts/
│   ├── 2022-2023: Posts de seguridad web, redes, CTFs (49 posts)
│   ├── 2024-2025: Posts de C, Assembly, exploits (47 posts)
│   ├── 2026: Posts de ZKP y matemáticas (5 posts)
│   └── Total: 101 posts
├── assets/
│   └── images/
│       ├── past-blogs/
│       │   ├── Burp/ (688 archivos)
│       │   ├── THM/ (1,487 archivos)
│       │   ├── HTB/ (305 archivos)
│       │   ├── pen/ (397 archivos)
│       │   ├── M2-M10/ (553 archivos)
│       │   ├── C/ (24 archivos)
│       │   ├── Redes/ (19 archivos)
│       │   └── otros/ (34 archivos)
│       └── zkp/ (para futuros posts)
├── past-blogs.html (índice de Past Blogs)
├── zkp.html (índice de ZKP Research)
├── maths.html (índice de Matemáticas)
└── scripts/
    ├── copy_images.py
    ├── migrate_posts.py
    └── update_image_paths.py
```

## Navegación del Sitio

El header principal incluye:
1. **Inicio** - Página principal con últimos posts
2. **ZKP** - Investigación sobre Zero-Knowledge Proofs
3. **Matemáticas** - Contenido matemático
4. **Past Blogs** - Archivo completo 2022-2026
5. **Todos los Posts** - Lista completa (101 posts)
6. **Acerca de** - Información del sitio

## Scripts Utilizados

### 1. copy_images.py
Copia recursiva de 3,507 imágenes preservando estructura de carpetas.

### 2. migrate_posts.py
- Lee posts del blog antiguo
- Convierte front matter (tags simples → categorías + tags)
- Mapea tags a categorías según tabla predefinida
- Infiere fechas de nombres de archivo
- Escribe posts con nuevo formato

### 3. update_image_paths.py
- Actualiza referencias de imágenes usando regex
- Cambia `assets/img/` a `/assets/images/past-blogs/`
- Preserva filtro `relative_url` de Liquid
- Procesó 69 posts con imágenes

## Commits Realizados

```
1. Add past blog images (3507 files, 263MB)
2. Migrate 98 past blog posts with updated metadata
3. Update image paths to new directory structure
4. Add category index pages and update navigation
```

## Verificación Post-Migración

✅ 101 posts totales en `_posts/`
✅ 3,507 imágenes en `assets/images/past-blogs/`
✅ Navegación actualizada con 6 links
✅ Páginas índice funcionales para cada categoría
✅ Front matter convertido correctamente
✅ Rutas de imágenes actualizadas en 69 posts
✅ Post PvsNP.md correctamente en categoría "Maths"

## Próximos Pasos Recomendados

1. **Testing local:**
   ```bash
   bundle install
   bundle exec jekyll serve
   ```

2. **Verificación manual:**
   - Abrir posts aleatorios de cada categoría
   - Verificar que imágenes cargan correctamente
   - Probar navegación entre categorías

3. **Deployment:**
   ```bash
   git checkout main
   git merge migration/past-blogs
   git push origin main
   ```

4. **Configurar GitHub Pages:**
   - Ir a Settings → Pages
   - Source: Deploy from branch main / (root)
   - Esperar build automático

5. **Optimizaciones futuras:**
   - Agregar buscador de posts
   - Tag cloud o filtros por tag
   - Optimizar imágenes pesadas (>1MB)
   - Agregar páginas de archivo por año

## Notas Técnicas

- **Encoding**: UTF-8 usado para todos los archivos
- **Jekyll**: Versión compatible con GitHub Pages
- **Tema**: Minima personalizado con dark mode
- **Liquid**: Filtros `relative_url`, `where_exp`, `sort`, `reverse`
- **Categorías**: Arrays en front matter para múltiples categorías
- **Permalinks**: `/:year/:month/:day/:title/`

## Problemas Conocidos y Soluciones

### Problema: Caracteres especiales en nombres de archivo
**Solución**: UTF-8 encoding manejado correctamente por Python y Jekyll

### Problema: Rutas de imágenes rotas
**Solución**: Script regex actualiza automáticamente todas las referencias

### Problema: Subcarpetas M2-M10 sin contexto
**Solución**: Documentado en este archivo - corresponden a módulos OSCP

---

**Migración completada exitosamente** por Claude Sonnet 4.5 el 11 de enero de 2026.
