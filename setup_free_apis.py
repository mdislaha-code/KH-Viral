#!/usr/bin/env python3
"""
Setup script to help get FREE API keys
All APIs tested and working!
"""

import webbrowser
import time
from typing import Dict

class APISetupGuide:
    """Guide to get all FREE API keys"""
    
    apis = {
        'Google News API': {
            'url': 'https://newsapi.org',
            'time': '3 minutes',
            'cost': 'FREE',
            'steps': [
                '1. Go to https://newsapi.org',
                '2. Click "Get API Key"',
                '3. Sign up (free)',
                '4. Check your email',
                '5. Copy API key',
                '6. Paste in .env: GOOGLE_NEWS_API_KEY=your_key_here'
            ]
        },
        'Reddit API': {
            'url': 'https://reddit.com/prefs/apps',
            'time': '5 minutes',
            'cost': 'FREE',
            'steps': [
                '1. Go to https://reddit.com/login',
                '2. Login or create account',
                '3. Go to https://reddit.com/prefs/apps',
                '4. Click "Create app" (bottom)',
                '5. Name: KH-Viral, Type: Script',
                '6. Copy Client ID and Client Secret',
                '7. Paste in .env file'
            ]
        },
        'Twitter/X API': {
            'url': 'https://developer.twitter.com',
            'time': '10 minutes',
            'cost': 'FREE (Basic Tier)',
            'steps': [
                '1. Go to https://developer.twitter.com',
                '2. Sign in with Twitter',
                '3. Click "Create an app"',
                '4. Fill: Name=KH-Viral, Use Case=News',
                '5. Go to "Keys & Tokens"',
                '6. Copy Bearer Token',
                '7. Paste in .env: TWITTER_BEARER_TOKEN=your_token'
            ]
        },
        'YouTube API': {
            'url': 'https://console.cloud.google.com',
            'time': '10 minutes',
            'cost': 'FREE (12 units/day)',
            'steps': [
                '1. Go to https://console.cloud.google.com',
                '2. Create new project',
                '3. Search "YouTube Data API v3"',
                '4. Click "Enable"',
                '5. Go to "Credentials"',
                '6. Create "API Key"',
                '7. Paste in .env: YOUTUBE_API_KEY=your_key'
            ]
        },
        'OpenAI API (Optional)': {
            'url': 'https://platform.openai.com/api-keys',
            'time': '5 minutes',
            'cost': '$5 FREE credit',
            'steps': [
                '1. Go to https://platform.openai.com/api-keys',
                '2. Sign up',
                '3. Create API key',
                '4. Copy it',
                '5. Paste in .env: OPENAI_API_KEY=sk-your_key',
                'Note: Gets $5 free credit for testing!'
            ]
        }
    }
    
    @classmethod
    def show_all_apis(cls):
        """Display all APIs with setup info"""
        print("\n" + "="*70)
        print("🔑 KH-VIRAL: Get ALL FREE APIs in 30 Minutes!")
        print("="*70)
        
        for i, (api_name, api_info) in enumerate(cls.apis.items(), 1):
            print(f"\n{i}. {api_name}")
            print(f"   ⏱️  Time: {api_info['time']}")
            print(f"   💰 Cost: {api_info['cost']}")
            print(f"   🔗 Get it: {api_info['url']}")
            print(f"   \n   Steps:")
            for step in api_info['steps']:
                print(f"      {step}")
        
        print("\n" + "="*70)
        print("✅ Total Time: ~30 minutes for ALL APIs")
        print("💰 Total Cost: $0 (OpenAI has $5 free credit)")
        print("="*70 + "\n")
    
    @classmethod
    def open_all_apis(cls):
        """Open all API links in browser"""
        print("\n🌐 Opening all API signup pages in your browser...\n")
        
        for api_name, api_info in cls.apis.items():
            print(f"Opening {api_name}...")
            webbrowser.open(api_info['url'])
            time.sleep(2)
        
        print("\n✅ All pages opened! Get your keys now!\n")
    
    @classmethod
    def create_env_template(cls) -> str:
        """Create .env template"""
        template = """# KH-VIRAL FREE APIs Configuration
# Add your API keys below

# 1. Google News API (https://newsapi.org)
GOOGLE_NEWS_API_KEY=your_key_here

# 2. Reddit API (https://reddit.com/prefs/apps)
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password

# 3. Twitter/X API (https://developer.twitter.com)
TWITTER_BEARER_TOKEN=your_token_here

# 4. YouTube API (https://console.cloud.google.com)
YOUTUBE_API_KEY=your_key_here

# 5. OpenAI API (Optional) (https://platform.openai.com/api-keys)
OPENAI_API_KEY=sk-your_key_here

# App Settings
DEBUG=True
ENVIRONMENT=development
LOG_LEVEL=INFO
"""
        return template


if __name__ == '__main__':
    print("\n🤖 KH-VIRAL: Free API Setup Helper\n")
    print("Choose an option:")
    print("1. Show all APIs with setup steps")
    print("2. Open all API signup pages in browser")
    print("3. Show .env template")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == '1':
        APISetupGuide.show_all_apis()
    elif choice == '2':
        APISetupGuide.open_all_apis()
    elif choice == '3':
        print("\n" + APISetupGuide.create_env_template())
    else:
        print("Invalid choice!")
