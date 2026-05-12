import os
import glob
from pathlib import Path
import re

def simple_markdown(text):
    # Headers
    text = re.sub(r'^# (.*)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.*)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.*)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    
    # Bold / Italic
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    
    # Blockquotes
    text = re.sub(r'^> (.*)$', r'<blockquote>\1</blockquote>', text, flags=re.MULTILINE)
    
    # Lists
    text = re.sub(r'^\d+\. (.*)$', r'<li>\1</li>', text, flags=re.MULTILINE)
    text = re.sub(r'^- (.*)$', r'<li>\1</li>', text, flags=re.MULTILINE)
    text = re.sub(r'(<li>.*?</li>\n)+', lambda m: f"<ul>\n{m.group(0)}</ul>\n", text, flags=re.MULTILINE|re.DOTALL)
    
    # Paragraphs
    paragraphs = text.split('\n\n')
    formatted = []
    for p in paragraphs:
        if p.strip() and not p.strip().startswith('<'):
            formatted.append(f'<p>{p.strip()}</p>')
        else:
            formatted.append(p)
            
    return '\n'.join(formatted)

def build_viewer():
    vault_dir = Path("vault")
    md_files = sorted(glob.glob(str(vault_dir / "*.md")))
    
    ideas_html = []
    nav_links = []
    
    for file in md_files:
        path = Path(file)
        content = path.read_text(encoding='utf-8')
        html = simple_markdown(content)
        title = path.stem.replace('_', ' ').title()
        
        icon = "💡"
        if "game" in path.stem: icon = "🎮"
        elif "app" in path.stem: icon = "💻"
        elif "scholarly" in path.stem: icon = "📚"
        
        nav_links.append(f'<li><a href="#{path.stem}">{icon} {title}</a></li>')
        
        ideas_html.append(f'''
        <article id="{path.stem}" class="idea-card">
            <div class="idea-content">
                {html}
            </div>
        </article>
        ''')
        
    template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Idea Vault - Wikipedia Viewer</title>
    <style>
        :root {{
            --bg: #f8f9fa;
            --text: #202122;
            --link: #0645ad;
            --border: #a2a9b1;
            --sidebar: #f8f9fa;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            color: var(--text);
            background: var(--bg);
            margin: 0;
            display: flex;
            line-height: 1.6;
        }}
        #sidebar {{
            width: 280px;
            background: var(--sidebar);
            border-right: 1px solid var(--border);
            padding: 20px;
            height: 100vh;
            position: sticky;
            top: 0;
            overflow-y: auto;
            box-sizing: border-box;
        }}
        #sidebar h2 {{ font-size: 1.2rem; border-bottom: 1px solid var(--border); padding-bottom: 5px; }}
        #sidebar ul {{ list-style: none; padding: 0; }}
        #sidebar li {{ margin-bottom: 10px; }}
        #sidebar a {{ color: var(--link); text-decoration: none; font-size: 0.95rem; }}
        #sidebar a:hover {{ text-decoration: underline; }}
        #content {{
            flex: 1;
            padding: 40px;
            max-width: 900px;
            background: white;
            border-left: 1px solid #eaecf0;
            min-height: 100vh;
            box-sizing: border-box;
        }}
        .idea-card {{
            border-bottom: 1px solid var(--border);
            padding-bottom: 40px;
            margin-bottom: 40px;
        }}
        h1 {{ border-bottom: 1px solid var(--border); padding-bottom: 10px; font-family: "Linux Libertine", "Georgia", "Times", serif; font-weight: normal; margin-top: 0; }}
        h2 {{ font-family: "Linux Libertine", "Georgia", "Times", serif; font-weight: normal; margin-top: 30px; }}
        blockquote {{ border-left: 4px solid var(--border); margin: 0; padding-left: 15px; color: #54595d; font-style: italic; background: #f8f9fa; padding: 10px 15px; }}
        .home-link {{ display: inline-block; margin-bottom: 20px; color: var(--text); text-decoration: none; font-weight: bold; font-family: "Linux Libertine", "Georgia", "Times", serif; }}
        strong {{ color: #000; }}
    </style>
</head>
<body>
    <nav id="sidebar">
        <a href="index.html" class="home-link">← Return to DBCatalog</a>
        <h2>Vault Contents</h2>
        <ul>
            {''.join(nav_links)}
        </ul>
    </nav>
    <main id="content">
        <div style="background: #eaf3ff; border: 1px solid #c8dcf0; padding: 15px; margin-bottom: 40px;">
            <strong>Wikipedia Reader:</strong> This page dynamically renders all extracted nuggets from the <code>/vault/</code> directory.
        </div>
        {''.join(ideas_html)}
    </main>
</body>
</html>'''

    Path("ideas.html").write_text(template, encoding='utf-8')
    print("Generated ideas.html")

if __name__ == "__main__":
    build_viewer()
