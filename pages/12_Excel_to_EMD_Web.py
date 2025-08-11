import streamlit as st
from utils.branding import apply_custom_css
from utils.navigation import create_breadcrumb, create_back_button

# Page configuration
st.set_page_config(
    page_title="Excel to EMD-Web | PWD Tools Hub",
    page_icon="🔗",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("Excel to EMD-Web")

def main():
    col1, col2, col3 = st.columns([1, 8, 1])
    with col2:
        st.markdown("### Choose Access Method:")
        st.info("This tool opens an external web app in a new tab")

        external_url = "https://marudharhr.onrender.com/"

        col_a, col_b, col_c = st.columns(3)
        with col_a:
            if st.button("🔗 Open in New Tab", use_container_width=True):
                st.markdown(
                    f"""
                    <script>
                        window.open('{external_url}', '_blank');
                    </script>
                    """,
                    unsafe_allow_html=True,
                )
                st.success("Opened in a new tab")
        with col_b:
            if st.button("📋 Copy Link", use_container_width=True):
                st.code(external_url)
                st.success("Link copied!")
        with col_c:
            st.markdown(f"🔗 [Direct Link]({external_url})")

# Navigation
create_back_button()

# Run main function
if __name__ == "__main__":
    main()