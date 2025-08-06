#!/usr/bin/env python3
"""
Test production CORS configuration locally
"""
import os
import sys
from src.core.config.production import ProductionConfig

def test_production_config():
    """Test production configuration locally"""
    
    # Set environment variables for testing
    os.environ['ENVIRONMENT'] = 'production'
    os.environ['FRONTEND_URL'] = 'https://ui-ai-agent.vercel.app'
    
    print("🔧 Testing Production CORS Configuration")
    print("=" * 50)
    
    # Create production config
    config = ProductionConfig()
    
    print(f"Environment: {config.ENVIRONMENT}")
    print(f"Frontend URL: {config.FRONTEND_URL}")
    print(f"Allowed Origins: {config.get_cors_origins()}")
    print(f"Is Production: {config.is_production()}")
    
    # Test if Vercel URL is in allowed origins
    vercel_url = "https://ui-ai-agent.vercel.app"
    if vercel_url in config.get_cors_origins():
        print(f"✅ {vercel_url} is in allowed origins")
    else:
        print(f"❌ {vercel_url} is NOT in allowed origins")
    
    # Test if Vercel URL with trailing slash is in allowed origins
    vercel_url_slash = "https://ui-ai-agent.vercel.app/"
    if vercel_url_slash in config.get_cors_origins():
        print(f"✅ {vercel_url_slash} is in allowed origins")
    else:
        print(f"❌ {vercel_url_slash} is NOT in allowed origins")
    
    print("\n" + "=" * 50)
    print("Production config test completed!")

if __name__ == "__main__":
    test_production_config() 