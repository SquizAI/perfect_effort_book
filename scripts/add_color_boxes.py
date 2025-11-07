#!/usr/bin/env python3
"""
Add colorful GitHub callout boxes to enhance visual appeal
"""

from pathlib import Path
import re

CHAPTERS_DIR = Path(__file__).parent.parent / '03_Book_Chapters'

def add_color_callouts(content):
    """Wrap key sections in colored callouts"""
    
    lines = content.split('\n')
    enhanced = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Wrap comparison sections (✅/❌) in WARNING callouts
        if ('❌' in line or '✅' in line) and '**' in line:
            # Start a warning callout for the comparison
            if i == 0 or not lines[i-1].startswith('>'):
                enhanced.append('')
                enhanced.append('> [!WARNING]')
            enhanced.append(f'> {line}')
            i += 1
            continue
            
        # Wrap "Rule #" sections in IMPORTANT callouts  
        if line.startswith('## Rule #'):
            enhanced.append('')
            enhanced.append('> [!IMPORTANT]')
            enhanced.append(f'> {line}')
            enhanced.append('>')
            i += 1
            continue
        
        # Wrap key takeaways in TIP callouts
        if 'remember' in line.lower() or 'key takeaway' in line.lower() or 'the bottom line' in line.lower():
            if line.startswith('##'):
                enhanced.append('')
                enhanced.append('> [!TIP]')
                enhanced.append(f'> {line}')
                i += 1
                continue
                
        # Regular line
        enhanced.append(line)
        i += 1
    
    return '\n'.join(enhanced)

def enhance_chapter(filepath):
    """Add colored callouts to chapter"""
    
    print(f"🎨 Adding color boxes to {filepath.name}...")

    with open(filepath, 'r') as f:
        content = f.read()

    content = add_color_callouts(content)

    with open(filepath, 'w') as f:
        f.write(content)

    print(f"✅ Enhanced {filepath.name}")
    return True

def main():
    print("╔" + "="*60 + "╗")
    print("║" + " "*16 + "Color Box Styling Tool" + " "*22 + "║")
    print("╚" + "="*60 + "╝\n")

    chapter_files = sorted(CHAPTERS_DIR.glob('chapter_*.md'))

    for filepath in chapter_files[:20]:
        enhance_chapter(filepath)

    print("\n✅ All chapters enhanced with colorful callouts!")

if __name__ == "__main__":
    main()
