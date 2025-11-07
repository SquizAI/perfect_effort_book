#!/usr/bin/env python3
"""
Remove old HTML span styling and add blue headers using LaTeX
"""

from pathlib import Path
import re

CHAPTERS_DIR = Path(__file__).parent.parent / '03_Book_Chapters'

def remove_old_styling(content):
    """Remove HTML span tags from headers"""
    # Remove <span style="color: #0969DA">text</span> from headers
    content = re.sub(r'## <span style="color: #0969DA">(.*?)</span>', r'## \1', content)
    content = re.sub(r'### <span style="color: #0969DA">(.*?)</span>', r'### \1', content)
    return content

def add_latex_blue_headers(content):
    """Add blue color to ## and ### headers using LaTeX math"""

    lines = content.split('\n')
    result = []

    for line in lines:
        # Color ## headers (major sections) in blue using LaTeX
        if line.startswith('## ') and not line.startswith('##  ') and not '$$' in line:
            header_text = line.replace('## ', '').strip()
            # Replace spaces with \space for LaTeX
            latex_text = header_text.replace(' ', r' \space ')
            result.append(f'## $${{\\color{{blue}}{latex_text}}}$$')

        # Color ### headers (subsections) in blue using LaTeX
        elif line.startswith('### ') and not line.startswith('###  ') and not '$$' in line:
            header_text = line.replace('### ', '').strip()
            # Replace spaces with \space for LaTeX
            latex_text = header_text.replace(' ', r' \space ')
            result.append(f'### $${{\\color{{blue}}{latex_text}}}$$')

        else:
            result.append(line)

    return '\n'.join(result)

def fix_chapter(filepath):
    """Remove old styling and add LaTeX blue headers"""

    print(f"🔧 Fixing {filepath.name}...")

    with open(filepath, 'r') as f:
        content = f.read()

    # Remove old HTML span styling
    content = remove_old_styling(content)

    # Add LaTeX blue headers
    content = add_latex_blue_headers(content)

    with open(filepath, 'w') as f:
        f.write(content)

    print(f"✅ Fixed {filepath.name}")
    return True

def main():
    print("╔" + "="*60 + "╗")
    print("║" + " "*15 + "Fix Blue Headers (LaTeX)" + " "*20 + "║")
    print("╚" + "="*60 + "╝\n")

    chapter_files = sorted(CHAPTERS_DIR.glob('chapter_*.md'))

    for filepath in chapter_files[:20]:
        fix_chapter(filepath)

    print("\n✅ All chapter headers now use LaTeX blue formatting!")

if __name__ == "__main__":
    main()
