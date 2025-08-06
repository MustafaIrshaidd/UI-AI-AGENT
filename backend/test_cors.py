#!/usr/bin/env python3
"""
Test script to verify CORS configuration
"""
import requests
import json

def test_cors_configuration():
    """Test CORS configuration endpoints"""
    
    # Test URLs
    base_url = "https://ui-ai-agent.onrender.com"
    test_origins = [
        "https://ui-ai-agent.vercel.app",
        "http://localhost:3000",
        "https://example.com"  # Should be rejected
    ]
    
    print("🔧 Testing CORS Configuration")
    print("=" * 50)
    
    # Test 1: Check CORS config endpoint
    print("\n1. Testing CORS config endpoint:")
    try:
        response = requests.get(f"{base_url}/cors-config")
        if response.status_code == 200:
            config = response.json()
            print(f"✅ CORS config endpoint working")
            print(f"   Allowed origins: {config.get('allowed_origins', [])}")
            print(f"   Environment: {config.get('environment', 'unknown')}")
            print(f"   Frontend URL: {config.get('frontend_url', 'unknown')}")
        else:
            print(f"❌ CORS config endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error accessing CORS config: {e}")
    
    # Test 2: Test preflight requests
    print("\n2. Testing preflight requests:")
    for origin in test_origins:
        try:
            headers = {
                'Origin': origin,
                'Access-Control-Request-Method': 'GET',
                'Access-Control-Request-Headers': 'Content-Type'
            }
            response = requests.options(f"{base_url}/health", headers=headers)
            
            cors_headers = {
                'Access-Control-Allow-Origin': response.headers.get('Access-Control-Allow-Origin'),
                'Access-Control-Allow-Methods': response.headers.get('Access-Control-Allow-Methods'),
                'Access-Control-Allow-Headers': response.headers.get('Access-Control-Allow-Headers'),
                'Access-Control-Allow-Credentials': response.headers.get('Access-Control-Allow-Credentials'),
            }
            
            if origin in ["https://ui-ai-agent.vercel.app", "http://localhost:3000"]:
                if cors_headers['Access-Control-Allow-Origin'] == origin:
                    print(f"✅ Preflight for {origin}: ALLOWED")
                else:
                    print(f"❌ Preflight for {origin}: DENIED (expected ALLOWED)")
            else:
                if cors_headers['Access-Control-Allow-Origin'] != origin:
                    print(f"✅ Preflight for {origin}: DENIED (expected)")
                else:
                    print(f"❌ Preflight for {origin}: ALLOWED (expected DENIED)")
                    
        except Exception as e:
            print(f"❌ Error testing preflight for {origin}: {e}")
    
    # Test 3: Test actual requests
    print("\n3. Testing actual requests:")
    for origin in test_origins:
        try:
            headers = {'Origin': origin}
            response = requests.get(f"{base_url}/health", headers=headers)
            
            cors_origin = response.headers.get('Access-Control-Allow-Origin')
            if origin in ["https://ui-ai-agent.vercel.app", "http://localhost:3000"]:
                if cors_origin == origin:
                    print(f"✅ Request from {origin}: ALLOWED")
                else:
                    print(f"❌ Request from {origin}: DENIED (expected ALLOWED)")
            else:
                if cors_origin != origin:
                    print(f"✅ Request from {origin}: DENIED (expected)")
                else:
                    print(f"❌ Request from {origin}: ALLOWED (expected DENIED)")
                    
        except Exception as e:
            print(f"❌ Error testing request from {origin}: {e}")
    
    print("\n" + "=" * 50)
    print("CORS test completed!")

if __name__ == "__main__":
    test_cors_configuration() 