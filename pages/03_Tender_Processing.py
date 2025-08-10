import streamlit as st
from utils.branding import apply_custom_css, show_header
from utils.navigation import create_breadcrumb, create_back_button

# Page configuration
st.set_page_config(
    page_title="Tender Processing | PWD Tools Hub",
    page_icon="📑",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("Tender Processing")

def main():
    # Access button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔗 Open Tool", type="primary", use_container_width=True):
            st.markdown("""
            <script>
                window.open('https://priyankatenderfinal-unlhs2yudbpg2ipxgdggws.streamlit.app/', '_blank');
            </script>
            """, unsafe_allow_html=True)
            st.success("Tool opened!")
            st.markdown("🔗 [Open Tool](https://priyankatenderfinal-unlhs2yudbpg2ipxgdggws.streamlit.app/)")

# Navigation
create_back_button()

# Run main function
if __name__ == "__main__":
    main()