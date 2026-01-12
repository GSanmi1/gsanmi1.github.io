# ZKP Research & Notes - GitHub Pages

Sitio web personal para documentar investigaciones, apuntes y estudios sobre Zero-Knowledge Proofs (ZKP) y criptografía avanzada.

## Estructura del Proyecto

```
WebTests/
├── _config.yml          # Configuración principal de Jekyll
├── Gemfile             # Dependencias de Ruby
├── index.html          # Página de inicio
├── posts.html          # Archivo de todos los posts
├── about.md            # Página "Acerca de"
├── _layouts/           # Plantillas HTML
│   ├── default.html    # Layout base
│   └── post.html       # Layout para posts
├── _posts/             # Artículos del blog
│   └── YYYY-MM-DD-titulo.md
├── _includes/          # Componentes reutilizables
└── assets/             # Recursos estáticos
    ├── css/
    │   └── style.css
    ├── js/
    └── images/
```

## Configuración Inicial

### 1. Instalar Ruby y Jekyll (si no lo tienes)

**En Windows:**
```bash
# Descargar e instalar Ruby+Devkit desde https://rubyinstaller.org/
# Después de instalar, ejecutar:
gem install jekyll bundler
```

**En Linux/Mac:**
```bash
sudo apt install ruby-full build-essential zlib1g-dev  # Ubuntu/Debian
gem install jekyll bundler
```

### 2. Instalar Dependencias

```bash
cd C:\Users\sanmi\Documents\DocumentosDeGerman\GitRepos\WebTests
bundle install
```

### 3. Probar Localmente

```bash
bundle exec jekyll serve
```

Visita `http://localhost:4000` en tu navegador.

## Publicar en GitHub Pages

### Opción 1: Repositorio de Usuario/Organización (gsanmi1.github.io)

1. **Crear repositorio** en GitHub con el nombre exacto: `gsanmi1.github.io`

2. **Actualizar _config.yml:**
```yaml
url: "https://gsanmi1.github.io"
baseurl: ""
```

3. **Subir el código:**
```bash
git add .
git commit -m "Initial commit: ZKP Research site"
git branch -M main
git remote add origin https://github.com/gsanmi1/gsanmi1.github.io.git
git push -u origin main
```

4. **Configurar GitHub Pages:**
   - Ve a Settings → Pages
   - Source: Deploy from a branch
   - Branch: main / (root)
   - Save

5. El sitio estará disponible en: `https://gsanmi1.github.io`

### Opción 2: Repositorio de Proyecto

1. **Crear repositorio** con cualquier nombre, ej: `zkp-blog`

2. **Actualizar _config.yml:**
```yaml
url: "https://gsanmi1.github.io"
baseurl: "/zkp-blog"  # Nombre del repositorio
```

3. **Subir código y configurar** (mismo proceso)

4. El sitio estará en: `https://gsanmi1.github.io/zkp-blog`

## Crear Nuevos Posts

### 1. Formato de Archivo

Los posts deben seguir la nomenclatura:
```
_posts/YYYY-MM-DD-titulo-del-post.md
```

### 2. Plantilla de Post

```markdown
---
layout: post
title: "Título del Post"
date: 2026-01-11 10:00:00 +0000
categories: [Categoría1, Categoría2]
tags: [tag1, tag2, tag3]
author: German Sanmi
---

# Título Principal

Introducción del post...

## Sección 1

Contenido...

### Subsección

Más contenido...

## Código

\`\`\`python
def ejemplo():
    return "Hola ZKP"
\`\`\`

## Conclusión

Cierre del post...

---

*Nota final o call-to-action*
```

### 3. Syntax Highlighting

Jekyll soporta syntax highlighting para múltiples lenguajes:

````markdown
```python
# Código Python
```

```javascript
// Código JavaScript
```

```rust
// Código Rust
```
````

## Personalización

### Cambiar Colores

Edita [assets/css/style.css](assets/css/style.css):

```css
:root {
    --primary-color: #2c3e50;      /* Color principal */
    --secondary-color: #3498db;     /* Color secundario */
    --link-color: #0366d6;          /* Color de enlaces */
}
```

### Añadir Google Analytics

En [_config.yml](_config.yml):

```yaml
google_analytics: UA-XXXXXXXXX-X
```

### Cambiar Tema

GitHub Pages soporta varios temas. En [_config.yml](_config.yml):

```yaml
theme: minima  # o minimal-mistakes, jekyll-theme-cayman, etc.
```

## Estructura de un Post Típico

```markdown
---
layout: post
title: "ZK-SNARKs vs ZK-STARKs: Comparativa Técnica"
date: 2026-01-12 15:30:00 +0000
categories: [ZKP, Comparativas]
tags: [snarks, starks, análisis]
author: German Sanmi
excerpt: "Análisis detallado de las diferencias técnicas entre SNARKs y STARKs"
---

Contenido aquí...
```

## Front Matter Disponible

| Campo | Descripción | Requerido |
|-------|-------------|-----------|
| `layout` | Layout a usar (`post` o `default`) | Sí |
| `title` | Título del post | Sí |
| `date` | Fecha y hora de publicación | Sí |
| `categories` | Categorías (lista) | No |
| `tags` | Tags (lista) | No |
| `author` | Autor del post | No |
| `excerpt` | Resumen personalizado | No |

## Comandos Útiles

```bash
# Construir el sitio
bundle exec jekyll build

# Servir localmente con recarga automática
bundle exec jekyll serve --livereload

# Servir en modo borrador (incluye posts en _drafts/)
bundle exec jekyll serve --drafts

# Limpiar archivos generados
bundle exec jekyll clean

# Ver versión de Jekyll
bundle exec jekyll --version
```

## Borradores

Para posts en progreso, crea una carpeta `_drafts/`:

```
_drafts/
└── titulo-del-borrador.md
```

No necesitan fecha en el nombre. Para previsualizarlos:
```bash
bundle exec jekyll serve --drafts
```

## Tips y Mejores Prácticas

### 1. Nombres de Archivo
- Usa kebab-case: `mi-post-sobre-zkp.md`
- Incluye la fecha: `2026-01-11-mi-post.md`
- Sé descriptivo pero conciso

### 2. Imágenes
Guarda imágenes en `assets/images/`:
```markdown
![Descripción](/assets/images/diagrama-zkp.png)
```

### 3. Matemáticas
Para ecuaciones, usa MathJax (añadir a `_layouts/post.html`):
```html
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
```

Luego en posts:
```markdown
$$e^{i\pi} + 1 = 0$$
```

### 4. Enlaces Internos
```markdown
[Ver post anterior]({% post_url 2026-01-10-zkp-ecosystem %})
```

### 5. Excerpts Automáticos
Jekyll usa el primer párrafo como excerpt por defecto. Para personalizar, añade:
```markdown
---
excerpt: "Tu resumen personalizado aquí"
---
```

O usa el separador:
```markdown
Texto del excerpt...

<!--more-->

Resto del contenido...
```

## Troubleshooting

### Error: "Could not find gem 'github-pages'"
```bash
bundle update
bundle install
```

### El sitio no se actualiza en GitHub Pages
- Verifica que el branch correcto esté seleccionado en Settings → Pages
- Los cambios pueden tardar 1-2 minutos en reflejarse
- Revisa el tab "Actions" para ver si hay errores de build

### Estilos no se cargan
- Asegúrate que `baseurl` en `_config.yml` esté configurado correctamente
- Usa `{{ '/assets/css/style.css' | relative_url }}` en lugar de rutas absolutas

## Recursos Adicionales

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Markdown Cheatsheet](https://www.markdownguide.org/cheat-sheet/)
- [Liquid Template Language](https://shopify.github.io/liquid/)

## Actualizar Información Personal

No olvides actualizar en [_config.yml](_config.yml):

```yaml
title: "ZKP Research & Notes"
author: "Tu Nombre"
email: tu-email@example.com
github_username: tu-usuario
```

Y en [about.md](about.md) tu información personal.

## Licencia

Siéntete libre de usar esta plantilla para tu propio blog. El contenido de los posts de ejemplo es de dominio público para fines educativos.

---

**¡Happy Blogging sobre ZKP! 🔐✨**

Para preguntas o mejoras, abre un issue en GitHub.
