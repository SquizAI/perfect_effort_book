#!/bin/bash

# Generate Book Cover for Perfect Effort
# Uses Gemini 2.5 Flash Image API

# Load environment variables
set -a
source "$(dirname "$0")/../../.env"
set +a

# Configuration
OUTPUT_DIR="$(dirname "$0")/../../images/generated"
OUTPUT_FILE="$OUTPUT_DIR/book_cover.png"
API_ENDPOINT="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent"

# Ensure output directory exists
mkdir -p "$OUTPUT_DIR"

# Book cover prompt - designed for 2:3 aspect ratio (typical book cover)
PROMPT="Create a professional book cover image for 'Perfect Effort: Winning at the Game of Life'.
The book is aimed at middle and high school students teaching them success fundamentals.

Design requirements:
- Bold, energetic, modern design that appeals to teens
- Sports/athletic theme but not limited to one sport
- Championship/winning imagery (trophy, podium, victory gestures)
- Color palette: vibrant blues, golds, and energetic colors
- Clean, professional typography-ready space at top for title
- Inspirational and empowering mood
- No text overlay - just the visual design
- High quality, print-ready aesthetic
- Abstract or illustrative style, not photorealistic
- Dynamic movement and energy

The cover should convey: growth, achievement, excellence, potential, and the excitement of mastering life's fundamentals."

# Create JSON payload
JSON_PAYLOAD=$(cat <<EOF
{
  "contents": [{
    "parts": [{
      "text": "$PROMPT"
    }]
  }],
  "generationConfig": {
    "responseModalities": ["Image"],
    "imageConfig": {
      "aspectRatio": "2:3"
    }
  }
}
EOF
)

echo "Generating book cover..."
echo "Output will be saved to: $OUTPUT_FILE"

# Make API request
RESPONSE=$(curl -s -X POST "$API_ENDPOINT" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d "$JSON_PAYLOAD")

# Check for errors
if echo "$RESPONSE" | grep -q "error"; then
  echo "Error generating image:"
  echo "$RESPONSE" | jq .
  exit 1
fi

# Extract base64 image data and save
echo "$RESPONSE" | grep -o '"data": "[^"]*"' | head -1 | cut -d'"' -f4 | base64 -d > "$OUTPUT_FILE"

if [ -f "$OUTPUT_FILE" ]; then
  echo "✅ Book cover generated successfully!"
  echo "📁 Location: $OUTPUT_FILE"

  # Get file size
  FILE_SIZE=$(ls -lh "$OUTPUT_FILE" | awk '{print $5}')
  echo "📊 File size: $FILE_SIZE"
else
  echo "❌ Failed to save image"
  exit 1
fi
