import re

with open("index.html", "r") as f:
    content = f.read()

# Extract script
match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
if match:
    js_content = match.group(1).strip()
    
    # Replace function definitions with window.funcName = function
    # e.g., function showResults(href) -> window.showResults = function(href)
    js_content = re.sub(r'^(\s*)function\s+([a-zA-Z0-9_]+)\s*\(', r'\1window.\2 = function(', js_content, flags=re.MULTILINE)
    
    # Also change const panelMenu = ... to window.panelMenu = ...
    js_content = re.sub(r'const\s+panelMenu\s*=\s*\(\)\s*=>\s*\{', r'window.panelMenu = function() {', js_content)
    
    with open("drupal/scripts.js", "w") as f:
        f.write(js_content)
    
    # Update index.html
    new_content = content[:match.start()] + '<script src="scripts.js"></script>' + content[match.end():]
    with open("drupal/index.html", "w") as f:
        f.write(new_content)
        
    print("Done")
else:
    print("No script found")
