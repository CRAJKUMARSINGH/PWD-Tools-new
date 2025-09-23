import streamlit as st
import time
import sys
import os

# Debug information
st.write("DEBUG: Running main app.py")
st.write(f"Current working directory: {os.getcwd()}")
st.write(f"Python path: {sys.path}")

# Ensure the current directory is in the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Version identifier for debugging
APP_VERSION = "1.0.2-debug"

# Import only the functions we actually use
try:
    from utils.branding import apply_custom_css, show_header, show_credits
    st.write("DEBUG: Successfully imported from utils.branding")
except Exception as e:
    st.write(f"DEBUG: Failed to import from utils.branding: {e}")
    st.write(f"DEBUG: utils directory exists: {os.path.exists('utils')}")
    if os.path.exists('utils'):
        st.write(f"DEBUG: utils files: {os.listdir('utils')}")
    raise

try:
    from components.tool_buttons import create_tool_grid
    st.write("DEBUG: Successfully imported from components.tool_buttons")
except Exception as e:
    st.write(f"DEBUG: Failed to import from components.tool_buttons: {e}")
    st.write(f"DEBUG: components directory exists: {os.path.exists('components')}")
    if os.path.exists('components'):
        st.write(f"DEBUG: components files: {os.listdir('components')}")
    raise

# Page configuration
st.set_page_config(
    page_title="PWD Tools Hub | Infrastructure Management Suite",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styling and branding
apply_custom_css()

# Show header with branding
show_header()

# Main content area
def main():
    # Welcome section
    st.markdown("### 🎯 PWD Tools Hub")
    st.markdown("**Infrastructure Management Tools** - Simple tools for PWD operations")
    
    st.markdown("---")
    
    # Tools grid section
    st.markdown("### 🔧 Available Tools")
    
    # Create the main tool grid
    create_tool_grid()

# Main app execution
if __name__ == "__main__":
    main()
    
    # Show credits at bottom
    st.markdown("---")
    show_credits()