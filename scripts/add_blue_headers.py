#!/usr/bin/env python3
"""
Add blue color to section headers using HTML
"""

from pathlib import Path

CHAPTERS_DIR = Path(__file__).parent.parent / '03_Book_Chapters'

def colorize_headers(content):
    """Add blue color to ## and ### headers"""
    
    lines = content.split('\n')
    result = []
    
    for line in lines:
        # Color ## headers (major sections) in blue
        if line.startswith('## ') and not line.startswith('##  '):
            header_text = line.replace('## ', '')
            result.append(f'## <span style="color: #0969DA">{header_text}</span>')
        
        # Color ### headers (subsections) in blue
        elif line.startswith('### ') and not line.startswith('###  '):
            header_text = line.replace('### ', '')
            result.append(f'### <span style="color: #0969DA">{header_text}</span>')
        
        else:
            result.append(line)
    
    return '\n'.join(result)

def enhance_chapter(filepath):
    """Add blue headers to chapter"""
    
    print(f"🔵 Adding blue headers to {filepath.name}...")

    with open(filepath, 'r') as f:
        content = f.read()

    content = colorize_headers(content)

    with open(filepath, 'w') as f:
        f.write(content)

    print(f"✅ Enhanced {filepath.name}")
    return True

def main():
    print("╔" + "="*60 + "╗")
    print("║" + " "*18 + "Blue Header Tool" + " "*26 + "║")
    print("╚" + "="*60 + "╝\n")

    chapter_files = sorted(CHAPTERS_DIR.glob('chapter_*.md'))

    for filepath in chapter_files[:20]:
        enhance_chapter(filepath)

    print("\n✅ All chapter headers are now blue!")

if __name__ == "__main__":
    main()
