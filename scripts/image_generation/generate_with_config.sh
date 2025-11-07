#!/bin/bash

# Generate Perfect Effort Images using visual_config.json
# Cartoon Realism Style - Fun, Educational, Pixar-quality

# Load environment variables
set -a
source "$(dirname "$0")/../../.env"
set +a

# Configuration
SCRIPT_DIR="$(dirname "$0")"
CONFIG_FILE="$SCRIPT_DIR/visual_config.json"
OUTPUT_DIR="$SCRIPT_DIR/../../images/generated"
CHAPTERS_DIR="$OUTPUT_DIR/chapters_v2"
API_ENDPOINT="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent"

# Ensure directories exist
mkdir -p "$OUTPUT_DIR"
mkdir -p "$CHAPTERS_DIR"

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "❌ Error: jq is required but not installed"
    echo "Install with: brew install jq"
    exit 1
fi

# Function to generate book cover
generate_book_cover() {
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "Generating Book Cover (Cartoon Realism Style)"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  local output_file="$OUTPUT_DIR/book_cover_v2.png"
  local aspect_ratio=$(jq -r '.bookCover.aspectRatio' "$CONFIG_FILE")
  local prompt=$(jq -r '.bookCover.prompt' "$CONFIG_FILE")

  # Create JSON payload
  local json_payload=$(cat <<EOF
{
  "contents": [{
    "parts": [{
      "text": "$prompt"
    }]
  }],
  "generationConfig": {
    "responseModalities": ["Image"],
    "imageConfig": {
      "aspectRatio": "$aspect_ratio"
    }
  }
}
EOF
)

  # Make API request
  local response=$(curl -s -X POST "$API_ENDPOINT" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d "$json_payload")

  # Check for errors
  if echo "$response" | grep -q "error"; then
    echo "❌ Error generating book cover:"
    echo "$response" | jq .
    return 1
  fi

  # Extract and save image
  echo "$response" | grep -o '"data": "[^"]*"' | head -1 | cut -d'"' -f4 | base64 -d > "$output_file"

  if [ -f "$output_file" ]; then
    local file_size=$(ls -lh "$output_file" | awk '{print $5}')
    echo "✅ Book cover generated!"
    echo "📁 Location: $output_file"
    echo "📊 Size: $file_size"
    return 0
  else
    echo "❌ Failed to save image"
    return 1
  fi
}

# Function to generate a single chapter image
generate_chapter() {
  local chapter_num=$1
  local chapter_key=$(printf "%02d" $chapter_num)

  # Get chapter data from JSON
  local title=$(jq -r ".chapters.imagePrompts.\"$chapter_key\".title" "$CONFIG_FILE")
  local main_element=$(jq -r ".chapters.imagePrompts.\"$chapter_key\".mainElement" "$CONFIG_FILE")
  local chapter_style=$(jq -r ".chapters.imagePrompts.\"$chapter_key\".style" "$CONFIG_FILE")

  if [ "$title" == "null" ]; then
    echo "❌ Chapter $chapter_num not found in config"
    return 1
  fi

  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "Generating Chapter $chapter_key: $title"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  # Build unified theme from JSON
  local unified_theme=$(jq -r '.chapters.unifiedTheme |
    "Setting: \(.setting). " +
    "Lighting: \(.lighting). " +
    "Floor: \(.floor). " +
    "Background: \(.background). " +
    "Color palette: Primary \(.colorPalette.primary), Secondary \(.colorPalette.secondary), Accent \(.colorPalette.accent), Pops of \(.colorPalette.pops). " +
    "Artistic style: \(.style). " +
    "Perspective: \(.perspective). " +
    "Composition: \(.composition). " +
    "Depth of field: \(.depthOfField). " +
    "Mood: \(.mood). " +
    "Target audience: \(.targetAudience)."' "$CONFIG_FILE")

  # Build full prompt
  local full_prompt="$main_element

$unified_theme

Chapter-specific style: $chapter_style

Requirements:
- 16:9 aspect ratio, perfect for chapter headers
- No text or typography in the image
- Pixar/Disney-quality 3D cartoon realism
- Fun but educational - appeals to ages 12-18
- High quality, publication-ready
- Maintains visual consistency with all other chapter images
- Professional cartoon rendering with personality"

  local output_file="$CHAPTERS_DIR/chapter_${chapter_key}_${title// /_}.png"
  local aspect_ratio=$(jq -r '.chapters.aspectRatio' "$CONFIG_FILE")

  # Create JSON payload
  local json_payload=$(cat <<EOF
{
  "contents": [{
    "parts": [{
      "text": "$full_prompt"
    }]
  }],
  "generationConfig": {
    "responseModalities": ["Image"],
    "imageConfig": {
      "aspectRatio": "$aspect_ratio"
    }
  }
}
EOF
)

  # Make API request
  local response=$(curl -s -X POST "$API_ENDPOINT" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d "$json_payload")

  # Check for errors
  if echo "$response" | grep -q "error"; then
    echo "❌ Error generating Chapter $chapter_key:"
    echo "$response" | jq .
    return 1
  fi

  # Extract and save image
  echo "$response" | grep -o '"data": "[^"]*"' | head -1 | cut -d'"' -f4 | base64 -d > "$output_file"

  if [ -f "$output_file" ]; then
    local file_size=$(ls -lh "$output_file" | awk '{print $5}')
    echo "✅ Generated successfully!"
    echo "📁 Location: $output_file"
    echo "📊 Size: $file_size"
  else
    echo "❌ Failed to save image"
    return 1
  fi

  # Rate limiting
  sleep 2
}

# Main execution
echo "╔════════════════════════════════════════════════════════╗"
echo "║    Perfect Effort - Cartoon Realism Image Generator   ║"
echo "║         Fun • Educational • Pixar-Quality 3D           ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""

# Parse command line arguments
case "$1" in
  "cover")
    generate_book_cover
    ;;
  "chapter")
    if [ -z "$2" ]; then
      echo "❌ Please specify chapter number: ./generate_with_config.sh chapter 5"
      exit 1
    fi
    generate_chapter "$2"
    ;;
  "all")
    # Generate book cover
    generate_book_cover
    echo ""

    # Generate all 20 chapters
    SUCCESS=0
    FAILED=0

    for i in {1..20}; do
      if generate_chapter $i; then
        ((SUCCESS++))
      else
        ((FAILED++))
      fi
    done

    echo ""
    echo "╔════════════════════════════════════════════════════════╗"
    echo "║                  Generation Complete                   ║"
    echo "╚════════════════════════════════════════════════════════╝"
    echo ""
    echo "✅ Successful: $SUCCESS"
    echo "❌ Failed: $FAILED"
    echo "📁 Book Cover: $OUTPUT_DIR/book_cover_v2.png"
    echo "📁 Chapters: $CHAPTERS_DIR/"
    ;;
  *)
    echo "Usage:"
    echo "  ./generate_with_config.sh cover           # Generate book cover"
    echo "  ./generate_with_config.sh chapter 5       # Generate specific chapter"
    echo "  ./generate_with_config.sh all             # Generate everything"
    exit 1
    ;;
esac
