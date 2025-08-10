import streamlit as st
import time
from utils.branding import apply_custom_css, show_header, show_credits, show_balloons
from components.tool_buttons import create_tool_grid

# Page configuration
st.set_page_config(
    page_title="PWD Tools Hub | Infrastructure Management Suite",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styling and branding
apply_custom_css()

# Show header with branding
show_header()

# Main content area
def main():
    # Welcome section
    st.markdown("### 🎯 Welcome to PWD Tools Hub")
    st.markdown("""
    **Your comprehensive infrastructure management solution** - A unified platform for all PWD operations 
    designed specifically for nascent clerks with simple, colorful, and intuitive interface.
    """)
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🛠️ Total Tools", "10", "Active")
    with col2:
        st.metric("📊 Categories", "5", "Infrastructure")
    with col3:
        st.metric("👥 User Type", "Clerks", "Friendly")
    with col4:
        st.metric("🎨 Interface", "Colorful", "Simple")
    
    st.markdown("---")
    
    # Tools grid section
    st.markdown("### 🔧 Available Tools")
    st.markdown("Click on any tool below to access its features:")
    
    # Create the main tool grid
    create_tool_grid()
    
    # Quick access sidebar
    with st.sidebar:
        st.markdown("### 🚀 Quick Access")
        st.markdown("#### 📌 Most Used Tools")
        
        if st.button("📊 Excel se EMD", key="quick_emd", use_container_width=True):
            st.switch_page("pages/01_Excel_se_EMD.py")
        
        if st.button("💰 Bill & Deviation", key="quick_bill", use_container_width=True):
            st.switch_page("pages/02_Bill_Deviation.py")
        
        if st.button("📋 Tender Processing", key="quick_tender", use_container_width=True):
            st.switch_page("pages/03_Tender_Processing.py")
        
        st.markdown("---")
        st.markdown("#### 🎯 Quick Search")
        search_term = st.text_input("Search tools...", placeholder="Type tool name")
        
        if search_term:
            tools = [
                "Excel se EMD", "Bill & Deviation", "Tender Processing",
                "Contract Management", "Work Order System", "Payment Processing",
                "Material Management", "Quality Control", "Progress Monitoring", "Report Generator"
            ]
            filtered_tools = [tool for tool in tools if search_term.lower() in tool.lower()]
            for tool in filtered_tools:
                st.write(f"🔍 {tool}")
        
        st.markdown("---")
        st.markdown("#### 📱 Tool Categories")
        st.markdown("""
        - 💰 **Financial**: Bills, Payments, EMD
        - 📋 **Processing**: Tenders, Contracts
        - 🏗️ **Operations**: Work Orders, Materials
        - 📊 **Monitoring**: Quality, Progress, Reports
        """)

# Success animation
def show_success_animation():
    """Display celebration animation for successful operations"""
    show_balloons()

# Main app execution
if __name__ == "__main__":
    main()
    
    # Show credits at bottom
    st.markdown("---")
    show_credits()
    
    # Footer
    st.markdown("""
    <div style='text-align: center; padding: 20px; color: #666;'>
        🏗️ PWD Tools Hub - Built for Infrastructure Excellence | Made with ❤️ using Streamlit
    </div>
    """, unsafe_allow_html=True)
