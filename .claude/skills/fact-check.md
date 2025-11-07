---
name: fact-check
description: Verify facts, statistics, and research claims in book content for accuracy. Use when checking chapter drafts, research notes, or any content containing factual claims or citations.
---

# Fact-Check Skill

This skill verifies the accuracy of claims, statistics, and research references used in the book.

## Instructions

1. **Identify Claims**: Extract all factual claims and statistics from the provided content
2. **Verify Sources**: Use web search to check if sources are credible and current
3. **Cross-Reference**: Compare claims against multiple authoritative sources
4. **Flag Issues**: Highlight inaccuracies, outdated information, or unsupported claims
5. **Provide Corrections**: Suggest accurate information with proper citations

## Process Steps

### Input Analysis
- Read through the content thoroughly
- Mark every factual claim, statistic, and research reference
- Note any missing citations

### Verification
- Search for each claim using web search tools
- Check publication dates (research should be within last 10 years ideally)
- Verify author credentials and institutional affiliations
- Cross-check statistics across multiple sources
- Confirm research findings haven't been disputed

### Output Report

Create a markdown report with:

```markdown
## ✅ Verified Facts
[List confirmed facts with sources]

## ⚠️ Needs Clarification
[List claims that need better sourcing or context]

## ❌ Inaccurate Information
[List errors with corrections and proper sources]

## 📚 Source Quality
[Assess credibility of cited sources]

## 💡 Recommendations
[Suggest improvements for citations and claims]
```

## Focus Areas

- Growth mindset research (Carol Dweck)
- Grit studies (Angela Duckworth)
- Flow state research (Steven Kotler, Flow Research Collective)
- Sports psychology findings
- Adolescent brain development
- Habit formation science (James Clear, BJ Fogg)
- Learning and memory research
- Success statistics and case studies

## Examples

**Good Claim**: "Research from Stanford psychologist Carol Dweck shows that students with a growth mindset achieve higher grades over time."
- ✅ Verifiable, credible source, specific

**Bad Claim**: "Studies show that 90% of successful people wake up early."
- ❌ Vague source, likely inaccurate statistic, needs citation

## Save Results

Save reports to: `02_Documents/fact_checks/ChapterXX_factcheck_YYYY-MM-DD.md`
