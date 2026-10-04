import streamlit as st
from config import init_session, apply_styles, IS_VI
from database import init_sqlite_db
from views.auth import login_page
from views.home import home_page
from views.assessment import assessment_page
from views.assistant import ai_assistant_page
from views.roadmap import timeline_page, export_roadmap_page
from views.analytics import progress_page, ai_analytics_page
from views.resources import resources_page
from views.goals import goal_planner_page
from views.admin import admin_page

# Initialize DB & Session & Styling
init_sqlite_db()
init_session()
apply_styles()

def main():
    if not st.session_state.logged_in:
        login_page()
        return

    with st.sidebar:
        st.markdown("""
        <div style="text-align:center; padding: 12px 0 16px 0;">
            <div style="font-size:2.5rem;">🎓</div>
            <h2 style="margin:4px 0 0 0; color:#312e81; font-weight:800;">AI Advisor</h2>
            <p style="color:#64748b; font-size:0.85rem; margin:0;">Student Learning Platform</p>
        </div>
        """, unsafe_allow_html=True)
        st.write(f"👋 **{st.session_state.user_name}**")
        
        st.markdown("---")
        st.session_state.lang = st.radio("🌐 Language / Ngôn ngữ", ["🇻🇳 Tiếng Việt", "🇬🇧 English"], 
                                         index=0 if st.session_state.lang == "🇻🇳 Tiếng Việt" else 1)
        st.markdown("---")

        options = [
            "Home" if not IS_VI() else "Trang chủ",
            "AI Assessment" if not IS_VI() else "Đánh giá & Gợi ý AI",
            "AI Assistant Chatbot" if not IS_VI() else "🤖 Trợ lý AI Hỏi đáp",
            "Roadmap & Report" if not IS_VI() else "Lộ trình & Xuất Báo cáo",
            "Analytics & History" if not IS_VI() else "Thống kê & So sánh AI",
            "Course Library" if not IS_VI() else "Thư viện Khóa học",
            "Goal Planner" if not IS_VI() else "Lập Mục tiêu Học tập"
        ]
        if st.session_state.user_role == "admin":
            options.append("Admin Console")

        if st.session_state.nav_radio not in options:
            st.session_state.nav_radio = options[0]

        choice = st.radio("Chuyển trang:" if IS_VI() else "Go to:", options, key="nav_radio")

        st.markdown("---")
        if st.button("🚪 " + ("Đăng xuất" if IS_VI() else "Logout"), use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.nav_radio = "Trang chủ" if IS_VI() else "Home"
            st.rerun()

    # Route mapping
    if "Trang chủ" in choice or "Home" in choice:
        home_page()
    elif "Đánh giá" in choice or "AI Assessment" in choice:
        assessment_page()
    elif "Trợ lý AI" in choice or "AI Assistant" in choice:
        ai_assistant_page()
    elif "Lộ trình" in choice or "Roadmap" in choice:
        timeline_page()
        st.markdown("---")
        export_roadmap_page()
    elif "Thống kê" in choice or "Analytics" in choice:
        progress_page()
        st.markdown("---")
        ai_analytics_page()
    elif "Thư viện" in choice or "Course Library" in choice:
        resources_page()
    elif "Mục tiêu" in choice or "Goal Planner" in choice:
        goal_planner_page()
    elif "Admin" in choice:
        admin_page()

if __name__ == "__main__":
    main()
