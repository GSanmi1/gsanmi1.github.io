# Authoring guide

How to write posts for the notebook. Nothing here changes how your LaTeX
works — math still runs on **MathJax 3** with the same macros and delimiters
as before.

## Front matter

Every post lives in `_posts/` as `YYYY-MM-DD-Title.md` and starts with:

```yaml
---
layout: post
title: "3. Euclidean Spaces"
subtitle: "Introduction to Euclidean Spaces. Metric Spaces"
date: 2026-06-16 09:00:00 +0000
categories: ['Maths', 'analisis_rudin']   # free-form, optional
tags: ['Maths']                           # shown as chips at the foot
author: German Sanmi
subject: real-analysis                    # <-- files the post under a subject
lang: en                                  # en | es  (shows a small badge)
---
```

The **`subject:`** field is what places a post in the navigation. Valid slugs
live in [`_data/verticals.yml`](_data/verticals.yml):

| Vertical | Subject slugs |
| --- | --- |
| Foundations | `logic-set-theory`, `number-systems`, `graph-theory` |
| Algebra | `linear-algebra`, `abstract-algebra` |
| Analysis | `real-analysis`, `complex-analysis`, `differential-equations`, `functional-analysis`, `measure-integration` |
| Geometry & Topology | `geometry`, `differential-geometry`, `topology` |
| Probability & Statistics | `probability`, `statistical-inference`, `stochastic-processes` |
| Applied Mathematics | `numerical-analysis`, `optimization`, `modeling-computation` |

To add a new subject area, edit `_data/verticals.yml` — the sidebar, landing
page and vertical pages all update automatically.

## Math

Inline math with `$ ... $`, display math with `$$ ... $$`. The macros defined
in `_layouts/default.html` are available everywhere, e.g. `\R \N \Z \C \E
\Var \argmax \negl \Set{...}`. Display equations are centred, get vertical
breathing room, and scroll horizontally on small screens.

## Theorem environments

Wrap the statement in a `<div>` whose class is the environment name. The
**first bold run** becomes the label. Two rules for the Markdown inside to be
parsed (this site uses kramdown with `parse_block_html`):

1. Put the block at the **top level** of the post — don't nest it inside
   another `<div>`.
2. `markdown="1"` is optional but harmless; include it if in doubt.

```html
<div class="theorem" markdown="1">
**Theorem 2.3 (Bolzano–Weierstrass).** Every bounded sequence in $\R^n$ has a
convergent subsequence.
</div>

<div class="proof" markdown="1">
**Proof.** Bisect the bounding box repeatedly ... hence the limit exists.
</div>
```

Available classes:

| Class | Style |
| --- | --- |
| `theorem`, `lemma`, `proposition`, `corollary` | tinted background, italic body, accent label |
| `definition` | left border, upright body |
| `remark`, `example` | soft, muted |
| `proof` | upright; automatically closed with a `∎` tombstone |

Numbering is manual (write `Theorem 2.3.` yourself) — this keeps full control
and avoids fragile auto-numbering across separate notes.

## Tufte-style margin notes (optional)

```html
Some prose.<span class="sidenote">This floats into the right margin on wide
screens, and inlines on narrow ones.</span>
```

## Local preview

```bash
bundle exec jekyll serve --livereload
```

then open <http://localhost:4000>.
