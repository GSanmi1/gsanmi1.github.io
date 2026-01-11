# Configuración de MathJax para Renderizado LaTeX

## Problemas Identificados y Soluciones

### ❌ Problema 1: Orden Incorrecto de Carga

**Error Original:**
```html
<!-- INCORRECTO -->
<script src="mathjax.js" async></script>
<script>
    MathJax = { /* configuración */ };
</script>
```

**Solución Aplicada:**
```html
<!-- CORRECTO -->
<script>
    window.MathJax = { /* configuración */ };
</script>
<script src="mathjax.js" async></script>
```

**Por qué:** La configuración debe definirse **ANTES** de cargar el script MathJax. Como el script se carga de forma asíncrona (`async`), si la configuración va después, MathJax puede cargarse antes de que la configuración esté disponible, usando los valores por defecto.

---

### ❌ Problema 2: Uso de `MathJax` en lugar de `window.MathJax`

**Error Original:**
```javascript
MathJax = { tex: { ... } };
```

**Solución Aplicada:**
```javascript
window.MathJax = { tex: { ... } };
```

**Por qué:** Usar `window.MathJax` asegura que la configuración se defina en el ámbito global correcto y esté disponible cuando MathJax se inicialice.

---

### ❌ Problema 3: Renderizador Inadecuado

**Antes:**
```
tex-mml-chtml.js
```

**Ahora:**
```
tex-svg.js
```

**Por qué:**
- `tex-svg.js` genera salida SVG, que es más compatible y escalable
- Mejor rendimiento en navegadores modernos
- Menos problemas de fuentes y rendering
- SVG se adapta mejor a temas oscuros

---

### ❌ Problema 4: Falta de Protección para Bloques de Código

**Antes:**
```javascript
skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']
```

**Ahora:**
```javascript
skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
```

**Por qué:** Sin `'code'` en la lista, MathJax podría intentar procesar símbolos matemáticos dentro de bloques de código, lo cual no es deseado.

---

## Configuración Final Completa

```html
<!-- MathJax Configuration (MUST be BEFORE loading the script) -->
<script>
    window.MathJax = {
        tex: {
            // Delimitadores para matemáticas inline
            inlineMath: [['$', '$'], ['\\(', '\\)']],

            // Delimitadores para matemáticas en display
            displayMath: [['$$', '$$'], ['\\[', '\\]']],

            // Procesar escapes (\$, \%, etc.)
            processEscapes: true,

            // Procesar entornos LaTeX (align, matrix, etc.)
            processEnvironments: true,

            // Numeración automática estilo AMS
            tags: 'ams',

            // Macros personalizadas
            macros: {
                N: "\\mathbb{N}",  // Naturales
                Z: "\\mathbb{Z}",  // Enteros
                R: "\\mathbb{R}",  // Reales
                C: "\\mathbb{C}"   // Complejos
            }
        },
        options: {
            // Etiquetas HTML a ignorar
            skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
        },
        svg: {
            // Caché global de fuentes para mejor rendimiento
            fontCache: 'global'
        },
        startup: {
            // Callback cuando MathJax esté listo
            ready: () => {
                console.log('MathJax is loaded and ready!');
                MathJax.startup.defaultReady();
            }
        }
    };
</script>
<!-- MathJax Library -->
<script type="text/javascript" id="MathJax-script" async
    src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js">
</script>
```

---

## Sintaxis Soportada

### Matemáticas Inline
```markdown
El número $\pi$ es aproximadamente $3.14159$.
```

Renderiza: El número π es aproximadamente 3.14159.

### Matemáticas Display (Centradas)
```markdown
$$
E = mc^2
$$
```

Renderiza una ecuación centrada.

### Ecuaciones con Numeración
```markdown
$$
\begin{equation}
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
\end{equation}
$$
```

### Matrices
```markdown
$$
A = \begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$
```

### Sistemas de Ecuaciones
```markdown
$$
\begin{cases}
x + y = 5 \\
x - y = 1
\end{cases}
$$
```

### Uso de Macros Personalizadas
```markdown
Sea $n \in \N$ un número natural...
```

Equivale a: `$n \in \mathbb{N}$`

---

## Estilos CSS Agregados

Para mejorar la visualización en tema oscuro:

```css
/* Contenedores MathJax */
mjx-container {
    display: inline-block;
    margin: 0.5em 0;
}

mjx-container[display="true"] {
    display: block;
    margin: 1em 0;
    text-align: center;
}

/* Color legible en fondo oscuro */
.MathJax, .MathJax_Display, .MathJax_Preview {
    color: var(--text-color) !important;
}

/* Ecuaciones largas con scroll horizontal */
.post-content mjx-container[jax="SVG"][display="true"] {
    display: block;
    margin: 1.5em auto;
    overflow-x: auto;
    overflow-y: hidden;
    max-width: 100%;
}

/* Scrollbar personalizado para ecuaciones */
mjx-container::-webkit-scrollbar {
    height: 8px;
}

mjx-container::-webkit-scrollbar-thumb {
    background: var(--border-color);
    border-radius: 4px;
}
```

---

## Testing

Para verificar que MathJax funciona correctamente:

1. **Abrir la consola del navegador** (F12)
2. **Buscar el mensaje**: `"MathJax is loaded and ready!"`
3. **Verificar que las ecuaciones se renderizan** en el post PvsNP
4. **Comprobar que no hay errores** en la consola

### Ejemplo de Test Rápido

Agregar este código a un post:

```markdown
Inline: $E = mc^2$

Display:
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

Con macro: $n \in \N$
```

Si todo funciona, deberías ver:
- La ecuación inline integrada en el texto
- La integral centrada y más grande
- El símbolo de naturales ℕ renderizado correctamente

---

## Recursos Adicionales

- **Documentación MathJax 3**: https://docs.mathjax.org/en/latest/
- **LaTeX Cheat Sheet**: https://wch.github.io/latexsheet/
- **Símbolos matemáticos**: https://www.cmor-faculty.rice.edu/~heinken/latex/symbols.pdf
- **MathJax CDN**: https://cdn.jsdelivr.net/npm/mathjax@3/

---

## Notas Importantes

1. **Rendimiento**: MathJax se carga de forma asíncrona para no bloquear la carga de la página
2. **Compatibilidad**: SVG es compatible con todos los navegadores modernos
3. **Tema oscuro**: Los estilos CSS aseguran legibilidad en fondo oscuro
4. **Responsive**: Las ecuaciones largas tienen scroll horizontal en móviles
5. **Cache**: Las fuentes se cachean globalmente para mejor rendimiento en múltiples páginas

---

**Última actualización**: 11 de enero de 2026
