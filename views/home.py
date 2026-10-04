import streamlit as st
import numpy as np
import pandas as pd
from config import IS_VI, render_kpi_card
from database import get_db

def home_page():
    st.markdown(f"""
    <div class="hero-banner">
        <span class="hero-badge">⚡ AI Student Learning Dashboard</span>
        <h1 style="margin:8px 0; font-size:2.2rem; font-weight:800;">{'Xin chào' if IS_VI() else 'Welcome back'}, {st.session_state.user_name}! 👋</h1>
        <p style="font-size:1.05rem; opacity:0.9; margin:0;">AI Learning Path Recommendation & Student Performance Tracking Platform</p>
    </div>
    """, unsafe_allow_html=True)

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assessments WHERE user_id = ? ORDER BY created_at DESC", (st.session_state.user_id,))
    user_assessments = cursor.fetchall()
    conn.close()

    total_tests = len(user_assessments)
    latest_level = user_assessments[0]["predicted_level"] if total_tests > 0 else ("Chưa đánh giá" if IS_VI() else "No Assessment")
    avg_marks = round(np.mean([a["marks"] for a in user_assessments]), 1) if total_tests > 0 else 0

    col1, col2, col3, col4 = st.columns(4, gap="medium")
    with col1:
        render_kpi_card("Tổng bài đánh giá" if IS_VI() else "Total Assessments", total_tests, icon="📊")
    with col2:
        render_kpi_card("Trình độ hiện tại" if IS_VI() else "Latest Level", latest_level, icon="🎯")
    with col3:
        render_kpi_card("Điểm số trung bình" if IS_VI() else "Average Score", f"{avg_marks}/100", icon="⭐")
    with col4:
        render_kpi_card("Vai trò tài khoản" if IS_VI() else "Account Role", st.session_state.user_role.capitalize(), icon="👤")

    st.markdown("<br>", unsafe_allow_html=True)

    col_a, col_b = st.columns([1.8, 1.2], gap="large")

    with col_a:
        st.markdown('<div class="bw-card">', unsafe_allow_html=True)
        st.subheader("📌 " + ("Lịch sử Đánh giá Gần nhất" if IS_VI() else "Recent Assessment History"))
        if total_tests > 0:
            df_history = pd.DataFrame([dict(a) for a in user_assessments[:5]])
            st.dataframe(df_history[["subject", "marks", "interest", "time_spent", "predicted_level", "confidence", "created_at"]], use_container_width=True)
        else:
            st.info("ℹ️ Bạn chưa thực hiện bài đánh giá nào. Bấm **📝 Đánh giá AI** ở thanh menu để bắt đầu!" if IS_VI() else "ℹ️ You haven't taken any assessments yet. Click **📝 AI Assessment** in the sidebar to start!")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_b:
        st.markdown('<div class="bw-card">', unsafe_allow_html=True)
        st.subheader("⚡ " + ("Truy cập Nhanh" if IS_VI() else "Quick Shortcuts"))
        
        if st.button("📝 " + ("Đánh giá & Gợi ý AI" if IS_VI() else "Take AI Assessment"), use_container_width=True):
            st.session_state.nav_radio = "Đánh giá & Gợi ý AI" if IS_VI() else "AI Assessment"
            st.rerun()
            
        if st.button("🗺️ " + ("Lộ trình & Xuất Báo cáo" if IS_VI() else "Roadmap & Report"), use_container_width=True):
            st.session_state.nav_radio = "Lộ trình & Xuất Báo cáo" if IS_VI() else "Roadmap & Report"
            st.rerun()
            
        if st.button("📊 " + ("Thống kê & So sánh AI" if IS_VI() else "Analytics & History"), use_container_width=True):
            st.session_state.nav_radio = "Thống kê & So sánh AI" if IS_VI() else "Analytics & History"
            st.rerun()
            
        if st.button("📚 " + ("Thư viện Khóa học" if IS_VI() else "Course Library"), use_container_width=True):
            st.session_state.nav_radio = "Thư viện Khóa học" if IS_VI() else "Course Library"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
