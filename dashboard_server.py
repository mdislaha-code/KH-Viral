#!/usr/bin/env python3
"""
Agent Chat Interface - Web Server
Serves the interactive dashboard where you can chat with the agent
"""

import os
import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from loguru import logger

class AgentDashboardHandler(SimpleHTTPRequestHandler):
    """HTTP handler for the agent dashboard."""
    
    def do_GET(self):
        """Handle GET requests."""
        if self.path == '/':
            self.path = '/dashboard.html'
        return super().do_GET()
    
    def end_headers(self):
        """Add CORS headers."""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def start_dashboard_server(port=8000):
    """Start the agent dashboard web server."""
    # Change to current directory
    os.chdir(Path(__file__).parent)
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, AgentDashboardHandler)
    
    logger.info(f"🤖 KH-Viral Agent Dashboard started!")
    logger.info(f"📱 Access at: http://localhost:{port}")
    logger.info(f"Press Ctrl+C to stop the server\n")
    
    print(f"""
    ╔════════════════════════════════════════════╗
    ║      🤖 KH-VIRAL AGENT DASHBOARD 🤖       ║
    ╠════════════════════════════════════════════╣
    ║  Open your browser and go to:              ║
    ║  👉 http://localhost:{port}                   ║
    ║                                            ║
    ║  You can now:                              ║
    ║  ✅ See your agent visualization           ║
    ║  ✅ Chat with your agent                   ║
    ║  ✅ Monitor real-time statistics           ║
    ║  ✅ View agent status                      ║
    ║                                            ║
    ║  Press Ctrl+C to stop                      ║
    ╚════════════════════════════════════════════╝
    """)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("\n🛑 Dashboard server stopped")
        httpd.server_close()

if __name__ == '__main__':
    start_dashboard_server()
