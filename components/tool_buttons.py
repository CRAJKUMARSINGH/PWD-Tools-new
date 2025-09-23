import streamlit as st
from utils.branding import get_tool_colors

def create_tool_grid():
    """Create the main grid of tool buttons with enhanced styling"""
    
    # Tool definitions with categories and external links
    tools = [
        {
            "name": "Excel se EMD",
            "description": "Excel to EMD Refund Generator",
            "icon": "📊",
            "category": "financial",
            "status": "internal",
            "page": "pages/01_Excel_se_EMD.py"
        },
        {
            "name": "Bill Note Sheet",
            "description": "Generate Bill Note Sheets",
            "icon": "📝",
            "category": "financial",
            "status": "internal",
            "page": "pages/04_Bill_Note_Sheet.py"
        },
        {
            "name": "Deductions Table",
            "description": "Manage Deductions in Contracts",
            "icon": "➖",
            "category": "financial",
            "status": "internal",
            "page": "pages/05_Deductions_Table.py"
        },
        {
            "name": "Delay Calculator",
            "description": "Calculate Work Delays and Penalties",
            "icon": "⏱️",
            "category": "calculations",
            "status": "internal",
            "page": "pages/06_Delay_Calculator.py"
        },
        {
            "name": "EMD Refund",
            "description": "EMD Refund Calculator and Tracker",
            "icon": "💸",
            "category": "financial",
            "status": "internal",
            "page": "pages/07_EMD_Refund.py"
        },
        {
            "name": "Financial Progress",
            "description": "Track Financial Progress of Projects",
            "icon": "📈",
            "category": "monitoring",
            "status": "internal",
            "page": "pages/08_Financial_Progress.py"
        },
        {
            "name": "Security Refund",
            "description": "Security Deposit Refund Calculator",
            "icon": "🔒",
            "category": "financial",
            "status": "internal",
            "page": "pages/09_Security_Refund.py"
        },
        {
            "name": "Stamp Duty",
            "description": "Calculate Stamp Duty for Documents",
            "icon": " Stamp Duty Calculator",
            "category": "calculations",
            "status": "internal",
            "page": "pages/10_Stamp_Duty.py"
        },
        {
            "name": "Hand Receipt",
            "description": "Generate Hand Receipts",
            "icon": "📜",
            "category": "documentation",
            "status": "internal",
            "page": "pages/11_Hand_Receipt_Generator.py"
        },
        {
            "name": "Bill & Deviation",
            "description": "Infrastructure Billing System with deviation tracking",
            "icon": "💰",
            "category": "financial", 
            "status": "external",
            "url": "https://raj-bill-generator-v01.streamlit.app/",
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
        }
    ]
    
    colors = get_tool_colors()
    
    # Create enhanced grid layout with better visual hierarchy
    st.markdown("""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <div class="header-container" style="padding: 10px 20px; border-radius: 50px; font-weight: bold;">
            🏗️ 11 Essential Tools Available
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Create grid layout dynamically in rows of 3 columns to match repo design
    num_columns = 3
    for start_index in range(0, len(tools), num_columns):
        cols = st.columns(num_columns)
        for col_idx, col in enumerate(cols):
            tool_idx = start_index + col_idx
            if tool_idx < len(tools):
                tool = tools[tool_idx]
                with col:
                    create_tool_button(tool, colors)


def create_tool_button(tool, colors):
    """Create individual tool button with enhanced styling"""
    
    category_color = colors.get(tool["category"], colors["operations"])
    status_indicator = "🔗 External" if tool["status"] == "external" else "🏠 Internal"
    status_color = "#DC143C" if tool["status"] == "external" else "#2E8B57"
    
    # Create enhanced button container with design closer to repo
    button_html = f"""
    <div class="tool-button">
        <div style="font-size: 3rem; margin-bottom: 15px;">{tool['icon']}</div>
        <div style="font-size: 1.2rem; font-weight: bold; color: #2E8B57; margin-bottom: 10px;">
            {tool['name']}
        </div>
        <div style="font-size: 0.9rem; color: #555; min-height: 60px; margin-bottom: 15px;">
            {tool['description']}
        </div>
        <div style="font-size: 0.8rem; color: {status_color}; font-weight: bold; margin-top: auto; padding: 5px 10px; border-radius: 20px; background-color: rgba(46, 139, 87, 0.1);">
            {status_indicator}
        </div>
    </div>
    """
    
    st.markdown(button_html, unsafe_allow_html=True)
    
    # Navigation link with enhanced styling - restoring the cool design
    if tool["status"] == "external" and tool["url"]:
        st.markdown(f"""
        <a href="{tool['url']}" target="_blank">
            Open External Tool ↗
        </a>
        """, unsafe_allow_html=True)
    else:
        st.page_link(tool["page"], label="Open Tool", icon="▶️", 
                    use_container_width=True)

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
        st.metric("🔗 External Tools", "1", "Connected")
    with col2:
        st.metric("🏠 Internal Tools", "10", "Available")
    with col3:
        st.metric("📊 Total Categories", "5", "Organized")
