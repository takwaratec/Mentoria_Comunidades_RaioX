import os
import re

docs_dir = "/Users/fabiotakwara/Documents/GitHub/Mentoria_Comunidades_RaioX/docs"

html_link_pattern = re.compile(r'href="([^"]+)\.html"')
md_link_pattern = re.compile(r'\]\(([^)]+)\.html\)')

for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content
            
            # Replace HTML href attributes
            # Ex: href="03_ESTRUTURA_FORMATO/PASSO_03_Estrutura.html" -> href="03_ESTRUTURA_FORMATO/PASSO_03_Estrutura.md"
            def replace_href(match):
                path = match.group(1)
                if not (path.startswith('http') or path.startswith('mailto') or path.startswith('tel')):
                    return f'href="{path}.md"'
                return match.group(0)

            content = html_link_pattern.sub(replace_href, content)

            # Replace markdown links
            # Ex: [link](PASSO_05_Precificacao.html) -> [link](PASSO_05_Precificacao.md)
            def replace_md_link(match):
                path = match.group(1)
                if not (path.startswith('http') or path.startswith('mailto') or path.startswith('tel')):
                    return f']({path}.md)'
                return match.group(0)

            content = md_link_pattern.sub(replace_md_link, content)

            if content != original_content:
                print(f"Fixing links in {file_path}")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
