#!/usr/bin/env python3
"""
Add premium visual styling with GitHub markdown features
"""

from pathlib import Path
import re

CHAPTERS_DIR = Path(__file__).parent.parent / '03_Book_Chapters'

def add_premium_styling(content):
    """Add visual enhancements to chapter content"""
    
    lines = content.split('\n')
    enhanced = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Add colored callouts for opening sections (after header, before first ## )
        if i > 10 and line.strip() and not line.startswith('#') and not line.startswith('>') and not line.startswith('**[') and not line.startswith('---') and not line.startswith('<'):
            # Check if we're in the opening paragraph (before first ##)
            has_h2_before = any('## ' in lines[j] for j in range(0, i))
            if not has_h2_before and len(line) > 50:
                # This is opening content - add a tip callout
                enhanced.append('> [!TIP]')
                enhanced.append(f'> {line}')
                i += 1
                continue
        
        # Style example sections with special callout
        if line.startswith('###') and ('example' in line.lower() or 'story' in line.lower()):
            enhanced.append('')
            enhanced.append('> [!NOTE]')
            enhanced.append(f'> {line.replace("### ", "**📖 ")}**')
            i += 1
            continue
            
        # Style action items / how-to sections
        if 'how to' in line.lower() or 'your turn' in line.lower() or 'action' in line.lower():
            if line.startswith('##'):
                enhanced.append('')
                enhanced.append('> [!IMPORTANT]')
                enhanced.append(f'> {line}')
                i += 1
                continue
        
        # Keep the line as-is
        enhanced.append(line)
        i += 1
    
    return '\n'.join(enhanced)

def enhance_chapter_file(filepath):
    """Apply enhanced styling to a chapter file"""
    
    if not filepath.exists():
        return False

    print(f"🎨 Enhancing {filepath.name}...")

    with open(filepath, 'r') as f:
        content = f.read()

    # Apply enhancements
    content = add_premium_styling(content)

    with open(filepath, 'w') as f:
        f.write(content)

    print(f"✅ Enhanced {filepath.name}")
    return True

def main():
    print("╔" + "="*60 + "╗")
    print("║" + " "*12 + "Premium Visual Styling Tool" + " "*21 + "║")
    print("║" + " "*10 + "Adding Colors & Visual Breaks" + " "*20 + "║")
    print("╚" + "="*60 + "╝\n")

    chapter_files = sorted(CHAPTERS_DIR.glob('chapter_*.md'))

    success = 0
    for filepath in chapter_files[:20]:
        if enhance_chapter_file(filepath):
            success += 1

    print("\n" + "╔" + "="*60 + "╗")
    print("║" + " "*18 + "Enhancement Complete" + " "*21 + "║")
    print("╚" + "="*60 + "╝\n")
    print(f"✅ Successfully enhanced: {success} chapters")

if __name__ == "__main__":
    main()
