---
description: Translate Chinese blog posts to English
allowed-tools: Read, Write, Glob, Bash, Edit
---

Translate Chinese blog posts from `content/zh/posts/` to English and save them in `content/en/posts/`.

## Instructions

1. First, list all `.md` files in `content/zh/posts/` and `content/en/posts/` to find which Chinese posts don't have an English version yet.

2. For each untranslated Chinese post:
   - Read the Chinese markdown file
   - Translate the **entire content** (body text) to natural, fluent English
   - Keep the front matter structure, but translate:
     - `title` to English
     - `categories` values to English (e.g. "thinking" stays as "thinking", "学习" → "learning", "工具" → "tools")
     - `tags` values to English
   - Keep these front matter fields unchanged: `date`, `lastmod`, `draft`, `slug`, `authors`
   - Preserve all markdown formatting, links, image references, and shortcodes exactly as-is
   - Write the translated file to `content/en/posts/` with the **same filename**

3. Translation style guidelines:
   - Use natural, readable English — not literal translation
   - Preserve the author's personal voice and tone
   - Keep Chinese proper nouns, book titles, and cultural references with brief context where helpful
   - Do not add or remove content

4. After translating all posts, report which files were translated.

## Arguments

`$ARGUMENTS` supports the following:
- No arguments: translate all untranslated Chinese posts
- A filename (e.g., `blog-12.md`): translate only that specific file
- `--all`: re-translate ALL posts, including ones that already have an English version (overwrite existing translations)
- `--force <filename>`: re-translate a specific file even if it already has an English version
