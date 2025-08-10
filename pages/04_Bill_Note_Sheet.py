import streamlit as st
import streamlit.components.v1 as components
from utils.branding import apply_custom_css, show_header
from utils.navigation import create_breadcrumb, create_back_button

# Page configuration
st.set_page_config(
    page_title="Contract Management | PWD Tools Hub",
    page_icon="📝",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("Contract Management System")

def main():
    st.markdown("## 📝 Bill Note Sheet Generator")
    
    st.info("""
    **बिल नोट शीट जेनरेटर (हिन्दी)**
    
    Generate bill note sheets for PWD documentation in Hindi language with all required statutory formats.
    """)
    
    # Read and display the HTML content
    try:
        with open("static/html/BillNoteSheet.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Display the HTML content
        components.html(html_content, height=800, scrolling=True)
        
    except FileNotFoundError:
        st.error("Bill Note Sheet tool is currently unavailable. Please contact administrator.")
        
        # Fallback information
        st.markdown("### Tool Features:")
        st.markdown("""
        - Generate Hindi bill note sheets
        - Support for running and final bills
        - Automatic date formatting
        - Statutory PWD compliance
        - Print-ready format
        """)

# Navigation
create_back_button()

if __name__ == "__main__":
    main()
