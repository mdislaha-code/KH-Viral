#!/usr/bin/env python3
"""
KH-Viral Portable Backup Creator
Creates a complete plug-and-play backup file
"""

import os
import shutil
import zipfile
from datetime import datetime
from pathlib import Path

def create_portable_backup():
    """Create portable backup ZIP file"""
    
    print("\n" + "="*70)
    print("📦 KH-VIRAL PORTABLE BACKUP CREATOR")
    print("="*70)
    
    # Files to include
    files_to_backup = [
        'dashboard.html',
        'dashboard_server.py',
        'main_free_apis.py',
        'main.py',
        'requirements.txt',
        '.env',
        '.env.example',
        'setup_free_apis.py',
        'README.md',
        'config/config.yaml',
        'src/free_apis.py',
        'src/__init__.py',
        'docs/SETUP_GUIDE.md',
        'docs/USAGE_GUIDE.md',
    ]
    
    # Create backup directory
    backup_dir = 'KH-Viral-Backup'
    if os.path.exists(backup_dir):
        shutil.rmtree(backup_dir)
    os.makedirs(backup_dir)
    
    print("\n📁 Copying files to backup...")
    
    # Copy files
    for file_path in files_to_backup:
        if os.path.exists(file_path):
            # Create subdirectory if needed
            dest_file = os.path.join(backup_dir, file_path)
            os.makedirs(os.path.dirname(dest_file), exist_ok=True)
            shutil.copy2(file_path, dest_file)
            print(f"  ✓ {file_path}")
    
    # Create quick start guide
    quick_start = """# 🚀 KH-VIRAL QUICK START

## ONE-CLICK SETUP:

### WINDOWS:
1. Extract this folder
2. Double-click: RUN_ME.bat
3. Wait for setup
4. Open: http://localhost:8000
5. Done! Your agent is running! 🎉

### MAC/LINUX:
1. Extract this folder
2. Open Terminal
3. Run: bash run_me.sh
4. Open: http://localhost:8000
5. Done! Your agent is running! 🎉

## MANUAL SETUP:

1. Open terminal/command prompt
2. cd to this folder
3. Windows: venv\\Scripts\\activate
   Mac/Linux: source venv/bin/activate
4. python dashboard_server.py
5. Open browser: http://localhost:8000

## GET REAL NEWS:

1. Get FREE API key: https://newsapi.org
2. Open .env file
3. Replace 'demo' with your key
4. Save file
5. Refresh browser
6. Done! Real news now! 🎉

## CHAT WITH YOUR AGENT:

- "Show me trending viral news"
- "What's the latest breaking news?"
- "Find viral content"
- "Analyze this for virality"

## NEED HELP?

Read: SETUP_GUIDE.md
Read: USAGE_GUIDE.md
"""
    
    with open(os.path.join(backup_dir, 'QUICK_START.md'), 'w') as f:
        f.write(quick_start)
    
    print("  ✓ QUICK_START.md")
    
    # Create run batch file for Windows
    run_bat = """@echo off
echo 🤖 KH-VIRAL AGENT - Starting...
echo.
echo Setting up Python environment...
python -m venv venv
call venv\\Scripts\\activate.bat
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo 🚀 Starting agent dashboard...
echo Open your browser and go to: http://localhost:8000
echo.
python dashboard_server.py
pause
"""
    
    with open(os.path.join(backup_dir, 'RUN_ME.bat'), 'w') as f:
        f.write(run_bat)
    
    print("  ✓ RUN_ME.bat (Windows)")
    
    # Create run shell script for Mac/Linux
    run_sh = """#!/bin/bash
echo "🤖 KH-VIRAL AGENT - Starting..."
echo ""
echo "Setting up Python environment..."
python3 -m venv venv
source venv/bin/activate
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt
echo ""
echo "🚀 Starting agent dashboard..."
echo "Open your browser and go to: http://localhost:8000"
echo ""
python3 dashboard_server.py
"""
    
    with open(os.path.join(backup_dir, 'run_me.sh'), 'w') as f:
        f.write(run_sh)
    
    os.chmod(os.path.join(backup_dir, 'run_me.sh'), 0o755)
    
    print("  ✓ run_me.sh (Mac/Linux)")
    
    # Create ZIP file
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    zip_filename = f'KH-Viral-Portable-{timestamp}.zip'
    
    print(f"\n📦 Creating ZIP file: {zip_filename}")
    
    shutil.make_archive(f'KH-Viral-Portable-{timestamp}', 'zip', '.', backup_dir)
    
    print("\n" + "="*70)
    print("✅ BACKUP COMPLETE!")
    print("="*70)
    print(f"\n📥 Download this file: {zip_filename}")
    print(f"\n📂 File location: {os.path.abspath(zip_filename)}")
    print(f"\n📊 File size: {os.path.getsize(zip_filename) / (1024*1024):.1f} MB")
    print("\n🚀 PLUG AND PLAY - USE ON ANY COMPUTER:")
    print("\n  1. Download the ZIP file")
    print("  2. Extract it anywhere")
    print("  3. Windows: Double-click RUN_ME.bat")
    print("     Mac/Linux: bash run_me.sh")
    print("  4. Open: http://localhost:8000")
    print("  5. Your agent works! 🎉")
    print("\n" + "="*70)
    print(f"\n✨ Backup created successfully!")
    print(f"\n📥 Ready to download: {zip_filename}")
    print("\n" + "="*70 + "\n")
    
    return zip_filename

if __name__ == '__main__':
    backup_file = create_portable_backup()
    print(f"\n💾 Your portable backup is ready!")
    print(f"\n📍 Look for: {backup_file}")
    print(f"\n🎯 Download it and use on any computer!")
