#!/usr/bin/env python3
"""
CORS Test Script for Deployment

This script helps you test CORS configuration on your deployed backend.
Run this script to verify that your CORS settings are working correctly.
"""

import requests
import json
import sys
from urllib.parse import urlparse

def test_cors_configuration(backend_url, frontend_origin):
    """Test CORS configuration for deployment"""
    
    print("🔧 Testing CORS Configuration for Deployment")
    print("=" * 60)
    print(f"Backend URL: {backend_url}")
    print(f"Frontend Origin: {frontend_origin}")
    print()
    
    # Test 1: Check CORS config endpoint
    print("1. Testing CORS config endpoint:")
    try:
        response = requests.get(f"{backend_url}/cors-config")
        if response.status_code == 200:
            config = response.json()
            print(f"✅ CORS config endpoint working")
            print(f"   Environment: {config.get('environment', 'unknown')}")
            print(f"   Frontend URL: {config.get('frontend_url', 'unknown')}")
            print(f"   Allowed origins: {config.get('allowed_origins', [])}")
            print(f"   Additional origins: {config.get('additional_origins', '')}")
        else:
            print(f"❌ CORS config endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error accessing CORS config: {e}")
        return False
    
    # Test 2: Test preflight request
    print("\n2. Testing preflight request:")
    try:
        headers = {
            'Origin': frontend_origin,
            'Access-Control-Request-Method': 'GET',
            'Access-Control-Request-Headers': 'Content-Type'
        }
        response = requests.options(f"{backend_url}/health", headers=headers)
        
        cors_headers = {
            'Access-Control-Allow-Origin': response.headers.get('Access-Control-Allow-Origin'),
            'Access-Control-Allow-Methods': response.headers.get('Access-Control-Allow-Methods'),
            'Access-Control-Allow-Headers': response.headers.get('Access-Control-Allow-Headers'),
            'Access-Control-Allow-Credentials': response.headers.get('Access-Control-Allow-Credentials'),
        }
        
        if cors_headers['Access-Control-Allow-Origin'] == frontend_origin:
            print(f"✅ Preflight for {frontend_origin}: ALLOWED")
        else:
            print(f"❌ Preflight for {frontend_origin}: DENIED")
            print(f"   Expected: {frontend_origin}")
            print(f"   Got: {cors_headers['Access-Control-Allow-Origin']}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing preflight: {e}")
        return False
    
    # Test 3: Test actual request
    print("\n3. Testing actual request:")
    try:
        headers = {'Origin': frontend_origin}
        response = requests.get(f"{backend_url}/health", headers=headers)
        
        cors_origin = response.headers.get('Access-Control-Allow-Origin')
        if cors_origin == frontend_origin:
            print(f"✅ Request from {frontend_origin}: ALLOWED")
        else:
            print(f"❌ Request from {frontend_origin}: DENIED")
            print(f"   Expected: {frontend_origin}")
            print(f"   Got: {cors_origin}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing request: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("✅ CORS test completed successfully!")
    return True

def main():
    """Main function"""
    if len(sys.argv) < 3:
        print("Usage: python test_cors_deployment.py <backend_url> <frontend_origin>")
        print("Example: python test_cors_deployment.py https://myapp.onrender.com https://myapp.vercel.app")
        sys.exit(1)
    
    backend_url = sys.argv[1].rstrip('/')
    frontend_origin = sys.argv[2].rstrip('/')
    
    # Validate URLs
    try:
        urlparse(backend_url)
        urlparse(frontend_origin)
    except Exception as e:
        print(f"❌ Invalid URL format: {e}")
        sys.exit(1)
    
    success = test_cors_configuration(backend_url, frontend_origin)
    
    if success:
        print("\n🎉 CORS is configured correctly!")
        print("Your frontend should be able to communicate with the backend.")
        sys.exit(0)
    else:
        print("\n💡 To fix CORS issues:")
        print("1. Check your environment variables in Render")
        print("2. Verify FRONTEND_URL is set correctly")
        print("3. Add additional origins with ADDITIONAL_CORS_ORIGINS")
        print("4. Check the CORS troubleshooting guide: CORS_TROUBLESHOOTING.md")
        sys.exit(1)

if __name__ == "__main__":
    main() 