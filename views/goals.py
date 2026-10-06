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
        
        with st.form("add_goal_form", clear_on_submit=True):
            g_subj = st.selectbox("Môn học" if IS_VI() else "Goal Subject", all_subjects)
            g_title = st.text_input("Tiêu đề mục tiêu" if IS_VI() else "Goal Title", placeholder="e.g. Hoàn thành 5 bài tập Python")
            g_date = st.date_input("Hạn hoàn thành" if IS_VI() else "Target Completion Date", value=date.today())
            st.markdown("<br>", unsafe_allow_html=True)
            submit_goal = st.form_submit_button("✨ " + ("Lưu Mục tiêu" if IS_VI() else "Save Goal Target"), use_container_width=True)
            
            if submit_goal:
                if g_title and g_title.strip():
                    conn = get_db()
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO goals (user_id, subject, goal_title, target_date, status) VALUES (?, ?, ?, ?, ?)",
                                   (st.session_state.user_id, g_subj, g_title.strip(), str(g_date), "In Progress"))
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
                cols = st.columns([2.5, 2.3, 1.2], gap="small")
                with cols[0]:
                    status_icon = "✅" if g["status"] == "Completed" else "⏳"
                    st.markdown(f"<h4 style='margin:0 0 4px 0; font-size:1.1rem; font-weight:700; color:#1e1b4b;'>{status_icon} {g['goal_title']}</h4>", unsafe_allow_html=True)
                    if IS_VI():
                        status_str = "Đã hoàn thành" if g["status"] == "Completed" else "Đang thực hiện"
                        st.caption(f"📘 Môn học: **{g['subject']}** | Hạn: **{g['target_date']}** | Trạng thái: **{status_str}**")
                    else:
                        status_str = "Completed" if g["status"] == "Completed" else "In Progress"
                        st.caption(f"📘 Subject: **{g['subject']}** | Target Date: **{g['target_date']}** | Status: **{status_str}**")
                with cols[1]:
                    if g["status"] != "Completed":
                        if st.button("✅ " + ("Hoàn thành" if IS_VI() else "Complete"), key=f"goal_{g['id']}", use_container_width=True):
                            conn = get_db()
                            c = conn.cursor()
                            c.execute("UPDATE goals SET status = 'Completed' WHERE id = ?", (g['id'],))
                            conn.commit()
                            conn.close()
                            st.rerun()
                    else:
                        st.button("✅ " + ("Đã hoàn thành" if IS_VI() else "Completed"), key=f"completed_{g['id']}", disabled=True, use_container_width=True)
                with cols[2]:
                    if st.button("🗑️ " + ("Xóa" if IS_VI() else "Delete"), key=f"del_goal_{g['id']}", use_container_width=True):
                        conn = get_db()
                        c = conn.cursor()
                        c.execute("DELETE FROM goals WHERE id = ?", (g['id'],))
                        conn.commit()
                        conn.close()
                        st.rerun()
                st.markdown("<hr style='margin:14px 0; border:0; border-top:1px solid #e2e8f0;'>", unsafe_allow_html=True)
        else:
            st.info("ℹ️ Chưa có mục tiêu nào được tạo." if IS_VI() else "ℹ️ No active goals yet. Add your first learning milestone on the left!")
        st.markdown('</div>', unsafe_allow_html=True)
