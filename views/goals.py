import streamlit as st
from datetime import date
from config import IS_VI
from database import get_db, get_all_subjects

def goal_planner_page():
    st.markdown(f"""
    <div class="hero-banner">
        <span class="hero-badge">🎯 Milestone Management</span>
        <h1 style="margin:8px 0; font-size:2.2rem; font-weight:800;">{"Lập Kế hoạch Mục tiêu & Cột mốc Học tập" if IS_VI() else "Personal Goal & Milestone Planner"}</h1>
        <p style="font-size:1.05rem; opacity:0.9; margin:0;">Set study targets, track deadlines, and check off learning milestones</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.1, 1.9], gap="large")

    with col1:
        st.markdown('<div class="bw-card">', unsafe_allow_html=True)
        st.subheader("➕ " + ("Thêm Mục tiêu Mới" if IS_VI() else "Add New Goal"))
        all_subjects = get_all_subjects()
        g_subj = st.selectbox("Môn học" if IS_VI() else "Goal Subject", all_subjects)
        g_title = st.text_input("Tiêu đề mục tiêu" if IS_VI() else "Goal Title", placeholder="e.g. Hoàn thành 5 bài tập Python")
        g_date = st.date_input("Hạn hoàn thành" if IS_VI() else "Target Completion Date", value=date.today())

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("✨ " + ("Lưu Mục tiêu" if IS_VI() else "Save Goal Target"), use_container_width=True):
            if g_title:
                conn = get_db()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO goals (user_id, subject, goal_title, target_date, status) VALUES (?, ?, ?, ?, ?)",
                               (st.session_state.user_id, g_subj, g_title, str(g_date), "In Progress"))
                conn.commit()
                conn.close()
                st.success("✅ Đã lưu mục tiêu học tập!" if IS_VI() else "✅ Learning goal saved!")
                st.rerun()
            else:
                st.warning("⚠️ Vui lòng nhập tiêu đề." if IS_VI() else "⚠️ Please provide a goal title.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="bw-card">', unsafe_allow_html=True)
        st.subheader("📌 " + ("Danh sách Mục tiêu Đang Thực hiện" if IS_VI() else "Active Milestones & Goals Tracker"))
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM goals WHERE user_id = ? ORDER BY target_date ASC", (st.session_state.user_id,))
        goals = cursor.fetchall()
        conn.close()

        if goals:
            for g in goals:
                cols = st.columns([3.8, 1.1, 1.1], gap="small")
                with cols[0]:
                    status_icon = "✅" if g["status"] == "Completed" else "⏳"
                    st.markdown(f"<h3 style='margin:0; font-size:1.25rem; font-weight:700; color:#1e1b4b;'>{status_icon} {g['goal_title']}</h3>", unsafe_allow_html=True)
                    st.caption(f"📘 Subject: **{g['subject']}** | Target Date: **{g['target_date']}** | Status: **{g['status']}**")
                with cols[1]:
                    if g["status"] != "Completed":
                        if st.button("Done", key=f"goal_{g['id']}", use_container_width=True):
                            conn = get_db()
                            c = conn.cursor()
                            c.execute("UPDATE goals SET status = 'Completed' WHERE id = ?", (g['id'],))
                            conn.commit()
                            conn.close()
                            st.rerun()
                with cols[2]:
                    if st.button("🗑️ Del", key=f"del_goal_{g['id']}", use_container_width=True):
                        conn = get_db()
                        c = conn.cursor()
                        c.execute("DELETE FROM goals WHERE id = ?", (g['id'],))
                        conn.commit()
                        conn.close()
                        st.rerun()
                st.markdown("<hr style='margin:12px 0; border:0; border-top:1px solid #e2e8f0;'>", unsafe_allow_html=True)
        else:
            st.info("ℹ️ Chưa có mục tiêu nào được tạo." if IS_VI() else "ℹ️ No active goals yet. Add your first learning milestone on the left!")
        st.markdown('</div>', unsafe_allow_html=True)
