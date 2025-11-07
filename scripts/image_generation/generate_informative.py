#!/usr/bin/env python3
"""
Generate Informative Chapter Images - Teaching Through Visuals
Each image communicates the core lesson visually using Gemini API
"""

import os
import json
import base64
import time
import urllib.request
from pathlib import Path

# Load environment
API_KEY = os.getenv('GEMINI_API_KEY')
if not API_KEY:
    # Try loading from .env file
    env_path = Path(__file__).parent.parent.parent / '.env'
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if line.startswith('GEMINI_API_KEY'):
                    API_KEY = line.split('=', 1)[1].strip()
                    break

API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent"
OUTPUT_DIR = Path(__file__).parent.parent.parent / 'images' / 'generated'
CHAPTERS_DIR = OUTPUT_DIR / 'chapters_informative'

# Create directories
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)

# Book cover prompt
BOOK_COVER_PROMPT = """Create a vibrant Pixar-style 3D cartoon book cover embodying PERFECT EFFORT philosophy.

Central visual: A diverse group of middle and high school students in a championship arena, each giving their absolute best effort in different ways - not perfect, but fully committed. Show imperfect but earnest attempts: one student helping another up, one studying intensely with determination, one practicing a skill with focus, one being coached and held accountable. All showing EFFORT over perfection.

Foreground: Students with visible determination, sweat, focus - giving everything they have. Some succeeding, some struggling, ALL trying their hardest. Growth mindset visible on faces.

Background: Scoreboard showing EFFORT metrics instead of perfect scores. Championship stadium with blue-gold atmosphere representing life as a game to win.

Symbolic elements:
- Trophy labeled Best Effort (not First Place)
- Accountability partners high-fiving
- Growth arrows showing progress over perfection
- Game board or life map showing the journey

Top area: Clean space for title PERFECT EFFORT
Bottom area: Space for subtitle Winning at the Game of Life

Color palette: Championship blue, victory gold, energetic orange, inspiring atmosphere
Style: Pixar Disney-quality 3D cartoon realism
Mood: Inspiring, accountable, growth-focused, earnest effort
Message: You don't need to be perfect - you need to give your best effort. That's how we win at life.

3:2 aspect ratio for book cover. NO text in image - text added separately. Pure visual storytelling of the Perfect Effort philosophy."""

# Global style for all chapters
GLOBAL_STYLE = """Pixar-quality 3D cartoon realism with informative visual storytelling. Each image should TEACH the lesson visually - someone should understand the core concept just by looking at the image. Fun but educational, colorful championship stadium setting with blue-gold palette. 16:9 aspect ratio. NO text or typography. High quality, publication-ready."""

# Chapter data with visual metaphors
CHAPTERS = {
    "01": {
        "title": "Life is a Sport",
        "visualMetaphor": "A cartoon student standing at a basketball free-throw line, but the court transforms/morphs into different life scenarios - classroom desk, stage with microphone, workplace, gym. Same game mechanics apply everywhere. The student has a determined smile showing comfort with discomfort. Blue-gold stadium lights overhead. Style: Pixar 3D, showing life's universal game mechanics.",
        "teachingPoint": "Life operates like a sport with rules and scoreboards - you're already in the game"
    },
   "02": {
        "title": "Know Your Stats",
        "visualMetaphor": "A cartoon student looking at themselves in a mirror, but instead of their reflection, they see a glowing holographic video game character sheet displaying life stats: Study Hours, Sleep Quality, Friendship Level, Skills Progress, etc. The stats glow in blue-gold neon. Stadium setting. Style: Pixar 3D with video game UI aesthetic.",
        "teachingPoint": "You can't improve what you don't measure - track your stats to level up"
    },
    "03": {
        "title": "The Scoreboard That Matters",
        "visualMetaphor": "Split-screen cartoon scene: Left side shows an external scoreboard with social media likes, followers, comparisons fading away like smoke. Right side shows a solid, glowing internal scoreboard with personal values, growth metrics, character stats that are stable and bright. Cartoon student choosing the internal scoreboard. Blue-gold championship setting.",
        "teachingPoint": "Choose the scoreboard you can control - internal values over external validation"
    },
    "04": {
        "title": "Practice Like a Pro",
        "visualMetaphor": "Side-by-side comparison in cartoon: Left court shows player mindlessly shooting 100 shots while distracted on phone (shots missing). Right court shows player shooting 50 shots with laser focus, video camera recording, analyzing form (shots swishing, improvement arrows). Blue-gold stadium lighting. Pixar 3D showing deliberate practice vs mindless reps.",
        "teachingPoint": "Deliberate practice beats mindless repetition - focus on quality over quantity"
    },
    "05": {
        "title": "Your Inner Coach",
        "visualMetaphor": "Cartoon student at crossroads with two large speech bubbles: Dark bubble on left says 'I'm not good at this' (negative, shadowy). Bright glowing bubble on right says 'I'm not good at this YET' (positive, energized with growth symbols). Student pointing toward bright bubble making the choice. Stadium with blue-gold spotlights. Pixar 3D showing power of reframing.",
        "teachingPoint": "Your inner dialogue determines your performance - choose the coach, not the critic"
    },
    "06": {
        "title": "Losing is Learning",
        "visualMetaphor": "Cartoon film room with multiple screens showing replays of mistakes/failures, but instead of showing losses, the screens have bright highlighted lessons, adjustments, and notes like a sports analyst breaking down game film. Cartoon student taking notes excitedly. Blue-gold professional atmosphere. Pixar 3D showing failure as valuable data.",
        "teachingPoint": "Every failure contains a lesson - extract the data like a pro"
    },
    "07": {
        "title": "Focus Mode On",
        "visualMetaphor": "Cartoon student inside a protective bubble of deep focus (glowing blue shield). Outside the bubble, notifications, social media icons, phone alerts, distractions are swirling and bouncing off the shield. Student intensely focused on work inside, in flow state. Stadium setting. Pixar 3D showing attention protection.",
        "teachingPoint": "Protect your focus like a superpower - it's your competitive advantage"
    },
    "08": {
        "title": "The Pressure Test",
        "visualMetaphor": "Cartoon basketball player at free-throw line with visible holographic displays showing elevated heart rate, nervous system activation, pressure indicators. BUT their internal thought bubble shows calm, process-focused thinking. Split-screen showing body's alarm vs mind's control. Blue-gold lighting. Pixar 3D showing pressure reframing.",
        "teachingPoint": "Your preparation determines your performance under pressure"
    },
    "09": {
        "title": "Morning Warm-Up",
        "visualMetaphor": "Two parallel morning timelines in cartoon split-screen: Left path shows CHAOS - snooze button, rushed stress, scattered start (dark, frantic). Right path shows CONTROL - structured routine, calm energy (bright, organized). Same person, different outcomes based on morning choice. Blue-gold championship morning light. Pixar 3D showing morning momentum.",
        "teachingPoint": "Win your morning, win your day - design your opening plays"
    },
    "10": {
        "title": "Fuel Your Engine",
        "visualMetaphor": "Cartoon student as high-performance race car with visible transparent engine showing fuel systems, energy levels, performance gauges. Left side shows garbage fuel = sputtering engine (dark smoke). Right side shows premium fuel (healthy food, water, sleep) = purring engine (blue-gold energy glow). Dashboard displays performance metrics. Pixar 3D showing body as machine.",
        "teachingPoint": "Your body is your engine - fuel it like a Ferrari, not a garbage truck"
    },
    "11": {
        "title": "The Recovery Room",
        "visualMetaphor": "Time-lapse cartoon plant growing in three stages: Stress (watering/sunlight), RECOVERY period (rest), GROWTH explosion (visible size increase). Arrows showing cycle: Stress, Recovery, Adaptation. Plant grows during rest, not during stress. Peaceful blue-gold recovery atmosphere. Pixar 3D showing growth happens in recovery.",
        "teachingPoint": "Recovery isn't weakness - it's when growth happens"
    },
    "12": {
        "title": "Time is Your Currency",
        "visualMetaphor": "Cartoon student at crossroads with two paths showing hourglasses: Path 1 shows hours invested in scrolling/distraction - sand disappearing into nothing (1x return, fading). Path 2 shows hours invested in skills/growth - sand multiplying exponentially (100x return, compounding). Visual comparison of time ROI. Blue-gold dramatic lighting. Pixar 3D showing time investment returns.",
        "teachingPoint": "Time is non-renewable currency - invest it in what compounds"
    },
    "13": {
        "title": "The Compound Effect",
        "visualMetaphor": "Large exponential curve graph in cartoon 3D showing two paths: Flat blue line labeled Same every day staying at baseline. Bright gold exponential curve labeled 1 percent daily improvement starting flat then curving upward dramatically. Markers at Day 30 (barely visible change), Day 90 (starting to curve), Day 365 (37x higher, explosive growth). Cartoon student celebrating at top. Pixar 3D showing compound mathematics visually.",
        "teachingPoint": "Small daily improvements compound exponentially - patience through the invisible phase wins"
    },
    "14": {
        "title": "Choose Your Teammates",
        "visualMetaphor": "Cartoon diverse hands in team huddle with glowing blue-gold energy bonds connecting them. Each hand represents different strengths (brain icons, muscle icons, heart icons, creative icons). Selective collaboration - quality connections over quantity. Stadium championship teamwork atmosphere. Pixar 3D.",
        "teachingPoint": "Strategic relationships amplify your potential - choose your team wisely"
    },
    "15": {
        "title": "The Mentor Advantage",
        "visualMetaphor": "Two cartoon characters on stepped platform: wise mentor (elevated) and eager student (learning). Mentor pointing forward, illuminating student's path with golden light beam filled with knowledge symbols (books, lightbulbs, stars). Transfer of wisdom shown visually. Blue-gold championship guidance atmosphere. Pixar 3D.",
        "teachingPoint": "Mentors accelerate your journey - learn from their experience"
    },
    "16": {
        "title": "Building Your Support System",
        "visualMetaphor": "Cartoon structural foundation made of glowing pillars labeled Family, Friends, Mentors, Team supporting platform where student stands strong. Network web connecting pillars with blue-gold energy. Shows support system as critical infrastructure. Pixar 3D.",
        "teachingPoint": "Your support system is your foundation - build it strong"
    },
    "17": {
        "title": "Level Up Your Skills",
        "visualMetaphor": "Ascending cartoon stairway with clear progression levels: Bronze, Silver, Gold, Platinum. Each step shows skill advancement with glowing achievement badges, power-up stars, progression indicators. Cartoon student climbing with determination. Video game achievement aesthetic. Blue-gold championship progression. Pixar 3D.",
        "teachingPoint": "Skills compound through consistent leveling - master the progression path"
    },
    "18": {
        "title": "Play Your Position",
        "visualMetaphor": "Cartoon chess piece (king) perfectly positioned on strategic board with happy confident expression OR cartoon athlete in ideal position/stance with spotlight. Finding sweet spot visualization. Blue-gold strategic lighting showing optimal positioning. Pixar 3D.",
        "teachingPoint": "Find your unique position where your strengths shine"
    },
    "19": {
        "title": "Clutch Moments",
        "visualMetaphor": "Cartoon basketball frozen mid-swish at rim with energy particles and slow-motion effect OR cartoon sprinter breaking finish tape with victory explosion of confetti and stars. Peak performance moment captured. Blue-gold dramatic lighting showing clutch execution. Pixar 3D.",
        "teachingPoint": "Clutch moments are built through preparation - deliver when it matters"
    },
    "20": {
        "title": "The Long Game",
        "visualMetaphor": "Winding cartoon marathon path with friendly mile markers leading from arena floor to distant mountain peak with victory flag. Cartoon student silhouette journeying forward along glowing blue-gold path showing progress over time. Long-term persistence visualization. Pixar 3D.",
        "teachingPoint": "Champions play the long game - patience and persistence win"
    }
}

def generate_image(prompt, aspect_ratio="16:9"):
    """Generate image using Gemini API"""
    payload = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }],
        "generationConfig": {
            "responseModalities": ["Image"],
            "imageConfig": {
                "aspectRatio": aspect_ratio
            }
        }
    }

    headers = {
        "x-goog-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    # Create request
    req = urllib.request.Request(
        API_ENDPOINT,
        data=json.dumps(payload).encode('utf-8'),
        headers=headers
    )

    # Send request
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))

    if "error" in data:
        raise Exception(f"API Error: {data['error']}")

    # Extract base64 image data
    image_data = data['candidates'][0]['content']['parts'][0]['inlineData']['data']
    return base64.b64decode(image_data)

def generate_chapter(chapter_num):
    """Generate a single chapter image"""
    chapter_key = f"{chapter_num:02d}"

    if chapter_key not in CHAPTERS:
        print(f"❌ Chapter {chapter_num} not found")
        return False

    chapter = CHAPTERS[chapter_key]
    print(f"\n{'='*60}")
    print(f"📚 Chapter {chapter_key}: {chapter['title']}")
    print(f"{'='*60}")
    print(f"💡 Teaching Point: {chapter['teachingPoint']}\n")

    # Build full prompt
    full_prompt = f"""{chapter['visualMetaphor']}

{GLOBAL_STYLE}

Key Teaching Objective: {chapter['teachingPoint']}"""

    try:
        image_bytes = generate_image(full_prompt, "16:9")

        # Save image
        filename = f"chapter_{chapter_key}_{chapter['title'].replace(' ', '_')}.png"
        filepath = CHAPTERS_DIR / filename

        with open(filepath, 'wb') as f:
            f.write(image_bytes)

        size = len(image_bytes) / (1024 * 1024)  # MB
        print(f"✅ Generated successfully!")
        print(f"📁 Location: {filepath}")
        print(f"📊 Size: {size:.1f}M")

        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def generate_book_cover():
    """Generate the Perfect Effort book cover"""
    print("\n" + "="*60)
    print("📘 Generating Perfect Effort Book Cover")
    print("="*60 + "\n")

    try:
        image_bytes = generate_image(BOOK_COVER_PROMPT, "3:2")

        # Save image
        filepath = OUTPUT_DIR / 'book_cover_perfect_effort.png'

        with open(filepath, 'wb') as f:
            f.write(image_bytes)

        size = len(image_bytes) / (1024 * 1024)  # MB
        print("✅ Book cover generated successfully!")
        print(f"📁 Location: {filepath}")
        print(f"📊 Size: {size:.1f}M")

        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def generate_social_preview():
    """Generate GitHub social preview image (1280x640px / 2:1 aspect ratio)"""
    print("\n" + "="*60)
    print("🌐 Generating GitHub Social Preview")
    print("="*60 + "\n")

    # Social preview prompt - Pixar style matching chapter images
    social_prompt = """Create a vibrant Pixar-style 3D cartoon social media banner for Perfect Effort.

TITLE TEXT (include in image):
"PERFECT EFFORT"
"by Professor Matty"
Bold, championship-style typography in white with blue-gold glow at top center

MAIN VISUAL - Wide panoramic championship arena scene:
Diverse group of cartoon middle/high school students in a championship stadium, each giving their absolute best effort in different ways - not perfect, but fully committed.

Left section: Students struggling but persisting - one studying intensely, one practicing a skill with determination, showing visible effort
Center section (below title): Key moment - students helping each other, accountability partners high-fiving, growth mindset in action
Right section: Students progressing forward, celebrating effort achievements, showing improvement over time

Visual elements:
- Championship stadium with bright blue-gold lighting and atmosphere
- Scoreboard displaying "EFFORT" metrics instead of perfect scores
- Trophy labeled "Best Effort" visible in scene
- Students with determination, sweat, focus - some succeeding, some struggling, ALL trying their hardest
- Growth arrows and progress indicators
- Warm, inspiring championship atmosphere

Style: Pixar/Disney-quality 3D cartoon realism - same style as the chapter images
Color palette: Championship blue (#2563EB), victory gold (#FBBF24), energetic orange
Mood: Fun, inspiring, accountable, growth-focused, celebrating effort over perfection
Message: You don't need to be perfect - you need to give your best effort

16:9 aspect ratio. Include "PERFECT EFFORT by Professor Matty" text. High quality, vibrant Pixar-style social banner."""

    try:
        # Use 16:9 as closest to 2:1 (Gemini doesn't support 2:1 directly)
        image_bytes = generate_image(social_prompt, "16:9")

        # Save image
        filepath = OUTPUT_DIR / 'social_preview_perfect_effort.png'

        with open(filepath, 'wb') as f:
            f.write(image_bytes)

        size = len(image_bytes) / (1024 * 1024)  # MB
        print("✅ Social preview generated successfully!")
        print(f"📁 Location: {filepath}")
        print(f"📊 Size: {size:.1f}M")
        print(f"ℹ️  16:9 aspect ratio - crop top/bottom equally to reach 2:1 (1280×640px) for GitHub")

        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("╔" + "="*58 + "╗")
    print("║" + " "*10 + "Perfect Effort - Informative Visuals" + " "*12 + "║")
    print("║" + " "*3 + "Each Image Teaches the Lesson Through Visual Story" + " "*4 + "║")
    print("╚" + "="*58 + "╝\n")

    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python generate_informative.py cover        # Generate book cover")
        print("  python generate_informative.py social       # Generate social preview")
        print("  python generate_informative.py chapter 5    # Generate specific chapter")
        print("  python generate_informative.py all          # Generate all chapters + cover")
        return

    command = sys.argv[1]

    if command == "cover":
        generate_book_cover()

    elif command == "social":
        generate_social_preview()

    elif command == "chapter":
        if len(sys.argv) < 3:
            print("❌ Please specify chapter number")
            return
        chapter_num = int(sys.argv[2])
        generate_chapter(chapter_num)

    elif command == "all":
        # Generate book cover first
        cover_success = generate_book_cover()
        time.sleep(2)

        # Generate all chapters
        success = 0
        failed = 0

        for i in range(1, 21):
            if generate_chapter(i):
                success += 1
            else:
                failed += 1

            # Rate limiting
            if i < 20:
                time.sleep(2)

        print(f"\n╔{'='*58}╗")
        print(f"║{' '*15}Generation Complete{' '*23}║")
        print(f"╚{'='*58}╝\n")
        print(f"📘 Book Cover: {'✅' if cover_success else '❌'}")
        print(f"✅ Successful: {success} chapters")
        print(f"❌ Failed: {failed} chapters")
        print(f"📁 Book Cover: {OUTPUT_DIR}/book_cover_perfect_effort.png")
        print(f"📁 Chapters: {CHAPTERS_DIR}/")

    else:
        print(f"❌ Unknown command: {command}")

if __name__ == "__main__":
    main()
