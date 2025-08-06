#!/usr/bin/env python3
"""
Database Connection Test Script

This script helps you test database connectivity and debug connection issues.
Run this script to verify your database configuration before deployment.
"""

import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_database_connection(database_url=None):
    """Test database connection with the provided URL"""
    
    if not database_url:
        database_url = os.getenv("DATABASE_URL")
    
    if not database_url:
        print("❌ No DATABASE_URL found!")
        print("Please set the DATABASE_URL environment variable or pass it as an argument.")
        return False
    
    print(f"🔍 Testing connection to: {database_url[:50]}...")
    
    try:
        # Create engine
        engine = create_engine(database_url)
        
        # Test connection
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1 as test"))
            row = result.fetchone()
            
            if row and row[0] == 1:
                print("✅ Database connection successful!")
                return True
            else:
                print("❌ Database connection failed - unexpected result")
                return False
                
    except OperationalError as e:
        print(f"❌ Database connection failed: {str(e)}")
        print("\n🔧 Troubleshooting tips:")
        print("1. Check if the database server is running")
        print("2. Verify the connection string format")
        print("3. Check if the database exists")
        print("4. Verify username and password")
        print("5. Check if the port is correct")
        return False
        
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return False

def main():
    """Main function"""
    print("🚀 Database Connection Test")
    print("=" * 40)
    
    # Test with environment variable
    success = test_database_connection()
    
    if success:
        print("\n🎉 Database is ready for deployment!")
        sys.exit(0)
    else:
        print("\n💡 To fix this issue:")
        print("1. Create a PostgreSQL database in Render")
        print("2. Set the DATABASE_URL environment variable")
        print("3. Make sure the database is accessible")
        print("\n📖 See RENDER_DEPLOYMENT.md for detailed instructions")
        sys.exit(1)

if __name__ == "__main__":
    main() 