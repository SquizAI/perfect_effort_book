# Image Generation Scripts

Automated scripts for generating book cover and chapter images using the Gemini 2.5 Flash Image API.

## Prerequisites

- **Gemini API Key**: Stored in `.env` file at project root
- **Dependencies**: `curl`, `jq`, `base64` (should be pre-installed on macOS)
- **jq installation** (if needed): `brew install jq`

## Setup

1. Ensure `.env` file exists with your API key:
```bash
GEMINI_API_KEY=your_api_key_here
```

2. Make scripts executable (already done):
```bash
chmod +x generate_book_cover.sh
chmod +x generate_chapter_images.sh
```

## Usage

### Generate Book Cover

```bash
./generate_book_cover.sh
```

**Output:**
- Location: `../../images/generated/book_cover.png`
- Aspect Ratio: 2:3 (832x1248) - Standard book cover dimensions
- Style: Modern, energetic, youth-focused design

### Generate Chapter Images

**Generate all 20 chapter images:**
```bash
./generate_chapter_images.sh
```

**Generate a specific chapter:**
```bash
./generate_chapter_images.sh 5    # Generates only Chapter 5
```

**Output:**
- Location: `../../images/generated/chapters/`
- Naming: `chapter_XX_Title_Name.png`
- Aspect Ratio: 16:9 (1344x768) - Perfect for chapter headers
- Style: Consistent, professional, age-appropriate

## Image Specifications

### Book Cover
- **Aspect Ratio**: 2:3
- **Resolution**: 832x1248
- **Use Case**: Front cover, promotional materials
- **Theme**: Championship, achievement, youth empowerment

### Chapter Images
- **Aspect Ratio**: 16:9
- **Resolution**: 1344x768
- **Use Case**: Chapter headers, digital displays
- **Theme**: Varies per chapter, consistent style

## Chapter List

| # | Title | Theme |
|---|-------|-------|
| 01 | Life is a Sport | Sports/gaming metaphor |
| 02 | Know Your Stats | Self-awareness, metrics |
| 03 | The Scoreboard That Matters | Personal success definition |
| 04 | Practice Like a Pro | Deliberate practice |
| 05 | Your Inner Coach | Positive self-talk |
| 06 | Losing is Learning | Growth from failure |
| 07 | Focus Mode: On | Deep concentration |
| 08 | The Pressure Test | Performing under pressure |
| 09 | Morning Warm-Up | Morning routines |
| 10 | Fuel Your Engine | Nutrition and wellness |
| 11 | The Recovery Room | Rest and recovery |
| 12 | Time is Your Currency | Time management |
| 13 | The Compound Effect | Consistency and growth |
| 14 | Choose Your Teammates | Strategic relationships |
| 15 | The Mentor Advantage | Learning from others |
| 16 | Building Your Support System | Community support |
| 17 | Level Up Your Skills | Continuous improvement |
| 18 | Play Your Position | Finding your role |
| 19 | Clutch Moments | Peak performance |
| 20 | The Long Game | Long-term thinking |

## API Details

- **Endpoint**: `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent`
- **Authentication**: Header `x-goog-api-key`
- **Token Usage**: ~1290 tokens per image
- **Rate Limiting**: 2-second delay between requests

## Troubleshooting

### Error: "jq: command not found"
Install jq: `brew install jq`

### Error: "Permission denied"
Make scripts executable: `chmod +x *.sh`

### Error: API authentication failed
Check your `.env` file and ensure `GEMINI_API_KEY` is set correctly

### Images not generating
1. Verify internet connection
2. Check API key validity
3. Review error messages in terminal output
4. Ensure output directories exist

## Output Directory Structure

```
images/
└── generated/
    ├── book_cover.png
    └── chapters/
        ├── chapter_01_Life_is_a_Sport.png
        ├── chapter_02_Know_Your_Stats.png
        ├── chapter_03_The_Scoreboard_That_Matters.png
        └── ... (all 20 chapters)
```

## Notes

- Images are generated without text overlays (text added separately in design software)
- Style is consistent across all chapters for cohesive book design
- All prompts designed specifically for middle/high school audience (ages 12-18)
- Rate limiting built-in to respect API quotas

## Cost Estimation

Based on Gemini API pricing (as of 2025):
- Book Cover: 1 image × 1290 tokens
- All Chapters: 20 images × 1290 tokens
- **Total**: ~25,800 tokens

Refer to current Gemini API pricing for exact costs.
