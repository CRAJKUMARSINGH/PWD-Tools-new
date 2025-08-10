import streamlit as st
import streamlit.components.v1 as components
from utils.branding import apply_custom_css, show_header
from utils.navigation import create_breadcrumb, create_back_button

# Page configuration
st.set_page_config(
    page_title="Financial Progress | PWD Tools Hub",
    page_icon="📈",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("Financial Progress")

def main():
    st.markdown("## 📈 Financial Progress Tracker")
    
    st.info("""
    **Track Financial Progress and Liquidity Damages**
    
    Calculate financial progress and liquidity damages for PWD projects.
    """)
    
    # Read and display the HTML content
    try:
        with open("static/html/FinancialProgressTracker.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Display the HTML content
        components.html(html_content, height=800, scrolling=True)
        
    except FileNotFoundError:
        st.error("Financial Progress tool is currently unavailable. Please contact administrator.")

# Navigation
create_back_button()

# Run main function
if __name__ == "__main__":
    main()