import streamlit as st
import streamlit.components.v1 as components
from utils.branding import apply_custom_css, show_header
from utils.navigation import create_breadcrumb, create_back_button

# Page configuration
st.set_page_config(
    page_title="Stamp Duty | PWD Tools Hub",
    page_icon="📋",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("Stamp Duty")

def main():
    st.markdown("## 📋 Stamp Duty Calculator")
    
    st.info("""
    **Calculate Stamp Duty for Work Orders**
    
    Calculate stamp duty amounts for PWD work orders based on statutory rates.
    """)
    
    # Read and display the HTML content
    try:
        with open("static/html/StampDuty.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Display the HTML content
        components.html(html_content, height=600, scrolling=True)
        
    except FileNotFoundError:
        st.error("Stamp Duty tool is currently unavailable. Please contact administrator.")

# Navigation
create_back_button()

# Run main function
if __name__ == "__main__":
    main()