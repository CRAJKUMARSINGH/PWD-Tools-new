import streamlit as st
from utils.branding import apply_custom_css, show_header
from utils.navigation import create_breadcrumb, create_back_button

# Page configuration
st.set_page_config(
    page_title="Material Management | PWD Tools Hub",
    page_icon="📦",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("Material Management System")

def main():
    st.markdown("## 📦 Material Management System")
    
    st.info("""
    **Comprehensive inventory and material tracking**
    
    Manage all construction materials, track inventory levels, monitor usage patterns, 
    and optimize procurement for PWD infrastructure projects.
    """)
    
    # Coming soon notice
    st.warning("🚧 **Tool Under Development** - This internal tool is currently being developed and will be available soon!")
    
    # Core features
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ✨ Key Features")
        st.markdown("""
        - 📊 **Inventory Tracking**: Real-time stock level monitoring
        - 🛒 **Procurement Management**: Purchase order and supplier management
        - 📋 **Quality Control**: Material quality testing and certification
        - 📈 **Usage Analytics**: Consumption patterns and forecasting
        - 🔄 **Asset Tracking**: Equipment and tool management
        - 📱 **Mobile Access**: Field-friendly mobile interface
        """)
    
    with col2:
        st.markdown("### 🔄 Material Lifecycle")
        st.markdown("""
        1. **Procurement Planning**: Demand forecasting and planning
        2. **Purchase & Receipt**: Supplier management and receiving
        3. **Quality Testing**: Material testing and certification
        4. **Storage Management**: Warehouse and inventory tracking
        5. **Issue & Consumption**: Project allocation and usage tracking
        6. **Audit & Reporting**: Stock reconciliation and analytics
        """)
    
    # Material categories
    st.markdown("### 🏗️ Material Categories")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🧱 Construction", "⚡ Electrical", "🚰 Plumbing", "🛠️ Tools"])
    
    with tab1:
        st.markdown("""
        **Construction Materials:**
        - Cement, sand, aggregates, and concrete mix
        - Steel bars, structural steel, and reinforcement
        - Bricks, blocks, tiles, and masonry materials
        - Paints, primers, and finishing materials
        - Lumber, plywood, and wooden components
        - Waterproofing and insulation materials
        """)
    
    with tab2:
        st.markdown("""
        **Electrical Materials:**
        - Cables, wires, and conduits
        - Switches, sockets, and electrical fittings
        - Circuit breakers, panels, and distribution boards
        - Lighting fixtures and LED systems
        - Motors, pumps, and electrical equipment
        - Safety equipment and protective devices
        """)
    
    with tab3:
        st.markdown("""
        **Plumbing Materials:**
        - Pipes (PVC, GI, copper) and fittings
        - Valves, taps, and plumbing fixtures
        - Pumps, tanks, and water storage systems
        - Drainage and sewerage components
        - Water treatment and filtration equipment
        - Bathroom and kitchen fixtures
        """)
    
    with tab4:
        st.markdown("""
        **Tools & Equipment:**
        - Hand tools and power tools
        - Measuring and testing instruments
        - Safety equipment and protective gear
        - Construction machinery and equipment
        - Vehicles and transportation equipment
        - IT equipment and office supplies
        """)
    
    # System modules
    st.markdown("### 🛠️ System Modules")
    
    modules = [
        ("📊", "Inventory Management", "Stock tracking, reorder alerts, and warehouse management"),
        ("🛒", "Procurement", "Vendor management, purchase orders, and supplier evaluation"),
        ("✅", "Quality Control", "Material testing, certification, and quality assurance"),
        ("📈", "Analytics", "Usage reports, trend analysis, and demand forecasting"),
        ("🔄", "Asset Tracking", "Equipment management, maintenance scheduling, and lifecycle tracking"),
        ("📱", "Mobile App", "Field access, barcode scanning, and real-time updates")
    ]
    
    for icon, module, description in modules:
        with st.container():
            col1, col2, col3 = st.columns([1, 3, 6])
            with col1:
                st.markdown(f"### {icon}")
            with col2:
                st.markdown(f"**{module}**")
            with col3:
                st.markdown(description)
    
    # Inventory management features
    st.markdown("### 📋 Inventory Management Features")
    
    inventory_col1, inventory_col2 = st.columns(2)
    
    with inventory_col1:
        st.markdown("""
        **Stock Management:**
        - Real-time inventory level monitoring
        - Automatic reorder point alerts
        - ABC analysis and categorization
        - Batch and lot number tracking
        - Expiry date management
        - Stock rotation and FIFO/LIFO methods
        """)
    
    with inventory_col2:
        st.markdown("""
        **Warehouse Operations:**
        - Multiple location management
        - Bin location and storage optimization
        - Goods receipt and issue tracking
        - Physical stock counting and reconciliation
        - Damage and wastage tracking
        - Transfer between locations
        """)
    
    # Procurement workflow
    st.markdown("### 🛒 Procurement Workflow")
    
    workflow_steps = [
        ("1️⃣", "Indent Creation", "Project teams create material indents"),
        ("2️⃣", "Approval Process", "Multi-level approval workflow"),
        ("3️⃣", "Vendor Selection", "Competitive quotations and vendor selection"),
        ("4️⃣", "Purchase Order", "PO generation and vendor notification"),
        ("5️⃣", "Material Receipt", "Goods receipt and quality inspection"),
        ("6️⃣", "Invoice Processing", "Invoice verification and payment processing")
    ]
    
    for step_num, step_name, step_desc in workflow_steps:
        with st.container():
            col1, col2, col3 = st.columns([1, 3, 6])
            with col1:
                st.markdown(f"**{step_num}**")
            with col2:
                st.markdown(f"**{step_name}**")
            with col3:
                st.markdown(step_desc)
    
    # Development progress
    st.markdown("---")
    st.markdown("### 📊 Development Status")
    
    progress_col1, progress_col2 = st.columns([3, 1])
    
    with progress_col1:
        st.progress(0.30)
        st.caption("Development Progress: 30%")
    
    with progress_col2:
        st.metric("Phase", "30%", "Requirements")
    
    # Development phases
    st.markdown("#### 🗓️ Development Phases")
    
    phases = [
        ("✅", "Requirements Analysis", "Complete", "Material management process analysis"),
        ("✅", "Database Design", "Complete", "Inventory and procurement database design"),
        ("🔄", "Core Module Development", "In Progress", "Inventory tracking and basic features"),
        ("⏳", "Procurement Module", "Planned", "Purchase order and vendor management"),
        ("⏳", "Mobile App Development", "Future", "Field access and barcode integration"),
        ("⏳", "Integration & Testing", "Final", "System integration and user acceptance testing")
    ]
    
    for status, phase, stage, description in phases:
        with st.container():
            col1, col2, col3, col4 = st.columns([1, 3, 2, 5])
            with col1:
                st.markdown(status)
            with col2:
                st.markdown(f"**{phase}**")
            with col3:
                if stage == "Complete":
                    st.success(stage)
                elif stage == "In Progress":
                    st.info(stage)
                else:
                    st.warning(stage)
            with col4:
                st.caption(description)
    
    # Expected benefits
    st.markdown("### 🎯 Expected Benefits")
    
    benefits = [
        "📉 **Cost Reduction**: 15-20% reduction in material costs through better procurement",
        "⏰ **Time Savings**: 40% reduction in material search and procurement time",
        "📊 **Visibility**: Real-time visibility into material availability and usage",
        "🎯 **Accuracy**: Elimination of manual errors in inventory management",
        "🔄 **Efficiency**: Streamlined procurement and approval processes",
        "📱 **Mobility**: Field access through mobile applications",
        "📈 **Analytics**: Data-driven decision making with usage analytics",
        "🔍 **Audit Trail**: Complete traceability of all material transactions"
    ]
    
    for benefit in benefits:
        st.markdown(f"- {benefit}")
    
    # Integration capabilities
    st.markdown("### 🔄 Integration Capabilities")
    
    integrations = [
        "💰 **Financial System**: Integration with payment processing and accounting",
        "📋 **Project Management**: Connect with work order and project tracking systems",
        "🏪 **Supplier Portals**: Direct integration with vendor and supplier systems",
        "📊 **ERP Systems**: Integration with existing government ERP solutions",
        "📱 **Barcode/RFID**: Hardware integration for automated tracking",
        "🚚 **Logistics**: Integration with transportation and delivery systems"
    ]
    
    for integration in integrations:
        st.markdown(f"- {integration}")
    
    # Launch information
    st.markdown("---")
    st.markdown("### 🚀 Launch Timeline")
    st.info("""
    **Expected Beta Release**: Q4 2025
    
    📋 **Pilot Testing**: Initial rollout in select PWD divisions for testing and feedback
    
    🎓 **Training Program**: Comprehensive training for inventory managers and field staff
    
    📱 **Mobile App**: Mobile application for field teams and site supervisors
    
    🔄 **Phased Rollout**: Gradual deployment across all PWD offices with support and training
    """)

# Navigation
create_back_button()

if __name__ == "__main__":
    main()
