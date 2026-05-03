#!/usr/bin/env python3
"""
Main Agent with Free APIs Integration
Collects viral news from multiple FREE sources
No Python knowledge needed - everything is pre-configured!
"""

import os
import json
from datetime import datetime
from dotenv import load_dotenv
from src.free_apis import FreeAPIsCollector, analyze_viral_potential, get_trending_topics

# Load environment variables
load_dotenv()

class KHViralAgent:
    """Main agent with all FREE APIs integrated"""
    
    def __init__(self):
        self.collector = FreeAPIsCollector()
        self.results = {}
        
    def run(self):
        """Run the complete agent workflow"""
        print("\n" + "="*70)
        print("🤖 KH-VIRAL AGENT - WITH FREE APIs INTEGRATION")
        print("="*70)
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("\n📊 Starting agent workflow...\n")
        
        # Step 1: Collect from all sources
        print("[STEP 1] Collecting news from FREE sources...")
        articles_data = self.collector.collect_all_sources()
        
        # Step 2: Analyze viral potential
        print("\n[STEP 2] Analyzing viral potential...")
        all_articles = []
        for source_name, articles in articles_data.items():
            if source_name not in ['timestamp', 'total_collected']:
                all_articles.extend(articles)
        
        if all_articles:
            viral_articles = analyze_viral_potential(all_articles)
            print(f"✅ Analyzed {len(viral_articles)} articles")
        else:
            viral_articles = []
            print("⚠️  No articles collected (API keys may be needed)")
        
        # Step 3: Display top articles
        print("\n[STEP 3] Top Viral Articles:\n")
        for i, article in enumerate(viral_articles[:5], 1):
            print(f"{i}. {article['title'][:60]}...")
            print(f"   Source: {article['source']}")
            print(f"   Viral Score: {article.get('viral_score', 'N/A'):.1f}/100")
            print()
        
        # Step 4: Summary
        print("[STEP 4] Agent Summary:")
        print(f"✅ Total articles collected: {len(all_articles)}")
        print(f"✅ Articles analyzed: {len(viral_articles)}")
        print(f"✅ Top viral score: {viral_articles[0].get('viral_score', 0):.1f}/100" if viral_articles else "❌ No data")
        
        # Step 5: Save results
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'status': 'success',
            'sources': {
                'google_news': len(articles_data.get('google_news', [])),
                'reddit': len(articles_data.get('reddit', [])),
                'youtube': len(articles_data.get('youtube', [])),
            },
            'total_collected': len(all_articles),
            'top_articles': [
                {
                    'title': a['title'],
                    'source': a['source'],
                    'viral_score': a.get('viral_score', 0),
                    'url': a.get('url', '')
                }
                for a in viral_articles[:5]
            ]
        }
        
        # Create output directory if needed
        os.makedirs('output', exist_ok=True)
        
        # Save results
        output_file = f'output/results_{timestamp}.json'
        with open(output_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\n✅ Results saved to: {output_file}")
        
        print("\n" + "="*70)
        print("🎉 AGENT WORKFLOW COMPLETE!")
        print("="*70)
        print("\n💡 Next steps:")
        print("   1. Get your FREE API keys (3-30 minutes)")
        print("   2. Add them to .env file")
        print("   3. Run agent again for REAL viral news!")
        print("\n🔗 Get FREE API keys:")
        print("   • Google News: https://newsapi.org")
        print("   • Reddit: https://reddit.com/prefs/apps")
        print("   • Twitter: https://developer.twitter.com")
        print("   • YouTube: https://console.cloud.google.com")
        print("\n" + "="*70 + "\n")

if __name__ == '__main__':
    agent = KHViralAgent()
    agent.run()
