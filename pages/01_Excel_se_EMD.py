import streamlit as st
from utils.branding import apply_custom_css, show_header
from utils.navigation import create_breadcrumb, create_back_button, show_external_link_warning

# Page configuration
st.set_page_config(
    page_title="Excel se EMD | Hand Receipt Generator",
    page_icon="📊",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("Excel se EMD - Hand Receipt Generator")

# Main content
def main():
    st.markdown("## 📊 Excel se EMD - Hand Receipt Generator")
    
    # Tool description
    st.info("""
    **Generate professional hand receipts from Excel files**
    
    This tool allows you to upload Excel files with payee information and automatically generate 
    PDF hand receipts for EMD (Earnest Money Deposit) processing.
    """)
    
    # External link warning
    show_external_link_warning()
    
    # Tool features
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ✨ Features")
        st.markdown("""
        - 📤 **Excel File Upload**: Upload files with payee data
        - 📄 **PDF Generation**: Automatic receipt creation
        - 💰 **EMD Processing**: Handle earnest money deposits
        - 📊 **Data Validation**: Ensure all required fields are present
        - 🔄 **Batch Processing**: Handle multiple entries at once
        """)
    
    with col2:
        st.markdown("### 📋 Required Excel Columns")
        st.markdown("""
        Your Excel file must contain these columns:
        - **Payee Name**: Name of the person/organization
        - **Amount**: EMD amount in numbers
        - **Work**: Description of the work/project
        
        *Note: Column names should match exactly*
        """)
    
    # Instructions
    st.markdown("### 📖 How to Use")
    st.markdown("""
    1. **Prepare Excel File**: Ensure your file has the required columns (Payee Name, Amount, Work)
    2. **Upload File**: Use the upload feature on the external tool
    3. **Generate PDF**: Click generate to create hand receipts
    4. **Download**: Save the generated PDF documents
    """)
    
    # Access button
    st.markdown("---")
    st.markdown("### 🚀 Access Tool")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔗 Open Excel se EMD Tool", type="primary", use_container_width=True):
            st.markdown("""
            <script>
                window.open('https://marudharhr.onrender.com/', '_blank');
            </script>
            """, unsafe_allow_html=True)
            st.success("✅ Tool opened in new tab! If it didn't open automatically, click the link below:")
            st.markdown("🔗 [Open Excel se EMD Tool](https://marudharhr.onrender.com/)")
    
    # Additional help
    st.markdown("---")
    st.markdown("### ❓ Need Help?")
    
    with st.expander("📚 Troubleshooting & Tips"):
        st.markdown("""
        **Common Issues:**
        - **Tool not loading**: Check your internet connection and try refreshing
        - **Excel file not accepted**: Ensure columns are named exactly as specified
        - **PDF not generating**: Verify all required data is present and valid
        
        **Tips for Best Results:**
        - Use clean, well-formatted Excel files
        - Ensure amount values are numeric
        - Keep payee names and work descriptions clear and concise
        - Test with a small sample first before processing large batches
        """)
    
    with st.expander("📊 Sample Excel Format"):
        st.markdown("**Example of properly formatted Excel data:**")
        
        import pandas as pd
        sample_data = {
            "Payee Name": ["ABC Construction Ltd", "XYZ Engineers", "PQR Contractors"],
            "Amount": [50000, 75000, 100000],
            "Work": ["Road Construction Project", "Bridge Maintenance Work", "Building Construction"]
        }
        sample_df = pd.DataFrame(sample_data)
        st.dataframe(sample_df, use_container_width=True)

# Navigation
create_back_button()

# Execute main function
if __name__ == "__main__":
    main()
