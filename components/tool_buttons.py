import streamlit as st
from utils.branding import get_tool_colors

def create_tool_grid():
    """Create the main grid of tool buttons"""
    
    # Tool definitions with categories and external links
    tools = [
        {
            "name": "Excel se EMD",
            "description": "Hand Receipt Generator from Excel files",
            "icon": "📊",
            "category": "financial",
            "status": "external",
            "url": "https://marudharhr.onrender.com/",
            "page": "pages/01_Excel_se_EMD.py"
        },
        {
            "name": "Bill & Deviation",
            "description": "Infrastructure Billing System with deviation tracking",
            "icon": "💰",
            "category": "financial", 
            "status": "external",
            "url": "https://stream-bill-generator-pjzpbb7a9fdxfmpgpg7t4d.streamlit.app/",
            "page": "pages/02_Bill_Deviation.py"
        },
        {
            "name": "Tender Processing",
            "description": "Comprehensive tender management system",
            "icon": "📋",
            "category": "processing",
            "status": "external", 
            "url": "https://priyankatenderfinal-unlhs2yudbpg2ipxgdggws.streamlit.app/",
            "page": "pages/03_Tender_Processing.py"
        },
        {
            "name": "Contract Management",
            "description": "Contract lifecycle and document management",
            "icon": "📝",
            "category": "processing",
            "status": "internal",
            "url": None,
            "page": "pages/04_Contract_Management.py"
        },
        {
            "name": "Work Order System", 
            "description": "Generate and track work orders efficiently",
            "icon": "🏗️",
            "category": "operations",
            "status": "internal",
            "url": None,
            "page": "pages/05_Work_Order_System.py"
        },
        {
            "name": "Payment Processing",
            "description": "Handle payments, bills and financial transactions",
            "icon": "💳",
            "category": "financial",
            "status": "internal", 
            "url": None,
            "page": "pages/06_Payment_Processing.py"
        },
        {
            "name": "Material Management",
            "description": "Track inventory, supplies and material usage",
            "icon": "📦",
            "category": "operations",
            "status": "internal",
            "url": None,
            "page": "pages/07_Material_Management.py"
        },
        {
            "name": "Quality Control",
            "description": "Quality assurance and compliance tracking",
            "icon": "✅",
            "category": "monitoring",
            "status": "internal",
            "url": None,
            "page": "pages/08_Quality_Control.py"
        },
        {
            "name": "Progress Monitoring",
            "description": "Track project progress and milestone completion",
            "icon": "📈", 
            "category": "monitoring",
            "status": "internal",
            "url": None,
            "page": "pages/09_Progress_Monitoring.py"
        },
        {
            "name": "Report Generator",
            "description": "Generate comprehensive PWD reports and analytics",
            "icon": "📄",
            "category": "monitoring",
            "status": "internal",
            "url": None,
            "page": "pages/10_Report_Generator.py"
        }
    ]
    
    colors = get_tool_colors()
    
    # Create grid layout (2 rows of 5 tools each)
    for row in range(2):
        cols = st.columns(5)
        for col_idx, col in enumerate(cols):
            tool_idx = row * 5 + col_idx
            if tool_idx < len(tools):
                tool = tools[tool_idx]
                with col:
                    create_tool_button(tool, colors)

def create_tool_button(tool, colors):
    """Create individual tool button with proper styling"""
    
    category_color = colors.get(tool["category"], colors["operations"])
    status_indicator = "🔗" if tool["status"] == "external" else "🏠"
    
    # Create button container
    button_html = f"""
    <div class="tool-button" style="
        background: linear-gradient(135deg, {category_color['bg']} 0%, #ffffff 100%);
        border: 2px solid {category_color['border']};
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
        min-height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    ">
        <div style="font-size: 3rem; margin-bottom: 10px;">{tool['icon']}</div>
        <div style="font-size: 1.1rem; font-weight: bold; color: {category_color['border']}; margin-bottom: 8px;">
            {tool['name']} {status_indicator}
        </div>
        <div style="font-size: 0.85rem; color: #666; line-height: 1.3;">
            {tool['description']}
        </div>
        <div style="margin-top: 10px;">
            <span style="background-color: {category_color['border']}; color: white; padding: 4px 8px; border-radius: 12px; font-size: 0.7rem;">
                {tool['category'].title()}
            </span>
        </div>
    </div>
    """
    
    st.markdown(button_html, unsafe_allow_html=True)
    
    # Create clickable button
    button_key = f"tool_{tool['name'].lower().replace(' ', '_')}"
    if st.button(f"Open {tool['name']}", key=button_key, use_container_width=True):
        if tool["status"] == "external" and tool["url"]:
            # For external tools, navigate to the page which will handle the redirect
            st.switch_page(tool["page"])
        else:
            # For internal tools, navigate directly to the page
            st.switch_page(tool["page"])

def create_category_filter():
    """Create category filter for tools"""
    st.sidebar.markdown("### 🎯 Filter by Category")
    
    categories = ["All", "Financial", "Processing", "Operations", "Monitoring"]
    selected_category = st.sidebar.selectbox("Select Category:", categories)
    
    return selected_category.lower() if selected_category != "All" else None

def show_tool_stats():
    """Display statistics about available tools"""
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🔗 External Tools", "3", "Connected")
    with col2:
        st.metric("🏠 Internal Tools", "7", "Available")
    with col3:
        st.metric("📊 Total Categories", "4", "Organized")
