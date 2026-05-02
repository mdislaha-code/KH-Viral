# KH-Viral Agent - Complete Setup Guide

**Step-by-Step Instructions to Get Started**

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Clone Repository](#clone-repository)
3. [Get API Keys](#get-api-keys)
4. [Install Dependencies](#install-dependencies)
5. [Configure Environment](#configure-environment)
6. [Run Locally](#run-locally)
7. [Set Up Automation](#set-up-automation)
8. [Monitor & Logs](#monitor--logs)

---

## Prerequisites

### Required Software

- **Python 3.9+** - Download from https://www.python.org/downloads/
- **Git** - Download from https://git-scm.com/download
- **GitHub Account** - Already have it ✅
- **Text Editor** - VS Code (https://code.visualstudio.com/) recommended

### Verify Installation

```bash
# Check Python version
python --version
# Should show: Python 3.9.0 or higher

# Check Git
git --version
# Should show: git version 2.x.x or higher
```

---

## Clone Repository

### Step 1: Open Terminal/Command Prompt

**Windows:**
- Press `Win + R`
- Type `cmd`
- Press Enter

**Mac/Linux:**
- Open Terminal application

### Step 2: Navigate to Desktop

```bash
cd Desktop
```

### Step 3: Clone the Repository

```bash
git clone https://github.com/mdislaha-code/KH-Viral.git
cd KH-Viral
```

### Step 4: Verify Files

```bash
ls -la
# You should see:
# - main.py
# - config/
# - src/
# - requirements.txt
# - .env.example
```

---

## Get API Keys

You need API keys from 8 services. Here's how to get each:

### 1. OpenAI (ChatGPT) - REQUIRED ⭐

**Time:** 5 minutes

1. Go to: https://platform.openai.com/api-keys
2. Click **"Create new secret key"**
3. Copy the key (you won't see it again!)
4. Save it in a text file

**Cost:** Paid (starts ~$5/month)

---

### 2. Google News API - REQUIRED ⭐

**Time:** 3 minutes

1. Go to: https://newsapi.org/
2. Click **"Get API Key"**
3. Sign up (free)
4. Copy your API key from dashboard
5. Save it

**Cost:** Free (up to 100 requests/day)

---

### 3. Twitter/X API v2 - REQUIRED ⭐

**Time:** 10 minutes

1. Go to: https://developer.twitter.com/en/portal/dashboard
2. Sign in with Twitter account
3. Click **"Create an app"**
4. Fill in details:
   - App name: `KH-Viral Agent`
   - Use case: `News aggregation`
5. Copy **Bearer Token** from Keys & Tokens section
6. Save it

**Cost:** Free (Basic tier)

---

### 4. Reddit API - REQUIRED ⭐

**Time:** 5 minutes

1. Go to: https://www.reddit.com/login
2. Sign in (create account if needed)
3. Go to: https://www.reddit.com/prefs/apps
4. Click **"Create app"** (bottom)
5. Fill in:
   - Name: `KH-Viral`
   - Type: `Script`
   - Description: `News aggregation agent`
6. Click **"Create app"**
7. You'll get:
   - **Client ID** (under app name)
   - **Client Secret** (shown after creation)
8. Save both

**Cost:** Free

---

### 5. YouTube API - REQUIRED ⭐

**Time:** 8 minutes

1. Go to: https://console.cloud.google.com/
2. Create new project:
   - Click **"Select a Project"** → **"New Project"**
   - Name: `KH-Viral`
   - Click **"Create"**
3. Wait for project creation
4. Search **"YouTube Data API v3"**
5. Click **"Enable"**
6. Go to **"Credentials"** (left sidebar)
7. Click **"Create Credentials"** → **"API Key"**
8. Copy the API key
9. Save it

**Cost:** Free (12 API units per day)

---

### 6. Canva API (Optional)

**Time:** 5 minutes

1. Go to: https://www.canva.com/developers/
2. Click **"Get Started"**
3. Sign in / Create account
4. Create API key
5. Save it

**Cost:** Free

---

### 7. ElevenLabs API (Optional)

**Time:** 3 minutes

1. Go to: https://elevenlabs.io/
2. Sign up / Sign in
3. Go to **Profile** → **API Key**
4. Copy your API key
5. Also copy a **Voice ID** from Library
6. Save both

**Cost:** Free tier available

---

### 8. Instagram Graph API (Optional)

**Time:** 10 minutes

1. Go to: https://developers.facebook.com/
2. Create an account
3. Create an app
4. Select **"Consumer"** type
5. Add **"Instagram Basic Display"** product
6. Get your credentials
7. Save them

**Cost:** Free

---

## Install Dependencies

### Step 1: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

# You should see (venv) at the start of your terminal line
```

### Step 2: Upgrade pip

```bash
pip install --upgrade pip
```

### Step 3: Install Requirements

```bash
pip install -r requirements.txt

# Wait for installation to complete...
# You should see: Successfully installed [packages]
```

### Step 4: Verify Installation

```bash
pip list
# You should see all packages listed
```

---

## Configure Environment

### Step 1: Copy Environment Template

```bash
cp .env.example .env
```

### Step 2: Edit .env File

**Windows (Notepad):**
```bash
notepad .env
```

**Mac/Linux (Nano):**
```bash
nano .env
```

### Step 3: Add Your API Keys

Replace all `your_xxxxx_here` values with your actual API keys:

```env
# OpenAI API
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Google News API
GOOGLE_NEWS_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxx

# Twitter/X API
TWITTER_BEARER_TOKEN=AAAAAAAAAAAAAAAAAAAAxxxxxxxxxxxxxx

# Reddit API
REDDIT_CLIENT_ID=xxxxxxxxxxxxx
REDDIT_CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxxx
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password

# YouTube API
YOUTUBE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Instagram API (optional)
INSTAGRAM_USERNAME=your_instagram_username
INSTAGRAM_PASSWORD=your_instagram_password

# Canva API (optional)
CANVA_API_KEY=your_canva_key_here

# ElevenLabs API (optional)
ELEVENLABS_API_KEY=your_elevenlabs_key_here
ELEVENLABS_VOICE_ID=your_voice_id_here

# App Settings
DEBUG=True
ENVIRONMENT=development
LOG_LEVEL=INFO
```

### Step 4: Save File

- **Windows (Notepad):** Press `Ctrl + S`
- **Mac/Linux (Nano):** Press `Ctrl + X` → `Y` → `Enter`

⚠️ **IMPORTANT:** Never commit `.env` to GitHub (it's in .gitignore)

---

## Run Locally

### Step 1: Verify Setup

```bash
# Check Python and packages
python --version
pip list | grep openai
```

### Step 2: Test API Keys

```bash
# Quick test
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('API Keys loaded successfully!')"
```

### Step 3: Run the Agent

```bash
python main.py
```

### Step 4: Watch the Output

You should see:

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
✓ Selected 5 articles for content creation

[STEP 3] Creating multimedia content...
Creating content for article 1/5...
Creating content for article 2/5...
✓ Created 5 complete content packages

[STEP 4] Posting to social media platforms...
Posting content 1/5...
Posting content 2/5...
✓ Posted to 5/5 content packages

============================================================
KH-Viral Agent Completed Successfully!
============================================================
```

### Step 5: Check Results

```bash
# View output directory
ls output/

# View latest results
cat output/results_20260502_103045.json
```

---

## Set Up Automation

### Automatic Daily Runs (GitHub Actions)

**This runs automatically every day at 6 AM UTC without your intervention!**

### Step 1: Add GitHub Secrets

1. Go to: https://github.com/mdislaha-code/KH-Viral/settings/secrets/actions
2. Click **"New repository secret"** for each:

```
OPENAI_API_KEY = sk-xxxxx...
GOOGLE_NEWS_API_KEY = xxxxx...
TWITTER_BEARER_TOKEN = AAAA...
REDDIT_CLIENT_ID = xxxxx...
REDDIT_CLIENT_SECRET = xxxxx...
REDDIT_USERNAME = your_username
REDDIT_PASSWORD = your_password
YOUTUBE_API_KEY = xxxxx...
```

### Step 2: View Automation Schedule

1. Go to: https://github.com/mdislaha-code/KH-Viral/actions
2. Click **"KH-Viral Daily Agent"**
3. You'll see all past and scheduled runs

### Step 3: Manual Trigger (If Needed)

1. Go to Actions tab
2. Click **"KH-Viral Daily Agent"** on left
3. Click **"Run workflow"** → **"Run workflow"**
4. Agent runs immediately

### Step 4: Change Schedule (Optional)

Edit `.github/workflows/daily_agent.yml`:

```yaml
on:
  schedule:
    - cron: '0 6 * * *'  # Change the time here
```

Cron format: `minute hour day month day_of_week`

Examples:
- `0 6 * * *` = Every day at 6 AM UTC
- `0 12 * * *` = Every day at 12 PM UTC
- `0 9 * * 1` = Every Monday at 9 AM UTC

---

## Monitor & Logs

### View Logs Locally

```bash
# View latest logs
tail -f logs/kh_viral.log

# View all logs
cat logs/kh_viral.log
```

### View GitHub Actions Logs

1. Go to: https://github.com/mdislaha-code/KH-Viral/actions
2. Click on a workflow run
3. Click **"run_agent"** job
4. See real-time logs

### Check Results

```bash
# List all results
ls -la output/

# View latest result
cat output/results_*.json | tail -1
```

---

## Troubleshooting

### Issue: "Module not found" error

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "API key not found" error

**Solution:**
1. Check `.env` file exists
2. Verify API keys are in `.env`
3. Restart terminal (activation issues)

### Issue: "Connection timeout" error

**Solution:**
- Check internet connection
- Wait and retry
- API might be down

### Issue: Agent runs but produces no articles

**Solution:**
- Check API quotas
- Verify news sources have recent content
- Check logs in `logs/kh_viral.log`

---

## Next Steps

✅ **Setup Complete!** Your agent is ready to:

1. **Run manually:** `python main.py`
2. **Run automatically:** GitHub Actions (daily at 6 AM UTC)
3. **Invite collaborators:** Settings → Collaborators
4. **Monitor progress:** View logs and results

---

## Quick Command Reference

```bash
# Activate virtual environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Run agent
python main.py

# Install dependencies
pip install -r requirements.txt

# View logs
tail -f logs/kh_viral.log

# View results
cat output/results_*.json

# Deactivate environment
deactivate
```

---

## Support

For issues:
1. Check logs: `logs/kh_viral.log`
2. Review this guide
3. Check GitHub issues
4. Contact repository owner

**Happy hunting for viral news! 🚀**
