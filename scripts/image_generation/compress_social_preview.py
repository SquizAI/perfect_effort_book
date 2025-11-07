#!/usr/bin/env python3
"""
Compress social preview image to under 1MB for GitHub
"""

from pathlib import Path
from PIL import Image
import sys

INPUT_FILE = Path(__file__).parent.parent.parent / 'images' / 'generated' / 'social_preview_perfect_effort.png'
OUTPUT_FILE = INPUT_FILE  # Overwrite the original

def compress_image(input_path, output_path, max_size_mb=1.0):
    """Compress image to be under max_size_mb"""

    # Open image
    img = Image.open(input_path)

    # Target size in bytes
    max_size = int(max_size_mb * 1024 * 1024)

    # Start with high quality
    quality = 95

    print(f"📁 Input: {input_path}")
    print(f"📊 Original size: {input_path.stat().st_size / (1024 * 1024):.2f}MB")
    print(f"🎯 Target: < {max_size_mb}MB")
    print()

    # Binary search for optimal quality
    while quality > 50:
        # Save to temp with current quality
        img.save(output_path, 'PNG', optimize=True, quality=quality)

        size = output_path.stat().st_size
        size_mb = size / (1024 * 1024)

        print(f"⚙️  Quality {quality}: {size_mb:.2f}MB", end='')

        if size <= max_size:
            print(" ✅")
            print()
            print(f"✅ Compressed successfully!")
            print(f"📁 Output: {output_path}")
            print(f"📊 Final size: {size_mb:.2f}MB")
            print(f"🎨 Quality: {quality}")
            return True
        else:
            print(f" (too large, reducing...)")
            quality -= 5

    # If we can't get under 1MB with PNG, try JPEG
    print()
    print("⚠️  PNG compression insufficient, converting to JPEG...")

    # Convert to RGB (JPEG doesn't support transparency)
    if img.mode in ('RGBA', 'LA', 'P'):
        background = Image.new('RGB', img.size, (255, 255, 255))
        if img.mode == 'P':
            img = img.convert('RGBA')
        background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
        img = background

    # Save as JPEG
    jpeg_output = output_path.with_suffix('.jpg')
    quality = 90

    while quality > 60:
        img.save(jpeg_output, 'JPEG', optimize=True, quality=quality)

        size = jpeg_output.stat().st_size
        size_mb = size / (1024 * 1024)

        print(f"⚙️  JPEG Quality {quality}: {size_mb:.2f}MB", end='')

        if size <= max_size:
            print(" ✅")
            print()
            print(f"✅ Compressed successfully as JPEG!")
            print(f"📁 Output: {jpeg_output}")
            print(f"📊 Final size: {size_mb:.2f}MB")
            print(f"🎨 Quality: {quality}")

            # Remove original PNG
            if output_path.exists():
                output_path.unlink()
                print(f"🗑️  Removed original PNG")

            return True
        else:
            print(f" (too large, reducing...)")
            quality -= 5

    print()
    print("❌ Could not compress to under 1MB")
    return False

if __name__ == "__main__":
    if not INPUT_FILE.exists():
        print(f"❌ Input file not found: {INPUT_FILE}")
        sys.exit(1)

    compress_image(INPUT_FILE, OUTPUT_FILE)
