#!/usr/bin/env python3
"""
Script to help deploy the PWD Tools Hub to Streamlit Cloud
"""

import os
import sys
import subprocess
import webbrowser

def check_git_status():
    """Check if repository is clean and up to date"""
    try:
        # Check if repository is clean
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, check=True)
        if result.stdout.strip():
            print("⚠️  Warning: You have uncommitted changes!")
            print("Please commit and push your changes before deploying.")
            return False
        
        # Check if local branch is up to date with remote
        subprocess.run(['git', 'fetch'], check=True)
        local_result = subprocess.run(['git', 'rev-parse', 'HEAD'], 
                                    capture_output=True, text=True, check=True)
        remote_result = subprocess.run(['git', 'rev-parse', '@{u}'], 
                                     capture_output=True, text=True, check=True)
        
        if local_result.stdout.strip() != remote_result.stdout.strip():
            print("⚠️  Warning: Your local branch is not up to date with remote!")
            print("Please push your changes before deploying.")
            return False
            
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error checking git status: {e}")
        return False

def get_suggested_app_names():
    """Return a list of suggested app names"""
    return [
        "pwd-tools-hub",
        "infrastructure-suite",
        "raj-pwd-utilities",
        "pwd-management-tools",
        "construction-tools-hub",
        "public-works-suite",
        "pwd-calculators",
        "infrastructure-calculators",
        "raj-infrastructure-tools",
        "pwd-estimation-tools"
    ]

def open_streamlit_cloud():
    """Open Streamlit Cloud in the default browser"""
    try:
        webbrowser.open("https://streamlit.io/cloud")
        print("✅ Opening Streamlit Cloud in your browser...")
        print("Please log in with your GitHub credentials and follow the deployment steps.")
    except Exception as e:
        print(f"❌ Could not open browser: {e}")
        print("Please manually visit: https://streamlit.io/cloud")

def show_deployment_instructions():
    """Show deployment instructions"""
    print("\n" + "="*60)
    print("🚀 PWD Tools Hub - Streamlit Cloud Deployment")
    print("="*60)
    
    print("\n📋 DEPLOYMENT STEPS:")
    print("1. Log in to Streamlit Cloud with your GitHub account")
    print("2. Click 'New app'")
    print("3. Select repository: CRAJKUMARSINGH/PWD-Tools-new")
    print("4. Set branch: main")
    print("5. Set main file path: app.py")
    print("6. Choose a beautiful app name from the suggestions below")
    print("7. Click 'Deploy!'")
    
    print("\n🎨 SUGGESTED APP NAMES:")
    for i, name in enumerate(get_suggested_app_names(), 1):
        print(f"   {i}. {name}")
    
    print("\n🔗 AFTER DEPLOYMENT:")
    print("- Your app will be available at: https://[your-app-name].streamlit.app")
    print("- The app will automatically update when you push changes to the main branch")
    
    print("\n💡 TIPS:")
    print("- Choose a short, memorable name for your app URL")
    print("- The magenta theme will make your app stand out")
    print("- All 9 tools will be accessible from the main dashboard")

def main():
    """Main function"""
    print("🏗️  PWD Tools Hub - Streamlit Deployment Helper")
    print("="*50)
    
    # Check if we're in the right directory
    if not os.path.exists("app.py"):
        print("❌ Error: app.py not found!")
        print("Please run this script from the project root directory.")
        sys.exit(1)
    
    # Check git status
    print("🔍 Checking repository status...")
    if not check_git_status():
        response = input("\nDo you want to continue deployment anyway? (y/N): ")
        if response.lower() != 'y':
            print("Deployment cancelled.")
            sys.exit(1)
    
    # Show deployment instructions
    show_deployment_instructions()
    
    # Ask user if they want to open Streamlit Cloud
    print("\n" + "-"*50)
    response = input("Do you want to open Streamlit Cloud in your browser now? (Y/n): ")
    if response.lower() != 'n':
        open_streamlit_cloud()
    
    print("\n🎉 Deployment helper complete!")
    print("Follow the instructions above to deploy your app to Streamlit Cloud.")

if __name__ == "__main__":
    main()