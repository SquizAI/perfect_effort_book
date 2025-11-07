#!/bin/bash

# Generate Chapter Images for Perfect Effort
# Uses Gemini 2.5 Flash Image API

# Load environment variables
set -a
source "$(dirname "$0")/../../.env"
set +a

# Configuration
OUTPUT_DIR="$(dirname "$0")/../../images/generated/chapters"
API_ENDPOINT="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent"

# Ensure output directory exists
mkdir -p "$OUTPUT_DIR"

# Unified Visual Theme: Championship Stadium/Arena
# All images share: blue-gold palette, stadium setting, dramatic lighting, polished arena floor
UNIFIED_THEME="Setting: Professional championship stadium/arena environment. Lighting: Dramatic overhead spotlights creating focused illumination on the main element. Arena floor: Polished, reflective surface with subtle blue-gold glow. Background: Soft-focused stadium seating in deep navy, subtle crowd atmosphere. Color palette: Deep championship blue (#1E3A8A), victory gold (#F59E0B), energetic orange accents (#EA580C). Artistic style: Modern 3D illustration, smooth gradients, professional finish. Perspective: Slightly elevated view (15-20 degrees), centered composition. Depth of field: Sharp focus on main element, soft blurred stadium background. Mood: Inspirational championship atmosphere, energetic yet professional."

# Chapter definitions with focused prompts (main element only)
declare -A CHAPTERS=(
  ["01"]="Life is a Sport|Main element: Collection of diverse sports equipment (basketball, soccer ball, chess pieces, running shoes, gaming controller) artfully arranged on a pedestal at center arena. Equipment glows subtly with blue-gold lighting."

  ["02"]="Know Your Stats|Main element: Holographic digital dashboard floating above arena floor, displaying glowing metrics, progress bars, and analytics in blue-gold neon light. Futuristic HUD design."

  ["03"]="The Scoreboard That Matters|Main element: Modern championship scoreboard mounted on pedestal, displaying unconventional success metrics (growth, learning, relationships) instead of points. Gold frame, blue digital displays."

  ["04"]="Practice Like a Pro|Main element: Training equipment arranged in focused training station - weights, practice dummy, musical instrument, books - spotlit on arena floor. Shows dedication to deliberate practice."

  ["05"]="Your Inner Coach|Main element: Glowing human silhouette figure in arena center with radiating golden inner light representing inner wisdom and self-talk. Ethereal, empowering presence."

  ["06"]="Losing is Learning|Main element: Phoenix rising sculpture in gold and blue flames, or broken trophy pieces reassembling into stronger form, placed on arena pedestal. Transformation imagery."

  ["07"]="Focus Mode: On|Main element: Massive illuminated target/bullseye on arena floor with single arrow in dead center. Intense spotlight beam. Represents laser focus and flow state."

  ["08"]="The Pressure Test|Main element: Diamond forming under visible pressure forces, displayed in glass case on arena floor. Dramatic lighting showing transformation under pressure. Blue-gold crystalline structure."

  ["09"]="Morning Warm-Up|Main element: Sunrise breaking through arena skylight, illuminating morning ritual items on platform - yoga mat, healthy meal, journal, water. Dawn golden light mixing with arena blue."

  ["10"]="Fuel Your Engine|Main element: Stylized engine made of fresh fruits, water droplets, and energy symbols on display stand in arena. Vibrant, health-focused, powered-up aesthetic with blue-gold energy glow."

  ["11"]="The Recovery Room|Main element: Serene recovery station in arena - meditation cushion, gentle plants, rest zone - bathed in calm blue light. Peaceful refuge within championship environment."

  ["12"]="Time is Your Currency|Main element: Ornate hourglass on pedestal where sand is made of gold coins, clock elements integrated. Time-as-treasure metaphor. Precious metal and blue glass construction."

  ["13"]="The Compound Effect|Main element: Domino chain mid-fall creating exponential growth pattern, or single seed sprouting into glowing golden tree. Small-to-large progression visual on arena floor."

  ["14"]="Choose Your Teammates|Main element: Circle of diverse hands reaching inward, forming unified team huddle above arena floor. Connected with blue-gold energy bonds. Selective collaboration."

  ["15"]="The Mentor Advantage|Main element: Two figures - mentor and mentee - on stepped platform, mentor illuminating mentee's path with golden light beam. Guidance and wisdom transfer visual."

  ["16"]="Building Your Support System|Main element: Strong architectural pillars forming supportive structure, or network web glowing with connection points. Foundation strength visual in blue-gold tones."

  ["17"]="Level Up Your Skills|Main element: Ascending stairway of skill levels (beginner to mastery) with glowing progression indicators, achievement symbols at each level. Upward trajectory on arena floor."

  ["18"]="Play Your Position|Main element: Chess piece (king or queen) perfectly positioned on strategic board space, or athlete in ideal stance. Finding-your-role visual. Gold piece on blue board."

  ["19"]="Clutch Moments|Main element: Basketball frozen at rim mid-swish, or sprinter breaking finish tape in victory. Game-winning instant captured. Peak performance moment under spotlight."

  ["20"]="The Long Game|Main element: Winding marathon path leading from arena floor to distant mountain peak visible through arena opening. Long journey visual. Patient persistence pathway in blue-gold."
)

# Function to generate a single chapter image
generate_chapter_image() {
  local chapter_num=$1
  local chapter_data=$2
  local title=$(echo "$chapter_data" | cut -d'|' -f1)
  local prompt=$(echo "$chapter_data" | cut -d'|' -f2)

  local output_file="$OUTPUT_DIR/chapter_${chapter_num}_${title// /_}.png"

  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "Generating Chapter $chapter_num: $title"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  # Combine main element with unified theme
  FULL_PROMPT="$prompt

$UNIFIED_THEME

Additional requirements:
- 16:9 aspect ratio, perfect for chapter headers
- No text or typography in the image
- Appeals to middle and high school students (ages 12-18)
- High quality, publication-ready
- Maintains visual consistency with all other chapter images
- All images must look like they belong to the same series"

  # Create JSON payload
  JSON_PAYLOAD=$(cat <<EOF
{
  "contents": [{
    "parts": [{
      "text": "$FULL_PROMPT"
    }]
  }],
  "generationConfig": {
    "responseModalities": ["Image"],
    "imageConfig": {
      "aspectRatio": "16:9"
    }
  }
}
EOF
)

  # Make API request
  RESPONSE=$(curl -s -X POST "$API_ENDPOINT" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d "$JSON_PAYLOAD")

  # Check for errors
  if echo "$RESPONSE" | grep -q "error"; then
    echo "❌ Error generating image for Chapter $chapter_num:"
    echo "$RESPONSE" | jq .
    return 1
  fi

  # Extract base64 image data and save
  echo "$RESPONSE" | grep -o '"data": "[^"]*"' | head -1 | cut -d'"' -f4 | base64 -d > "$output_file"

  if [ -f "$output_file" ]; then
    FILE_SIZE=$(ls -lh "$output_file" | awk '{print $5}')
    echo "✅ Generated successfully!"
    echo "📁 Location: $output_file"
    echo "📊 File size: $FILE_SIZE"
  else
    echo "❌ Failed to save image"
    return 1
  fi

  # Small delay to respect rate limits
  sleep 2
}

# Main execution
echo "╔════════════════════════════════════════════════════════╗"
echo "║         Perfect Effort - Chapter Image Generator       ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""

# Check if specific chapter requested
if [ -n "$1" ]; then
  chapter_num=$(printf "%02d" $(echo $1 | sed 's/^0*//'))
  if [ -n "${CHAPTERS[$chapter_num]}" ]; then
    generate_chapter_image "$chapter_num" "${CHAPTERS[$chapter_num]}"
  else
    echo "❌ Chapter $1 not found. Valid chapters: 1-20"
    exit 1
  fi
else
  # Generate all chapters
  SUCCESS_COUNT=0
  FAIL_COUNT=0

  for chapter_num in $(echo "${!CHAPTERS[@]}" | tr ' ' '\n' | sort); do
    if generate_chapter_image "$chapter_num" "${CHAPTERS[$chapter_num]}"; then
      ((SUCCESS_COUNT++))
    else
      ((FAIL_COUNT++))
    fi
  done

  echo ""
  echo "╔════════════════════════════════════════════════════════╗"
  echo "║                    Generation Complete                 ║"
  echo "╚════════════════════════════════════════════════════════╝"
  echo ""
  echo "✅ Successful: $SUCCESS_COUNT"
  echo "❌ Failed: $FAIL_COUNT"
  echo "📁 Output directory: $OUTPUT_DIR"
fi
