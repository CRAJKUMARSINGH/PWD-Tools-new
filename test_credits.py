"""
Test script to verify that the initiative credit information is displayed correctly.
"""

import sys
import os

# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from utils.branding import show_credits
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Credits Test | PWD Tools Hub",
    page_icon="🏛️",
    layout="centered"
)

st.title("Initiative Credit Verification")

st.markdown("""
This page tests that the initiative credit information is displayed correctly.
The credit information should include:
- Mrs. Premlata Jain
- Additional Administrative Officer, PWD Udaipur
- Version 2.0 | Last Updated: September 2025
""")

st.markdown("---")
st.markdown("### Displayed Credits:")

# Show the credits
show_credits()

st.markdown("---")
st.markdown("✅ If you can see the initiative credit information above, the implementation is working correctly.")