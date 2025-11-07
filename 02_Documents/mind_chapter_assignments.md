# Perfect Effort: Mind Reasoner Chapter Assignments

## Assignment Strategy

Each chapter will be assigned to a digital expert mind whose perspective aligns with the chapter's theme. The Mind Reasoner will simulate how that expert would approach teaching that concept to teens.

---

## Part 1: The Game (Foundation)

### Chapter 1: Life is a Sport
**Mind**: **Steve Jobs** (id: 16c1b8bd-5a2b-46e3-b2e6-3657ca2bc964)
**Why**: Jobs' perfectionism, competitive drive, and ability to frame complex ideas simply makes him ideal for establishing the "life as sport" metaphor.

### Chapter 2: Know Your Stats
**Mind**: **Jensen Huang** (id: 21d8cf46-c1b2-4635-9725-c837a0919be7)
**Why**: Huang's data-driven approach and emphasis on metrics at NVIDIA aligns with self-assessment and knowing where you stand.

### Chapter 3: The Scoreboard That Matters
**Mind**: **Warren Buffett** (id: 5e42c54b-5393-4bc3-9a88-48aa548f8fec)
**Why**: Buffett's focus on internal scorecard vs. external validation is perfect for defining success on your own terms.

### Chapter 4: Practice Like a Pro
**Mind**: **Elon Musk** (id: e3ed83be-c970-4c6a-bcd2-f10cbec205fc)
**Why**: Musk's relentless work ethic, first principles thinking, and deliberate practice mindset.

---

## Part 2: Mental Game (Mindset)

### Chapter 5: Your Inner Coach
**Mind**: **Brian Chesky** (id: 6bb7baed-58c5-4ab9-bbe3-8eef3a37ddce)
**Why**: Chesky's resilience through Airbnb's challenges and positive self-talk under pressure.

### Chapter 6: Losing is Learning
**Mind**: **Jeff Bezos** (id: a35d3d7e-da19-4a4d-bbf3-6adfe01544e3)
**Why**: Bezos' embrace of failure, Day 1 mentality, and long-term thinking despite setbacks.

### Chapter 7: Focus Mode: On
**Mind**: **Andrej Karpathy** (id: 2a9f6362-0261-409b-9efd-277c2ab58185)
**Why**: Karpathy's deep technical focus, ability to concentrate on complex problems, and teaching clarity.

### Chapter 8: The Pressure Test
**Mind**: **Sam Altman** (id: 35525c86-24fc-40d5-b1bc-cc0b9b3cef8f)
**Why**: Altman's experience handling extreme pressure (OpenAI board crisis, rapid scaling) and performing under scrutiny.

---

## Part 3: Daily Training (Habits)

### Chapter 9: Morning Warm-Up
**Mind**: **Jony Ive** (id: 29332f6c-fcdb-43c4-92b1-a859a837c564)
**Why**: Ive's discipline, attention to detail, and systematic creative process for starting each day.

### Chapter 10: Fuel Your Engine
**Mind**: **Satya Nadella** (id: 94ebb860-5c8f-433e-8c7d-c697b1b36e46)
**Why**: Nadella's balanced approach, emphasis on well-being, and sustainable performance mindset.

### Chapter 11: The Recovery Room
**Mind**: **Reed Hastings** (id: b328276b-7232-4125-9fb4-668e350fff5c)
**Why**: Hastings' "freedom and responsibility" culture at Netflix emphasizes balance, vacation time, and recovery.

### Chapter 12: Time is Your Currency
**Mind**: **Peter Thiel** (id: ad836d14-9f52-49f2-8027-49fd018e1ed4)
**Why**: Thiel's contrarian thinking about time allocation and focusing on what truly matters.

### Chapter 13: The Compound Effect
**Mind**: **Marc Andreessen** (id: 73e571b8-f33d-472b-b71f-b83e44e766a1)
**Why**: Andreessen's long-term compounding mindset in tech investments and building enduring companies.

---

## Part 4: Team Play (Relationships)

### Chapter 14: Choose Your Team
**Mind**: **Paul Graham** (id: 8600002e-4058-4b66-8e85-c44596300692)
**Why**: Graham's Y Combinator experience emphasizes choosing the right co-founders and team composition.

### Chapter 15: Be a Team Player
**Mind**: **Sheryl Sandberg** (id: e993e5f1-b461-4e9a-94e7-25fcdc1bc860)
**Why**: Sandberg's collaborative leadership at Facebook and emphasis on teamwork and communication.

### Chapter 16: Find Your Coach
**Mind**: **Marc Benioff** (id: 503e2857-2eb8-4bbf-b0c8-7001bc7e7c66)
**Why**: Benioff's mentorship approach, Ohana culture at Salesforce, and emphasis on learning from others.

---

## Part 5: Championship Level (Excellence)

### Chapter 17: Level Up Your Skills
**Mind**: **Ilya Sutskever** (id: 9ac371ba-ede7-4566-8900-dfe9e38553f7)
**Why**: Sutskever's continuous learning in AI, pushing boundaries, and mastering increasingly complex skills.

### Chapter 18: Play Your Position
**Mind**: **Whitney Wolfe Herd** (id: 43ca9862-678e-420e-a41c-71ae4ed03736)
**Why**: Herd's journey finding her unique position (Bumble's women-first approach) and owning her strengths.

### Chapter 19: Clutch Moments
**Mind**: **Travis Kalanick** (id: aebabf0c-0017-4c2c-a04f-a8666fc3e260)
**Why**: Kalanick's aggressive, high-stakes decision-making under pressure and seizing opportunities at Uber.

### Chapter 20: The Long Game
**Mind**: **Angela Ahrendts** (id: 87413c61-2e3e-4bf2-b375-9c8ea1a57747)
**Why**: Ahrendts' patient, values-driven leadership transforming Burberry and Apple Retail with long-term vision.

---

## Alternate Option: Daniel Ek

**Daniel Ek** (id: 747581fa-8cca-4665-9baf-c9fd85087d9f) - Could be used for any chapter if preferred. Ek's Spotify journey shows patience, vision, and disrupting established industries.

---

## Mind Reasoner Workflow

For each chapter, the process will be:

1. **Create Chapter Outline** - Using `/outline-chapter` command or chapter-writer agent
2. **Simulate with Mind** - Use `mcp__mind-reasoner__simulate` with the assigned mind ID
3. **Query the Mind** - Ask: "How would you teach [chapter concept] to a 15-year-old in a way that makes them excited to apply it?"
4. **Extract Insights** - Use the mind's reasoning to inform chapter writing
5. **Write Chapter** - Use chapter-writer agent incorporating mind's perspective
6. **Edit & Polish** - Use editor-agent to refine

---

## Notes

- Each mind brings unique perspective aligned with chapter theme
- Minds have completed snapshots (status: "completed") ready for simulation
- The digital twin ID for each is in the `_default` twin
- All research is complete and available in `01_Research/` folder

---

## Next Steps

1. Start with Chapter 1 (Steve Jobs mind)
2. Create detailed outline
3. Simulate Steve Jobs' approach to teaching "Life is a Sport"
4. Write chapter incorporating his perspective
5. Iterate through all 20 chapters

This approach combines AI research, human expertise (via digital twins), and our specialized writing agents for maximum quality.
