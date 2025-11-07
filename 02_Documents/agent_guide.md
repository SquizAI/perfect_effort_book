# Perfect Effort: Agent Guide

## Overview

This project uses specialized Claude Code subagents to efficiently produce the book. All agents inherit the model from the main conversation and have access to all MCP tools.

---

## Available Agents

### 🔬 research-agent
**Purpose:** Gather credible sources on psychology, habits, flow state, and success principles

**When to Use:**
- Researching topics like growth mindset, grit, flow state
- Finding academic sources and expert opinions
- Gathering statistics and data
- Investigating sports psychology concepts

**Invocation:** "Use the research-agent to investigate [topic]"

**Output Location:** `01_Research/`

---

### ✍️ chapter-writer
**Purpose:** Draft engaging chapters with authentic teen voice

**When to Use:**
- After chapter outline is complete
- When research and examples are gathered
- For creating first drafts following template

**Invocation:** "Use the chapter-writer to draft Chapter [X]"

**Output Location:** `03_Book_Chapters/ChapterXX_Title.md`

**Prerequisites:**
- Chapter outline exists
- Relevant research completed
- Examples gathered

---

### ✏️ editor-agent
**Purpose:** Polish chapters while maintaining voice and philosophy

**When to Use:**
- After chapter draft is complete
- For improving clarity and engagement
- To ensure output-focused language
- For fact-checking coordination

**Invocation:** "Use the editor-agent to polish Chapter [X]"

**Output Locations:**
- `03_Book_Chapters/ChapterXX_Title_edited.md`
- `02_Documents/editor_notes/ChapterXX_notes.md`

---

### 🧠 meta-agent
**Purpose:** Analyze, update, and enhance other agents

**When to Use:**
- When agent outputs need improvement
- To create new specialized agents
- To update agent instructions
- For maintaining alignment with core principles

**Invocation:** "Use the meta-agent to improve [agent-name]"

**What It Does:**
- Reviews agent performance
- Updates system prompts
- Creates new agents when needed
- Ensures consistency across agents

---

### 🎯 orchestrator-agent
**Purpose:** Coordinate multi-agent workflows and run agents in parallel

**When to Use:**
- For complex tasks requiring multiple agents
- When parallelization can speed up work
- To manage agent handoffs
- For coordinating full chapter pipelines

**Invocation:** "Use the orchestrator-agent to [coordinate workflow]"

**Key Capabilities:**
- Runs independent agents in parallel
- Manages sequential dependencies
- Optimizes workflow efficiency
- Tracks progress across agents

---

## Workflow Examples

### Example 1: Research and Write Chapter 1

**Approach:**
```
1. Tell orchestrator: "Coordinate research and writing for Chapter 1: Life is a Sport"

2. Orchestrator will:
   - Launch research-agent (life-as-sport metaphor)
   - Launch example-finder skill (young athletes)
   [Both in parallel]

   Then:
   - Create chapter outline
   - Launch chapter-writer with research + examples

   Then:
   - Launch editor-agent and fact-check in parallel

   Finally:
   - Incorporate feedback for final version
```

**Timeline:** 3-4 days

---

### Example 2: Research Sprint for Part 1

**Approach:**
```
Tell orchestrator: "Research all topics needed for Part 1 (Chapters 1-4)"

Orchestrator launches in parallel:
- research-agent: Sports psychology
- research-agent: Self-awareness research
- research-agent: Goal-setting frameworks
- research-agent: Deliberate practice
- example-finder: Young athletes
- example-finder: Self-aware students
```

**Timeline:** 1-2 days for all topics

---

### Example 3: Edit Multiple Chapters

**Approach:**
```
Tell orchestrator: "Edit and fact-check Chapters 1-5"

Orchestrator will:
- Edit all 5 chapters in parallel
- Fact-check all 5 chapters in parallel
- Incorporate feedback in parallel
```

**Timeline:** 1 day for 5 chapters

---

## Direct Agent Invocation

You can also invoke agents directly without orchestrator:

**Single Agent:**
```
"Use the research-agent to investigate flow state research from Steven Kotler"
```

**Multiple Agents (Parallel):**
```
"Use the research-agent to investigate growth mindset, and simultaneously use the example-finder to locate young entrepreneurs"
```

---

## Agent Capabilities Summary

| Agent | Research | Writing | Editing | Coordination | Enhancement |
|-------|----------|---------|---------|--------------|-------------|
| research-agent | ✅ | ❌ | ❌ | ❌ | ❌ |
| chapter-writer | ❌ | ✅ | ❌ | ❌ | ❌ |
| editor-agent | ❌ | ❌ | ✅ | ❌ | ❌ |
| orchestrator-agent | ❌ | ❌ | ❌ | ✅ | ❌ |
| meta-agent | ❌ | ❌ | ❌ | ❌ | ✅ |

---

## Skills (Auto-Activate)

### fact-check
Automatically activates when verifying claims, statistics, or sources.

**Manual Invocation:**
```
"Use the fact-check skill to verify Chapter 3"
```

### example-finder
Automatically activates when looking for success stories.

**Manual Invocation:**
```
"Use the example-finder skill to find contemporary student athletes"
```

---

## Core Principles (All Agents Embed These)

1. **"The sooner you learn to be comfortable with being uncomfortable, the sooner you will win in life."**

2. **Focus on OUTPUT, not tasks** - Frame everything as achieving outcomes

3. **Life is a sport** - Consistent metaphor throughout

4. **Teen voice** - Authentic, not condescending (ages 11-18)

5. **Contemporary** - Examples from 2020s, not outdated

---

## Best Practices

### When to Use Orchestrator
- Multi-step workflows
- Parallel opportunities
- Complex dependencies
- Time-sensitive deadlines

### When to Use Individual Agents
- Single, focused tasks
- Learning agent capabilities
- Quick edits or research
- Testing workflows

### When to Use Meta-Agent
- Agent outputs aren't meeting standards
- Need new specialized capability
- Want to improve existing agent
- Ensuring consistency across agents

---

## Quick Reference

**Research a topic:**
```
"Use the research-agent to investigate [topic]"
```

**Write a chapter:**
```
"Use the orchestrator-agent to coordinate Chapter [X] from research to final edit"
```

**Edit a chapter:**
```
"Use the editor-agent to polish Chapter [X]"
```

**Fact-check:**
```
"Use the fact-check skill to verify Chapter [X]"
```

**Find examples:**
```
"Use the example-finder skill to locate [type of success story]"
```

**Improve an agent:**
```
"Use the meta-agent to enhance [agent-name] for better [capability]"
```

**Coordinate complex workflow:**
```
"Use the orchestrator-agent to [describe workflow]"
```

---

## Agent Locations

All agents are stored in: `.claude/agents/`

**Files:**
- `research-agent.md`
- `chapter-writer.md`
- `editor-agent.md`
- `meta-agent.md`
- `orchestrator-agent.md`

**Configuration:**
- All use `model: inherit` (inherits from main chat)
- All have access to full MCP tool suite
- All embed core project principles
