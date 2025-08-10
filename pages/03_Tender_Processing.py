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
    # Center content with full width
    col1, col2, col3 = st.columns([1, 8, 1])
    with col2:
        # Access button
        if st.button("🔗 Open Tool", type="primary", use_container_width=True):
            st.warning("This tool requires login. Contact administrator for access.")
            st.markdown("🔗 [Open Tool](https://priyankatenderfinal-unlhs2yudbpg2ipxgdggws.streamlit.app/)")

# Navigation
create_back_button()

# Run main function
if __name__ == "__main__":
    main()