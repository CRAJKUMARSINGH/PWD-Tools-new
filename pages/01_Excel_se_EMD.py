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
    st.markdown("## 📊 Excel se EMD")
    
    # Access button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔗 Open Excel se EMD Tool", type="primary", use_container_width=True):
            st.markdown("""
            <script>
                window.open('https://marudharhr.onrender.com/', '_blank');
            </script>
            """, unsafe_allow_html=True)
            st.success("Tool opened!")
            st.markdown("🔗 [Open Excel se EMD Tool](https://marudharhr.onrender.com/)")

# Navigation
create_back_button()

# Run main function
if __name__ == "__main__":
    main()