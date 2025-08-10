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
    st.markdown("### 🎯 PWD Tools Hub")
    st.markdown("**Infrastructure Management Tools** - Simple tools for PWD operations")
    
    st.markdown("---")
    
    # Tools grid section
    st.markdown("### 🔧 Available Tools")
    
    # Create the main tool grid
    create_tool_grid()
    
    # Simplified sidebar
    with st.sidebar:
        st.markdown("### 🔧 Quick Access")
        
        if st.button("📊 Excel se EMD", key="quick_emd", use_container_width=True):
            st.switch_page("pages/01_Excel_se_EMD.py")
        
        if st.button("💰 Bill & Deviation", key="quick_bill", use_container_width=True):
            st.switch_page("pages/02_Bill_Deviation.py")
        
        if st.button("📋 Tender Processing", key="quick_tender", use_container_width=True):
            st.switch_page("pages/03_Tender_Processing.py")



# Main app execution
if __name__ == "__main__":
    main()
    
    # Show credits at bottom
    st.markdown("---")
    show_credits()
    

