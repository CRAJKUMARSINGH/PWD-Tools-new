import streamlit as st
from utils.branding import apply_custom_css, show_header
from utils.navigation import create_breadcrumb, create_back_button, show_external_link_warning

# Page configuration
st.set_page_config(
    page_title="Tender Processing | Tender Management System",
    page_icon="📋",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("Tender Processing - Tender Management System")

# Main content
def main():
    st.markdown("## 📋 Tender Processing - Tender Management System")
    
    # Tool description
    st.info("""
    **Comprehensive tender lifecycle management**
    
    Handle all aspects of tender processing from creation to award, ensuring compliance 
    with procurement regulations and maintaining transparent documentation.
    """)
    
    # External link warning
    show_external_link_warning()
    
    # Tool features
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ✨ Key Features")
        st.markdown("""
        - 📝 **Tender Creation**: Create detailed tender documents
        - 📊 **Bid Management**: Handle multiple vendor submissions
        - 🔍 **Evaluation System**: Systematic bid evaluation process
        - 📋 **Document Management**: Organize all tender-related documents
        - ⚖️ **Compliance Tracking**: Ensure regulatory compliance
        - 📈 **Progress Monitoring**: Track tender process stages
        """)
    
    with col2:
        st.markdown("### 🔄 Process Stages")
        st.markdown("""
        1. **Tender Preparation**: Document creation and specifications
        2. **Publication**: Tender advertisement and dissemination
        3. **Bid Collection**: Receive and organize vendor submissions
        4. **Technical Evaluation**: Assess technical compliance
        5. **Financial Evaluation**: Compare financial proposals
        6. **Award Process**: Final selection and contract award
        """)
    
    # Process workflow
    st.markdown("### 🔄 Tender Workflow")
    
    # Create workflow visualization
    workflow_steps = [
        ("1️⃣", "Tender Preparation", "Create specifications, terms, and conditions"),
        ("2️⃣", "Document Review", "Internal review and approval process"),
        ("3️⃣", "Publication", "Advertise tender through official channels"),
        ("4️⃣", "Pre-bid Meeting", "Clarifications and site visits"),
        ("5️⃣", "Bid Submission", "Collect vendor proposals by deadline"),
        ("6️⃣", "Technical Evaluation", "Assess technical compliance and capability"),
        ("7️⃣", "Financial Evaluation", "Compare prices and financial terms"),
        ("8️⃣", "Award Decision", "Select winning bid and process award")
    ]
    
    for step_num, step_name, step_desc in workflow_steps:
        with st.container():
            col1, col2, col3 = st.columns([1, 3, 6])
            with col1:
                st.markdown(f"### {step_num}")
            with col2:
                st.markdown(f"**{step_name}**")
            with col3:
                st.markdown(step_desc)
    
    # Document types
    st.markdown("### 📄 Document Management")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📋 Tender Docs", "💼 Bid Management", "🔍 Evaluation", "📊 Reports"])
    
    with tab1:
        st.markdown("""
        **Tender Documents:**
        - Notice Inviting Tender (NIT)
        - Technical Specifications
        - Commercial Terms & Conditions
        - Contract Agreement Format
        - Drawings and Schedules
        - Pre-qualification Criteria
        """)
    
    with tab2:
        st.markdown("""
        **Bid Management:**
        - Bid Registration System
        - Document Checklist Verification
        - Compliance Matrix
        - Clarification Management
        - Amendment Tracking
        - Deadline Monitoring
        """)
    
    with tab3:
        st.markdown("""
        **Evaluation Process:**
        - Technical Evaluation Matrix
        - Financial Comparison Sheets
        - Scoring and Ranking System
        - Evaluation Committee Reports
        - Deviation Analysis
        - Recommendation Reports
        """)
    
    with tab4:
        st.markdown("""
        **Reports & Analytics:**
        - Tender Summary Reports
        - Vendor Performance Analysis
        - Process Timeline Reports
        - Compliance Audit Reports
        - Cost Analysis Reports
        - Award Statistics
        """)
    
    # Instructions
    st.markdown("### 📖 How to Use")
    st.markdown("""
    1. **Access the Tool**: Click the link below to access the tender processing system
    2. **Create New Tender**: Start with tender details and specifications
    3. **Manage Documents**: Upload and organize all required documentation
    4. **Track Submissions**: Monitor bid submissions and maintain records
    5. **Conduct Evaluation**: Use built-in evaluation tools and matrices
    6. **Generate Reports**: Create comprehensive reports for decision-making
    """)
    
    # Access button
    st.markdown("---")
    st.markdown("### 🚀 Access Tool")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔗 Open Tender Processing Tool", type="primary", use_container_width=True):
            st.markdown("""
            <script>
                window.open('https://priyankatenderfinal-unlhs2yudbpg2ipxgdggws.streamlit.app/', '_blank');
            </script>
            """, unsafe_allow_html=True)
            st.success("✅ Tool opened in new tab! If it didn't open automatically, click the link below:")
            st.markdown("🔗 [Open Tender Processing Tool](https://priyankatenderfinal-unlhs2yudbpg2ipxgdggws.streamlit.app/)")
    
    # Additional resources
    st.markdown("---")
    st.markdown("### 📚 Resources & Support")
    
    with st.expander("📋 Tender Process Guidelines"):
        st.markdown("""
        **Key Principles:**
        - **Transparency**: Open and fair process for all vendors
        - **Competitiveness**: Encourage maximum participation
        - **Accountability**: Clear documentation and audit trails
        - **Efficiency**: Streamlined processes with defined timelines
        - **Quality**: Focus on technical competency and value for money
        
        **Compliance Requirements:**
        - Follow government procurement rules and regulations
        - Maintain proper documentation at each stage
        - Ensure equal opportunity for all qualified vendors
        - Adhere to specified evaluation criteria
        """)
    
    with st.expander("🔧 System Capabilities"):
        st.markdown("""
        **Advanced Features:**
        - Multi-user access with role-based permissions
        - Automated workflow notifications and alerts
        - Document version control and audit trails
        - Integration with government procurement portals
        - Advanced search and filtering capabilities
        - Comprehensive reporting and analytics
        
        **Security Features:**
        - Secure document storage and access control
        - Digital signatures and authentication
        - Encrypted data transmission
        - Regular security audits and updates
        """)
    
    with st.expander("❓ Frequently Asked Questions"):
        st.markdown("""
        **Q: How do I create a new tender?**
        A: Use the "Create New Tender" option and follow the step-by-step wizard.
        
        **Q: Can I track bid submissions in real-time?**
        A: Yes, the system provides real-time updates on bid submissions and status.
        
        **Q: How is bid evaluation conducted?**
        A: The system provides evaluation matrices and scoring tools for systematic assessment.
        
        **Q: Can I generate custom reports?**
        A: Yes, the system offers various report templates and custom report generation options.
        
        **Q: Is the system compliant with government regulations?**
        A: Yes, the system is designed to comply with standard government procurement processes.
        """)

# Navigation
create_back_button()

# Execute main function
if __name__ == "__main__":
    main()
