import streamlit as st
from utils.branding import apply_custom_css, show_header
from utils.navigation import create_breadcrumb, create_back_button, show_external_link_warning

# Page configuration
st.set_page_config(
    page_title="Bill & Deviation | Infrastructure Billing System",
    page_icon="💰",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("Bill & Deviation - Infrastructure Billing System")

# Main content
def main():
    st.markdown("## 💰 Bill & Deviation - Infrastructure Billing System")
    
    # Tool description
    st.info("""
    **Professional infrastructure billing with deviation tracking**
    
    Generate comprehensive billing documents, track deviations, and manage financial aspects 
    of infrastructure projects with statutory compliance.
    """)
    
    # External link warning
    show_external_link_warning()
    
    # Tool features
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ✨ Features")
        st.markdown("""
        - 📊 **Excel Processing**: Handle complex billing data from Excel
        - 📋 **Multiple Documents**: Generate various billing certificates
        - 📈 **Deviation Tracking**: Monitor and report project deviations
        - 🏗️ **Infrastructure Focus**: PWD-specific billing formats
        - ✅ **Statutory Compliance**: Approved government formats
        - 🎨 **Professional Design**: Crane logo branding throughout
        """)
    
    with col2:
        st.markdown("### 📄 Generated Documents")
        st.markdown("""
        - **First Page Summary**: Project overview and totals
        - **Deviation Statement**: Track changes from original scope
        - **Final Bill Scrutiny**: Detailed billing verification
        - **Extra Items Statement**: Additional work documentation
        - **Certificate II & III**: Official completion certificates
        - **Combined PDF Package**: All documents in one file
        """)
    
    # Document types
    st.markdown("### 📋 Document Categories")
    
    tab1, tab2, tab3 = st.tabs(["💰 Financial", "📊 Certificates", "📈 Tracking"])
    
    with tab1:
        st.markdown("""
        **Financial Documents:**
        - First Page Summary with total calculations
        - Final Bill Scrutiny Sheet with detailed breakdowns
        - Extra Items Statement for additional work
        - Deviation cost analysis and impact assessment
        """)
    
    with tab2:
        st.markdown("""
        **Official Certificates:**
        - Certificate II: Work completion verification
        - Certificate III: Final acceptance and quality assurance
        - Professional formatting with PWD branding
        - Statutory compliance with approved formats
        """)
    
    with tab3:
        st.markdown("""
        **Progress Tracking:**
        - Deviation Statement with variance analysis
        - Progress monitoring against original estimates
        - Quality control checkpoints
        - Timeline and milestone tracking
        """)
    
    # Instructions
    st.markdown("### 📖 Usage Instructions")
    st.markdown("""
    1. **Excel Preparation**: Prepare Excel file with required sheets (Title, Work Order, Bill Quantity, Extra Items)
    2. **File Upload**: Upload your Excel file through the tool interface
    3. **Data Processing**: System automatically extracts and validates data
    4. **Document Generation**: All billing documents are generated simultaneously  
    5. **Download Package**: Receive ZIP file with all documents in multiple formats
    """)
    
    # Access button
    st.markdown("---")
    st.markdown("### 🚀 Access Tool")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔗 Open Bill & Deviation Tool", type="primary", use_container_width=True):
            st.markdown("""
            <script>
                window.open('https://stream-bill-generator-pjzpbb7a9fdxfmpgpg7t4d.streamlit.app/', '_blank');
            </script>
            """, unsafe_allow_html=True)
            st.success("✅ Tool opened in new tab! If it didn't open automatically, click the link below:")
            st.markdown("🔗 [Open Bill & Deviation Tool](https://stream-bill-generator-pjzpbb7a9fdxfmpgpg7t4d.streamlit.app/)")
    
    # Additional help
    st.markdown("---")
    st.markdown("### ❓ Support & Documentation")
    
    with st.expander("📚 Excel File Requirements"):
        st.markdown("""
        **Required Excel Sheets:**
        - **Title Sheet**: Project information and basic details
        - **Work Order Sheet**: Original work order specifications
        - **Bill Quantity Sheet**: Quantity measurements and calculations  
        - **Extra Items Sheet**: Additional work items and costs
        
        **Column Requirements:**
        - Item/Item No: Description of work items
        - Quantity/Qty: Measured quantities
        - Rate: Unit rates for calculations
        - Amount: Total costs (calculated or provided)
        """)
    
    with st.expander("🔧 Troubleshooting Guide"):
        st.markdown("""
        **Common Issues & Solutions:**
        - **File Upload Failed**: Ensure Excel file is not corrupted and sheets are properly named
        - **Missing Data**: Verify all required columns are present with correct names
        - **Calculation Errors**: Check that numeric values are properly formatted
        - **Document Generation Issues**: Ensure all mandatory fields contain valid data
        
        **Performance Tips:**
        - Use clean, well-structured Excel files
        - Avoid merged cells in data ranges
        - Keep file sizes reasonable for faster processing
        """)
    
    with st.expander("🏆 Quality Standards"):
        st.markdown("""
        **Document Quality Features:**
        - Professional PWD branding with crane logo (🏗️)
        - Statutory format compliance as per government requirements
        - Comprehensive error handling and validation
        - Clean, readable document layouts
        - Proper mathematical calculations and cross-references
        """)

# Navigation
create_back_button()

# Execute main function
if __name__ == "__main__":
    main()
