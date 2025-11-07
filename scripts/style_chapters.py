#!/usr/bin/env python3
"""
Add premium GitHub styling to all Perfect Effort chapters
"""

from pathlib import Path
import re

CHAPTERS_DIR = Path(__file__).parent.parent / '03_Book_Chapters'

# Chapter metadata
CHAPTERS = {
    1: {
        "file": "chapter_01_life_is_a_sport.md",
        "title": "Life is a Sport",
        "image": "../images/generated/chapters_informative/chapter_01_Life_is_a_Sport.png",
        "next": 2,
        "prev": None
    },
    2: {
        "file": "chapter_02_know_your_stats.md",
        "title": "Know Your Stats",
        "image": "../images/generated/chapters_informative/chapter_02_Know_Your_Stats.png",
        "next": 3,
        "prev": 1
    },
    3: {
        "file": "chapter_03_the_scoreboard_that_matters.md",
        "title": "The Scoreboard That Matters",
        "image": "../images/generated/chapters_informative/chapter_03_The_Scoreboard_That_Matters.png",
        "next": 4,
        "prev": 2
    },
    4: {
        "file": "chapter_04_practice_like_a_pro.md",
        "title": "Practice Like a Pro",
        "image": "../images/generated/chapters_informative/chapter_04_Practice_Like_a_Pro.png",
        "next": 5,
        "prev": 3
    },
    5: {
        "file": "chapter_05_your_inner_coach.md",
        "title": "Your Inner Coach",
        "image": "../images/generated/chapters_informative/chapter_05_Your_Inner_Coach.png",
        "next": 6,
        "prev": 4
    },
    6: {
        "file": "chapter_06_losing_is_learning.md",
        "title": "Losing is Learning",
        "image": "../images/generated/chapters_informative/chapter_06_Losing_is_Learning.png",
        "next": 7,
        "prev": 5
    },
    7: {
        "file": "chapter_07_focus_mode_on.md",
        "title": "Focus Mode: On",
        "image": "../images/generated/chapters_informative/chapter_07_Focus_Mode:_On.png",
        "next": 8,
        "prev": 6
    },
    8: {
        "file": "chapter_08_the_pressure_test.md",
        "title": "The Pressure Test",
        "image": "../images/generated/chapters_informative/chapter_08_The_Pressure_Test.png",
        "next": 9,
        "prev": 7
    },
    9: {
        "file": "chapter_09_morning_warm_up.md",
        "title": "Morning Warm-Up",
        "image": "../images/generated/chapters_informative/chapter_09_Morning_Warm-Up.png",
        "next": 10,
        "prev": 8
    },
    10: {
        "file": "chapter_10_fuel_your_engine.md",
        "title": "Fuel Your Engine",
        "image": "../images/generated/chapters_informative/chapter_10_Fuel_Your_Engine.png",
        "next": 11,
        "prev": 9
    },
    11: {
        "file": "chapter_11_the_recovery_room.md",
        "title": "The Recovery Room",
        "image": "../images/generated/chapters_informative/chapter_11_The_Recovery_Room.png",
        "next": 12,
        "prev": 10
    },
    12: {
        "file": "chapter_12_time_is_your_currency.md",
        "title": "Time is Your Currency",
        "image": "../images/generated/chapters_informative/chapter_12_Time_is_Your_Currency.png",
        "next": 13,
        "prev": 11
    },
    13: {
        "file": "chapter_13_the_compound_effect.md",
        "title": "The Compound Effect",
        "image": "../images/generated/chapters_informative/chapter_13_The_Compound_Effect.png",
        "next": 14,
        "prev": 12
    },
    14: {
        "file": "chapter_14_choose_your_teammates.md",
        "title": "Choose Your Teammates",
        "image": "../images/generated/chapters_informative/chapter_14_Choose_Your_Teammates.png",
        "next": 15,
        "prev": 13
    },
    15: {
        "file": "chapter_15_the_mentor_advantage.md",
        "title": "The Mentor Advantage",
        "image": "../images/generated/chapters_informative/chapter_15_The_Mentor_Advantage.png",
        "next": 16,
        "prev": 14
    },
    16: {
        "file": "chapter_16_building_your_support_system.md",
        "title": "Building Your Support System",
        "image": "../images/generated/chapters_informative/chapter_16_Building_Your_Support_System.png",
        "next": 17,
        "prev": 15
    },
    17: {
        "file": "chapter_17_level_up_your_skills.md",
        "title": "Level Up Your Skills",
        "image": "../images/generated/chapters_informative/chapter_17_Level_Up_Your_Skills.png",
        "next": 18,
        "prev": 16
    },
    18: {
        "file": "chapter_18_play_your_position.md",
        "title": "Play Your Position",
        "image": "../images/generated/chapters_informative/chapter_18_Play_Your_Position.png",
        "next": 19,
        "prev": 17
    },
    19: {
        "file": "chapter_19_clutch_moments.md",
        "title": "Clutch Moments",
        "image": "../images/generated/chapters_informative/chapter_19_Clutch_Moments.png",
        "next": 20,
        "prev": 18
    },
    20: {
        "file": "chapter_20_the_long_game.md",
        "title": "The Long Game",
        "image": "../images/generated/chapters_informative/chapter_20_The_Long_Game.png",
        "next": None,
        "prev": 19
    }
}

def create_header(chapter_num, title, image_path):
    """Create beautiful chapter header with image"""
    return f"""<div align="center">

<img src="{image_path}" alt="Chapter {chapter_num}: {title}" width="600"/>

# Chapter {chapter_num}: {title}

**[🏠 Back to Home](../README.md)** | **[📚 All Chapters](../README.md#-the-chapters)**

---

</div>

"""

def create_navigation(chapter_num):
    """Create chapter navigation footer"""
    meta = CHAPTERS[chapter_num]

    nav_parts = []

    if meta['prev']:
        prev_meta = CHAPTERS[meta['prev']]
        nav_parts.append(f"[⬅️ Previous: Chapter {meta['prev']} - {prev_meta['title']}]({prev_meta['file']})")
    else:
        nav_parts.append("[🏠 Back to Home](../README.md)")

    nav_parts.append("[📚 All Chapters](../README.md#-the-chapters)")

    if meta['next']:
        next_meta = CHAPTERS[meta['next']]
        nav_parts.append(f"[Next: Chapter {meta['next']} - {next_meta['title']} ➡️]({next_meta['file']})")
    else:
        nav_parts.append("[🏠 Back to Home](../README.md)")

    return f"""

---

<div align="center">

{' | '.join(nav_parts)}

</div>
"""

def style_blockquotes(content):
    """Convert regular blockquotes to GitHub-styled callouts"""
    # Find blockquote lines
    lines = content.split('\n')
    styled_lines = []
    i = 0
    in_blockquote = False

    while i < len(lines):
        line = lines[i]

        # Skip if already a callout
        if line.startswith('> [!'):
            styled_lines.append(line)
            i += 1
            in_blockquote = True
            continue

        # Start of a new blockquote section
        if line.startswith('> ') and not in_blockquote:
            # Check if this is a key insight blockquote (has **Core Concept**: or **The Output**:)
            if (i < len(lines) - 1 and line.startswith('> **') and '**:' in line):
                # Add callout markers ONCE at the start of the blockquote
                styled_lines.append('> [!NOTE]')
                styled_lines.append('> **💡 Key Insight**')
            styled_lines.append(line)
            in_blockquote = True
        elif line.startswith('> '):
            # Continue existing blockquote
            styled_lines.append(line)
        else:
            # End of blockquote
            in_blockquote = False
            styled_lines.append(line)

        i += 1

    return '\n'.join(styled_lines)

def style_chapter(chapter_num):
    """Add premium styling to a chapter"""
    meta = CHAPTERS[chapter_num]
    filepath = CHAPTERS_DIR / meta['file']

    if not filepath.exists():
        print(f"⚠️  Chapter {chapter_num} file not found: {filepath}")
        return False

    print(f"✨ Styling Chapter {chapter_num}: {meta['title']}")

    # Read current content
    with open(filepath, 'r') as f:
        content = f.read()

    # Check if header already exists - if so, skip
    if content.startswith('<div align="center">') and f'Chapter {chapter_num}:' in content[:500]:
        print(f"⏭️  Chapter {chapter_num} already styled, skipping...")
        return True

    # Remove old header if exists (both markdown and HTML versions)
    content = re.sub(r'^# Chapter \d+:.*?\n\n', '', content, flags=re.MULTILINE)
    # Remove any existing header block
    content = re.sub(r'^<div align="center">.*?</div>\n\n', '', content, flags=re.DOTALL)

    # Create new styled content
    header = create_header(chapter_num, meta['title'], meta['image'])
    navigation = create_navigation(chapter_num)
    styled_content = style_blockquotes(content)

    # Combine
    new_content = header + styled_content + navigation

    # Write back
    with open(filepath, 'w') as f:
        f.write(new_content)

    print(f"✅ Chapter {chapter_num} styled successfully!")
    return True

def main():
    print("╔" + "="*60 + "╗")
    print("║" + " "*15 + "Chapter Styling Tool" + " "*25 + "║")
    print("║" + " "*10 + "Adding Premium GitHub Styling" + " "*20 + "║")
    print("╚" + "="*60 + "╝\n")

    success = 0
    failed = 0

    for chapter_num in range(1, 21):
        if style_chapter(chapter_num):
            success += 1
        else:
            failed += 1

    print("\n" + "╔" + "="*60 + "╗")
    print("║" + " "*20 + "Styling Complete" + " "*24 + "║")
    print("╚" + "="*60 + "╝\n")
    print(f"✅ Successfully styled: {success} chapters")
    print(f"❌ Failed: {failed} chapters")

if __name__ == "__main__":
    main()
