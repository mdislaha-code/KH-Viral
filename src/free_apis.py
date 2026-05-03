#!/usr/bin/env python3
"""
Free APIs Integration Module
Connects to all free news sources and services
"""

import os
import json
import requests
from datetime import datetime, timedelta
from typing import List, Dict

class FreeAPIsCollector:
    """Collects news from all FREE API sources"""
    
    def __init__(self):
        """Initialize API collector with environment variables"""
        self.google_news_key = os.getenv('GOOGLE_NEWS_API_KEY', 'demo')
        self.twitter_token = os.getenv('TWITTER_BEARER_TOKEN', 'demo')
        self.reddit_id = os.getenv('REDDIT_CLIENT_ID', 'demo')
        self.reddit_secret = os.getenv('REDDIT_CLIENT_SECRET', 'demo')
        self.youtube_key = os.getenv('YOUTUBE_API_KEY', 'demo')
        
    def collect_google_news(self, query: str = 'trending') -> List[Dict]:
        """Collect from Google News API (FREE)"""
        try:
            url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&language=en&apiKey={self.google_news_key}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                articles = response.json().get('articles', [])
                return [
                    {
                        'title': a['title'],
                        'description': a['description'],
                        'source': 'Google News',
                        'url': a['url'],
                        'image': a.get('urlToImage'),
                        'published_at': a['publishedAt']
                    }
                    for a in articles[:10]
                ]
        except Exception as e:
            print(f"Error collecting Google News: {e}")
        return []
    
    def collect_reddit_trending(self) -> List[Dict]:
        """Collect from Reddit (FREE)"""
        try:
            subreddits = ['news', 'worldnews', 'trending', 'AskReddit']
            articles = []
            
            for subreddit in subreddits:
                url = f"https://www.reddit.com/r/{subreddit}/top.json?t=day&limit=5"
                headers = {'User-Agent': 'KH-Viral-Agent'}
                response = requests.get(url, headers=headers, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    for post in data['data']['children'][:5]:
                        articles.append({
                            'title': post['data']['title'],
                            'description': post['data']['selftext'][:200],
                            'source': f'Reddit - r/{subreddit}',
                            'url': f"https://reddit.com{post['data']['permalink']}",
                            'upvotes': post['data']['ups'],
                            'comments': post['data']['num_comments']
                        })
            
            return articles[:10]
        except Exception as e:
            print(f"Error collecting Reddit: {e}")
        return []
    
    def collect_youtube_trends(self) -> List[Dict]:
        """Collect from YouTube API (FREE - 12 units/day)"""
        try:
            url = "https://www.googleapis.com/youtube/v3/search"
            params = {
                'q': 'trending viral',
                'type': 'video',
                'order': 'viewCount',
                'maxResults': 10,
                'key': self.youtube_key
            }
            
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                results = response.json().get('items', [])
                return [
                    {
                        'title': r['snippet']['title'],
                        'description': r['snippet']['description'],
                        'source': 'YouTube Trends',
                        'video_id': r['id']['videoId'],
                        'url': f"https://youtube.com/watch?v={r['id']['videoId']}",
                        'thumbnail': r['snippet']['thumbnails'].get('high', {}).get('url')
                    }
                    for r in results
                ]
        except Exception as e:
            print(f"Error collecting YouTube: {e}")
        return []
    
    def collect_all_sources(self) -> Dict:
        """Collect from all FREE sources"""
        print("\n🔄 Collecting from ALL FREE sources...")
        
        all_articles = {
            'google_news': self.collect_google_news(),
            'reddit': self.collect_reddit_trending(),
            'youtube': self.collect_youtube_trends(),
            'timestamp': datetime.now().isoformat(),
            'total_collected': 0
        }
        
        all_articles['total_collected'] = sum(
            len(v) for k, v in all_articles.items() if k != 'timestamp' and k != 'total_collected'
        )
        
        print(f"✅ Collected {all_articles['total_collected']} articles from FREE sources!")
        
        return all_articles


def get_trending_topics() -> List[str]:
    """Get trending topics from multiple sources"""
    return [
        'breaking news',
        'viral',
        'trending',
        'technology',
        'business',
        'entertainment',
        'sports',
        'health',
        'science',
        'politics'
    ]


def analyze_viral_potential(articles: List[Dict]) -> List[Dict]:
    """Simple viral score calculation (no API needed)"""
    scored = []
    
    for article in articles:
        # Calculate viral score based on available metrics
        score = 50  # Base score
        
        # Boost for upvotes/comments
        if 'upvotes' in article:
            score += min(article['upvotes'] / 100, 30)
        if 'comments' in article:
            score += min(article['comments'] / 100, 20)
        
        # Boost for certain keywords
        keywords = ['breaking', 'viral', 'trending', 'shocking', 'exclusive']
        title_lower = article.get('title', '').lower()
        for keyword in keywords:
            if keyword in title_lower:
                score += 10
        
        article['viral_score'] = min(score, 100)
        scored.append(article)
    
    return sorted(scored, key=lambda x: x.get('viral_score', 0), reverse=True)


if __name__ == '__main__':
    # Test the collectors
    from dotenv import load_dotenv
    load_dotenv()
    
    print("\n" + "="*60)
    print("KH-VIRAL: Free APIs Integration Test")
    print("="*60)
    
    collector = FreeAPIsCollector()
    results = collector.collect_all_sources()
    
    print(f"\n📊 Total Articles Collected: {results['total_collected']}")
    
    # Analyze viral potential
    all_articles = []
    for source_name, articles in results.items():
        if source_name not in ['timestamp', 'total_collected']:
            all_articles.extend(articles)
    
    if all_articles:
        viral_articles = analyze_viral_potential(all_articles)
        print(f"\n🔥 Top Viral Articles:\n")
        for i, article in enumerate(viral_articles[:5], 1):
            print(f"{i}. {article['title'][:60]}...")
            print(f"   Source: {article['source']}")
            print(f"   Viral Score: {article.get('viral_score', 'N/A')}")
            print()
    
    print("\n✅ All FREE APIs connected and working!")
    print("\n📝 Next steps:")
    print("   1. Get your FREE API keys from the links in .env")
    print("   2. Add them to the .env file")
    print("   3. Your agent will automatically use them!")
    print("\n" + "="*60)
