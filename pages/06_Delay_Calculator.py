import streamlit as st
import streamlit.components.v1 as components
from utils.branding import apply_custom_css, show_header
from utils.navigation import create_breadcrumb, create_back_button

# Page configuration
st.set_page_config(
    page_title="Delay Calculator | PWD Tools Hub",
    page_icon="⏰",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("Delay Calculator")

def main():
    st.markdown("## ⏰ Delay Calculator")
    
    st.info("""
    **Project Delay Analysis Tool**
    
    Calculate project delays and analyze timeline variations for PWD infrastructure projects.
    """)
    
    # Read and display the HTML content
    try:
        with open("static/html/DelayCalculator.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Display the HTML content
        components.html(html_content, height=600, scrolling=True)
        
    except FileNotFoundError:
        st.error("Delay Calculator tool is currently unavailable. Please contact administrator.")
        
        # Fallback information
        st.markdown("### Tool Features:")
        st.markdown("""
        - Calculate project delays
        - Timeline analysis
        - Date comparison
        - Delay reporting
        - Simple interface
        """)

# Navigation
create_back_button()

# Run main function
if __name__ == "__main__":
    main()