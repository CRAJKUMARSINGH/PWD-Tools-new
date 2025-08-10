import streamlit as st
import time

def apply_custom_css():
    """Apply custom CSS styling with crane branding and green gradient theme"""
    st.markdown("""
    <style>
    /* Main app styling */
    .main > div {
        padding-top: 0rem;
    }
    
    /* Header styling with green gradient */
    .header-container {
        background: linear-gradient(135deg, #2E8B57 0%, #90EE90 100%);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Tool button styling */
    .tool-button {
        background: linear-gradient(135deg, #f0f8f5 0%, #e8f5e8 100%);
        border: 2px solid #2E8B57;
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .tool-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        border-color: #228B22;
    }
    
    /* Metric styling */
    .metric-container {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #2E8B57;
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #f0f8f5;
    }
    
    /* Success animation */
    .celebration {
        animation: bounce 1s ease-in-out infinite alternate;
    }
    
    @keyframes bounce {
        0% { transform: translateY(0px); }
        100% { transform: translateY(-10px); }
    }
    
    /* Credits styling */
    .credits {
        background: linear-gradient(135deg, #2E8B57 0%, #3CB371 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        background-color: #2E8B57;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #228B22;
        transform: translateY(-1px);
    }
    </style>
    """, unsafe_allow_html=True)

def show_header():
    """Display the main header with crane logo and branding"""
    st.markdown("""
    <div class="header-container">
        <h1>🏗️ PWD Tools Hub</h1>
        <h3>Infrastructure Management Suite</h3>
    </div>
    """, unsafe_allow_html=True)

def show_credits():
    """Display credits and attribution"""
    st.markdown("""
    <div class="credits">
        <h4>🏆 Initiative Credit</h4>
        <p><strong>Mrs. Premlata Jain</strong><br>
        Additional Administrative Officer<br>
        Public Works Department (PWD), Udaipur</p>
        <p>🎯 <em>"Empowering Infrastructure Excellence Through Digital Innovation"</em></p>
    </div>
    """, unsafe_allow_html=True)

def show_balloons():
    """Display celebration balloons animation"""
    st.balloons()
    time.sleep(1)

def get_tool_colors():
    """Return color schemes for different tool categories"""
    return {
        "financial": {"bg": "#E8F5E8", "border": "#2E8B57", "icon": "💰"},
        "processing": {"bg": "#F0F8FF", "border": "#4169E1", "icon": "📋"},
        "operations": {"bg": "#FFF8DC", "border": "#FF8C00", "icon": "🏗️"},
        "monitoring": {"bg": "#F5F5DC", "border": "#8B4513", "icon": "📊"},
        "external": {"bg": "#FFE4E1", "border": "#DC143C", "icon": "🔗"}
    }
