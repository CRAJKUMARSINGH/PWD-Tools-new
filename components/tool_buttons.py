import streamlit as st
from utils.branding import get_tool_colors

def create_tool_grid():
    """Create the main grid of tool buttons with enhanced styling using a 3-column layout"""
    
    # Tool definitions with categories and external links
    # Updated to match actual available pages
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
            "icon": "⚖️",
            "category": "calculations",
            "status": "internal",
            "page": "pages/10_Stamp_Duty.py"
        },
    ]
    
    # Use existing color scheme from branding
    colors = get_tool_colors()
    
    # Create header with tool count
    st.markdown(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <div class="header-container" style="padding: 10px 20px; border-radius: 50px; font-weight: bold;">
            🏗️ {len(tools)} Essential Tools Available
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Create 3-column grid layout for tools
    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]
    
    for i, tool in enumerate(tools):
        with columns[i % 3]:
            # Apply custom button styling with hover effects matching the CTkButton style
            st.markdown(f"""
            <style>
            .tool-card-ctk-{i} {{
                background: linear-gradient(135deg, #f0f8f5 0%, #e8f5e8 100%);
                border: 2px solid #2E8B57;
                border-radius: 15px;
                padding: 20px;
                margin: 10px 0;
                text-align: center;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                min-height: 180px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }}
            
            .tool-card-ctk-{i}:hover {{
                transform: translateY(-3px);
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
                border-color: #228B22;
                background: linear-gradient(135deg, #e8f5e8 0%, #d4f0d4 100%);
            }}
            
            .tool-icon-ctk {{font-size: 2.5rem; margin-bottom: 10px;}}
            .tool-title-ctk {{font-weight: bold; font-size: 1.1rem; margin-bottom: 8px; color: #2E8B57;}}
            .tool-desc-ctk {{font-size: 0.9rem; color: #666; margin-bottom: 10px;}}
            .tool-status-ctk {{font-size: 0.8rem; padding: 3px 8px; border-radius: 10px; display: inline-block;}}
            .tool-status-internal {{background-color: #2E8B57; color: white;}}
            .tool-status-external {{background-color: #4682B4; color: white;}}
            </style>
            
            <div class="tool-card-ctk-{i}" onclick="document.getElementById('tool-button-{i}').click()">
                <div class="tool-icon-ctk">{tool['icon']}</div>
                <div class="tool-title-ctk">{tool['name']}</div>
                <div class="tool-desc-ctk">{tool['description']}</div>
                <div class="tool-status-ctk tool-status-{tool['status']}">{tool['status'].capitalize()}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Hidden button for navigation functionality
            if tool['status'] == 'internal':
                if st.button(f"Navigate to {tool['name']}", key=f"tool-button-{i}", disabled=True, use_container_width=True):
                    st.switch_page(tool['page'])
            else:
                if st.button(f"Open {tool['name']}", key=f"tool-button-{i}", disabled=True, use_container_width=True):
                    if 'url' in tool:
                        st.markdown(f"<meta http-equiv='refresh' content='0; url={tool['url']}'>", unsafe_allow_html=True)
    
    # Add JavaScript to handle click events since Streamlit doesn't support it directly
    st.markdown("""
    <script>
    // Add click event handlers to all tool cards
    document.querySelectorAll('[class^="tool-card-ctk-"]').forEach((card, index) => {
        card.addEventListener('click', () => {
            // Find the corresponding hidden button
            const button = document.getElementById(`tool-button-${index}`);
            if (button) {
                // Programmatically click the hidden button
                button.click();
            }
        });
    });
    </script>
    """, unsafe_allow_html=True)


