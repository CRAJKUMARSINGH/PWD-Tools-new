"""
Verification script to check that the initiative credit information is properly included.
"""

import sys
import os

# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

def verify_credits():
    """Verify that the credits include the initiative credit information"""
    try:
        # Read the branding.py file
        with open(os.path.join(current_dir, 'utils', 'branding.py'), 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for required elements
        required_elements = [
            'Initiative Credit',
            'Mrs. Premlata Jain',
            'Additional Administrative Officer, PWD Udaipur',
            'Version 2.0',
            'Last Updated: September 2025'
        ]
        
        missing_elements = []
        for element in required_elements:
            if element not in content:
                missing_elements.append(element)
        
        if missing_elements:
            print("❌ MISSING ELEMENTS:")
            for element in missing_elements:
                print(f"  - {element}")
            return False
        else:
            print("✅ All required elements found in credits:")
            for element in required_elements:
                print(f"  - {element}")
            return True
            
    except Exception as e:
        print(f"❌ Error verifying credits: {e}")
        return False

if __name__ == "__main__":
    print("Verifying initiative credit information...")
    print("=" * 50)
    success = verify_credits()
    print("=" * 50)
    if success:
        print("✅ Verification PASSED")
    else:
        print("❌ Verification FAILED")