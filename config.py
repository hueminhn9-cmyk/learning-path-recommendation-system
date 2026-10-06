import streamlit as st

def init_session():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user_id = None
        st.session_state.user_email = ""
        st.session_state.user_name = ""
        st.session_state.user_role = "student"
        st.session_state.lang = "🇻🇳 Tiếng Việt"

    if "nav_radio" not in st.session_state:
        st.session_state.nav_radio = "Trang chủ" if st.session_state.lang == "🇻🇳 Tiếng Việt" else "Home"

def IS_VI():
    return st.session_state.lang == "🇻🇳 Tiếng Việt"

VI_EN_MAP = {
    "học máy": "Machine Learning",
    "hoc may": "Machine Learning",
    "trí tuệ nhân tạo": "Artificial Intelligence",
    "tri tue nhan tao": "Artificial Intelligence",
    "khoa học dữ liệu": "Data Science",
    "khoa hoc du lieu": "Data Science",
    "bảo mật mạng": "Cybersecurity",
    "bao mat mang": "Cybersecurity",
    "an toàn thông tin": "Cybersecurity",
    "an toan thong tin": "Cybersecurity",
    "bảo mật": "Cybersecurity",
    "bao mat": "Cybersecurity",
    "lập trình web": "Web Development",
    "lap trinh web": "Web Development",
    "phát triển web": "Web Development",
    "điện toán đám mây": "Cloud Computing",
    "dien toan dam may": "Cloud Computing",
    "đám mây": "Cloud Computing",
    "dam may": "Cloud Computing",
    "lập trình di động": "Mobile App Development",
    "lap trinh di dong": "Mobile App Development",
    "kỹ thuật phần mềm": "Software Engineering",
    "ky thuat phan mem": "Software Engineering",
    "cơ sở dữ liệu": "Database Systems",
    "co so du lieu": "Database Systems",
    "mạng máy tính": "Computer Networks",
    "mang may tinh": "Computer Networks"
}

def translate_subject_vi_to_en(query):
    if not query:
        return ""
    q_lower = query.strip().lower()
    for vi_term, en_term in VI_EN_MAP.items():
        if vi_term in q_lower:
            return en_term
    return query.strip()

def render_kpi_card(label, value, icon="📊", badge_text=None):
    badge_html = f'<span style="font-size:0.75rem; font-weight:700; background:#e0e7ff; color:#4338ca; padding:2px 8px; border-radius:6px; margin-left:auto;">{badge_text}</span>' if badge_text else ''
    val_str = str(value)
    if len(val_str) > 12:
        val_font_size = "1.15rem"
    elif len(val_str) > 8:
        val_font_size = "1.3rem"
    else:
        val_font_size = "1.6rem"

    st.markdown(f"""
    <div style="
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 20px 22px;
        box-shadow: 0 4px 14px -3px rgba(15, 23, 42, 0.05);
        transition: all 0.25s ease;
        margin-bottom: 8px;
        min-height: 125px;
        height: 125px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-sizing: border-box;
    ">
        <div style="font-size: 0.875rem; font-weight: 700; color: #64748b; display: flex; align-items: center; gap: 6px;">
            <span style="font-size: 1.1rem;">{icon}</span> <span>{label}</span> {badge_html}
        </div>
        <div style="font-size: {val_font_size}; font-weight: 800; color: #1e1b4b; line-height: 1.2; word-wrap: break-word; overflow-wrap: break-word;">
            {val_str}
        </div>
    </div>
    """, unsafe_allow_html=True)

def apply_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* Widen Main Container to full width with comfortable margins */
    [data-testid="block-container"], .main .block-container {
        max-width: 95% !important;
        width: 95% !important;
        padding-top: 1.5rem !important;
        padding-bottom: 2.5rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        margin: 0 auto !important;
    }

    .stApp {
        background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%) !important;
    }

    /* Headings line height & breathing room */
    h1, h2, h3, h4, h5, h6 {
        line-height: 1.35 !important;
        letter-spacing: -0.01em !important;
    }

    /* Glassmorphism Card Utility */
    .bw-card, .custom-card {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 20px !important;
        padding: 28px 32px !important;
        margin-bottom: 24px !important;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.04), 0 8px 10px -6px rgba(15, 23, 42, 0.02) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    .bw-card:hover, .custom-card:hover {
        box-shadow: 0 20px 30px -10px rgba(99, 102, 241, 0.12), 0 10px 15px -5px rgba(15, 23, 42, 0.04) !important;
        transform: translateY(-2px) !important;
        border-color: #cbd5e1 !important;
    }

    /* Hero Banner */
    .hero-banner {
        background: linear-gradient(135deg, #1e1b4b 0%, #312e81 40%, #4338ca 100%) !important;
        border-radius: 22px !important;
        padding: 36px 40px !important;
        color: #ffffff !important;
        margin-bottom: 28px !important;
        box-shadow: 0 20px 35px -10px rgba(67, 56, 202, 0.35) !important;
        position: relative !important;
        overflow: hidden !important;
    }

    .hero-banner h1, .hero-banner h2, .hero-banner h3, .hero-banner p, .hero-banner span {
        color: #ffffff !important;
    }

    .hero-badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.18);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.25);
        padding: 6px 16px;
        border-radius: 9999px;
        font-size: 0.825rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        color: #e0e7ff !important;
        margin-bottom: 12px;
    }

    /* Metric Boxes Override (No Ellipsis, Full Text Display) */
    [data-testid="stMetric"] {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 18px !important;
        padding: 18px 20px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03) !important;
        transition: all 0.2s ease !important;
        min-width: 0 !important;
        width: 100% !important;
    }
    [data-testid="stMetric"]:hover {
        border-color: #818cf8 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.1) !important;
    }
    [data-testid="stMetricValue"], [data-testid="stMetricValue"] * {
        color: #312e81 !important;
        font-weight: 800 !important;
        font-size: 1.55rem !important;
        white-space: normal !important;
        word-break: break-word !important;
        overflow: visible !important;
        text-overflow: clip !important;
        line-height: 1.25 !important;
    }
    [data-testid="stMetricLabel"], [data-testid="stMetricLabel"] * {
        color: #64748b !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        white-space: normal !important;
        word-break: break-word !important;
        overflow: visible !important;
        text-overflow: clip !important;
        line-height: 1.3 !important;
    }

    /* Vertical centering for multi-column rows */
    [data-testid="stHorizontalBlock"] {
        align-items: center !important;
    }

    /* Gradient Buttons */
    .stButton>button, button[kind="primary"], button[kind="secondary"] {
        background: linear-gradient(135deg, #4f46e5 0%, #6366f1 50%, #8b5cf6 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-size: 0.875rem !important;
        padding: 8px 12px !important;
        box-shadow: 0 4px 12px -2px rgba(79, 70, 229, 0.3) !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        white-space: nowrap !important;
        word-break: keep-all !important;
        min-height: 38px !important;
        width: 100% !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    .stButton>button *, button[kind="primary"] *, button[kind="secondary"] * {
        color: #ffffff !important;
        font-weight: 700 !important;
        white-space: nowrap !important;
        font-size: 0.875rem !important;
    }

    .stButton>button:hover, button[kind="primary"]:hover, button[kind="secondary"]:hover {
        background: linear-gradient(135deg, #4338ca 0%, #4f46e5 50%, #7c3aed 100%) !important;
        box-shadow: 0 8px 18px -4px rgba(79, 70, 229, 0.4) !important;
        transform: translateY(-1px) !important;
    }

    /* Red/Rose styling for Delete buttons (keys starting with del_) */
    div[class*="st-key-del_"] button {
        background: linear-gradient(135deg, #e11d48 0%, #f43f5e 50%, #fb7185 100%) !important;
        box-shadow: 0 4px 12px -2px rgba(225, 29, 72, 0.35) !important;
    }

    div[class*="st-key-del_"] button:hover {
        background: linear-gradient(135deg, #be123c 0%, #e11d48 50%, #f43f5e 100%) !important;
        box-shadow: 0 8px 18px -4px rgba(225, 29, 72, 0.45) !important;
        transform: translateY(-1px) !important;
    }

    /* Green styling for Completed Goal status buttons (keys starting with completed_) */
    div[class*="st-key-completed_"] button, div[class*="st-key-completed_"] button:disabled {
        background: linear-gradient(135deg, #059669 0%, #10b981 50%, #34d399 100%) !important;
        color: #ffffff !important;
        border: none !important;
        opacity: 1 !important;
        cursor: default !important;
        box-shadow: 0 4px 12px -2px rgba(16, 185, 129, 0.35) !important;
    }

    /* Form Controls & Inputs */
    .stTextInput input, .stSelectbox select, .stTextArea textarea, div[data-baseweb="select"] {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 12px !important;
        font-weight: 500 !important;
        padding: 12px 16px !important;
        font-size: 0.95rem !important;
    }

    .stTextInput input:focus, .stTextArea textarea:focus, div[data-baseweb="select"]:focus-within {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3.5px rgba(99, 102, 241, 0.18) !important;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: #ffffff !important;
        border-right: 1px solid #e2e8f0 !important;
    }
    [data-testid="stSidebar"] * {
        color: #1e293b !important;
    }

    /* Tabs */
    button[data-baseweb="tab"] {
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        color: #64748b !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
    }

    button[aria-selected="true"] {
        color: #4f46e5 !important;
        border-bottom-color: #4f46e5 !important;
    }

    /* Progress Bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%) !important;
        border-radius: 9999px !important;
    }
    </style>
    """, unsafe_allow_html=True)
