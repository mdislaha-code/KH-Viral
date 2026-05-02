# KH-Viral Agent - Complete Usage Guide

**How to Use Your Private AI Viral News Agent**

---

## 📋 Table of Contents

1. [Quick Start](#quick-start)
2. [Running the Agent](#running-the-agent)
3. [Understanding Output](#understanding-output)
4. [Managing Collaborators](#managing-collaborators)
5. [Advanced Usage](#advanced-usage)
6. [Troubleshooting](#troubleshooting)

---

## Quick Start

### For First-Time Users

```bash
# 1. Navigate to project
cd KH-Viral

# 2. Activate environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# 3. Run the agent
python main.py

# 4. Wait for completion (usually 2-5 minutes)
# 5. Check results in output/ folder
```

---

## Running the Agent

### Method 1: Manual Run (Local)

**Step 1: Open Terminal**

```bash
cd KH-Viral
```

**Step 2: Activate Environment**

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**Step 3: Run Agent**

```bash
python main.py
```

**Output:**
```
============================================================
KH-Viral Agent Started
Timestamp: 2026-05-02T10:30:45.123456
============================================================

[STEP 1] Collecting news from all sources...
✓ Collected 127 articles
✓ Filtered to 45 articles with emotional themes
✓ Top 5 articles by engagement selected

[STEP 2] Processing articles with ChatGPT...
✓ Processed 5 articles

[STEP 3] Creating multimedia content...
✓ Created 5 complete content packages

[STEP 4] Posting to social media platforms...
✓ Posted to 5/5 content packages

============================================================
KH-Viral Agent Completed Successfully!
============================================================
```

---

### Method 2: Automatic Daily Run (GitHub Actions)

**How it works:**
- Runs every day at **6 AM UTC** automatically
- No manual intervention needed
- Results are automatically saved
- You can view logs on GitHub

**To trigger manually:**

1. Go to: https://github.com/mdislaha-code/KH-Viral/actions
2. Click **"KH-Viral Daily Agent"** workflow
3. Click **"Run workflow"** dropdown
4. Click **"Run workflow"** button
5. Wait 2-5 minutes for completion

---

### Method 3: Schedule Custom Time

**Edit the schedule:**

1. Open `.github/workflows/daily_agent.yml`
2. Find this line:
```yaml
on:
  schedule:
    - cron: '0 6 * * *'  # 6 AM UTC daily
```

3. Change time using cron format:

| Time | Cron |
|------|------|
| Every day at 8 AM UTC | `0 8 * * *` |
| Every day at 12 PM UTC | `0 12 * * *` |
| Every Monday at 6 AM | `0 6 * * 1` |
| Every 6 hours | `0 */6 * * *` |
| Every 30 minutes | `*/30 * * * *` |

---

## Understanding Output

### Output Structure

When the agent completes, it creates a JSON results file:

```
output/
└── results_20260502_103045.json
```

### Sample Output

```json
{
  "timestamp": "2026-05-02T10:30:45.123456",
  "status": "success",
  "workflow": {
    "news_collected": 127,
    "articles_filtered": 45,
    "articles_processed": 5,
    "content_packages_created": 5,
    "posts_successful": 5
  },
  "top_articles": [
    {
      "title": "Breaking News: Major Political Development",
      "source": "google_news",
      "viral_score": 89.5,
      "emotional_themes": ["politics", "breaking_news"]
    },
    {
      "title": "Celebrity Drama Unfolds",
      "source": "twitter",
      "viral_score": 87.2,
      "emotional_themes": ["celebrity_drama"]
    }
  ]
}
```

### Understanding Viral Scores

```
85-100  = Very High (Excellent posting candidate)
70-85   = High (Good posting candidate)
50-70   = Medium (Acceptable)
30-50   = Low (Borderline)
0-30    = Very Low (Not recommended)
```

### Log Files

```
logs/
└── kh_viral.log
```

**View logs:**

```bash
# Last 20 lines
tail -20 logs/kh_viral.log

# Follow in real-time
tail -f logs/kh_viral.log

# Search for errors
grep "ERROR" logs/kh_viral.log
```

---

## Managing Collaborators

### Add New User (Owner Only)

**Step 1: Go to Settings**
```
https://github.com/mdislaha-code/KH-Viral/settings/access
```

**Step 2: Click "Add People"**

**Step 3: Enter GitHub Username**

**Step 4: Select Permission Level**

| Level | Can Run | Can Code | Can Invite | Can Delete |
|-------|---------|----------|------------|------------|
| Read | ❌ | ❌ | ❌ | ❌ |
| Triage | ✅ | ❌ | ❌ | ❌ |
| Write | ✅ | ✅ | ❌ | ❌ |
| Maintain | ✅ | ✅ | ✅ | ❌ |
| Admin | ✅ | ✅ | ✅ | ✅ |

**Step 5: Send Invitation**

---

### Remove User (Owner Only)

**Step 1: Go to Settings**
```
https://github.com/mdislaha-code/KH-Viral/settings/access
```

**Step 2: Find User**

**Step 3: Click "Remove"**

**Step 4: Confirm**

---

### View Current Users

```
https://github.com/mdislaha-code/KH-Viral/settings/access
```

You'll see:
- Username
- Permission level
- When they joined

---

## Advanced Usage

### Customize News Sources

**Edit `config/config.yaml`:**

```yaml
news_collection:
  sources:
    - google_news      # Google News
    - twitter          # Twitter/X
    - reddit           # Reddit
    - youtube_trends   # YouTube
    - instagram_trends # Instagram
```

To disable a source, remove it from the list.

### Customize AI Processing

**Edit `config/config.yaml`:**

```yaml
ai_processing:
  model: gpt-4              # Change to gpt-3.5-turbo (cheaper) or gpt-4 (better)
  temperature: 0.7          # Lower = more consistent, Higher = more creative
  emotional_themes:         # Topics to focus on
    - war
    - politics
    - economy
    - crisis
    - human_stories
    - celebrity_drama
```

### Customize Posting Strategy

**Edit `config/config.yaml`:**

```yaml
social_posting:
  platforms:
    - instagram
    - tiktok
    - youtube_shorts
    - twitter
    - facebook
  
  posting_strategy:
    delay_hours_min: 1      # Post 1-3 hours after collection
    delay_hours_max: 3
    max_posts_per_day: 5    # Maximum 5 posts per day
    optimal_times:
      - '08:00'  # 8 AM
      - '12:00'  # 12 PM
      - '18:00'  # 6 PM
      - '20:00'  # 8 PM
```

---

## Troubleshooting

### Agent Won't Start

**Check 1: Python Version**
```bash
python --version
# Must be 3.9 or higher
```

**Check 2: Dependencies**
```bash
pip install -r requirements.txt
```

**Check 3: Virtual Environment**
```bash
# Deactivate and reactivate
deactivate
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

---

### "API Key not found" Error

**Step 1: Verify .env Exists**
```bash
ls -la .env
# Should show the file
```

**Step 2: Check API Keys**
```bash
grep OPENAI_API_KEY .env
# Should show your key
```

**Step 3: Restart**
```bash
# Deactivate and reactivate environment
deactivate
source venv/bin/activate
python main.py
```

---

### No Articles Collected

**Check API Quotas:**

- Google News: 100 requests/day (free tier)
- Twitter: Limited by tier
- Reddit: Generous limits
- YouTube: 12 API units/day (free tier)

**Solution:**
1. Check API quotas in respective dashboards
2. Upgrade to paid tier if needed
3. Wait for quota reset (usually daily at midnight UTC)

---

### Agent is Slow

**Possible causes:**
1. Slow internet connection
2. API servers are slow
3. ChatGPT processing is taking time

**Solutions:**
- Be patient (can take 5-10 minutes)
- Check your internet speed
- Try during off-peak hours

---

### GitHub Actions Not Running

**Check 1: Secrets Configured**
```
Settings → Secrets and Variables → Actions
```

Should show all API keys

**Check 2: Workflow File**
```
.github/workflows/daily_agent.yml
```

Should exist and have correct cron time

**Check 3: Logs**
```
GitHub → Actions tab → See workflow runs
```

---

## Performance Tips

### Reduce Processing Time

1. **Use cheaper AI model:**
   ```yaml
   model: gpt-3.5-turbo  # Instead of gpt-4
   ```

2. **Reduce articles processed:**
   ```yaml
   max_articles_per_source: 5  # Instead of 10
   ```

3. **Disable unused sources:**
   ```yaml
   sources:
     - google_news
     - twitter
     # Remove unused ones
   ```

### Reduce API Costs

1. **Use smaller article batches**
2. **Reduce posting frequency** (e.g., 3 posts/day instead of 5)
3. **Schedule at off-peak times**

---

## Common Workflows

### Workflow 1: Daily News Posting

1. ✅ Set `cron: '0 8 * * *'` (8 AM daily)
2. ✅ Configure 5 news sources
3. ✅ Set up GitHub Secrets
4. ✅ Let it run automatically

### Workflow 2: Trend Analysis

1. ✅ Run agent manually
2. ✅ Check results in `output/results_*.json`
3. ✅ Analyze viral scores
4. ✅ Export data for analysis

### Workflow 3: Influencer Content

1. ✅ Invite collaborators (Write access)
2. ✅ Each can run agent independently
3. ✅ Customize per-user settings
4. ✅ Share results privately

---

## Next Steps

✅ **Basic Setup:** Follow SETUP_GUIDE.md
✅ **First Run:** `python main.py`
✅ **Check Results:** `cat output/results_*.json`
✅ **Automate:** Add GitHub Secrets
✅ **Invite Team:** Add collaborators
✅ **Monitor:** View logs regularly

---

## FAQ

**Q: How long does one run take?**
A: Usually 2-5 minutes depending on API speeds

**Q: Can multiple people run it at once?**
A: Yes, but GitHub Actions will queue them

**Q: Do I need to pay for APIs?**
A: OpenAI requires payment, others have free tiers

**Q: Can I change the posting platforms?**
A: Yes, edit `config/config.yaml`

**Q: How do I see what was posted?**
A: Check `output/results_*.json` files

**Q: Can I delete my GitHub Secrets?**
A: Yes, but agent won't run without them

---

**Happy using KH-Viral! 🚀**
