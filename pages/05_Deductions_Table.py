import streamlit as st
import streamlit.components.v1 as components
from utils.branding import apply_custom_css, show_header
from utils.navigation import create_breadcrumb, create_back_button

# Page configuration
st.set_page_config(
    page_title="Deductions Table | PWD Tools Hub",
    page_icon="📊",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("Deductions Table")

def main():
    st.markdown("## 📊 Deductions Table")
    
    # Read and display the HTML content
    try:
        with open("static/html/DeductionsTable.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Display the HTML content
        components.html(html_content, height=800, scrolling=True)
        
    except FileNotFoundError:
        st.error("Tool not available")

# Navigation
create_back_button()

# Run main function
if __name__ == "__main__":
    main()