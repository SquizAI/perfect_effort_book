#!/bin/bash

# Compress social preview image to under 1MB using macOS sips

INPUT_FILE="../../images/generated/social_preview_perfect_effort.png"
OUTPUT_DIR="../../images/generated"

echo "📁 Input: $INPUT_FILE"

# Get original file size
ORIGINAL_SIZE=$(stat -f%z "$INPUT_FILE")
ORIGINAL_MB=$(echo "scale=2; $ORIGINAL_SIZE / 1048576" | bc)
echo "📊 Original size: ${ORIGINAL_MB}MB"
echo "🎯 Target: < 1.0MB"
echo ""

# Convert to JPEG with quality 85 (good balance of quality and size)
JPEG_FILE="$OUTPUT_DIR/social_preview_perfect_effort.jpg"

echo "⚙️  Converting PNG to JPEG with quality 85..."
sips -s format jpeg -s formatOptions 85 "$INPUT_FILE" --out "$JPEG_FILE" > /dev/null 2>&1

# Check size
JPEG_SIZE=$(stat -f%z "$JPEG_FILE")
JPEG_MB=$(echo "scale=2; $JPEG_SIZE / 1048576" | bc)

echo "📊 JPEG size: ${JPEG_MB}MB"

# If still over 1MB, reduce quality
if [ $JPEG_SIZE -gt 1048576 ]; then
    echo "⚠️  Still too large, reducing quality to 75..."
    sips -s format jpeg -s formatOptions 75 "$INPUT_FILE" --out "$JPEG_FILE" > /dev/null 2>&1

    JPEG_SIZE=$(stat -f%z "$JPEG_FILE")
    JPEG_MB=$(echo "scale=2; $JPEG_SIZE / 1048576" | bc)
    echo "📊 JPEG size: ${JPEG_MB}MB"
fi

# If still over 1MB, reduce quality more
if [ $JPEG_SIZE -gt 1048576 ]; then
    echo "⚠️  Still too large, reducing quality to 65..."
    sips -s format jpeg -s formatOptions 65 "$INPUT_FILE" --out "$JPEG_FILE" > /dev/null 2>&1

    JPEG_SIZE=$(stat -f%z "$JPEG_FILE")
    JPEG_MB=$(echo "scale=2; $JPEG_SIZE / 1048576" | bc)
    echo "📊 JPEG size: ${JPEG_MB}MB"
fi

echo ""
if [ $JPEG_SIZE -le 1048576 ]; then
    echo "✅ Compressed successfully!"
    echo "📁 Output: $JPEG_FILE"
    echo "📊 Final size: ${JPEG_MB}MB"
else
    echo "❌ Could not compress to under 1MB"
    echo "📊 Current size: ${JPEG_MB}MB"
fi
