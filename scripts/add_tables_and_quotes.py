#!/usr/bin/env python3
"""
Convert comparisons to styled tables and add highlighted quote boxes
"""

from pathlib import Path
import re

CHAPTERS_DIR = Path(__file__).parent.parent / '03_Book_Chapters'

def convert_comparisons_to_tables(content):
    """Convert ✅/❌ comparison pairs into styled tables"""
    
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Look for comparison patterns (❌ followed by ✅)
        if '❌' in line and '**' in line and i < len(lines) - 4:
            # Check if we have a comparison pair coming up
            next_lines = lines[i:i+10]
            has_checkmark = any('✅' in l for l in next_lines[:10])
            
            if has_checkmark:
                # Start building a comparison table
                comparisons = []
                j = i
                
                # Collect all comparison pairs
                while j < len(lines) and (('❌' in lines[j] or '✅' in lines[j]) or 
                      (j > i and lines[j].strip() == '' and j < len(lines)-1 and ('❌' in lines[j+1] or '✅' in lines[j+1]))):
                    
                    if '❌' in lines[j]:
                        wrong = lines[j].replace('❌ **', '').replace('**:', '').replace('> ', '').strip()
                        # Look for the matching ✅
                        k = j + 1
                        while k < len(lines) and '✅' not in lines[k]:
                            k += 1
                        if k < len(lines) and '✅' in lines[k]:
                            right = lines[k].replace('✅ **', '').replace('**:', '').replace('> ', '').strip()
                            comparisons.append((wrong, right))
                            j = k + 1
                        else:
                            j += 1
                    else:
                        j += 1
                
                if comparisons:
                    # Create a styled table
                    result.append('')
                    result.append('> [!WARNING]')
                    result.append('> <table>')
                    result.append('> <tr>')
                    result.append('> <th>❌ Avoid This</th>')
                    result.append('> <th>✅ Do This Instead</th>')
                    result.append('> </tr>')
                    
                    for wrong, right in comparisons:
                        result.append('> <tr>')
                        result.append(f'> <td>{wrong}</td>')
                        result.append(f'> <td>{right}</td>')
                        result.append('> </tr>')
                    
                    result.append('> </table>')
                    result.append('')
                    
                    i = j
                    continue
        
        result.append(line)
        i += 1
    
    return '\n'.join(result)

def highlight_powerful_quotes(content):
    """Wrap standalone powerful statements in highlighted quote boxes"""
    
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Look for bold standalone statements that are powerful quotes
        if (line.startswith('**') and line.endswith('**') and 
            len(line) > 20 and len(line) < 200 and
            not line.startswith('**[') and  # Not a link
            i > 0 and lines[i-1].strip() == ''):  # Standalone paragraph
            
            # Check if it's not already in a callout
            if i < 2 or not lines[i-2].startswith('> [!'):
                quote_text = line.strip('*')
                result.append('')
                result.append('> [!NOTE]')
                result.append('> **💭 Key Insight**')
                result.append(f'> *{quote_text}*')
                result.append('')
                i += 1
                continue
        
        # Also catch quotes that look like principles/rules
        if ('**' in line and any(word in line.lower() for word in 
            ['principle', 'rule:', 'truth:', 'reality:', 'fact:', 'law:']) and
            i > 0 and lines[i-1].strip() == ''):
            
            if i < 2 or not lines[i-2].startswith('> [!'):
                result.append('')
                result.append('> [!NOTE]')  
                result.append('> **🎯 Core Principle**')
                result.append(f'> {line}')
                result.append('')
                i += 1
                continue
        
        result.append(line)
        i += 1
    
    return '\n'.join(result)

def enhance_chapter(filepath):
    """Apply table and quote enhancements"""
    
    print(f"🎨 Enhancing {filepath.name}...")

    with open(filepath, 'r') as f:
        content = f.read()

    # Apply enhancements
    content = convert_comparisons_to_tables(content)
    content = highlight_powerful_quotes(content)

    with open(filepath, 'w') as f:
        f.write(content)

    print(f"✅ Enhanced {filepath.name}")
    return True

def main():
    print("╔" + "="*60 + "╗")
    print("║" + " "*10 + "Tables & Quote Box Styling Tool" + " "*19 + "║")
    print("╚" + "="*60 + "╝\n")

    chapter_files = sorted(CHAPTERS_DIR.glob('chapter_*.md'))

    for filepath in chapter_files[:20]:
        enhance_chapter(filepath)

    print("\n✅ All chapters enhanced with tables and quote boxes!")

if __name__ == "__main__":
    main()
