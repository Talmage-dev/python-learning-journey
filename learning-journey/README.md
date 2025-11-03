# Learning System Guide

## 📁 File Structure Overview

```
learning-journey/
├── README.md                      ← You are here!
├── 00-QUICK-START.md              ← Open this every morning
├── 01-learning-strategy.md        ← Reference weekly
├── 02-roadmap.md                  ← Reference monthly
├── 03-daily-template.md           ← Copy for each day
├── 04-weekly-review-template.md   ← Copy each Sunday
└── daily-logs/
    ├── 2025-11/
    │   ├── day-25-nov-03.md
    │   ├── day-26-nov-04.md
    │   └── ...
    └── 2025-12/
        └── ...
```

---

## 🚀 How to Use This System

### Every Morning (5 min):

1. **Open `00-QUICK-START.md`**
   - See today's focus at a glance
   - Check rotation schedule
   - Know what to work on

2. **Copy `03-daily-template.md`**
   ```bash
   # In terminal:
   cp 03-daily-template.md daily-logs/2025-11/day-25-nov-03.md
   ```
   
3. **Fill in today's objectives**
   - Based on yesterday's review
   - Adjust for current needs
   - Keep it specific and measurable

### During the Day:

- Work through objectives
- Check boxes as you complete
- Make quick notes of insights
- No need to update anything else yet

### Every Evening (10 min):

1. **Complete daily review section**
   - Score each objective (✅/⚠️/❌)
   - Calculate daily score
   - Write 1-2 sentence key insight
   - Create tomorrow's objectives

2. **Update `00-QUICK-START.md`** (if needed)
   - Skill moved from 🟡 to 🟢? Update it!
   - New topic in intensive practice? Add it!
   - Keep it current for tomorrow morning

### Every Sunday (20 min):

1. **Copy `04-weekly-review-template.md`**
   ```bash
   cp 04-weekly-review-template.md daily-logs/2025-11/week-05-review.md
   ```

2. **Complete weekly review**
   - Calculate weekly average
   - Update skills status
   - Check roadmap progress
   - Write teaching moment

3. **Update ALL tracking files:**

   **`00-QUICK-START.md`:**
   - Current milestone progress (%)
   - Skills moved between phases
   - Next week's focus areas
   - Rotation schedule if changed

   **`01-learning-strategy.md`:**
   - Usually no changes needed
   - Only update if strategy itself changes
   - Rare (maybe once a month)

   **`02-roadmap.md`:**
   - Update current milestone %
   - Adjust timeline if needed
   - Move completed topics to ✅
   - Update "Time Remaining" section

### Monthly (30 min):

- Review all weekly reviews
- Update roadmap with real progress
- Adjust estimates if needed
- Celebrate how far you've come!

---

## 📝 When to Update Each File

### `00-QUICK-START.md` - Update Often!
**When:**
- Daily (if skills status changes)
- Definitely on Sundays
- When starting new topic
- When moving between phases

**What to update:**
- Current skills status (%)
- Phase movements (🟡→🟢)
- This week's focus
- Rotation schedule

---

### `01-learning-strategy.md` - Update Rarely
**When:**
- Strategy isn't working (very rare)
- Major life change (schedule shift)
- New insight about learning
- Maybe once every 1-2 months

**What to update:**
- Daily time structure
- Intensive practice activities
- Objective categories
- Phase criteria

**⚠️ Warning:** Don't tinker too much! Strategy is working.

---

### `02-roadmap.md` - Update Weekly/Monthly
**When:**
- Every Sunday (quick updates)
- End of milestone (full update)
- Timeline needs adjustment
- Monthly progress review

**What to update:**
- Milestone completion %
- Timeline estimates
- Skills mastery levels
- "Progress Tracking" section
- "Time Remaining" estimates

---

### `03-daily-template.md` - Never Update!
**Purpose:** This is your blank template

**Keep it clean:**
- Never write actual progress here
- Only update if you change daily structure
- Copy it, don't modify it

---

### `04-weekly-review-template.md` - Never Update!
**Purpose:** This is your blank template

**Keep it clean:**
- Never write actual reviews here
- Only update if you change review structure
- Copy it, don't modify it

---

## 🔄 Typical Weekly Workflow

### Monday Morning:
```
1. Open 00-QUICK-START.md
2. See: "This week focus: Hash Tables + Insertion Sort"
3. Copy 03-daily-template.md to day-25-nov-03.md
4. Fill in objectives
5. Start working!
```

### Monday-Saturday:
```
- Work through daily objectives
- Evening: Score + plan tomorrow
- Quick update to 00-QUICK-START.md if needed
```

### Sunday Evening:
```
1. Copy 04-weekly-review-template.md to week-05-review.md
2. Calculate weekly average from 7 daily scores
3. Update skills status
4. Check roadmap progress
5. Write teaching moment
6. Update 00-QUICK-START.md with new week info
7. Update 02-roadmap.md with progress
```

---

## 🎯 Quick Reference: What File Do I Need?

**"What do I work on today?"**
→ Open `00-QUICK-START.md`

**"How do I do intensive practice?"**
→ Open `01-learning-strategy.md` - Phase 2 section

**"When do I move to the next milestone?"**
→ Open `02-roadmap.md` - Milestone Completion Criteria

**"What did I do yesterday?"**
→ Open yesterday's file in `daily-logs/`

**"How's my progress this week?"**
→ Open this week's daily logs and calculate average

**"What's my long-term timeline?"**
→ Open `02-roadmap.md` - Timeline Summary section

**"How do I structure today?"**
→ Copy `03-daily-template.md` to today

---

## 💡 Pro Tips

### Keep Quick Start Current
The `00-QUICK-START.md` is your daily driver. If it's outdated, you'll be lost. Update it religiously on Sundays.

### Don't Over-Update
Only update files when something actually changes. Don't tinker with the strategy just because you can.

### Daily Logs are History
Never delete or heavily edit old daily logs. They're your learning history. Even mistakes are valuable data.

### Use Git (Optional but Recommended)
```bash
git init
git add .
git commit -m "Day 25 complete - Insertion Sort mastered"
```

Benefits:
- Never lose your work
- See progress over time
- Revert if needed

### Search Your Logs
Keep daily logs in plain markdown so you can search:
```bash
grep -r "hash table" daily-logs/
# Find all days you worked on hash tables
```

---

## 🚨 Common Mistakes to Avoid

### ❌ Updating Strategy Too Often
You'll be tempted to "optimize" constantly. Don't. Give the current system at least 2-4 weeks before changing anything.

### ❌ Not Updating Quick Start
If Quick Start is outdated, your mornings will be confused. Update it every Sunday minimum.

### ❌ Over-Detailed Daily Logs
You're not writing a novel. Quick notes are fine. The template is the maximum detail needed.

### ❌ Ignoring Weekly Reviews
This is where you catch problems early. Don't skip it.

### ❌ Guilt About Timeline Changes
Roadmap is flexible! If you need to adjust, adjust. No guilt.

---

## 📊 Tracking Your Progress

### Daily Score Trend
Keep a simple list somewhere (notebook, spreadsheet, or just scan your daily logs):
```
Day 25: 4.5/5 (90%)
Day 26: 4.0/5 (80%)
Day 27: 4.5/5 (90%)
...
Weekly Avg: 4.3/5 (86%)
```

### Skills Progress
Your `00-QUICK-START.md` has this already! Just keep it updated.

### Milestone Progress
Check `02-roadmap.md` monthly to see how far you've come.

---

## 🎓 Example Day Workflow

### Morning (7:00 AM):
```
1. Red Bull
2. Open 00-QUICK-START.md
3. "Today: Maintenance (Stack), Intensive (Hash Tables), Learn (Insertion Sort)"
4. Copy template to day-25-nov-03.md
5. Fill in specific objectives
6. Start typing practice
```

### During Day:
```
- Complete objectives
- Check boxes
- Make notes
- Code, learn, practice
```

### Evening (8:00 PM):
```
1. Open today's log: day-25-nov-03.md
2. Score each objective: ✅✅⚠️✅✅ = 4.5/5 (90%)
3. Note: "Hash tables clicking! Insertion sort easier than expected."
4. Create tomorrow's objectives in the template section
5. Quick check: Did any skill level up? Update 00-QUICK-START.md if yes
6. Done! 
```

### Sunday (8:00 PM):
```
1. Copy weekly review template
2. List all 7 daily scores: 4.5, 4.0, 4.5, 5.0, 4.5, 4.0, 4.5
3. Average: 4.43/5 (88.6%) ← Excellent!
4. Update skills: Hash Tables 80% → 85%
5. Write teaching moment about hash tables
6. Update 00-QUICK-START.md: New percentages, next week focus
7. Update 02-roadmap.md: Milestone 3 now 88% complete
8. Plan next week's focus areas
9. Done!
```

---

## 🆘 Troubleshooting

**Q: I forgot to update Quick Start for 2 weeks. Now what?**
A: Spend 15 minutes going through your daily logs. Update skills status based on your recent scores. Fresh start!

**Q: My daily logs are all over the place. Should I reorganize?**
A: Yes! Create folders by month. Move files. Use consistent naming: `day-XX-mon-DD.md`

**Q: I want to change the daily structure. Which file?**
A: Change `01-learning-strategy.md` AND `03-daily-template.md` AND update `00-QUICK-START.md` to reflect the new structure.

**Q: Can I skip weekly reviews if I'm busy?**
A: You can, but don't make it a habit. Reviews are where you catch problems. At minimum, calculate your weekly average and update skill percentages.

**Q: The roadmap timeline is way off. What do I do?**
A: Update `02-roadmap.md` with realistic estimates. No guilt! Write a note about why (learning deeply, life events, etc.). The journey matters more than the timeline.

---

## ✅ Setup Checklist

Before starting Day 25, make sure you have:

- [ ] All 6 files in your `learning-journey/` folder
- [ ] `daily-logs/` folder created with `2025-11/` subfolder
- [ ] Read this README completely
- [ ] Bookmarked `00-QUICK-START.md` (you'll open it daily!)
- [ ] Copied `03-daily-template.md` to `day-25-nov-03.md`
- [ ] (Optional) Initialized git repository
- [ ] Ready to lock in and find your stride! 🚀

---

## 🎯 Remember

- **Quick Start** = Your daily command center
- **Daily logs** = Your learning history
- **Weekly reviews** = Your course correction
- **Strategy** = Rarely changes
- **Roadmap** = Adjusts as you learn

**Most important:** Actually doing the work beats perfect organization!

---

