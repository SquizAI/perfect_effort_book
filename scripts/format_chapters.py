#!/usr/bin/env python3
"""
Add premium formatting to Perfect Effort chapters with visual breaks and callouts
"""

from pathlib import Path
import re

CHAPTERS_DIR = Path(__file__).parent.parent / '03_Book_Chapters'

def add_visual_formatting(content):
    """Add spacing, callouts, and visual breaks to chapter content"""

    # Split into lines
    lines = content.split('\n')
    formatted = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Add extra spacing before major headers (##)
        if line.startswith('## ') and i > 0:
            formatted.append('')
            formatted.append('---')
            formatted.append('')
            formatted.append(line)
            formatted.append('')

        # Convert bold key phrases to callouts
        elif line.startswith('**') and line.endswith('**') and len(line) < 150:
            # This is a standalone bold statement - make it a callout
            text = line.strip('*')
            formatted.append('')
            formatted.append('> [!IMPORTANT]')
            formatted.append(f'> **{text}**')
            formatted.append('')

        # Style bullet points with better spacing
        elif line.startswith('- ') or line.startswith('* '):
            if i > 0 and not (lines[i-1].startswith('-') or lines[i-1].startswith('*')):
                formatted.append('')
            formatted.append(line)

        # Style numbered lists with better spacing
        elif re.match(r'^\d+\.', line):
            if i > 0 and not re.match(r'^\d+\.', lines[i-1]):
                formatted.append('')
            formatted.append(line)

        # Add spacing after lists
        elif i > 0 and (lines[i-1].startswith('-') or lines[i-1].startswith('*') or re.match(r'^\d+\.', lines[i-1])) and line and not line.startswith('-') and not line.startswith('*') and not re.match(r'^\d+\.', line):
            formatted.append('')
            formatted.append(line)

        # Style key takeaway sections
        elif 'key takeaway' in line.lower() or 'remember' in line.lower():
            formatted.append('')
            formatted.append('---')
            formatted.append('')
            formatted.append(line)

        # Style example sections
        elif line.startswith('### ') and 'example' in line.lower():
            formatted.append('')
            formatted.append('> [!TIP]')
            formatted.append(f'> {line.replace("### ", "**")}**')
            formatted.append('>')

        # Add spacing around horizontal rules
        elif line == '---':
            if i > 0 and lines[i-1] != '':
                formatted.append('')
            formatted.append(line)
            if i < len(lines) - 1 and lines[i+1] != '':
                formatted.append('')

        # Style comparison boxes (✅ vs ❌)
        elif '✅' in line or '❌' in line:
            formatted.append('')
            formatted.append(line)

        # Regular lines
        else:
            formatted.append(line)

        i += 1

    return '\n'.join(formatted)

def add_section_breaks(content):
    """Add visual section breaks between major sections"""
    # Add decorative breaks before major transitions
    content = re.sub(
        r'\n(## [^\n]+)\n',
        r'\n\n---\n\n\1\n\n',
        content
    )
    return content

def style_quotes(content):
    """Style blockquotes as callouts"""
    lines = content.split('\n')
    result = []
    in_quote = False

    for i, line in enumerate(lines):
        if line.startswith('> ') and not line.startswith('> [!'):
            if not in_quote:
                # Check if this is a key quote (has bold or important keywords)
                if '**' in line or any(word in line.lower() for word in ['rule', 'key', 'important', 'remember']):
                    result.append('> [!NOTE]')
                    result.append('> 💡 **Key Insight**')
                in_quote = True
            result.append(line)
        else:
            in_quote = False
            result.append(line)

    return '\n'.join(result)

def format_chapter_file(filepath):
    """Apply all formatting to a chapter file"""

    if not filepath.exists():
        return False

    print(f"📝 Formatting {filepath.name}...")

    with open(filepath, 'r') as f:
        content = f.read()

    # Apply formatting
    content = add_visual_formatting(content)
    content = style_quotes(content)

    # Write back
    with open(filepath, 'w') as f:
        f.write(content)

    print(f"✅ Formatted {filepath.name}")
    return True

def main():
    print("╔" + "="*60 + "╗")
    print("║" + " "*15 + "Chapter Formatting Tool" + " "*22 + "║")
    print("║" + " "*10 + "Adding Visual Breaks & Callouts" + " "*18 + "║")
    print("╚" + "="*60 + "╝\n")

    # Get all chapter files
    chapter_files = sorted(CHAPTERS_DIR.glob('chapter_*.md'))

    success = 0
    for filepath in chapter_files[:13]:  # Only chapters 1-13
        if format_chapter_file(filepath):
            success += 1

    print("\n" + "╔" + "="*60 + "╗")
    print("║" + " "*20 + "Formatting Complete" + " "*21 + "║")
    print("╚" + "="*60 + "╝\n")
    print(f"✅ Successfully formatted: {success} chapters")

if __name__ == "__main__":
    main()
