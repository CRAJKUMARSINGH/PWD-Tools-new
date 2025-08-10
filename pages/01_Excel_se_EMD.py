import streamlit as st
from utils.branding import apply_custom_css, show_header
from utils.navigation import create_breadcrumb, create_back_button

# Page configuration
st.set_page_config(
    page_title="Excel se EMD | PWD Tools Hub",
    page_icon="📊",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("Excel se EMD")

def main():
    # Center content with full width
    col1, col2, col3 = st.columns([1, 8, 1])
    with col2:
        # Three access buttons
        st.markdown("### Choose Access Method:")
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("🔗 Open in New Tab", use_container_width=True):
                st.markdown("""
                <script>
                    window.open('https://marudharhr.onrender.com/', '_blank');
                </script>
                """, unsafe_allow_html=True)
                st.success("Tool opened!")
        
        with col_b:
            if st.button("📋 Copy Link", use_container_width=True):
                st.code("https://marudharhr.onrender.com/")
                st.success("Link copied!")
        
        with col_c:
            st.markdown("🔗 [Direct Link](https://marudharhr.onrender.com/)")

# Navigation
create_back_button()

# Run main function
if __name__ == "__main__":
    main()