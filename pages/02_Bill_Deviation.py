import streamlit as st
from utils.branding import apply_custom_css, show_header
from utils.navigation import create_breadcrumb, create_back_button

# Page configuration
st.set_page_config(
    page_title="Bill & Deviation | PWD Tools Hub",
    page_icon="📋",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("Bill & Deviation")

def main():
    # Center content with full width
    col1, col2, col3 = st.columns([1, 8, 1])
    with col2:
        # Access button
        if st.button("🔗 Open Tool", type="primary", use_container_width=True):
            st.warning("This tool requires login. Contact administrator for access.")
            st.markdown("🔗 [Open Tool](https://stream-bill-generator-pjzpbb7a9fdxfmpgpg7t4d.streamlit.app/)")

# Navigation
create_back_button()

# Run main function
if __name__ == "__main__":
    main()