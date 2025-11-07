#!/bin/bash

# Generate Informative Chapter Images - Teaching Through Visuals
# Each image communicates the core lesson visually

# Load environment variables
set -a
source "$(dirname "$0")/../../.env"
set +a

# Configuration
SCRIPT_DIR="$(dirname "$0")"
CONFIG_FILE="$SCRIPT_DIR/visual_config_informative.json"
OUTPUT_DIR="$SCRIPT_DIR/../../images/generated"
CHAPTERS_DIR="$OUTPUT_DIR/chapters_informative"
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
  echo "Generating Informative Book Cover"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  local output_file="$OUTPUT_DIR/book_cover_informative.png"
  local aspect_ratio=$(jq -r '.bookCover.aspectRatio' "$CONFIG_FILE")
  local prompt=$(jq -r '.bookCover.prompt' "$CONFIG_FILE")

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

  local response=$(curl -s -X POST "$API_ENDPOINT" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d "$json_payload")

  if echo "$response" | grep -q "error"; then
    echo "❌ Error generating book cover:"
    echo "$response" | jq .
    return 1
  fi

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
  local title=$(jq -r ".chapters.\"$chapter_key\".title" "$CONFIG_FILE")
  local quote=$(jq -r ".chapters.\"$chapter_key\".quote" "$CONFIG_FILE")
  local visual_metaphor=$(jq -r ".chapters.\"$chapter_key\".visualMetaphor" "$CONFIG_FILE")
  local teaching_point=$(jq -r ".chapters.\"$chapter_key\".teachingPoint" "$CONFIG_FILE")
  local global_style=$(jq -r ".chapters.globalStyle" "$CONFIG_FILE")

  if [ "$title" == "null" ]; then
    echo "❌ Chapter $chapter_num not found in config"
    return 1
  fi

  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "📚 Chapter $chapter_key: $title"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "💡 Teaching Point: $teaching_point"
  echo ""

  # Build full prompt combining visual metaphor with global style
  local full_prompt="$visual_metaphor

Global Style Requirements: $global_style

Key Teaching Objective: $teaching_point

Requirements:
- 16:9 aspect ratio for chapter headers
- NO text or typography in the image - purely visual storytelling
- Image should TEACH the concept visually - viewer understands lesson from image alone
- Pixar/Disney-quality 3D cartoon realism
- Fun, colorful, educational - appeals to ages 12-18
- Blue-gold championship color palette
- High quality, publication-ready
- Informative and engaging visual communication"

  local output_file="$CHAPTERS_DIR/chapter_${chapter_key}_${title// /_}.png"
  local aspect_ratio="16:9"

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

  local response=$(curl -s -X POST "$API_ENDPOINT" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d "$json_payload")

  if echo "$response" | grep -q "error"; then
    echo "❌ Error generating Chapter $chapter_key:"
    echo "$response" | jq .
    return 1
  fi

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

  sleep 2
}

# Main execution
echo "╔════════════════════════════════════════════════════════╗"
echo "║         Perfect Effort - Informative Visuals           ║"
echo "║   Each Image Teaches the Lesson Through Visual Story  ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""

case "$1" in
  "cover")
    generate_book_cover
    ;;
  "chapter")
    if [ -z "$2" ]; then
      echo "❌ Please specify chapter number: ./generate_informative.sh chapter 5"
      exit 1
    fi
    generate_chapter "$2"
    ;;
  "all")
    generate_book_cover
    echo ""

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
    echo "║              Informative Generation Complete           ║"
    echo "╚════════════════════════════════════════════════════════╝"
    echo ""
    echo "✅ Successful: $SUCCESS chapters"
    echo "❌ Failed: $FAILED chapters"
    echo "📁 Book Cover: $OUTPUT_DIR/book_cover_informative.png"
    echo "📁 Chapters: $CHAPTERS_DIR/"
    ;;
  *)
    echo "Usage:"
    echo "  ./generate_informative.sh cover          # Generate book cover"
    echo "  ./generate_informative.sh chapter 5      # Generate specific chapter"
    echo "  ./generate_informative.sh all            # Generate everything"
    exit 1
    ;;
esac
