# LaTeX Rendering Fix Summary

## Problem
Kramdown was processing Markdown special characters (underscores, asterisks, pipes) inside LaTeX math expressions before MathJax could render them, causing incorrect rendering.

Example: `$\mathrm{Time}_{M}(x)$` was being rendered with the underscore interpreted as italic markdown.

## Solution

### 1. Delimiter Conversion (fix_latex_delimiters_v2.py)
Converted all inline math delimiters from single `$...$` to double `$$...$$`:
- **Before:** `$\mathrm{Time}_{M}(x)$`
- **After:** `$$\mathrm{Time}_{M}(x)$$`

Display math `$$...$$` remains unchanged.

**Stats:**
- 24 posts updated with LaTeX content
- 74 posts had no inline math
- Total: 98 posts processed

### 2. Kramdown Configuration (_config.yml)
```yaml
kramdown:
  math_engine: mathjax  # Protects $$ content from Markdown processing
  math_engine_opts:
    preview: true
    preview_as_code: false
  parse_block_html: true
```

This ensures Kramdown:
- Recognizes `$$...$$` as math delimiters
- Protects content inside from Markdown processing
- Outputs MathJax-compatible HTML

### 3. MathJax Configuration (_layouts/default.html)
Updated MathJax 3 configuration to:
- Accept `$$...$$` for inline math (matching new delimiter format)
- Process Kramdown's HTML output (script tags)
- Remove 'script' from skipHtmlTags
- Add processing for Kramdown-generated content

```javascript
tex: {
    inlineMath: [['$$', '$$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    // ... other settings
}
```

## How It Works

1. **Markdown files** contain `$$...$$` for both inline and display math
2. **Kramdown** recognizes these delimiters (due to `math_engine: mathjax`)
3. **Kramdown protects** the content from Markdown processing (no underscore → italic conversion)
4. **Kramdown outputs** special HTML that MathJax can process
5. **MathJax 3** renders the math expressions correctly

## Testing

To test the fix:

```bash
cd "C:\Users\sanmi\Documents\DocumentosDeGerman\GitRepos\WebTests"
bundle exec jekyll serve
```

Then open your browser to `http://localhost:4000` and check:
- [Maths section](http://localhost:4000/maths.html)
- [PvsNP post](http://localhost:4000/2026/01/11/PvsNP/)

Verify that expressions like `$$\mathrm{Time}_{M}(x)$$` render correctly with:
- Subscripts showing properly (_{M})
- No italic text from underscores
- Proper mathematical formatting

## Files Modified

1. `_config.yml` - Updated Kramdown configuration
2. `_layouts/default.html` - Updated MathJax configuration
3. `_posts/*.md` - 24 posts with inline math converted from `$...$` to `$$...$$`

## Scripts Created

- `scripts/fix_latex_delimiters_v2.py` - Conversion script (executed successfully)
- `scripts/fix_latex_delimiters.py` - Previous version (deprecated)
